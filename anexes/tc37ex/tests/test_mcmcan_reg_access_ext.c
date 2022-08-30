/**************************************************************************************************************************************************************************************************
* Integration test for mcmcan
*
* This test checks the mcmcan registers reset values
*
* Name: reg_access\test.c
*
* Description:
*       In this test, we check access to differents registers of three mcmcan and their associates mcan runs normally
*		Watch if access of different adress RAM for the RAM0, RAM1 and RAM2 is correct in read/write by the SW and the differents mcan
*
* Registers:
*       read/write =>  Many registers of mcmcan and mcan are write and read for check the goods dealing on the FPI (SPB bus) Spec AURIXTC3XX_ts_part1_V2.1.0 page 55
*                For more information on the registers present in this test go to the Spec AURIXTC3XX_ts_part2_V2.1.0 page 2052 Table 371
*
*
* Expected result:
*                We wait of this test just one check on the exchange on the platform bus and the mcmcan<-->mcan are good
*************************************************************************************************************************************************************************************************/


#include "IfxCan_reg_ext.h"

#include "Scu/Std/IfxScuWdt.h"

#include "Cpu0_Main.h"

/** \brief 114, Interrupt routing for Groups 1 */
#define CAN0_N0_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0208114u)
#define CAN0_N1_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0208514u)
#define CAN0_N2_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0208914u)
#define CAN0_N3_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0208D14u)
#define CAN1_N0_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0218114u)
#define CAN1_N1_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0218514u)
#define CAN1_N2_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0218914u)
#define CAN1_N3_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0218D14u)
#define CAN2_N0_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0228114u)
#define CAN2_N1_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0228514u)
#define CAN2_N2_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0228914u)
#define CAN2_N3_GRINT1 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT1*)0xF0228D14u)

/** \brief 118, Interrupt routing for Groups 2 */
#define CAN0_N0_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0208118u)
#define CAN0_N1_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0208518u)
#define CAN0_N2_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0208918u)
#define CAN0_N3_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0208D18u)
#define CAN1_N0_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0218118u)
#define CAN1_N1_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0218518u)
#define CAN1_N2_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0218918u)
#define CAN1_N3_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0218D18u)
#define CAN2_N0_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0228118u)
#define CAN2_N1_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0228518u)
#define CAN2_N2_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0228918u)
#define CAN2_N3_GRINT2 /*lint --e(923)*/ (*(volatile Ifx_CAN_N_GRINT2*)0xF0228D18u)

#define Ram0 /*lint --e(923)*/ (*(volatile maRAM0*)0xF0200000u)
#define Ram1 /*lint --e(923)*/ (*(volatile maRAM1*)0xF0210000u)
#define Ram2 /*lint --e(923)*/ (*(volatile maRAM2*)0xF0220000u)

typedef union
{
    Ifx_UReg_32Bit U;                 /**< \brief Unsigned access */
    Ifx_SReg_32Bit I;                 /**< \brief Signed access */
    Ifx_CAN_N_GRINT2_Bits B;            /**< \brief Bitfield access */
} maRAM0;

typedef union
{
    Ifx_UReg_32Bit U;                 /**< \brief Unsigned access */
    Ifx_SReg_32Bit I;                 /**< \brief Signed access */
    Ifx_CAN_N_GRINT2_Bits B;            /**< \brief Bitfield access */
} maRAM1;

typedef union
{
    Ifx_UReg_32Bit U;                 /**< \brief Unsigned access */
    Ifx_SReg_32Bit I;                 /**< \brief Signed access */
    Ifx_CAN_N_GRINT2_Bits B;            /**< \brief Bitfield access */
} maRAM2;

uint32 test_mcmcan_reg_access_ext(void)
{
	unsigned char test_pass = 1;
	unsigned int reg_data = 0;
  	Ifx_CAN *mcmcan0 = ((Ifx_CAN *)&MODULE_CAN0);
  	Ifx_CAN *mcmcan1 = ((Ifx_CAN *)&MODULE_CAN1);
  	Ifx_CAN *mcmcan2 = ((Ifx_CAN *)&MODULE_CAN2);

    ConsolePrintS("\n====================================\nMCMCAN0 reg access test\n====================================\n");
	ConsolePrintS("\n======================\nGlobal Register\n======================\n");

	if ((reg_data = mcmcan0->CLC.U) != 0x00000003)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_CLC read ok\n");

	if ((reg_data = mcmcan0->ACCEN0.U) != 0xFFFFFFFF)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_ACCEN0 reset value");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_ACCEN0 read ok\n");
	
	// To be able to change the clock settings the following programming sequence needs to be met (TC37xEXT_appx_um_v2.0.pdf p.850)
	mcmcan0->MCR.U = 0xC000001B;
	__dsync();
	mcmcan0->MCR.U = 0x0000001B;
	__dsync();
	if ((reg_data = mcmcan0->MCR.U) != 0x0000001B)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_MCR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_MCR write ok\n");

	ConsolePrintS("\n===================\nNode Specific Register\n===================\n");

	if ((reg_data = CAN0_N0_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_N0_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N0_STARTADR read ok\n");

	if ((reg_data = CAN0_N1_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_N1_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N1_STARTADR read ok\n");

	if ((reg_data = CAN0_N2_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_N2_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N2_STARTADR read ok\n");

	if ((reg_data = CAN0_N3_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_N3_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N3_STARTADR read ok\n");

	CAN0_N0_GRINT1.U = 0x76543210;
	if ((reg_data = CAN0_N0_GRINT1.U) != 0x76543210)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_N0_GRINT1 expected value = 0x76543210, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N0_GRINT1 read ok\n");

	CAN0_N0_GRINT2.U = 0xFEDCBA98;
	if ((reg_data = CAN0_N0_GRINT2.U) != 0xFEDCBA98)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_N0_GRINT2 expected value = 0xFEDCBA98, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N0_GRINT2 read ok\n");

	CAN0_N3_GRINT1.U = 0x76543210;
	if ((reg_data = CAN0_N3_GRINT1.U) != 0x76543210)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_N3_GRINT1 expected value = 0x76543210, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N3_GRINT1 read ok\n");

	CAN0_N3_GRINT2.U = 0xFEDCBA98;
	if ((reg_data = CAN0_N3_GRINT2.U) != 0xFEDCBA98)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_N3_GRINT2 expected value = 0xFEDCBA98, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_N3_GRINT2 read ok\n");

	ConsolePrintS("\n=======================\nMCAN Register\n=======================\n");

	if ((reg_data = CAN0_CCCR0.U) != 0x00000001)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_CCCR0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_CCCR0 read ok\n");

	if ((reg_data = CAN0_IE0.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error CAN0_IE0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_IE0 read ok\n");

	CAN0_IE0.U = 0xFFFFFFFF;
	if ((reg_data = CAN0_IE0.U) != 0x3fffffff)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_IE0 expected value = 0x3fffffff, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_IE0 read ok\n");

	CAN0_IE2.U = 0xFFFFFFFF;
	if ((reg_data = CAN0_IE2.U) != 0x3fffffff)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : CAN0_IE2 expected value = 0x3fffffff, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : CAN0_IE2 read ok\n");

	ConsolePrintS("\n=======================\n RAM0 \n=======================\n");

	Ram0.U = 0x00118218;
	if ((reg_data = Ram0.U) != 0x00118218)
	{
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT FAIL : Error RAM0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN0_reg_access_test : CHECKPOINT PASS : RAM0 read ok\n");

	ConsolePrintS("\n========================================================================\n");


	ConsolePrintS("\n====================================\nMCMCAN1 reg access test\n====================================\n");
	ConsolePrintS("\n======================\nGlobal Register\n======================\n");

	if ((reg_data = mcmcan1->CLC.U) != 0x00000003)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_CLC read ok\n");

	if ((reg_data = mcmcan1->ACCEN0.U) != 0xFFFFFFFF)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_ACCEN0 reset value");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_ACCEN0 read ok\n");

	// define the active Clocks on the mcan according to p.70 of AURIXTC3XX_ts_part2_V2.5.1.pdf
	mcmcan1->MCR.U = 0xC000001B;
	__dsync();
	mcmcan1->MCR.U = 0x0000001B;
	__dsync();
	if ((reg_data = mcmcan1->MCR.U) != 0x0000001B)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_MCR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_MCR write ok\n");

	ConsolePrintS("\n===================\nNode Specific Register\n===================\n");

	if ((reg_data = CAN1_N0_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_N0_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N0_STARTADR read ok\n");

	if ((reg_data = CAN1_N1_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_N1_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N1_STARTADR read ok\n");

	if ((reg_data = CAN1_N2_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_N2_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N2_STARTADR read ok\n");

	if ((reg_data = CAN1_N3_STARTADR.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_N3_STARTADR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N3_STARTADR read ok\n");

	CAN1_N0_GRINT1.U = 0x76543210;
	if ((reg_data = CAN1_N0_GRINT1.U) != 0x76543210)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_N0_GRINT1 expected value = 0x76543210, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N0_GRINT1 read ok\n");

	CAN1_N0_GRINT2.U = 0xFEDCBA98;
	if ((reg_data = CAN1_N0_GRINT2.U) != 0xFEDCBA98)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_N0_GRINT2 expected value = 0xFEDCBA98, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N0_GRINT2 read ok\n");

	CAN1_N3_GRINT1.U = 0x76543210;
	if ((reg_data = CAN1_N3_GRINT1.U) != 0x76543210)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_N3_GRINT1 expected value = 0x76543210, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N3_GRINT1 read ok\n");

	CAN1_N3_GRINT2.U = 0xFEDCBA98;
	if ((reg_data = CAN1_N3_GRINT2.U) != 0xFEDCBA98)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_N3_GRINT2 expected value = 0xFEDCBA98, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_N3_GRINT2 read ok\n");

	ConsolePrintS("\n=======================\nMCAN Register\n=======================\n");

	if ((reg_data = CAN1_CCCR0.U) != 0x00000001)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_CCCR0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_CCCR0 read ok\n");

	if ((reg_data = CAN1_IE0.U) != 0x00000000)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error CAN1_IE0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_IE0 read ok\n");

	CAN1_IE0.U = 0xFFFFFFFF;
	if ((reg_data = CAN1_IE0.U) != 0x3fffffff)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_IE0 expected value = 0x3fffffff, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_IE0 read ok\n");

	CAN1_IE2.U = 0xFFFFFFFF;
	if ((reg_data = CAN1_IE2.U) != 0x3fffffff)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : CAN1_IE2 expected value = 0x3fffffff, read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : CAN1_IE2 read ok\n");

	ConsolePrintS("\n=======================\n RAM0 \n=======================\n");

	Ram1.U = 0x00118712;
	if ((reg_data = Ram1.U) != 0x00118712)
	{
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT FAIL : Error RAM1 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("MCMCAN1_reg_access_test : CHECKPOINT PASS : RAM1 read ok\n");
	ConsolePrintS("\n========================================================================\n");

	ConsolePrintS("\n====================================\nMCMCAN2 reg access test\n====================================\n");
		ConsolePrintS("\n======================\nGlobal Register\n======================\n");

		if ((reg_data = mcmcan2->CLC.U) != 0x00000003)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_CLC reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_CLC read ok\n");

		if ((reg_data = mcmcan2->ACCEN0.U) != 0xFFFFFFFF)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_ACCEN0 reset value");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_ACCEN0 read ok\n");

		// define the active Clocks on the mcan according to p.70 of AURIXTC3XX_ts_part2_V2.5.1.pdf
		mcmcan2->MCR.U = 0xC000001B;
		__dsync();
		mcmcan2->MCR.U = 0x0000001B;
		__dsync();
		if ((reg_data = mcmcan2->MCR.U) != 0x0000001B)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_MCR reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_MCR write ok\n");

		ConsolePrintS("\n===================\nNode Specific Register\n===================\n");

		if ((reg_data = CAN2_N0_STARTADR.U) != 0x00000000)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_N0_STARTADR reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N0_STARTADR read ok\n");

		if ((reg_data = CAN2_N1_STARTADR.U) != 0x00000000)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_N1_STARTADR reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N1_STARTADR read ok\n");

		if ((reg_data = CAN2_N2_STARTADR.U) != 0x00000000)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_N2_STARTADR reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N2_STARTADR read ok\n");

		if ((reg_data = CAN2_N3_STARTADR.U) != 0x00000000)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_N3_STARTADR reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N3_STARTADR read ok\n");

		CAN2_N0_GRINT1.U = 0x76543210;
		if ((reg_data = CAN2_N0_GRINT1.U) != 0x76543210)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_N0_GRINT1 expected value = 0x76543210, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N0_GRINT1 read ok\n");

		CAN2_N0_GRINT2.U = 0xFEDCBA98;
		if ((reg_data = CAN2_N0_GRINT2.U) != 0xFEDCBA98)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_N0_GRINT2 expected value = 0xFEDCBA98, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N0_GRINT2 read ok\n");

		CAN2_N3_GRINT1.U = 0x76543210;
		if ((reg_data = CAN2_N3_GRINT1.U) != 0x76543210)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_N3_GRINT1 expected value = 0x76543210, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N3_GRINT1 read ok\n");

		CAN2_N3_GRINT2.U = 0xFEDCBA98;
		if ((reg_data = CAN2_N3_GRINT2.U) != 0xFEDCBA98)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_N3_GRINT2 expected value = 0xFEDCBA98, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_N3_GRINT2 read ok\n");

		ConsolePrintS("\n=======================\nMCAN Register\n=======================\n");

		if ((reg_data = CAN2_CCCR0.U) != 0x00000001)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_CCCR0 reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_CCCR0 read ok\n");

		if ((reg_data = CAN2_IE0.U) != 0x00000000)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error CAN2_IE0 reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_IE0 read ok\n");

		CAN2_IE0.U = 0xFFFFFFFF;
		if ((reg_data = CAN2_IE0.U) != 0x3fffffff)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_IE0 expected value = 0x3fffffff, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_IE0 read ok\n");

		CAN2_IE2.U = 0xFFFFFFFF;
		if ((reg_data = CAN2_IE2.U) != 0x3fffffff)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : CAN2_IE2 expected value = 0x3fffffff, read value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : CAN2_IE2 read ok\n");

		ConsolePrintS("\n=======================\n RAM0 \n=======================\n");

		Ram1.U = 0x00118712;
		if ((reg_data = Ram1.U) != 0x00118712)
		{
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT FAIL : Error RAM1 reset value ");
	        ConsolePrintI(reg_data);
	        ConsolePrintEol();
			test_pass = 0;
		}
		else
			ConsolePrintS("MCMCAN2_reg_access_test : CHECKPOINT PASS : RAM1 read ok\n");
		ConsolePrintS("\n========================================================================\n");

	CAN0_IE0.U = 0x00000000;
	CAN1_IE0.U = 0x00000000;
	CAN2_IE0.U = 0x00000000;

    ConsolePrintS("test_mcmcan_reg_access completed.\n");
	if (test_pass)
		return 0;
	else
		return 1;
}
