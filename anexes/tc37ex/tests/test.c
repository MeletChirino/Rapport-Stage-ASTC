#include "Ifx_reg.h"
#include "Scu/Std/IfxScuWdt.h"
#include "IfxCpu.h"

IFX_EXTERN void ConsolePrintTestPass(void);
IFX_EXTERN void ConsolePrintTestFail(void);
uint32 test_vp(void);
uint32 test_simple(void);
uint32 test_asclin_reg_access(void);
uint32 test_asclin_asc(void);
uint32 test_asclin_lin(void);
uint32 test_asclin_spi(void);
uint32 test_asclin_master(void);
uint32 test_asclin_slave(void);
uint32 test_dma_reg_access(void);
uint32 test_dma_spb_transfer(void);
uint32 test_dma_sri_transfer(void);
uint32 test_evadc_queue_transfer(void);
uint32 test_evadc_reg_access(void);
uint32 test_evadc_reg_protections(void);
uint32 test_edsadc_reg_access(void);
uint32 test_flexray_reg_access(void);
uint32 test_geth_reg_access(void);
uint32 test_geth_tx(void);
uint32 test_gtm_continental_issue_ldmst(void);
uint32 test_gtm_reg_access(void);
uint32 test_gtm_reg_access_astc_gtm(void);
uint32 test_lmu(void);
uint32 test_mcmcan_interrupts(void);
uint32 test_mcmcan_interrupts_token(void);
uint32 test_mcmcan_mcmcan1_send_to_mcmcan0(void);
uint32 test_mcmcan_mcmcan1_send_to_mcmcan0_fd(void);
uint32 test_mcmcan_mcmcan1_send_to_mcmcan0_fd_brse(void);
uint32 test_mcmcan_mcmcan1_send_to_mcmcan0_token(void);
uint32 test_mcmcan_node_can_ext_send_all_mcan_receives(void);
uint32 test_mcmcan_node_can_ext_send_all_mcan_receives_token(void);
uint32 test_mcmcan_node_can_ext_send_mcan_filter_receives(void);
uint32 test_mcmcan_node_can_ext_send_mcan_filter_receives_token(void);
uint32 test_mcmcan_reg_access(void);
uint32 test_mcmcan_reg_access_cccr_init(void);
uint32 test_mcmcan_reset_choice_clocks(void);
uint32 test_msc_basic_transmit(void);
uint32 test_msc_basic_transmit_interrupt(void);
uint32 test_nvm_load_page_64_bit(void);
uint32 test_nvm_pflash_erase_write_verify(void);
uint32 test_qspi_loopback(void);
uint32 test_qspi_mtsr_mrst(void);
uint32 test_qspi_mtsr_mrst_dma(void);
uint32 test_qspi_qspi_dma(void);
uint32 test_qspi_qspi_master_simple_rx_tx_testbench_slave(void);
uint32 test_qspi_qspi_slave_simple_rx_tx_testbench_master(void);
uint32 test_qspi_reg_access(void);
uint32 test_scu_app_reset(void);
uint32 test_scu_sys_reset(void);
uint32 test_sent_receive(void);
uint32 test_stm_reg_access(void);
uint32 test_stm_reg_reset(void);
uint32 test_stm_timeout_irq(void);
uint32 test_stm_timeout_irq_after_sys_reset(void);
uint32 test_scu_smu_app_reset(void);
uint32 test_dma_linked_list(void);
uint32 test_dma_memory_range(void);
uint32 test_dma_adc(void);
uint32 test_dflash_pflash(void);
uint32 test_smu_reg_access(void);
uint32 test_smu_emergency_stop(void);
uint32 test_smu_reset_alarm(void);
uint32 test_smu_ir_alarm(void);
uint32 test_smu_fault_signaling(void);
uint32 test_scu_smu_sys_reset(void);
// Next tests are only for TC37x_EXT
uint32 test_mcmcan_reg_access_ext(void);
uint32 test_geth_reg_access_ext(void);
uint32 test_emem_reg_access_ext_hs(void);// This is used for hs emem version
uint32 test_emem_reg_access_ext(void);
uint32 test_io_reg_access(void);
uint32 test_io_port_modes(void);
uint32 test_dma_pspr0_pspr1(void);
uint32 test_qspi_cpu(void);
uint32 test_dma_hw_sw_transactions(void);
uint32 test_dma_shadow_operation_read_only_mode_channel_active(void);
uint32 test_dma_move_sadr_equals_dadr(void);
uint32 test_dma_circular_buffer_transfer_starting_from_wrap_around_address(void);
uint32 test_dma_halt_active_channel_rroat_set(void);

volatile uint32 test_case = 0;
volatile uint32 test_case_next = 0;
volatile uint32 test_pass = 0;
volatile uint32 errors = 0;
volatile uint32 test_idx = 0;

void test_completed(void)
{
	test_case = 0;
}
uint32 get_test_case(void)
{
	return test_case;
}
void (*test_completed_ptr)(void) = &test_completed;
uint32(*get_test_case_ptr)(void) = &get_test_case;

uint32 (*test_ptrs[])() = {
		/*  0 */ test_vp, // not used
	    /*  1 */ test_vp,
	    /*  2 */ test_simple,
	    /*  3 */ test_asclin_reg_access,
		/*  4 */ test_asclin_asc,
	    /*  5 */ test_asclin_lin,
	    /*  6 */ test_asclin_spi,
	    /*  7 */ test_dma_reg_access,
	    /*  8 */ test_dma_spb_transfer,
	    /*  9 */ test_dma_sri_transfer,
	    /* 10 */ test_evadc_queue_transfer,
	    /* 11 */ test_evadc_reg_access,
	    /* 12 */ test_evadc_reg_protections,
	    /* 13 */ test_edsadc_reg_access,
	    /* 14 */ test_flexray_reg_access,
	    /* 15 */ test_geth_reg_access,
	    /* 16 */ test_geth_tx,
	    /* 17 */ test_gtm_continental_issue_ldmst,
	    /* 18 */ test_gtm_reg_access,
	    /* 19 */ test_gtm_reg_access_astc_gtm,
	    /* 20 */ test_lmu, // not used by tc36x since there is no LMU
	    /* 21 */ test_mcmcan_interrupts,
	    /* 22 */ test_mcmcan_interrupts_token,
	    /* 23 */ test_mcmcan_mcmcan1_send_to_mcmcan0,
	    /* 24 */ test_mcmcan_mcmcan1_send_to_mcmcan0_fd,
	    /* 25 */ test_mcmcan_mcmcan1_send_to_mcmcan0_fd_brse,
	    /* 26 */ test_mcmcan_mcmcan1_send_to_mcmcan0_token,
	    /* 27 */ test_mcmcan_node_can_ext_send_all_mcan_receives,
	    /* 28 */ test_mcmcan_node_can_ext_send_all_mcan_receives_token,
	    /* 29 */ test_mcmcan_node_can_ext_send_mcan_filter_receives,
	    /* 30 */ test_mcmcan_node_can_ext_send_mcan_filter_receives_token,
	    /* 31 */ test_mcmcan_reg_access,
	    /* 32 */ test_mcmcan_reg_access_cccr_init,
	    /* 33 */ test_mcmcan_reset_choice_clocks,
	    /* 34 */ test_msc_basic_transmit,
	    /* 35 */ test_msc_basic_transmit_interrupt,
	    /* 36 */ test_nvm_load_page_64_bit,
	    /* 37 */ test_nvm_pflash_erase_write_verify,
	    /* 38 */ test_qspi_loopback,
	    /* 39 */ test_qspi_mtsr_mrst,
	    /* 40 */ test_qspi_mtsr_mrst_dma,
	    /* 41 */ test_qspi_qspi_dma,
	    /* 42 */ test_qspi_qspi_master_simple_rx_tx_testbench_slave,
	    /* 43 */ test_qspi_qspi_slave_simple_rx_tx_testbench_master,
	    /* 44 */ test_qspi_reg_access,
	    /* 45 */ test_scu_app_reset,
	    /* 46 */ test_scu_sys_reset,
	    /* 47 */ test_sent_receive,
	    /* 48 */ test_stm_reg_access,
	    /* 49 */ test_stm_reg_reset,
	    /* 50 */ test_stm_timeout_irq,
	    /* 51 */ test_stm_timeout_irq_after_sys_reset,
	    /* 52 */ test_dma_linked_list,
	    /* 53 */ test_dma_memory_range,
	    /* 54 */ test_dma_adc,
	    /* 55 */ test_scu_smu_app_reset,
	    /* 56 */ test_dflash_pflash,
		/* 57 */ test_smu_reg_access,
		/* 58 */ test_smu_emergency_stop,
		/* 59 */ test_smu_reset_alarm,
		/* 60 */ test_smu_ir_alarm,
		/* 61 */ test_smu_fault_signaling,
		/* 62 */ test_scu_smu_sys_reset,
	    /* 63 */ test_io_reg_access,
	    /* 64 */ test_io_port_modes,
	    /* 65 */ test_dma_pspr0_pspr1,
	    /* 66 */ test_qspi_cpu,
		/* 67 */ test_dma_hw_sw_transactions,
		/* 68 */ test_asclin_slave,
		/* 69 */ test_asclin_master,
		// TC37x_ext tests
		/* 70 */ test_mcmcan_reg_access_ext,
		/* 71 */ test_geth_reg_access_ext,
		/* 72 */ test_emem_reg_access_ext,
		// Other DMA tests
		/* 73 */ test_dma_shadow_operation_read_only_mode_channel_active,
		/* 74 */ test_dma_move_sadr_equals_dadr,
		/* 75 */ test_dma_circular_buffer_transfer_starting_from_wrap_around_address,
		/* 76 */ test_dma_halt_active_channel_rroat_set,
		/* 77 */ test_emem_reg_access_ext_hs, // this test is used for testing emem hs version
};

void test(void)
{
	for(;;)
	{
		test_idx = (*get_test_case_ptr)();

		// Test case Index == 0 indicates no test to run
		if (test_idx == 0)
		{
			break;
		}
		errors |= (*test_ptrs[test_idx])();

		// Tests are interrupted if encountering an error
		if(errors)
		{
			break;
		}
	}
	if(errors)
	{
		ConsolePrintTestFail();
	}
	else
	{
		ConsolePrintTestPass();
	}

    // Used for VLAB script to detect the end of the test sequence
    (*test_completed_ptr)();
}
