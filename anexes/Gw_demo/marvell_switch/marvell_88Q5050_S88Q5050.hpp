// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2022.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC). The copyright notice does not evidence any actual
// or intended publication of such source code.

#ifndef VWORKS_MODELS_MARVELL_88Q5050_S88Q5050_HPP
#define VWORKS_MODELS_MARVELL_88Q5050_S88Q5050_HPP

#include "marvell_88Q5050_S88Q5050_base.hpp"

namespace vworks {
namespace models {

class marvell_88Q5050_S88Q5050 : public marvell_88Q5050_S88Q5050_base
{
public:
    marvell_88Q5050_S88Q5050(sc_core::sc_module_name name);
    virtual ~marvell_88Q5050_S88Q5050();

private:
    SC_HAS_PROCESS(marvell_88Q5050_S88Q5050);
};

} // models
} // vworks

#endif // VWORKS_MODELS_MARVELL_88Q5050_S88Q5050_HPP
