/**
 * Integration test for QSPI
 *
 * This test checks the QSPI registers reset values
 *
 */

#include "IfxGeth_reg_ext.h"

#include "Scu/Std/IfxScuWdt.h"

#include "Cpu0_Main.h"

// the goal of this test is to check STM registers reset values
uint32 test_geth_reg_access_ext(void)
{
	unsigned char test_pass = 1;
	unsigned int reg_data = 0;
	Ifx_GETH *gethBase = ((Ifx_GETH *)&MODULE_GETH);
	ConsolePrintS("\n==================\nTesting GETH\n==================\n");
    uint16 psw = IfxScuWdt_getCpuWatchdogPassword();

    /* Clear the ENDINIT bit in the WDT_CON0 register */
    IfxScuWdt_clearCpuEndinit(psw);

    ConsolePrintS("\n==================\nQSPI reg access test\n==================\n");

	if ((reg_data = gethBase->CLC.U) != 0x00000003)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : CLC read ok\n");


	//enable GETH
	gethBase->CLC.U = 0x00000000;

    IfxScuWdt_setCpuEndinit(psw);

	if ((reg_data = gethBase->CLC.U) != 0x00000000)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : CLC write ok\n");

	gethBase->MAC_CONFIGURATION.U = 0x3;
	if ((reg_data = gethBase->MAC_CONFIGURATION.U) != 0x00000003)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error MAC_CONFIGURATION reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : MAC_CONFIGURATION write ok\n");

	//disable GETH
	gethBase->CLC.U = 0x00000001;

	// ==== GETH1 Test ====

	gethBase = ((Ifx_GETH *)&MODULE_GETH1);
	ConsolePrintS("\n==================\nTesting GETH1\n==================\n");

	psw = IfxScuWdt_getCpuWatchdogPassword();

    /* Clear the ENDINIT bit in the WDT_CON0 register */
    IfxScuWdt_clearCpuEndinit(psw);

    ConsolePrintS("\n==================\nQSPI reg access test\n==================\n");

	if ((reg_data = gethBase->CLC.U) != 0x00000003)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : CLC read ok\n");

	//enable GETH
	gethBase->CLC.U = 0x00000000;

    IfxScuWdt_setCpuEndinit(psw);

	if ((reg_data = gethBase->CLC.U) != 0x00000000)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error CLC reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : CLC write ok\n");

	gethBase->MAC_CONFIGURATION.U = 0x3;
	if ((reg_data = gethBase->MAC_CONFIGURATION.U) != 0x00000003)
	{
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT FAIL : Error MAC_CONFIGURATION reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("GETH_reg_access_test : CHECKPOINT PASS : MAC_CONFIGURATION write ok\n");

	//disable GETH
	gethBase->CLC.U = 0x00000001;

    ConsolePrintS("test_geth_reg_access completed.\n");

	if (test_pass)
		return 0;
	else
		return 1;
}
