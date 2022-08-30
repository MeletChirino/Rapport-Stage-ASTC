// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2022.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC). The copyright notice does not evidence any actual
// or intended publication of such source code.

#include "marvell_88Q5050.hpp"
#include "reg_processing.hpp"
#include "registers.hpp"


//#define RMU_ETHER_TYPE 0x5CDA // According to AUTOSAR this is the one
#define RMU_ETHER_TYPE 0xDA5C // but this is the one we receive
#define IPV4_ETHER_TYPE 0x800
#define IPV6_ETHER_TYPE 0x86DD
#define SMI_PROC_TIME 300
#define PAYLOAD_SIZE 496

using namespace sc_core;
using namespace sc_dt;
using namespace vworks::genesis;

namespace vworks {
namespace models {

  std::vector<uint16_t> reorder_data(EthernetFrame::vector data){
    std::vector<uint16_t> new_data(PAYLOAD_SIZE, 0x0);

    size_t idx = 4;
    new_data[idx + 2] = data[idx + 3];
    new_data[idx + 3] = data[idx + 2];
    idx += 4;
    while(idx < PAYLOAD_SIZE){
      new_data[idx]   = data[idx+3];
      new_data[idx+1] = data[idx+2];
      new_data[idx+2] = data[idx+1];
      new_data[idx+3] = data[idx];
      if(idx + 4 > PAYLOAD_SIZE) break;
      idx += 4;
    }
    return new_data;
  }

  bool verify_dsa_tag(uint64_t dsa_tag, uint64_t ether_type){
  //printf("\n==> Verifiying DSA Tag <==\n");
  //verificar DSA Tag
  bool result;
  uint32_t Trg_Dev, reserved_1, pri, reserved_2, number, ver1, ver2, ver3;
  ver1 = (dsa_tag >> 29) & 0x3;
  ver2 = (dsa_tag >> 16) & 0b11;
  ver3 = (dsa_tag >> 12) & 0b1;
  Trg_Dev = (dsa_tag >> 24) & 0x1F;
  reserved_1 = (dsa_tag >> 18) & 0x3f;
  pri = (dsa_tag >> 13) & 0x3;
  reserved_2 = (dsa_tag >> 8) & 0xF;
  number = dsa_tag & 0xFF;

  result = (ver1 == 0b010 && reserved_1 == 0x3E && ver2 == 0 && reserved_2 == 0xF);
  //return result;

  if(ether_type == RMU_ETHER_TYPE)
    return true;
  else
    return false;
}

marvell_88Q5050::marvell_88Q5050(sc_module_name name) :
    marvell_88Q5050_base(name)
{
    // Add reset values of specific registers
    for(size_t i = 0x0; i <= 0x1F; i++){ // init registers to 0
        for(size_t j = 0x0; j <= 0x1F; j++){
            write_reg((int)i, (int)j, 0x00);
        }
      }
    for(size_t i = 0x0; i <= 0x8; i++){ // init registers to 0
        write_reg((int)i, 0x3, 0xA510); // Switch ID
        write_reg((int)i, 0xF, 0x9100); // Port Etype
    }

    SMI_CMD_REG.write(0x0);
    SMI_DATA_REG.write(0x0);
    GLB1[0x0].value = 0xC800; // Device ready for use

    SC_METHOD(on_MDIO_in_update);
    sensitive << MDIO_in;
    dont_initialize();

    SC_THREAD(smi_cmd_response);
    SC_THREAD(smi_data_response);

    int index = 1;
    for (int i = 0; i < N_PORTS; i++) {
        sc_spawn_options options;
        options.spawn_method();
        //printf("\n==> Setting sensitivity list for RX[%d] <==", int(index));
        options.set_sensitivity(&RX[i]);
        options.dont_initialize();
        sc_spawn(sc_bind(&marvell_88Q5050::on_RX_update, this, i),
                  sc_gen_unique_name("on_RX_update"), &options);
        index++;
    }
}

marvell_88Q5050::~marvell_88Q5050()
{
}

void marvell_88Q5050::on_RX_update(size_t index){
  //printf("\n==> RX #%zd <==\n", index);
  EthernetFrame received_frame = RX[index], response_frame;
  switch(index){
    case(8):
      _RX8_cbk();
      break;
    default:
      _eth_cbk(index);
      break;
  }
  /*
  uint64_t dsa_tag = (received_frame.GetWord(12, 4));
  uint64_t ether_type = received_frame.GetWord(16, 2);
  if(rmu_mode && index == 7 && verify_dsa_tag(dsa_tag, ether_type)){
    uint64_t source_addr, dest_addr;
    printf("DSA Command verified\n");
    response_frame = received_frame;
    source_addr = received_frame.GetSourceAddress();
    dest_addr = received_frame.GetDestAddress();
    response_frame.SetDestAddress(source_addr);
    response_frame.SetSourceAddress(dest_addr);
    TX[index].write(response_frame);
    //response_frame = received_frame.SetWord(12 * 8, 4 * 8, 0x01010101);
    //TX[index].write(response_frame);
  } else if (ether_type == IPV4_ETHER_TYPE || ether_type == IPV6_ETHER_TYPE) {
    printf("Regular EThFrame");
    for(int i = 0; i < N_PORTS; i++){
      if (i != index)
        TX[i].write(received_frame);
    }
  }*/
}

void marvell_88Q5050::_RX8_cbk(){
  // check if RMU mode is enabled
  EthernetFrame received_frame = RX[8].read(), response_frame;
  std::vector<uint16_t> data(received_frame.GetSize(), 0x0);
  uint64_t cmd;
  uint8_t pad, op, dev_addr, reg_addr;
  uint16_t cmd_data;
  size_t idx;
  if (((GLOBAL_CTRL2.value >> 8) & 0b111) == 0x3){ // check if rmu mode is enabled
      data = reorder_data(received_frame.GetPayload());
      response_frame.Resize(516);
      //simulation_pause();
      response_frame.SetDestAddress(received_frame.GetSourceAddress());
      response_frame.SetSourceAddress(received_frame.GetSourceAddress());
      response_frame.SetWord(13, 6, received_frame.GetWord(13, 6));

      cmd = (((uint64_t)data[4]) << 32) | (((uint64_t)data[5]) << 16) | (((uint64_t)data[6]) << 8) | data[7];
      response_frame.SetWord(19, 4, cmd);
      // cmd == 0x1 if not leave this mode
      cmd = (((uint64_t)data[8]) << 8) | data[9];
      response_frame.SetWord(23, 2, cmd);
      // cmd == 0x2000 if not leave this mode
      idx = 10;
      int i = 0;
      while(idx < received_frame.GetSize()){
        cmd = (((uint64_t)data[idx]) << 24) | (((uint64_t)data[idx+ 1]) << 16)
              | (((uint64_t)data[idx + 2]) << 8) | data[idx + 3];
        pad = (cmd >> 28) & 0xF; //
        if (pad == 0x0 && i != 121 && cmd != 0x0){
          op = (cmd >> 26) & 0b11; // 0b10 => read ; 0b01 => write
          dev_addr = (cmd >> 21) & 0b11111;
          reg_addr = (cmd >> 16) & 0b11111;
          cmd_data = cmd & 0xFFFF;
          if (op == 0b10){ //read operation
            cmd_data = read_reg(dev_addr, reg_addr);
          } else if(op == 0b01){ // write ooperation
            write_reg(dev_addr, reg_addr, cmd_data);
          } 
        } else if (pad == 0x1) {
          // wait a bit
          op = (cmd >> 26) & 0b11; // 0b00 => wait for 0 ; 0b11 => wait for 1
          dev_addr = (cmd >> 21) & 0b11111;
          reg_addr = (cmd >> 16) & 0b11111;

          uint8_t bit_to_wait = (cmd >> 8) & 0xF;
          uint16_t mask = (uint16_t)0xFFFFFFFE, value;
          value = read_reg(dev_addr, reg_addr);
          if (op == 0x0){
            mask = value & (mask << bit_to_wait);
          } else if (op == 0b11){
            mask = value | (~mask << bit_to_wait);
          }
          write_reg(dev_addr, reg_addr, mask);
        } else if (pad == 0xFF || i == 121 || cmd == 0x0) {
          // end of the line
          response_frame.SetWord(idx+13, 8, 0xFFFFFFFF);
          break;
        }
        
        if(idx + 4 > received_frame.GetSize()) break;
        if (cmd != 0x0) {
          response_frame.SetWord(idx+13, 8, cmd);
          idx+= 4; i ++;
        }
      }
      TX[8].write(response_frame);
  } else {
    _eth_cbk((size_t) 8);
  }
}

void marvell_88Q5050::_eth_cbk(size_t in_port){
  for (size_t i = 0; i < N_PORTS; i++){
    if (i != in_port){
      TX[i].write(RX[in_port].read());
    }
  }
}

void marvell_88Q5050::smi_data_response(){
  while(1){
    wait(smi_data_event);
    MDIO_out.write(SMI_DATA_REG.value);
    //printf("EVENT =>\n writing to the bus===> 0x%X\n===\n", SMI_DATA_REG.value);
  }
}

void marvell_88Q5050::smi_cmd_response(){
  while(1){
    wait(smi_cmd_event);
    MDIO_out.write(SMI_CMD_REG.value);// & 0x7FFF);
    //printf("EVENT => \nwriting to the bus===> 0x%X\n===\n", SMI_CMD_REG.value);
  }
}

void marvell_88Q5050::write_reg(int dev_addr, int reg_addr, uint16_t value){
    if(dev_addr <= 0x8  ||
       dev_addr == 0x1B ||
       dev_addr == 0x1C ||
       dev_addr == 0x1F) {
        (*_reg_map[(size_t)dev_addr])[(size_t) reg_addr].write(value);
        reg_callback(dev_addr, reg_addr);
    }
}
uint16_t marvell_88Q5050::read_reg(int dev_addr, int reg_addr){
    if(dev_addr <= 0x8  ||
       dev_addr == 0x1B ||
       dev_addr == 0x1C ||
       dev_addr == 0x1F) {
        return (*_reg_map[(size_t)dev_addr])[(size_t) reg_addr].read();
        //printf("_reg_map[0x%X][0x%X] =>%d\n", dev_addr, reg_addr, (*_reg_map[(size_t)dev_addr])[(size_t)reg_addr].value);
    } else {
        throw std::invalid_argument( "Reserved memory" );
    }
}

void marvell_88Q5050::reg_callback(int dev_addr, int reg_addr){
    if(dev_addr == 0x1B && reg_addr == 0x4){
        _GLB1_04_cbk();
    } else if (dev_addr == 0x1C && reg_addr == 0xD){
        _GLB2_0D_cbk();
    } else if (dev_addr == 0x1C && reg_addr == 0x18){
        _GLB2_18_cbk();
    } else if (dev_addr == 0x1C && reg_addr == 0x19){
        //printf("\nSMI_PHY_DATA_REG = 0x%X", SMI_PHY_DATA_REG.value);
    }
}

void marvell_88Q5050::_GLB2_18_cbk(){
  uint16_t value = SMI_PHY_CMD_REG.read();
  value &= 0x7FFF;
  SMI_PHY_CMD_REG.write(value);
  smi_cmd_phy();
}

void marvell_88Q5050::smi_cmd(){
  bool smi_mode;
  uint16_t dev_addr, reg_addr, smi_op, cmd;
  cmd = SMI_CMD_REG.read();
  smi_mode = (cmd >> 12) & 0x1;
  smi_op = (cmd >> 10) & 0x3;
  dev_addr = (cmd >> 5) & 0x1F;
  reg_addr = cmd & 0x1F;

  if(smi_op == 0x1){ // ==> write operation
    if(dev_addr <= 0x8 || dev_addr == 0x1B || dev_addr == 0x1C ||dev_addr == 0x1F)
      write_reg(dev_addr, reg_addr, SMI_DATA_REG.value);
    else
      printf("Zone reserved\n");

  } else if (smi_op == 0x2){ // ==> read operation
    if(dev_addr <= 0x8 || dev_addr == 0x1B || dev_addr == 0x1C ||dev_addr == 0x1F)
       SMI_DATA_REG.write(read_reg(dev_addr, reg_addr));
    else
      printf("Zone reserved");
  }
}

void marvell_88Q5050::smi_cmd_phy(){
  bool  smi_mode;
  uint16_t dev_addr, reg_addr, smi_op, cmd, smi_func;
  cmd = SMI_PHY_CMD_REG.read();
  smi_func = (cmd >> 13) & 0x3;
  smi_mode = (cmd >> 12) & 0x1;
  smi_op = (cmd >> 10) & 0x3;
  dev_addr = (cmd >> 5) & 0x1F;
  reg_addr = cmd & 0x1F;

  tcrv_88q1010_init();
}

bool marvell_88Q5050::tcrv_88q1010_init(){
  if ( (SMI_PHY_CMD_REG.value == 0x184E || SMI_PHY_CMD_REG.value == 0x186E ||
        SMI_PHY_CMD_REG.value == 0x18AE || SMI_PHY_CMD_REG.value == 0x148D || 
        SMI_PHY_CMD_REG.value == 0x182E ) &&  SMI_PHY_DATA_REG.value == 0x4001) {
    SMI_PHY_DATA_REG.write(0x2B); // for 88Q1010 transceivers
  return true;
  }
  return false;
}

bool marvell_88Q5050::tcrv_88q2112_init(uint16_t phy_addr, uint16_t reg_addr, 
                                        uint16_t op){
  if ((phy_addr == 0x3 && reg_addr == 0xE) && op == 0b10) {
    switch(tcrv_88q2112_st){
      case 0:
        SMI_DATA_REG.value = 0x2B;
        smi_data_event.notify(SMI_PROC_TIME, SC_US);
        tcrv_88q2112_st++;
        break;
      case 1:
        SMI_DATA_REG.value = 0x800;
        smi_data_event.notify(SMI_PROC_TIME, SC_US);
        tcrv_88q2112_st = 0;
        break;
    }
    return true;
  } else if ((phy_addr == 0x2 && reg_addr == 0xE) && op == 0b10) {
    switch(tcrv_88q2112_st){
      case 0:
        SMI_DATA_REG.value = 0x2B;
        smi_data_event.notify(SMI_PROC_TIME, SC_US);
        tcrv_88q2112_st++;
        break;
      case 1:
        SMI_DATA_REG.value = 0x800;
        smi_data_event.notify(SMI_PROC_TIME, SC_US);
        tcrv_88q2112_st = 0;
        break;
    }
    return true;
  }
  return false;
}

void marvell_88Q5050::on_MDIO_in_update(){
    uint32_t mdio = MDIO_in.read();
    uint16_t op, phy_addr, reg_addr, data, st;

    st = (mdio >> 30) & 0x3; // Start Frame MUST BE 01
    op = (mdio >> 28) & 0x3; // Operation
    phy_addr = (mdio >> 23) & 0x1f; // Physical address
    reg_addr = (mdio >> 18) & 0x1f; // Register address
    data = mdio & 0xffff; // Data

    if (st == 0x1 && mdio != 0x0) {
      // Clause 22
      // Next functions are for transceivers
      if(tcrv_88q2112_init(phy_addr, reg_addr, op)) return;
        if (op == 0x1){ // write operation
          if(reg_addr == 0x0 &&
            ((SMI_CMD_REG.value & 0x8000) == 0x0) ){
              tcrv_88q2112_st = 0; // reset tcrv init
             //write in smi_cmd register if SMIBusy bit is 0
              SMI_CMD_REG.value = data & 0x7FFF;
              smi_cmd();
          } else if (reg_addr == 0x1) // write in smi_data register
            SMI_DATA_REG.value = data;
        } else if(op == 0x2){//read opration
          if (reg_addr == 0x0){
            smi_cmd_event.notify(SMI_PROC_TIME, SC_US);
          }
          else if (reg_addr == 0x1){
            smi_data_event.notify(SMI_PROC_TIME, SC_US);
          }
      }
    }
    else if (st == 0x0) {
        // Clause 45
        #ifdef DEBUG
          printf("\n==> Clause 45 <==\n");
        #endif

        // TODO Not yet supported
        // TODO Generate an appropriate message
    }
    else {
        // Illegal start of frame
        // TODO Generate an appropriate message
    }
}
void marvell_88Q5050::_GLB1_04_cbk(){
    uint16_t value = SWITCH_GLB_CTRL.read();
    if((value & 0xC000) == 0xC000){ // Trigger switch reset
        //QC and MAC state machine are reset
        value &= 0x7FFF;
    }
    SWITCH_GLB_CTRL.write(value);
}

void marvell_88Q5050::_GLB2_0D_cbk(){
    uint16_t value = SWITCH_MAC_WOL_WOF_REG.read();
    if((value & 0x8000) == 0x8000){ // Update data bit
        uint8_t pointer = (value >> 8) & 0x3F;
        uint8_t data = value & 0xFF;
        SWITCH_MAC_WOL_WOF[pointer].value = data;
        value &= 0x7FFF;
    }
    SWITCH_MAC_WOL_WOF_REG.write(value);
}


} // models
} // vworks
