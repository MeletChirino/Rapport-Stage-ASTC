// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2022.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC). The copyright notice does not evidence any actual
// or intended publication of such source code.

#ifndef VWORKS_MODELS_MARVELL_88Q5050_HPP
#define VWORKS_MODELS_MARVELL_88Q5050_HPP

#include "marvell_88Q5050_base.hpp"

namespace vworks {
namespace models {

class marvell_88Q5050 : public marvell_88Q5050_base
{
public:
    marvell_88Q5050(sc_core::sc_module_name name);
    virtual ~marvell_88Q5050();

private:
    SC_HAS_PROCESS(marvell_88Q5050);
    std::vector<sc_core::sc_vector<vworks::genesis::reg16>*> _reg_map {
        &PORT0, // 0x0
        &PORT1, // 0x1
        &PORT2, // 0x2
        &PORT3, // 0x3
        &PORT4, // 0x4
        &PORT5, // 0x5
        &PORT6, // 0x6
        &PORT7, // 0x7
        &PORT8, // 0x8
        NULL,   // 0x9
        NULL,   // 0xA
        NULL,   // 0xB
        NULL,   // 0xC
        NULL,   // 0xD
        NULL,   // 0xE
        NULL,   // 0xF
        NULL,   // 0x10
        NULL,   // 0x11
        NULL,   // 0x12
        NULL,   // 0x13
        NULL,   // 0x14
        NULL,   // 0x15
        NULL,   // 0x16
        NULL,   // 0x17
        NULL,   // 0x18
        NULL,   // 0x19
        NULL,   // 0x1A
        &GLB1,  // 0x1B
        &GLB2,  // 0x1C
        NULL,   // 0x1D
        NULL,   // 0x1E
        &TCAM,  // 0x1F
    };

    void write_reg(int dev_addr, int reg_addr, uint16_t value);
    uint16_t read_reg(int dev_addr, int reg_addr);

    // Callback functions
    void on_RX_update(size_t index);
    void on_MDIO_in_update();
    void _RX8_cbk();
    void reg_callback(int dev_addr, int reg_addr);

    // register callback functions
    void _GLB1_04_cbk();
    void _GLB2_0D_cbk();
    void _GLB2_18_cbk();
    void _eth_cbk(size_t in_port);

    // Smi functions
    sc_core::sc_event smi_data_event;
    sc_core::sc_event smi_cmd_event;
    void smi_cmd_response();
    void smi_data_response();
    void smi_cmd();
    void smi_cmd_phy();

    // Transceivers init
    uint8_t tcrv_88q2112_st = 0;
    bool tcrv_88q2112_init(uint16_t phy_addr, uint16_t reg_addr, uint16_t op);
    bool tcrv_88q1010_init();
};

} // models
} // vworks

#endif // VWORKS_MODELS_MARVELL_88Q5050_HPP
