// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2022.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC). The copyright notice does not evidence any actual
// or intended publication of such source code.

#include "marvell_88Q5050_common.hpp"
#include "registers.hpp"

#ifndef NO_LICENSE
#include <astc/licensing/license_manager.hpp>
#include <stdexcept>
#endif

//DONT FORGET TO UNCOMMENT NEXT LINE
#define NO_LICENSE 2

using namespace sc_core;
using namespace sc_dt;
using namespace vworks::genesis;

namespace vworks {
namespace models {

static void checkout_license(const char *name)
{
#ifndef NO_LICENSE
    static astc::licensing::LicenseManager manager;
    std::string license("marvell_88q5050_model");
    std::string version("1.0");
    if (!manager.checkout(license, version)) {
        throw std::runtime_error(astc::licensing::format_error_message(
            astc::licensing::format_brief_error_message(license, version),
            manager.last_error_details(), "",
            astc::licensing::ASTC_SUPPORT_MESSAGE));
    }
#endif
}

marvell_88Q5050_common::marvell_88Q5050_common(sc_module_name name) :
    marvell_88Q5050_common_base(name)
{

  checkout_license(this->name());

}

marvell_88Q5050_common::~marvell_88Q5050_common()
{
}

void marvell_88Q5050_common::start_of_simulation()
{
    reset_ports();
}

} // models
} // vworks
