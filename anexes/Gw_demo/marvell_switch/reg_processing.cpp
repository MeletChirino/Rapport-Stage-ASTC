#include "reg_processing.hpp"

using namespace std;

unsigned int glb1_processing(unsigned int data, unsigned int reg_addr){
  switch(reg_addr){
    case 0x4: // SWITCH_GLB_CTRL
      if((data & 0xC000) == 0xC000)//swt reset done
        // QC and MAC state machinesare reset
        data &= 0x7FFF;// clearing SWReset bit after swt reset
      return data;
      break;
    default:
      return data;
  }
}

unsigned int glb2_processing(unsigned int data, unsigned int reg_addr){
  switch(reg_addr){
    case 0x4: // SWITCH_GLB_CTRL
      if((data & 0xC000) == 0xC000)//swt reset done
        // QC and MAC state machinesare reset
        data &= 0x7FFF;// clearing SWReset bit after swt reset
      return data;
      break;
    default:
      return data;
  }
}