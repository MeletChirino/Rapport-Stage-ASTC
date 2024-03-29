/**
 * \file IfxEmem_reg.h
 * \brief
 * \copyright Copyright (c) 2017 Infineon Technologies AG. All rights reserved.
 *
 *
 * Date: 2017-07-11 14:33:31 GMT
 * Version: TBD
 * Specification: TBD
 * MAY BE CHANGED BY USER [yes/no]: Yes
 *
 *                                 IMPORTANT NOTICE
 *
 *
 * Infineon Technologies AG (Infineon) is supplying this file for use
 * exclusively with Infineon's microcontroller products. This file can be freely
 * distributed within development tools that are supporting such microcontroller
 * products.
 *
 * THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED
 * OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.
 * INFINEON SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL,
 * OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
 *
 * MUST NOT be used with TC37x standard version
 *
 * \defgroup IfxLld_Emem_Registers_Cfg Emem address
 * \ingroup IfxLld_Emem_Registers
 *
 * \defgroup IfxLld_Emem_Registers_Cfg_BaseAddress Base address
 * \ingroup IfxLld_Emem_Registers_Cfg
 *
 * \defgroup IfxLld_Emem_Registers_Cfg_Emem 2-EMEM
 * \ingroup IfxLld_Emem_Registers_Cfg
 *
 *
 */
#ifndef IFXEMEM_REG_H
#define IFXEMEM_REG_H 1
/******************************************************************************/
#include "IfxEmem_regdef_ext.h"
/******************************************************************************/
/** \addtogroup IfxLld_Emem_Registers_Cfg_BaseAddress
 * \{  */

/** \brief EMEM object */
#define MODULE_EMEM /*lint --e(923)*/ ((*(Ifx_EMEM*)0xFA006000u))
/** \}  */


/******************************************************************************/
/******************************************************************************/
/** \addtogroup IfxLld_Emem_Registers_Cfg_Emem
 * \{  */
/** \brief 0, EMEM Core Clock Control Register */
#define EMEM_CLC /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_CLC*)0xFA006000u)

/** \brief 8, EMEM Core Module Identification Register */
#define EMEM_ID /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_ID*)0xFA006008u)

/** \brief 20, EMEM Core Tile Configuration Register */
#define EMEM_TILECONFIG /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_TILECONFIG*)0xFA006020u)

/** \brief 24, EMEM Core Tile Control Common Memory Register */
#define EMEM_TILECC /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_TILECC*)0xFA006024u)

/** \brief 28, EMEM Core Tile Control Trace Memory Register */
#define EMEM_TILECT /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_TILECT*)0xFA006028u)

/** \brief 2C, EMEM Core Tile Status Register */
#define EMEM_TILESTATE /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_TILESTATE*)0xFA00602Cu)

/** \brief 34, EMEM Core Standby RAM Control Register */
#define EMEM_SBRCTR /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_SBRCTR*)0xFA006034u)

/** \brief F8, EMEM Core Access Enable Register 1 */
#define EMEM_ACCEN1 /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_ACCEN1*)0xFA0060F8u)

/** \brief FC, EMEM Core Access Enable Register 0 */
#define EMEM_ACCEN0 /*lint --e(923, 9078)*/ (*(volatile Ifx_EMEM_ACCEN0*)0xFA0060FCu)


/** \}  */
/******************************************************************************/
/******************************************************************************/
#endif /* IFXEMEM_REG_H */
