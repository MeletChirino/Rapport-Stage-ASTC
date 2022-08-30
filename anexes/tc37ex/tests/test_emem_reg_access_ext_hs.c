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
uint32 test_emem_reg_access_ext_hs(void)
{
	unsigned int reg_data = 0;
	unsigned int test_pass = 1;
	Ifx_EMEM *emem_base = ((Ifx_EMEM *)&MODULE_EMEM);
	Ifx_EMEM_MPU *emem_mpu0 = ((Ifx_EMEM_MPU *) &MODULE_EMEMMPU0);
	Ifx_EMEM_MPU *emem_mpu1 = ((Ifx_EMEM_MPU *) &MODULE_EMEMMPU1);
	Ifx_EMEM_MPU *emem_mpu2 = ((Ifx_EMEM_MPU *) &MODULE_EMEMMPU2);

    uint16 psw = IfxScuWdt_getCpuWatchdogPassword();
    /* Clear the ENDINIT bit in the WDT_CON0 register */
    IfxScuWdt_clearCpuEndinit(psw);

    ConsolePrintS("\n======================\nEMEM_CONTROL Register\n======================\n");

   	emem_base->CLC.U = 0x1;
	reg_data = emem_base->CLC.U;
	if (emem_base->CLC.U != 0x3)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_CLC disable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_CLC disable is ok\n");

	emem_base->CLC.U = 0x0;
	reg_data = emem_base->CLC.U;
	if (emem_base->CLC.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_CLC enable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_CLC enable is ok\n");

	// This is a read only register.
	reg_data = emem_base->ID.U;
	reg_data &= 0xFFFFFF00;
	// reset value 0x00E0C0XX
	if (reg_data != 0x00E0C000)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_ID reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_ID read ok\n");

	// This is a write only register, every read process should return 0x0
	emem_base->TILECONFIG.U = 0xFF595555;
	reg_data = emem_base->TILECONFIG.U;
	if (emem_base->TILECONFIG.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECONFIG read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECONFIG read/write ok\n");

	emem_base->TILECC.U = 0x00FAF1FF;
	if (emem_base->TILECC.U != 0x00FAF1FF)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECC read/write value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECC read/write ok\n");//

	emem_base->TILECT.U = 0x000300D6;
	if (emem_base->TILECT.U != 0x000300D6)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILECT value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILECT read/write ok\n");

	//This is a read only field, verifying reset value
	reg_data = emem_base->TILESTATE.U;
	if (emem_base->TILESTATE.U != 0xFFFFFFFF)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_TILESTATE reset value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_TILESTATE read reset value ok\n");

	// Unlocking Stand by lock flag
	emem_base->SBRCTR.U = 0x2;
	emem_base->SBRCTR.U = 0x6;
	emem_base->SBRCTR.U = 0xE;
	reg_data = emem_base->SBRCTR.U;
	if (emem_base->SBRCTR.U != 0x1)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_SBRCTR not unlocked ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_SBRCTR unlock sequence ok\n");

	// Locking Stand by lock flag
	emem_base->SBRCTR.U = 0x90;
	reg_data = emem_base->SBRCTR.U;
	if (emem_base->SBRCTR.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_SBRCTR locked ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_SBRCTR lock ok\n");

	emem_base->ACCEN1.U = 0x0;
	if (emem_base->ACCEN1.U != 0x0)
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
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_ACCEN0 read value ");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_ACCEN0 read/write ok\n");

    ConsolePrintS("\n======================\nEMEM_MPU0 Register\n======================\n");

    emem_mpu0->CLC.U = 0x1;
	reg_data = emem_mpu0->CLC.U;
	if (emem_mpu0->CLC.U != 0x3)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC disable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC disable is ok\n");


    emem_mpu0->CLC.U = 0x0;
	reg_data = emem_mpu0->CLC.U;
	if (emem_mpu0->CLC.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC enable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC enable is ok\n");

	// MODID register
	// This is a read only register, verifying reset value
	reg_data = emem_mpu0->MODID.U;
	reg_data &= 0xFFFFFF00;
	if (reg_data != 0x0088C000){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MODID reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MODID reset value ok\n");

	// ACCEN0 register
	emem_mpu0->ACCEN0.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu0->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN0 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN0 read/write ok\n");

	// ACCEN1 register
	emem_mpu0->ACCEN1.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu0->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN1 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN1 read/write ok\n");

	// MEMCON
	// verifying reset value
	reg_data = emem_mpu0->MEMCON.U;
	if (reg_data != 0X0){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MEMCON reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MEMCON	reset value ok\n");

	// SCTRL
	// verifying reset value
	reg_data = emem_mpu0->SCTRL.U;
	if (reg_data != 0X20600){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_SCTRL reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_SCTRL	reset value ok\n");

	for(int i = 0; i < 8; i++){
		ConsolePrintS("\nIdx = ");
		ConsolePrintI(i);
		ConsolePrintEol();
		reg_data = emem_mpu0->RGNWRN[i].RGNLA.U;
		if (reg_data != 0x0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNLA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNLA	reset value ok\n");

		reg_data = emem_mpu0->RGNWRN[i].RGNUA.U;
		if (reg_data != 0xFFFFFFE0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNUA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNUA	reset value ok\n");

		reg_data = emem_mpu0->RGNWRN[i].RGNACCENWA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWA	reset value ok\n");

		reg_data = emem_mpu0->RGNWRN[i].RGNACCENWB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWB	reset value ok\n");

		reg_data = emem_mpu0->RGNACCEN[i].RGNACCENRA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRA	reset value ok\n");

		reg_data = emem_mpu0->RGNACCEN[i].RGNACCENRB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRB	reset value ok\n");
	}

    ConsolePrintS("\n======================\nEMEM_MPU1 Register\n======================\n");

    emem_mpu1->CLC.U = 0x1;
	reg_data = emem_mpu1->CLC.U;
	if (emem_mpu1->CLC.U != 0x3)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC disable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC disable is ok\n");


    emem_mpu1->CLC.U = 0x0;
	reg_data = emem_mpu1->CLC.U;
	if (emem_mpu1->CLC.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC enable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC enable is ok\n");

	// MODID register
	// This is a read only register, verifying reset value
	reg_data = emem_mpu1->MODID.U;
	reg_data &= 0xFFFFFF00;
	if (reg_data != 0x0088C000){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MODID reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MODID reset value ok\n");

	// ACCEN0 register
	emem_mpu1->ACCEN0.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu1->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN0 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN0 read/write ok\n");

	// ACCEN1 register
	emem_mpu1->ACCEN1.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu1->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN1 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN1 read/write ok\n");

	// MEMCON
	// verifying reset value
	reg_data = emem_mpu1->MEMCON.U;
	if (reg_data != 0X0){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MEMCON reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MEMCON	reset value ok\n");

	// SCTRL
	// verifying reset value
	reg_data = emem_mpu1->SCTRL.U;
	if (reg_data != 0X20600){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_SCTRL reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_SCTRL	reset value ok\n");

	for(int i = 0; i < 8; i++){
		ConsolePrintS("\nIdx = ");
		ConsolePrintI(i);
		ConsolePrintEol();
		reg_data = emem_mpu1->RGNWRN[i].RGNLA.U;
		if (reg_data != 0x0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNLA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNLA	reset value ok\n");

		reg_data = emem_mpu1->RGNWRN[i].RGNUA.U;
		if (reg_data != 0xFFFFFFE0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNUA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNUA	reset value ok\n");

		reg_data = emem_mpu1->RGNWRN[i].RGNACCENWA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWA	reset value ok\n");

		reg_data = emem_mpu1->RGNWRN[i].RGNACCENWB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWB	reset value ok\n");

		reg_data = emem_mpu1->RGNACCEN[i].RGNACCENRA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRA	reset value ok\n");

		reg_data = emem_mpu1->RGNACCEN[i].RGNACCENRB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRB	reset value ok\n");
	}


    ConsolePrintS("\n======================\nEMEM_MPU2 Register\n======================\n");

    emem_mpu2->CLC.U = 0x1;
	reg_data = emem_mpu2->CLC.U;
	if (emem_mpu2->CLC.U != 0x3)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC disable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC disable is ok\n");


    emem_mpu2->CLC.U = 0x0;
	reg_data = emem_mpu2->CLC.U;
	if (emem_mpu2->CLC.U != 0x0)
	{
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_CLC enable is not possible\n");
        ConsolePrintI(reg_data);
        ConsolePrintEol();
		test_pass = 0;
	}
	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_CLC enable is ok\n");

	// MODID register
	// This is a read only register, verifying reset value
	reg_data = emem_mpu2->MODID.U;
	reg_data &= 0xFFFFFF00;
	if (reg_data != 0x0088C000){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MODID reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MODID reset value ok\n");

	// ACCEN0 register
	emem_mpu2->ACCEN0.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu2->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN0 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN0 read/write ok\n");

	// ACCEN1 register
	emem_mpu2->ACCEN1.U = (unsigned int)TEST_VALUE;
	reg_data = emem_mpu2->ACCEN0.U;
	if (reg_data != TEST_VALUE){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_ACCEN1 read/write ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_ACCEN1 read/write ok\n");

	// MEMCON
	// verifying reset value
	reg_data = emem_mpu2->MEMCON.U;
	if (reg_data != 0X0){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_MEMCON reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_MEMCON	reset value ok\n");

	// SCTRL
	// verifying reset value
	reg_data = emem_mpu2->SCTRL.U;
	if (reg_data != 0X20600){
		ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_SCTRL reset value ");
		ConsolePrintI(reg_data);
		ConsolePrintEol();
		test_pass = 0;
	}	else
		ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_SCTRL	reset value ok\n");

	for(int i = 0; i < 8; i++){
		ConsolePrintS("\nIdx = ");
		ConsolePrintI(i);
		ConsolePrintEol();
		reg_data = emem_mpu2->RGNWRN[i].RGNLA.U;
		if (reg_data != 0x0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNLA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNLA	reset value ok\n");

		reg_data = emem_mpu2->RGNWRN[i].RGNUA.U;
		if (reg_data != 0xFFFFFFE0){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNUA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNUA	reset value ok\n");

		reg_data = emem_mpu2->RGNWRN[i].RGNACCENWA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWA	reset value ok\n");

		reg_data = emem_mpu2->RGNWRN[i].RGNACCENWB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENWB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENWB	reset value ok\n");

		reg_data = emem_mpu2->RGNACCEN[i].RGNACCENRA.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRA reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRA	reset value ok\n");

		reg_data = emem_mpu2->RGNACCEN[i].RGNACCENRB.U;
		if (reg_data != 0xFFFFFFFF){
			ConsolePrintS("emem_reg_access_test : CHECKPOINT FAIL : Error EMEM_MPU_RGNACCENRB reset value ");
			ConsolePrintI(reg_data);
			ConsolePrintEol();
			test_pass = 0;
		}	else
			ConsolePrintS("emem_reg_access_test : CHECKPOINT PASS : EMEM_MPU_RGNACCENRB reset value ok\n");
	}
	// =========================================================================
	// FINISH TEST
	// =========================================================================
	if (test_pass){
		ConsolePrintS("test_test_pass completed.\n");
		return 0;
	} else {
		ConsolePrintS("Error: ");
		ConsolePrintI(test_pass);
		ConsolePrintEol();
		return 1;
	}
}
