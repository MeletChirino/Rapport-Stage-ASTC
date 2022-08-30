// -----------------------------------------------------------------------------
// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2020.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC).  The copyright notice does not evidence any actual
// or intended publication of such source code.
// -----------------------------------------------------------------------------

#include <systemc>
#include "mdio_bus.hpp"

namespace vworks {
namespace models {

MDIO_bus::MDIO_bus(sc_core::sc_module_name name, uint32_t num_stas, uint32_t num_mmds) :
    sc_core::sc_module(name),
    MDIO_STA_in("MDIO_STA_in", num_stas),
    MDIO_STA_out("MDIO_STA_out", num_stas),
    MDIO_MMD_in("MDIO_MMD_in", num_mmds),
    MDIO_MMD_out("MDIO_MMD_out", num_mmds),
    m_active_sta(0)
{
    for (size_t i = 0; i < MDIO_STA_in.size(); i++)
    {
        sc_core::sc_spawn_options opt;
        opt.spawn_method();
        opt.set_sensitivity(&MDIO_STA_in[i]);
        opt.dont_initialize();
        sc_core::sc_spawn(sc_bind(&MDIO_bus::on_MDIO_STA_in_update, this, i),
            sc_core::sc_gen_unique_name("on_MDIO_STA_in_update"), &opt);
    }

    for (size_t i = 0; i < MDIO_MMD_in.size(); i++)
    {
        sc_core::sc_spawn_options opt;
        opt.spawn_method();
        opt.set_sensitivity(&MDIO_MMD_in[i]);
        opt.dont_initialize();
        sc_core::sc_spawn(sc_bind(&MDIO_bus::on_MDIO_MMD_in_update, this, i),
            sc_core::sc_gen_unique_name("on_MDIO_MMD_in_update"), &opt);
    }
}

void MDIO_bus::on_MDIO_STA_in_update(size_t index)
{
    m_active_sta = index;
    uint32_t value = MDIO_STA_in[index].read();

    for (size_t i = 0; i < MDIO_MMD_in.size(); i++)
    {
        MDIO_MMD_out[i].write(value);
    }
}

void MDIO_bus::on_MDIO_MMD_in_update(size_t index)
{
    uint32_t value = MDIO_MMD_in[index].read();
    MDIO_STA_out[m_active_sta].write(value);
}

} // models
} // vworks
