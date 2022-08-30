/**
 * Reg Access test for module EMEM for tc37xEXT
 *
 * This test checks EMEM registers read/write access.
 *
 */

 #include "IfxEmem_reg_ext.h"
 #include "IfxEmem_mpu_reg_ext.h"

#include "Scu/Std/IfxScuWdt.h"
#include "Cpu0_Main.h"
#include "test.h"

#define SECOND_TEST 0xFF12
#define TEST_VALUE 0xf1

// the goal of this test is to check if sw can read and write EMEM registers
uint32 test_emem_reg_access_ext(void)
{
	unsigned int reg_data = 0;
	unsigned int test_pass = 1;
	Ifx_EMEM *emem_base = ((Ifx_EMEM *)&MODULE_EMEM);

    uint16 psw = IfxScuWdt_getCpuWatchdogPassword();
    /* Clear the ENDINIT bit in the WDT_CON0 register */
    IfxScuWdt_clearCpuEndinit(psw);

    ConsolePrintS("\n======================\nAurix toolbox version\n======================\n");

    ConsolePrintS("\n======================\nEMEM_CONTROL Register\n======================\n");

	emem_base->CLC.U = TEST_VALUE;
	if (emem_base->CLC.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_CLC read ok\n");

	emem_base->ID.U = TEST_VALUE;
	if (emem_base->ID.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_ID reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_ID read ok\n");

	emem_base->TILECONFIG.U = TEST_VALUE;
	if (emem_base->TILECONFIG.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECONFIG reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECONFIG read ok\n");

	emem_base->TILECC.U = TEST_VALUE;
	if (emem_base->TILECC.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECC read ok\n");

	emem_base->TILECT.U = TEST_VALUE;
	if (emem_base->TILECT.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECT reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECT read ok\n");

	emem_base->TILESTATE.U = TEST_VALUE;
	if (emem_base->TILESTATE.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILESTATE reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILESTATE read ok\n");

	emem_base->SBRCTR.U = TEST_VALUE;
	if (emem_base->SBRCTR.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_SBRCTR reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_SBRCTR read ok\n");

	emem_base->ACCEN1.U = TEST_VALUE;
	if (emem_base->ACCEN1.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_ACCEN1 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_ACCEN1 read ok\n");

	emem_base->ACCEN0.U = TEST_VALUE;
	if (emem_base->ACCEN0.U != TEST_VALUE)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_ACCEN0 reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_ACCEN0 read ok\n");

	/* ================== MPU Registers ================== */
	uint32 offset[12] = {
		/*00*/0x0, //CLC
		/*01*/0x8, //MODID
		/*02*/0x10,//ACCEN0
		/*03*/0x14,//ACCEN1
		/*04*/0x20,//MEMCON
		/*05*/0x24,//SCTRL
		/*06*/0x50,//RGNLAi
		/*07*/0x54,//RGNUAi
		/*08*/0x58,//RGNACCENWAi
		/*09*/0x5c,//RGNACCENWBi
		/*10*/0xd8,//RGNACCENRAi
		/*11*/0xdc //RGNACCENRBi
	};

	uint32 emem_mpu_base_address[3] = {
		0xFB000000,//EMEM_MPU0
		0xFB010000,//EMEM_MPU1
		0xFB020000 //EMEM_MPU2
	};

	uint32 *base_address;
	int mpu, i;
	for(mpu = 0; mpu < 3; mpu++){
		ConsolePrintS("\n==================\nEMEM MPU");
		ConsolePrintI(mpu);
		ConsolePrintS(" reg access test\n==================\n");
		ConsolePrintEol();

		base_address = *(emem_mpu_base_address + mpu);
		for(i = 0; i < 12; i++){
			*(base_address + offset[i]) = SECOND_TEST;
			reg_data = *(base_address + offset[i]);
			if (reg_data != SECOND_TEST)
			{
				ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU reset value ");
				ConsolePrintI(offset[i]);
				ConsolePrintEol();
				test_pass = mpu*100 + i;
			}
			else
				ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU read ok\n");
		}
	}

	if (test_pass){
		ConsolePrintS("test_test_pass completed.\n");
		return 0;
	} else {
		ConsolePrintS("Error: ");
		ConsolePrintI(test_pass);
		ConsolePrintEol();
		test_pass = mpu*100 + i;
		return 1;
	}
}
