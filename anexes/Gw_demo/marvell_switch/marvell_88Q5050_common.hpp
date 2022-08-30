// Copyright (C) Australian Semiconductor Technology Company (ASTC). 2022.
// All Rights Reserved.
//
// This is unpublished proprietary source code of the Australian Semiconductor
// Technology Company (ASTC). The copyright notice does not evidence any actual
// or intended publication of such source code.

#ifndef VWORKS_MODELS_MARVELL_88Q5050_COMMON_HPP
#define VWORKS_MODELS_MARVELL_88Q5050_COMMON_HPP

#include "marvell_88Q5050_common_base.hpp"
#define N_PORTS 9

namespace vworks {
namespace models {

class marvell_88Q5050_common : public marvell_88Q5050_common_base
{
public:
    marvell_88Q5050_common(sc_core::sc_module_name name);
    virtual ~marvell_88Q5050_common();

protected:
    virtual void start_of_simulation();

private:

    SC_HAS_PROCESS(marvell_88Q5050_common);

};
} // models
} // vworks

#endif // VWORKS_MODELS_MARVELL_88Q5050_COMMON_HPP
