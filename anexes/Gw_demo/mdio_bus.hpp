// -----------------------------------------------------------------------------
// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2020.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC).  The copyright notice does not evidence any actual
// or intended publication of such source code.
// -----------------------------------------------------------------------------

#ifndef VWORKS_MODELS_MDIO_BUS_
#define VWORKS_MODELS_MDIO_BUS_

#include <systemc>

namespace vworks {
namespace models {

class MDIO_bus : public sc_core::sc_module
{
public:
    MDIO_bus(sc_core::sc_module_name name, uint32_t num_stas, uint32_t num_mmds);

    sc_core::sc_vector<sc_core::sc_in<unsigned int> > MDIO_STA_in;
    sc_core::sc_vector<sc_core::sc_out<unsigned int> > MDIO_STA_out;

    sc_core::sc_vector<sc_core::sc_in<unsigned int> > MDIO_MMD_in;
    sc_core::sc_vector<sc_core::sc_out<unsigned int> > MDIO_MMD_out;

private:
    SC_HAS_PROCESS(MDIO_bus);

    void on_MDIO_STA_in_update(size_t index);
    void on_MDIO_MMD_in_update(size_t index);

private:
    uint32_t m_active_sta;
};

} // namespace models
} // namespace vworks

#endif // VWORKS_MODELS_MDIO_BUS_
