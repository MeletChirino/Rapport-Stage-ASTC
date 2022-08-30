import aurix
import aurix.customtypes
import aurix.licensing
import aurix.common
import aurix.memblock
import aurix.gtm_debug_interface
import aurix.stub_utils
import aurix.software_probes
import aurix.gentest_scenario
import aurix.analysis_delegate
import aurix.testbench_components

#tc27xb variant
import aurix.tc27xb
import aurix.tc27xb.__main__
import aurix.tc27xb.sim
import aurix.tc27xb.description
import aurix.tc27xb.defines
import aurix.tc27xb.stubs

#tc27x variant
import aurix.tc27x
import aurix.tc27x.__main__
import aurix.tc27x.sim
import aurix.tc27x.description
import aurix.tc27x.defines
import aurix.tc27x.stubs

#tc29x variant
import aurix.tc29x
import aurix.tc29x.__main__
import aurix.tc29x.sim
import aurix.tc29x.description
import aurix.tc29x.defines
import aurix.tc29x.stubs

#tc33x variant
import aurix.tc33x
import aurix.tc33x.__main__
import aurix.tc33x.sim
import aurix.tc33x.description
import aurix.tc33x.defines
import aurix.tc33x.model_stubs
import aurix.tc33x.core
import aurix.tc33x.dmu
import aurix.tc33x.pin_mapping

#tc39x variant
import aurix.tc39x
import aurix.tc39x.__main__
import aurix.tc39x.sim
import aurix.tc39x.description
import aurix.tc39x.defines
import aurix.tc39x.model_stubs
import aurix.tc39x.core
import aurix.tc39x.dmu
import aurix.tc39x.lmu
import aurix.tc39x.dam
import aurix.tc39x.minimcds
import aurix.tc39x.ed_ram
import aurix.tc39x.bbb

#tc39xB variant
import aurix.tc39xb
import aurix.tc39xb.__main__
import aurix.tc39xb.sim
import aurix.tc39xb.description
import aurix.tc39xb.defines
import aurix.tc39xb.model_stubs
import aurix.tc39xb.core
import aurix.tc39xb.dmu
import aurix.tc39xb.lmu
import aurix.tc39xb.dam
import aurix.tc39xb.minimcds
import aurix.tc39xb.ed_ram
import aurix.tc39xb.bbb

#tc38x variant
import aurix.tc38x
import aurix.tc38x.__main__
import aurix.tc38x.sim
import aurix.tc38x.description
import aurix.tc38x.defines
import aurix.tc38x.model_stubs
import aurix.tc38x.core
import aurix.tc38x.dmu
import aurix.tc38x.lmu0
import aurix.tc38x.dam0
import aurix.tc38x.pin_mapping

#tc36x variant
import aurix.tc36x
import aurix.tc36x.__main__
import aurix.tc36x.sim
import aurix.tc36x.description
import aurix.tc36x.defines
import aurix.tc36x.model_stubs
import aurix.tc36x.core
import aurix.tc36x.dmu
import aurix.tc36x.lmu0
import aurix.tc36x.dam0
import aurix.tc36x.pin_mapping

#tc37x variant
import aurix.tc37x
import aurix.tc37x.__main__
import aurix.tc37x.sim
import aurix.tc37x.description
import aurix.tc37x.defines
import aurix.tc37x.model_stubs
import aurix.tc37x.core
import aurix.tc37x.dmu
import aurix.tc37x.dam0
import aurix.tc37x.pin_mapping

#tc3ex variant
import aurix.tc3ex
import aurix.tc3ex.__main__
import aurix.tc3ex.sim

#tc37xext variant
import aurix.tc37xext
import aurix.tc37xext.__main__
import aurix.tc37xext.sim
import aurix.tc37xext.emem

#tcxx_perf variant
import aurix.tcxx_perf
import aurix.tcxx_perf.__main__
import aurix.tcxx_perf.sim
import aurix.tcxx_perf.description
import aurix.tcxx_perf.defines
import aurix.tcxx_perf.model_stubs

#mini aurix with MCAN FD
# import aurix.tc2xx_mcan_fd
# import aurix.tc2xx_mcan_fd.__main__
# import aurix.tc2xx_mcan_fd.sim
# import aurix.tc2xx_mcan_fd.description
# import aurix.tc2xx_mcan_fd.defines


# Include all models

import aurix.ifx_tricore_tc162p
import aurix.ifx_tricore_tc162p.analysis_interface
import aurix.ifx_tricore_tc162p.assembler
import aurix.ifx_tricore_tc162p.core
import aurix.ifx_tricore_tc162p.description
import aurix.ifx_tricore_tc162p.disassembler
import aurix.ifx_tricore_tc162p.execution_logger
import aurix.ifx_tricore_tc162p.execution_tracer
import aurix.ifx_tricore_tc162p.iss_debug_facade
import aurix.ifx_tricore_tc162p.translation_tracer

# ASTC models
import aurix.sc_TSIM
import aurix.ifx_tc3xx_sri_xbar
import aurix.ifx_tc3xx_sri_xbar_description

# import aurix.mcan
import aurix.memory_model
import aurix.console
import aurix.ClockAdapter
import aurix.IfxTlmExtensions
import aurix.AnalogPorts
import aurix.ClockedRouter
import aurix.gtm_debug
import aurix.sc_splitter
import aurix.SentSensor
import aurix.socket_adapter
import aurix.NotGate
import aurix.OrGate
import aurix.AndGate
import aurix.IRAdapter

# import Marvell 88Q5050 switch
import aurix.MDIO_bus
import aurix.marvell_88Q5050

# IFX common models
import aurix.IfxConfigWrapper

# tc27xB
import aurix.IfxIr_TC27xB
import aurix.IfxScu2_TC27xB
import aurix.IfxAscLin_TC27xB
import aurix.IfxQspi_TC27xB
import aurix.IfxPsi5_TC27xB
import aurix.Gtm_TC27xB
import aurix.IfxGtmImplementation_TC27xB
import aurix.IfxVadc_TC27xB
import aurix.IfxDma_TC27xB

# tc27xC and tc29x
import aurix.IfxStm2
import aurix.IfxDsadc_TC27xC_TC29x
import aurix.IfxPorts2_TC27xC_TC29x
import aurix.IfxIr_TC27xC_TC29x
import aurix.IfxScu2_TC27xC_TC29x
import aurix.IfxAscLin_TC27xC_TC29x
import aurix.IfxQspi_TC27xC_TC29x
import aurix.IfxPsi5_TC27xC_TC29x
import aurix.Gtm_TC27xC_TC29x
import aurix.IfxGtmImplementation_TC27xC_TC29x
import aurix.IfxDma_TC27xC_TC29x
import aurix.IfxVadc_TC27xC_TC29x

# common tc3xx
import aurix.IfxIr_TC3xx
import aurix.IfxStm2_TC3xx
import aurix.IfxQspi_TC3xx
import aurix.IfxMsc3_TC3xx
import aurix.IfxSent2_TC3xx
import aurix.mcan
import aurix.mcan_description
import aurix.ifx_tc3xx_mcmcan #same model for all variants, attribute to be setup to choose the requested variant
import aurix.IfxPorts3_TC3xx
import aurix.Gtm_TC3xx
import aurix.ifx_tc3xx_stm
import aurix.ifx_tc3xx_stm_description
import aurix.ERay
import aurix.ERay_description
import aurix.ifx_tc3xx_dmu
import aurix.ifx_tc3xx_dmu_description
import aurix.IfxAscLin_TC3xx
# tc39xA step
import aurix.IfxScu3_TC39x
import aurix.IfxGtmImplementation_TC39x
import aurix.IfxEvadc_TC39x
import aurix.IfxSmu3_TC39x
import aurix.IfxDma_TC39x
import aurix.IfxEdsadc_TC39x
# tc39xB and TC38x
import aurix.IfxScu3_TC39xB_TC38x
import aurix.IfxGtmImplementation_TC39xB_TC38x
import aurix.IfxSmu3_TC39xB_TC38x
import aurix.IfxDma_TC39xB_TC38x
import aurix.IfxEvadc_TC38x
import aurix.IfxEvadc_TC39xB
import aurix.IfxEdsadc_TC39xB
import aurix.ifx_tc3xx_geth
import aurix.ifx_tc3xx_geth_description

# ASTC implementation of the Bosch's GTM
import aurix.bosch_gtm.vlab.bosch_gtm_description
import aurix.bosch_gtm_stub_description
import aurix.bosch_gtm.vlab.gtm_constants
import aurix.bosch_gtm.vlab.mcs_channel_description
import aurix.bosch_gtm.vlab.mcs_description
import aurix.bosch_gtm.vlab.proxy_modules
import aurix.bosch_gtm.gtm_pms_mcs.core
import aurix.bosch_gtm.gtm_pms_mcs.description
import aurix.bosch_gtm.gtm_pms_mcs.disassembler
import aurix.bosch_gtm.gtm_pms_mcs.execution_logger
import aurix.bosch_gtm.gtm_pms_mcs.execution_tracer
import aurix.bosch_gtm.gtm_pms_mcs.iss_debug_facade
import aurix.bosch_gtm.gtm_pms_mcs.translation_tracer
import aurix.bosch_gtm.GTM_RM_30325.standard.bosch_gtm
import aurix.bosch_gtm.GTM_RM_30325.enhanced.bosch_gtm
import aurix.bosch_gtm.GTM_RM_31504.standard.bosch_gtm
import aurix.bosch_gtm.GTM_RM_31504.enhanced.bosch_gtm
import aurix.bosch_gtm.GTM_RM_31505.standard.bosch_gtm
import aurix.bosch_gtm.GTM_RM_31505.enhanced.bosch_gtm

# Models metadata
#common tc2xx
import aurix.metadata_common_tc2xx.metadata_STM
import aurix.metadata_common_tc2xx.metadata_IR
import aurix.metadata_common_tc2xx.metadata_MCAN
import aurix.metadata_common_tc2xx.metadata_ASCLIN
import aurix.metadata_common_tc2xx.metadata_QSPI
import aurix.metadata_common_tc2xx.metadata_PSI5
import aurix.metadata_common_tc2xx.metadata_DMA
import aurix.metadata_common_tc2xx.metadata_PORTS
import aurix.metadata_common_tc2xx.metadata_LMU
#tc27xb
import aurix.metadata_tc27xb.metadata_SCU
import aurix.metadata_tc27xb.metadata_GTM
import aurix.metadata_tc27xb.metadata_GTMWrapper
import aurix.metadata_tc27xb.metadata_DSADC
import aurix.metadata_tc27xb.metadata_MultiCAN
import aurix.metadata_tc27xb.metadata_FLASH0
import aurix.metadata_tc27xb.metadata_MTU
import aurix.metadata_tc27xb.metadata_MTU_MC
import aurix.metadata_tc27xb.metadata_XBAR_SRI
import aurix.metadata_tc27xb.metadata_VADC
#tc27xc
import aurix.metadata_tc27xc.metadata_SCU
import aurix.metadata_tc27xc.metadata_GTM
import aurix.metadata_tc27xc.metadata_GTMWrapper
import aurix.metadata_tc27xc.metadata_DSADC
import aurix.metadata_tc27xc.metadata_MultiCAN
import aurix.metadata_tc27xc.metadata_FLASH0
import aurix.metadata_tc27xc.metadata_MTU
import aurix.metadata_tc27xc.metadata_MTU_MC
import aurix.metadata_tc27xc.metadata_XBAR_SRI
import aurix.metadata_tc27xc.metadata_VADC
#tc29x
import aurix.metadata_tc29x.metadata_SCU
import aurix.metadata_tc29x.metadata_GTM
import aurix.metadata_tc29x.metadata_GTMWrapper
import aurix.metadata_tc29x.metadata_DSADC
import aurix.metadata_tc29x.metadata_MultiCAN
import aurix.metadata_tc29x.metadata_FLASH0
import aurix.metadata_tc29x.metadata_MTU
import aurix.metadata_tc29x.metadata_MTU_MC
import aurix.metadata_tc29x.metadata_XBAR_SRI
import aurix.metadata_tc29x.metadata_EBU
import aurix.metadata_tc29x.metadata_VADC
#common tc3xx
import aurix.metadata_common_tc3xx.metadata_PORTS
import aurix.metadata_common_tc3xx.metadata_ASCLIN
#tc39x
import aurix.metadata_tc39x.metadata_SCU
import aurix.metadata_tc39x.metadata_GTM
import aurix.metadata_tc39x.metadata_GTMWrapper
import aurix.metadata_tc39x.metadata_STM # disable as model is uncomplete
import aurix.metadata_tc39x.metadata_SMU
import aurix.metadata_tc39x.metadata_IR
import aurix.metadata_tc39x.metadata_EVADC
import aurix.metadata_tc39x.metadata_QSPI
import aurix.metadata_tc39x.metadata_DMA
import aurix.metadata_tc39x.metadata_MSC
import aurix.metadata_tc39x.metadata_SENT
import aurix.metadata_tc39x.metadata_CAN
import aurix.metadata_tc39x.metadata_EDSADC
#tc39xB
import aurix.metadata_tc39xb.metadata_EDSADC
import aurix.metadata_tc39xb.metadata_CAN
import aurix.metadata_tc39xb.metadata_DMA
import aurix.metadata_tc39xb.metadata_SCU
import aurix.metadata_tc39xb.metadata_GTMWrapper
import aurix.metadata_tc39xb.metadata_IR
import aurix.metadata_tc39xb.metadata_EVADC
#tc38x
import aurix.metadata_tc38x.metadata_GTMWrapper
import aurix.metadata_tc38x.metadata_IR
import aurix.metadata_tc38x.metadata_EVADC
#tc36x
import aurix.metadata_tc36x.metadata_GTMWrapper
import aurix.metadata_tc36x.metadata_IR
import aurix.metadata_tc36x.metadata_EVADC
#tc37x
import aurix.metadata_tc37x.metadata_GTMWrapper
import aurix.metadata_tc37x.metadata_IR
import aurix.metadata_tc37x.metadata_EVADC
#tc33x
import aurix.metadata_tc33x.metadata_GTMWrapper
import aurix.metadata_tc33x.metadata_IR
import aurix.metadata_tc33x.metadata_EVADC

# Core Model Components
import aurix.ifx_tricore_tc162p_pms4
import aurix.ifx_tricore_tc162p_pms4.analysis_delegate
import aurix.ifx_tricore_tc162p_pms4.assembler
import aurix.ifx_tricore_tc162p_pms4.core
import aurix.ifx_tricore_tc162p_pms4.description
import aurix.ifx_tricore_tc162p_pms4.disassembler
import aurix.ifx_tricore_tc162p_pms4.execution_tracer
import aurix.ifx_tricore_tc162p_pms4.context_tracer
import aurix.ifx_tricore_tc162p_pms4.execution_logger
import aurix.ifx_tricore_tc162p_pms4.iss_debug_facade
import aurix.ifx_tricore_tc162p_pms4.profiler
import aurix.ifx_tricore_tc162p_pms4.synchronization_supervisor
import aurix.ifx_tricore_tc162p_pms4.mcd_tracer
