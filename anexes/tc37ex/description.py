"""Aurix simulator"""

#############################################################################
# References:
#    [TS 2.5.1] AURIX target specification AURIX3xx_ts_part2_V2.5.1.pdf
#    [TS APP 2.3.0] AURIX TS appendix tc37x_ts_appx_V2.3.0.pdf
#    [tc37x_ts_MCSFR] tc37x_ts_MCSFR.xml
##############################################################################

#check if the variant is specified then apply or if not use tc37x as default
tc37xext = False
if ("variant" in __args__) and (__args__["variant"] == "tc37xext"):
    tc37xext = True

import vlab
import sysc
from vlab import *
import aurix.debug_manager
import aurix.analysis_delegate
import aurix.tricore_variant
import aurix.tricore_iss_debug_facade
import aurix.common
if tc37xext:
    from aurix.tc37xext.defines import *
else:
    from aurix.tc37x.defines import *
import os
from aurix.stub_utils import create_stub_factory
import model_stubs
import aurix.ifx_tricore_tc162p.disassembler
import aurix.ifx_tricore_tc162p_pms4.disassembler
import aurix.ifx_tricore_tc162p_pms4.synchronization_supervisor
from aurix.common import _expose_alternate_name as expose_alternate_name

if tc37xext:
    vp_name = "tc37xext"
else:
    vp_name = "tc37x"

properties(name = vp_name, extensions = {"sc_writer_policy": "unchecked"})
__license__ = "aurix_tc37x_vp"

aurix.common.checkout_license_configuration(__license__)

version = vlab.version()

# Get aurix toolbox path
aurix_toolbox_path = vlab.get_properties()["toolboxes"]["aurix"]["path"]

os.environ["LM_LICENSE_FILE"] = os.path.join(aurix_toolbox_path,"ifx-license.lic")

real_sri_xbar = __args__["sri-arbitration"]
alt_io_name = __args__["use-alternate-io-names"]
if alt_io_name:
    from aurix.tc37x.pin_mapping import HW_IO_NAMES
    aurix.common._alternate_hw_io_mappings = HW_IO_NAMES
    aurix.common._alt_io_name = True

##############################################################
# PLATFORM IMPLEMENTATION
# Ref: p.49 of AURIXTC3XX_ts_part1_V2.5.1.pdf
##############################################################

# back-up clock used at power up
BACKUP_CLK = sysc.sc_time(10,sysc.SC_NS)

##############################################################
# NETLISTS
##############################################################

# This dictionnary allows to store the port netlists.
# Do not use it directly but use connect_digital_port() and connect_digital_port() instead.
Ports_Netlist  = {}

spbClk_Net = []
sriClk_Net = []
scuQspiClk_Net = []
allCpuEndInit_Net = []
safetyEndInit_Net = []
applOrSystRst_Net = []
scu_sys_rst_net = []
scu_app_rst_net = []
scuAsclinClk_Net = []
scuAsclinSClk_Net = []
emStop_Net = []
scuStmClk_Net = []
powerOnRst_Net = []
scuApplStmRst_Net = []
scuSleep_Net = []
scuOsc0Clk_Net = []

# EVADC
evadc_GxSR0_Net = []
evadc_GxSR1_Net = []
evadc_GxSR2_Net = []
evadc_GxSR3_Net = []
evadc_C0SR0_Net = []
evadc_C0SR1_Net = []
evadc_C0SR2_Net = []
evadc_C0SR3_Net = []
evadc_C1SR0_Net = []
evadc_C1SR1_Net = []
evadc_C1SR2_Net = []
evadc_C1SR3_Net = []
adc_trig0_out_Net = []
adc_trig1_out_Net = []
adc_trig2_out_Net = []
adc_trig3_out_Net = []
adc_trig4_out_Net = []
dsadc_trig0_out_Net = []

# netlist for HWCFG6
hwcfg6_net = None

##############################################################
# MODEL INSTANCES CONTAINERS
##############################################################

cores = []
stm = []
ports = {}

##############################################################
# UTILITIES FUNCTIONS
##############################################################

""" This is a helper function to connect peripherals to the router
    instance: instance object (the peripheral)
    name: name of the peripheral in the SPB_MEMORY_MAP
    busname: the bus slave name that the peripheral exposes
"""
def spb_router_connect(instance, name, busname, busindex=None, force_sync=False, no_dmi=True):
    global spb_slave_index
    if (name == "GTM"):
        # GTM is splitted into 2 separate memory areas
        connect((spb_router, 'initiator_socket', spb_slave_index), (instance, busname, busindex))
        spb_router.obj.add_address_mapping(spb_slave_index, SPB_MEMORY_MAP["GTM_part1"][0], SPB_MEMORY_MAP["GTM_part1"][1], SPB_MEMORY_MAP["GTM_part1"][0],True,no_dmi)
        spb_router.obj.add_address_mapping(spb_slave_index, SPB_MEMORY_MAP["GTM_part2"][0], SPB_MEMORY_MAP["GTM_part2"][1], SPB_MEMORY_MAP["GTM_part1"][0],True,no_dmi)
    else:
        start_addr = SPB_MEMORY_MAP[name][0]
        size = SPB_MEMORY_MAP[name][1]
        connect((spb_router, 'initiator_socket', spb_slave_index), (instance, busname, busindex))
        spb_router.obj.add_address_mapping(spb_slave_index, start_addr, size, start_addr, force_sync, no_dmi)

    # Table 60 on p. 179 of AURIXTC3XX_ts_part1_V2.5.1.pdf
    if name.startswith(("QSPI", "ASCLIN", "EVADC", "DSADC", "DMA")):
        module_wait_state = 1
    else:
        # TODO: could be more, we don't know for sure
        module_wait_state = 2
    spb_router.obj.set_read_latency(spb_slave_index, spb_bus_byte_latency_calculation(module_wait_state))
    spb_router.obj.set_write_latency(spb_slave_index, spb_bus_byte_latency_calculation(module_wait_state))
    spb_slave_index += 1

""" Utility to translate a Service Request Control Address to an Interrupt Number
    Refer to UM Section 18.14 Interrupt Router SRC Registers
"""
def SRC2IN(OffsetAddress):
    return (OffsetAddress / 4)

def connect_evadc_to_analog_pin(*args):
    if len(args) == 2:
        connect((analog_ports,'analogPorts_o',args[0]), (evadc,'adcCh_i',args[1]))
    elif len(args) == 3:
        connect((analog_ports,'analogPorts_o',args[0]), [(evadc,'adcCh_i',args[1]),(evadc,'adcCh_i',args[2])])

""" This helper function can be called all along the vp description to create netlists.
    Once all netlists are created, actually connect them to ports whith connect_all_digital_ports()
    port_name is "P00"
    port_type is "AltIn" or "Alt4"
    index is [0..7]
    new_connection is the port to connect to PORT
"""
def connect_digital_port(port_name, port_type, index, new_connection):
    if Ports_Netlist[port_name][port_type][index] == 0:
        Ports_Netlist[port_name][port_type][index] = new_connection
    elif isinstance(Ports_Netlist[port_name][port_type][index], tuple):
        if isinstance(new_connection, tuple):
            Ports_Netlist[port_name][port_type][index] = [Ports_Netlist[port_name][port_type][index], new_connection]
        else: # new_connection is a list
            new_connection.append(Ports_Netlist[port_name][port_type][index])
            Ports_Netlist[port_name][port_type][index] = new_connection
    else:
        Ports_Netlist[port_name][port_type][index].append(new_connection)

# This helper function actually connects the ports netlists to PORTS instances
def connect_all_digital_ports():
    for port_name in Ports_Netlist:
        for port_type in Ports_Netlist[port_name]:
            for index in range (16):
                if Ports_Netlist[port_name][port_type][index] != 0:
                    if port_type == "AltIn" :
                        connect((ports[port_name], "IfxPorts{0}_o".format(port_type), index), Ports_Netlist[port_name][port_type][index])
                    else:
                        connect((ports[port_name], "IfxPorts{0}_i".format(port_type), index), Ports_Netlist[port_name][port_type][index])

def get_tlm_slave_interface():
    if real_sri_xbar == False:
        return "target_socket"
    else:
        return "MCI"

def get_tlm_master_interface():
    if real_sri_xbar == False:
        return "initiator_socket"
    else:
        return "SCI"

def spb_bus_byte_latency_calculation(module_wait_state):
    # Set peripheral access latencies accoring to Aurix 2G User Manual, section 4.8
    # Table 60 on p. 179 of AURIXTC3XX_ts_part1_V2.5.1.pdf
    # We assume SPB freq is 100MHz, CPU freq is 300MHz. This needs to be
    # addressed later, so that any clock reprogramming is reflected
    # accordingly at the SPB router level.
    bus_byte_width = 4
    spb_bus_period = 10000 # ps, from 100 MHz
    return sysc.sc_time(spb_bus_period/bus_byte_width*(4+module_wait_state), sysc.SC_PS)

##############################################################
# MODELS INSTANTIATIONS
##############################################################

#Memory stub
memblock = component('AurixMEMBLOCK', module='aurix.memblock')

# Helper to create stub models from a description
stub_initiator = create_stub_factory(model_stubs)

if (__args__["iss"]=="fast"):
    disassembler = aurix.ifx_tricore_tc162p_pms4.disassembler.ls_ipDisassembler()
    supervisor = aurix.ifx_tricore_tc162p_pms4.synchronization_supervisor.synchronization_supervisor()
else:
    disassembler = aurix.ifx_tricore_tc162p.disassembler.ls_ip_disassembler()
    supervisor = None
disassembler.initialise()
if hasattr(vlab.disassembler, 'ls_ip') == False:
    vlab.add_disassembler(disassembler)

for i in range(0, NUM_CORES):
    cores.append(instantiate(component("core",description="aurix.tc37x.core"), "CPU%i_SUBSYSTEM"%i, args=dict({"cpu_id": i}.items() + {"disassembler": disassembler, "supervisor": supervisor}.items() + __args__.items()), doc="CPU%i subsystem"%i,groups="SRI_domain"))

if (__args__["iss"]=="fast"):
    vlab.analysis.delegate = aurix.analysis_delegate.FastIssAnalysisDelegate(True)
else:
    #Tsim analysis interface
    vlab.analysis.delegate = aurix.analysis_delegate.TsimAnalysisDelegate()
    vlab.analysis.scenario.function_profile(delegate=vlab.analysis.delegate,update=True)
    vlab.analysis.scenario.callgrind(delegate=vlab.analysis.delegate, update=True)

#SRI domain memorie,groups="SRI_domain"s
olda = instantiate(component("tlm_memory_32", module="vlab.components"), "OLDA", args=[vlab.NAME, SRI_MEMORY_MAP["OLDA"][1], 0, False], doc="OLDA memory stub",groups="SRI_domain")
xbar_dom0_reg = instantiate(component("tlm_memory_32", module="vlab.components"), "XBAR_DOM0_REG", args=[vlab.NAME, SRI_MEMORY_MAP["XBAR_DOM0"][1], 0, False], doc="XBAR_DOM0 REG memory stub",groups="SRI_domain")
amu00 = instantiate(component("tlm_memory_32", module="vlab.components"), "AMU00", args=[vlab.NAME, SRI_MEMORY_MAP["AMU00"][1], 0, False], doc="AMU00 memory stub",groups="SRI_domain")
amu01 = instantiate(component("tlm_memory_32", module="vlab.components"), "AMU01", args=[vlab.NAME, SRI_MEMORY_MAP["AMU01"][1], 0, False], doc="AMU01 memory stub",groups="SRI_domain")
adma0 = instantiate(component("tlm_memory_32", module="vlab.components"), "ADMA0", args=[vlab.NAME, SRI_MEMORY_MAP["ADMA0"][1], 0, False], doc="ADMA0 memory stub",groups="SRI_domain")
if not tc37xext:
    minimcds = instantiate(component("tlm_memory_32", module="vlab.components"), "ADMA1", args=[vlab.NAME, SRI_MEMORY_MAP["MINIMCDS"][1], 0, False], doc="MINIMCDS memory stub",groups="SRI_domain")

nvm = instantiate(component(description="aurix.tc37x.dmu"), "NVM", groups="SRI_domain")
dam0 = instantiate(component(description="aurix.tc37x.dam0"), "DAM0", groups="SRI_domain")
if tc37xext:
    emem0 = instantiate(component(description='aurix.tc37xext.emem'), 'EMEM0', groups='SRI_domain')
    emem1 = instantiate(component(description='aurix.tc37xext.emem'), 'EMEM1', groups='SRI_domain')
    emem2 = instantiate(component(description='aurix.tc37xext.emem'), 'EMEM2', groups='SRI_domain')
    xtm = instantiate(component('tlm_memory_32', module='vlab.components'), 'XTM', args=[vlab.NAME, SRI_MEMORY_MAP["XTM"][1], 0, False], doc="XTM REG memory stub", groups="SRI_domain")
    xtm_cached = instantiate(component('tlm_memory_32', module='vlab.components'), 'XTM_CACHED', args=[vlab.NAME, SRI_MEMORY_MAP["XTM_CACHED"][1], 0, False], doc="XTM_CACHED REG memory stub", groups="SRI_domain")
    emem_control = instantiate(component('tlm_memory_32', module='vlab.components'), 'EMEM_CONTROL', args=[vlab.NAME, SRI_MEMORY_MAP["EMEM_CONTROL"][1], 0, False], doc="EMEM_CONTROL REG memory stub", groups="SRI_domain")
    

#GTM Debug module
if __args__["astc-gtm-mcs"] == False:
    gtm_debug_component = vlab.component('gtm_debug', module='aurix.gtm_debug')
    gtm_debug = vlab.instantiate(gtm_debug_component,'GTMDebug',groups="Debug")

#IFX config module
config_dll_path = os.path.join(aurix_toolbox_path,"ConfigModule.dll")
config_component = vlab.component('IfxConfigWrapper', module='aurix.IfxConfigWrapper', kind='leaf')
vlab.instantiate(config_component,"CONFIG",args=["CONFIG","TC38x", '1.0', config_dll_path],visibility="hidden")

# Interrupt Router
ir_component = vlab.component(module='aurix.IfxIr_TC3xx', kind='leaf',description='aurix.metadata_tc37x.metadata_IR')
ir = vlab.instantiate(ir_component,"INTERRUPT_ROUTER",args=["INTERRUPT_ROUTER", aurix.common.get_debug_level(__args__["debug-level"],"INTERRUPT_ROUTER")],extensions={"version":"INFINEON V1.0.0"},groups="SPB_domain")

# STM
if (__args__["iss"]=="fast"):
    stm_component = vlab.component(module='aurix.ifx_tc3xx_stm', kind='leaf',description='aurix.ifx_tc3xx_stm_description')
else:
    stm_component = vlab.component(module='aurix.IfxStm2_TC3xx', kind='leaf',description='aurix.metadata_tc39x.metadata_STM')

# QSPI
qspi_component = vlab.component('IfxQspiWrapper', module='aurix.IfxQspi_TC3xx', kind='leaf',description='aurix.metadata_tc39x.metadata_QSPI')

# SCU : IfxScu3Wrapper
scu_component = vlab.component(module='aurix.IfxScu3_TC39xB_TC38x', kind='leaf', description='aurix.metadata_tc39xb.metadata_SCU')
scu = vlab.instantiate(scu_component,"SCU",args=["SCU", aurix.common.get_debug_level(__args__["debug-level"],"SCU")],extensions={"version":"INFINEON V2.0.0"},groups="SPB_domain")

# GTM
gtm_name        = "GTM"

if __args__["gtm-stub"]:
    gtm_stub_component = component(description = "aurix.bosch_gtm_stub_description", cls="synthesize")
    gtm = instantiate(  component   = gtm_stub_component,
                        name        = gtm_name,
                        groups      = "SPB_domain"  )
else:
    # Get the expected "bosch_gtm" module
    if __args__["astc-gtm-mcs"]:
        bosch_gtm_module    = 'aurix.bosch_gtm.GTM_RM_%d.enhanced.bosch_gtm'%(__args__["gtm-rm-version"])
        visibility_opt      = 'visible'
    else:
        bosch_gtm_module    = 'aurix.bosch_gtm.GTM_RM_%d.standard.bosch_gtm'%(__args__["gtm-rm-version"])
        visibility_opt      = 'visible'

    gtm_component   = component(    module      = bosch_gtm_module,
                                    description = "aurix.bosch_gtm.vlab.bosch_gtm_description",
                                    variant     = None,
                                    groups      = None,
                                    visibility  = visibility_opt  )

    # Customized Bosch's GTM RM
    if __args__["astc-gtm-mcs"]:
        mcs_iss_package = "aurix.bosch_gtm.gtm_pms_mcs"
    else:
        mcs_iss_package = ""

    if __args__["astc-gtm-mcs"]:
        # Debug options
        if __args__["astc-gtm-mcs-debug"] == 1:
            mcs_execution_debug     = True
            mcs_tracer_debug        = False
        elif __args__["astc-gtm-mcs-debug"] == 2:
            mcs_execution_debug     = True
            mcs_tracer_debug        = True
        else:
            mcs_execution_debug     = False
            mcs_tracer_debug        = False
    else:
        mcs_execution_debug = False
        mcs_tracer_debug    = False

    # GTM instantiation
    gtm = instantiate(  component   = gtm_component,
                        name        = gtm_name,
                        args        = { "name":                 gtm_name,
                                        "top_level_package":    "aurix.bosch_gtm.vlab",
                                        "fastiss_package":      mcs_iss_package,
                                        "device":               355,
                                        "translation_tracer":   mcs_tracer_debug,
                                        "execution_logger":     mcs_execution_debug,
                                        "execution_tracer":     mcs_tracer_debug
                                        },
                        obj_args    = [NAME, 355],
                        groups      = "SPB_domain"  )

    if __args__["astc-gtm-mcs"]:
        # Blocking TLM
        gtm.obj.set_blocking_tlm(False)
        # Set up target environment
        for core_object in vlab.get_cores():
            if "gtm_pms_mcs_channel_proxy" in core_object.component.name:
                core_object.component.extensions['target_environment'] = 'aurix'

    # Module report level
    gtm_debug_level = aurix.common.get_debug_level(__args__["debug-level"], "GTM")
    if  gtm_debug_level == 20:
        gtm.obj.SetModuleReportLevel("WARN")
    elif  gtm_debug_level == 30:
        gtm.obj.SetModuleReportLevel("INFO")
    elif  gtm_debug_level == 40:
        gtm.obj.SetModuleReportLevel("DBG1")
    elif  gtm_debug_level == 50:
        gtm.obj.SetModuleReportLevel("DBG2")
    elif  gtm_debug_level == 60:
        gtm.obj.SetModuleReportLevel("DBG3")

# GTM Wrapper : IfxGtm2FpiWrapper
gtm_wrapper_component = component(module='aurix.IfxGtmImplementation_TC39xB_TC38x', kind='leaf', description='aurix.metadata_tc37x.metadata_GTMWrapper')
gtm_wrapper = vlab.instantiate(gtm_wrapper_component,"GTMImplementation",args=["GTMImplementation", aurix.common.get_debug_level(__args__["debug-level"],"GTM")],extensions={"version":"INFINEON Gtm2FpiWrapper v2.0.0"},groups="SPB_domain")

#DMA
dma_component = component('DmaWrapper', module='aurix.IfxDma_TC39xB_TC38x', kind='leaf',description='aurix.metadata_tc39xb.metadata_DMA')
dma = vlab.instantiate(dma_component,"DMA",args=["DMA", 0xF0010000, aurix.common.get_debug_level(__args__["debug-level"],"DMA"), 128,0,4,8,12],extensions={"version":"INFINEON V2.0.0"},groups=["SRI_domain","SPB_domain"])

#EVADC
evadc_component = component(module='aurix.IfxEvadc_TC38x', kind='leaf',description='aurix.metadata_tc37x.metadata_EVADC')
evadc = vlab.instantiate(evadc_component,"EVADC",args=["EVADC", aurix.common.get_debug_level(__args__["debug-level"],"EVADC"), True],extensions={"version":"INFINEON EvadcV2.0.0"},groups="SPB_domain")

# Analog Input
analog_ports_component = component('AnalogPorts',module='aurix.AnalogPorts')
analog_ports = vlab.instantiate(analog_ports_component, 'AnalogicPorts',args=["AnalogicPorts",NUMBER_OF_EVADC_GROUPS,NUMBER_OF_EDSADC_GROUPS,NUMBER_OF_AN_PINS, NUMBER_OF_AI_PORTS] ,visibility="hidden")

ports_component = component('IfxPorts3Wrapper',module='aurix.IfxPorts3_TC3xx',description='aurix.metadata_common_tc3xx.metadata_PORTS')

# Ports instantiation : Build ports dictionary from memory map
for unit in SPB_MEMORY_MAP:
    if len(unit) == 3 and unit.startswith("P", 0, 1) and unit[1:].isdigit():
        # A port is detected in memory map
        address = SPB_MEMORY_MAP[unit][0]
        # Add port instance in the dictionary
        ports[unit] = instantiate(ports_component, unit, args=[unit, address, aurix.common.get_debug_level(__args__["debug-level"],"PORTS")],extensions={"version":"INFINEON v1.0"},groups="SPB_domain")
        # create netlists that will be useful for ports connection
        Ports_Netlist[unit] = { "AltIn" : [0 for x in range(16)], "Alt1" : [0 for x in range(16)], "Alt2" : [0 for x in range(16)], "Alt3" : [0 for x in range(16)],
                                "Alt4" : [0 for x in range(16)], "Alt5" : [0 for x in range(16)], "Alt6" : [0 for x in range(16)], "Alt7" : [0 for x in range(16)]  }
        # netlist creation for hwcfg6
        if hwcfg6_net == None:
            hwcfg6_net = vlab.connect((ports[unit], 'ifxporthwcfg_i'))
        else:
            hwcfg6_net = vlab.connect(hwcfg6_net, (ports[unit], 'ifxporthwcfg_i'))


#SMU
smu_component = component(module='aurix.IfxSmu3_TC39xB_TC38x', description='aurix.metadata_tc39x.metadata_SMU')
smu = vlab.instantiate(smu_component,"SMU",args=["SMU", aurix.common.get_debug_level(__args__["debug-level"],"SMU")],extensions={"version":"INFINEON V2.0.0"},groups="SPB_domain")


#MSC
msc_component = component('IfxMscWrapper',module='aurix.IfxMsc3_TC3xx', kind='leaf', description='aurix.metadata_tc39x.metadata_MSC')

#SENT
sent_component = component('IfxSentWrapper',module='aurix.IfxSent2_TC3xx', kind='leaf', description='aurix.metadata_tc39x.metadata_SENT')
sent = vlab.instantiate(sent_component,"SENT",args=["SENT", aurix.common.get_debug_level(__args__["debug-level"],"SENT")],extensions={"version":"INFINEON V0.1"},groups="SPB_domain")

# console
console_component = component('console', module='aurix.console')
console = vlab.instantiate(console_component, 'Console', visibility='hidden')

# MCMCAN and MCAN
mcmcan_component = component("ifx_tc3xx_mcmcan", description="aurix.metadata_tc39xb.metadata_CAN", module="aurix.ifx_tc3xx_mcmcan")
#mcmcan = []
mcmcan = []
if tc37xext:
    NUM_MCMCAN = 3
for i in range(NUM_MCMCAN):
    mcmcan.append(instantiate(mcmcan_component, "mcmcan%d"%i, args=[NAME, 1, 0x8000], extensions={"version":"ASTC V0.1"}, groups="SPB_domain")) #STEP_A = 0 / memory RAM
'''
mcmcan.append(instantiate(mcmcan_component, "mcmcan0", args=[NAME, 1, 0x8000], extensions={"version":"ASTC V0.1"}, groups="SPB_domain")) #STEP_A = 0 / memory RAM
mcmcan.append(instantiate(mcmcan_component, "mcmcan1", args=[NAME, 1, 0x8000], extensions={"version":"ASTC V0.1"}, groups="SPB_domain")) #STEP_A = 0 / memory RAM
mcmcan.append(instantiate(mcmcan_component, "mcmcan2", args=[NAME, 1, 0x8000], extensions={"version":"ASTC V0.1"}, groups="SPB_domain")) #STEP_A = 0 / memory RAM
'''

mcan_component = component("mcan", module="aurix.mcan",description="aurix.mcan_description", variant="rev_315")
mcmcan_mcan = []
for i in range(NUM_MCMCAN):
    mcanx = []
    for j in range(NUM_MCAN):
        mcanx.append(instantiate(mcan_component, "mcan%d%d" % (i,j), extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
    mcmcan_mcan.append(mcanx)

'''
mcan0x = []
mcan0x.append(instantiate(mcan_component, "mcan00", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan0x.append(instantiate(mcan_component, "mcan01", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan0x.append(instantiate(mcan_component, "mcan02", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan0x.append(instantiate(mcan_component, "mcan03", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcmcan_mcan.append(mcan0x)
mcan1x = []
mcan1x.append(instantiate(mcan_component, "mcan10", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan1x.append(instantiate(mcan_component, "mcan11", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan1x.append(instantiate(mcan_component, "mcan12", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan1x.append(instantiate(mcan_component, "mcan13", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcmcan_mcan.append(mcan1x)
mcan2x = []
mcan2x.append(instantiate(mcan_component, "mcan20", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan2x.append(instantiate(mcan_component, "mcan21", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan2x.append(instantiate(mcan_component, "mcan22", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcan2x.append(instantiate(mcan_component, "mcan23", extensions={"version":"ASTC V0.1"}, groups="SPB_domain"))
mcmcan_mcan.append(mcan2x)
'''
geth_component = component("ifx_tc3xx_geth", module="aurix.ifx_tc3xx_geth", description="aurix.ifx_tc3xx_geth_description")

geth = instantiate(geth_component, "GETH", args=[NAME, __args__["little-endian-frames"]], extensions={"version":"ASTC V0.1"},groups="SPB_domain")
if tc37xext:
    geth1_component = component("ifx_tc3xx_geth", module="aurix.ifx_tc3xx_geth", description="aurix.ifx_tc3xx_geth_description")
    geth1 = instantiate(geth1_component, "GETH1", args=[NAME, __args__["little-endian-frames"]], extensions={"version":"ASTC V0.1"},groups="SPB_domain")

##############################################################
# Models connections and bus routing
##############################################################

# Instantiate the bus router. It has 1 bus master (initiator socket) and
# 1 bus slave (target socket).
router_component = component('tlm_router_32', module='vlab.components')
spb_router_component = component('SystemPeripheralBus', module='aurix.SystemPeripheralBus')
spb_master_index = 0
spb_slave_index = 0

spb_router = instantiate(router_component, 'SPB',
                     args=[vlab.NAME, spb_num_masters,
                           spb_num_slaves],groups="SPB_domain")

# spbClk_Net.append((spb_router,'spbClock_i'))

if real_sri_xbar == False:
    sri_router = instantiate(router_component, 'SRI_XBAR',
                            args=[vlab.NAME, sri_num_masters,
                            sri_num_slaves],groups="SRI_domain")


    # Latencies are handled at memory level, not at routers level
    for slave_index in (0,15):
        sri_router.obj.set_fixed_latency(slave_index, sysc.SC_ZERO_TIME)
else:
    sri_xbar_component = component(module='aurix.ifx_tc3xx_sri_xbar', description='aurix.ifx_tc3xx_sri_xbar_description')
    sri_router = instantiate(sri_xbar_component, 'SRI_XBAR', args=[NAME, SRI_MEMORY_MAP["XBAR_DOM0"][0]], groups="SRI_domain")

#connect CPU SUBSYSTEM to SRI
for (core_id, mci) in SRI_CPU_MCI:
    connect((cores[core_id], 'sri_master'), (sri_router, get_tlm_slave_interface(), mci))

#connect CPU SUBSYSTEM to SPB
for i in range(0, NUM_CORES):
    connect((cores[i], 'spb_master'), (spb_router, 'target_socket',spb_master_index))
    spb_master_index += 1

# connect SRI router to CPU SUBSYSTEMS
for (i, cpup_interface, cpus_interface) in SRI_CPU_SCI:
    if cpup_interface != None:
        connect((sri_router, get_tlm_master_interface(), cpup_interface), (cores[i], 'cpup_sri_slave'))
        sri_router.obj.add_address_mapping(cpup_interface, CORE_LOCAL_MEMORY_MAP["PFLASH%i"%i][0], CORE_LOCAL_MEMORY_MAP["PFLASH%i"%i][1], 0)
        sri_router.obj.add_address_mapping(cpup_interface, CORE_LOCAL_MEMORY_MAP["PFLASH%i_CACHED"%i][0], CORE_LOCAL_MEMORY_MAP["PFLASH%i_CACHED"%i][1], 0)
    connect((sri_router, get_tlm_master_interface(), cpus_interface), (cores[i], 'cpus_sri_slave'))
    sri_router.obj.add_address_mapping(cpus_interface, CORE_LOCAL_MEMORY_MAP["DLMU%i"%i][0], CORE_LOCAL_MEMORY_MAP["DLMU%i"%i][1], 0)
    sri_router.obj.add_address_mapping(cpus_interface, CORE_LOCAL_MEMORY_MAP["DLMU%i_CACHED"%i][0], CORE_LOCAL_MEMORY_MAP["DLMU%i_CACHED"%i][1], 0)
    sri_router.obj.add_address_mapping(cpus_interface, CORE_LOCAL_MEMORY_MAP["SRI_SEG1_7_CPU%i"%i][0], CORE_LOCAL_MEMORY_MAP["SRI_SEG1_7_CPU%i"%i][1], 0)
    sri_router.obj.add_address_mapping(cpus_interface, CORE_LOCAL_MEMORY_MAP["CPU_%i_SFR_CSFR"%i][0], CORE_LOCAL_MEMORY_MAP["CPU_%i_SFR_CSFR"%i][1], 0)

# Connect CPU SUBSYSTEM ports
for i in range(0,NUM_CORES):
    spbClk_Net.append((cores[i],'CPU_SpbClock'))
    sriClk_Net.append((cores[i],'CPU_SriClock'))
    safetyEndInit_Net.append((cores[i],'CPU_SafetyEndInit'))
    applOrSystRst_Net.append((cores[i],'CPU_AppOrSystemReset'))
    powerOnRst_Net.append((cores[i],'CPU_PowerOnReset'))

#CPU0 has TOS 0
connect((cores[0],'CPU_InterruptBusControl'),(ir,'ifxIr3IspCtrl_i',0))
connect((cores[0],'CPU_InterruptBusStatus'),(ir,'ifxIr3IspStatus_o',0))
#DMA has TOS1
#other CPUs TOS start at 2
for i in range(1,NUM_CORES):
    connect((cores[i],'CPU_InterruptBusControl'),(ir,'ifxIr3IspCtrl_i',1+i))
    connect((cores[i],'CPU_InterruptBusStatus'),(ir,'ifxIr3IspStatus_o',1+i))


##### DAM0 #######
connect((sri_router, get_tlm_master_interface(), 2), (dam0, "DAM0_SLAVE"))
sri_router.obj.add_address_mapping(2, SRI_MEMORY_MAP["DAM0RAM"][0], SRI_MEMORY_MAP["DAM0RAM"][1], 0)
sri_router.obj.add_address_mapping(2, SRI_MEMORY_MAP["DAM0RAM_CACHED"][0], SRI_MEMORY_MAP["DAM0RAM_CACHED"][1], 0)
sri_router.obj.add_address_mapping(2, SRI_MEMORY_MAP["DAM0"][0], SRI_MEMORY_MAP["DAM0"][1], 0)

###### NVM ######
connect((sri_router, get_tlm_master_interface(), 1), (nvm, "NVM_SLAVE"))
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["DFLASH0"][0], SRI_MEMORY_MAP["DFLASH0"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["DFLASH0_UCB"][0], SRI_MEMORY_MAP["DFLASH0_UCB"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["DFLASH0_CFS"][0], SRI_MEMORY_MAP["DFLASH0_CFS"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["DFLASH1"][0], SRI_MEMORY_MAP["DFLASH1"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["PFI0"][0], SRI_MEMORY_MAP["PFI0"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["PFI1"][0], SRI_MEMORY_MAP["PFI1"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["EC0"][0], SRI_MEMORY_MAP["EC0"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["EC1"][0], SRI_MEMORY_MAP["EC1"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["BROM"][0], SRI_MEMORY_MAP["BROM"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["BROM_CACHED"][0], SRI_MEMORY_MAP["BROM_CACHED"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["DMU_REG"][0], SRI_MEMORY_MAP["DMU_REG"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["PMU_REG"][0], SRI_MEMORY_MAP["PMU_REG"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["FSI_RAM"][0], SRI_MEMORY_MAP["FSI_RAM"][1], 0)
sri_router.obj.add_address_mapping(1, SRI_MEMORY_MAP["FSI_REG"][0], SRI_MEMORY_MAP["FSI_REG"][1], 0)

dmu_to_pflash_router = instantiate(router_component, 'DMU_TO_PFLASH', args=[vlab.NAME, 1, NUM_CORES], groups="SRI_domain", visibility="hidden")
connect((nvm, 'PFLASH_FSI_MASTER'), (dmu_to_pflash_router, 'target_socket', 0))
for i in range(NUM_CORES):
    if "PFLASH%i"%i in CORE_LOCAL_MEMORY_MAP:
        connect((dmu_to_pflash_router, 'initiator_socket', i), (cores[i], 'pflash_fsi_slave'))
        dmu_to_pflash_router.obj.add_address_mapping(i, CORE_LOCAL_MEMORY_MAP["PFLASH%i"%i][0], CORE_LOCAL_MEMORY_MAP["PFLASH%i"%i][1], CORE_LOCAL_MEMORY_MAP["PFLASH%i"%i][0])
        dmu_to_pflash_router.obj.add_address_mapping(i, CORE_LOCAL_MEMORY_MAP["PFLASH%i_CACHED"%i][0], CORE_LOCAL_MEMORY_MAP["PFLASH%i_CACHED"%i][1], CORE_LOCAL_MEMORY_MAP["PFLASH%i_CACHED"%i][0])

##### SRI SFR registers #######
connect((sri_router, get_tlm_master_interface(), 16), (xbar_dom0_reg, 'target_socket'))
sri_router.obj.add_address_mapping(16, SRI_MEMORY_MAP["XBAR_DOM0"][0], SRI_MEMORY_MAP["XBAR_DOM0"][1], SRI_MEMORY_MAP["XBAR_DOM0"][0])

##### OLDA #######
# OLDA is mapped to default slave. Ref. 4.9 Module Interfaces
connect((sri_router, get_tlm_master_interface(), 15), (olda, 'target_socket'))
sri_router.obj.add_address_mapping(15, SRI_MEMORY_MAP["OLDA"][0], SRI_MEMORY_MAP["OLDA"][1], SRI_MEMORY_MAP["OLDA"][0])
sri_router.obj.add_address_mapping(15, SRI_MEMORY_MAP["OLDA_CACHED"][0], SRI_MEMORY_MAP["OLDA_CACHED"][1], SRI_MEMORY_MAP["OLDA_CACHED"][0])

if tc37xext:
    for i in range(NUM_EMEM):
        ##### EMEMi #######
        connect((sri_router, get_tlm_master_interface(), 17 + i), (emem0, "EMEM{}_SLAVE".format(i)))
        sri_router.obj.add_address_mapping(17 + i, SRI_MEMORY_MAP["EMEM{}_RAM".format(i)][0], SRI_MEMORY_MAP["EMEM{}_RAM".format(i)][1], 0)
        sri_router.obj.add_address_mapping(17 + i, SRI_MEMORY_MAP["EMEM{}_RAM_CACHED".format(i)][0], SRI_MEMORY_MAP["EMEM{}_RAM_CACHED".format(i)][1], 0)
        sri_router.obj.add_address_mapping(17 + i, SRI_MEMORY_MAP["EMEM{}".format(i)][0], SRI_MEMORY_MAP["EMEM{}".format(i)][1], 0)

    ##### EMEM_CONTROL #####
    connect((sri_router, get_tlm_master_interface(), 20), (emem_control, 'target_socket'))
    sri_router.obj.add_address_mapping(20, SRI_MEMORY_MAP['EMEM_CONTROL'][0], SRI_MEMORY_MAP['EMEM_CONTROL'][1], SRI_MEMORY_MAP['EMEM_CONTROL'][0])
    
    ##### SRI XTM registers #######
    connect((sri_router, get_tlm_master_interface(), 21), (xtm, 'target_socket'))
    sri_router.obj.add_address_mapping(21, SRI_MEMORY_MAP['XTM'][0], SRI_MEMORY_MAP['XTM'][1], SRI_MEMORY_MAP['XTM'][0])
    connect((sri_router, get_tlm_master_interface(), 22), (xtm_cached, 'target_socket'))
    sri_router.obj.add_address_mapping(22, SRI_MEMORY_MAP['XTM_CACHED'][0], SRI_MEMORY_MAP['XTM_CACHED'][1], SRI_MEMORY_MAP['XTM_CACHED'][0])
else:
    ##### Mini MCDS #######
    slave_if = 14
    connect(
        (sri_router, get_tlm_master_interface(), slave_if),
        (minimcds, 'target_socket')
        )
    sri_router.obj.add_address_mapping(
        slave_if, SRI_MEMORY_MAP["MINIMCDS"][0], SRI_MEMORY_MAP["MINIMCDS"][1],
        SRI_MEMORY_MAP["MINIMCDS"][0]
        ) 

# Stub SCI 0, 12, 13
connect((sri_router, get_tlm_master_interface(), 0), vlab.STUB)
connect((sri_router, get_tlm_master_interface(), 12), vlab.STUB)
connect((sri_router, get_tlm_master_interface(), 13), vlab.STUB)


#DMA
#connect SPB slave
spb_router_connect(dma, 'DMA','dtedma_ifc')
#connect SPB master
connect((spb_router, 'target_socket', spb_master_index), (dma, 'spbInitiator'))
spb_master_index += 1
#connect SRI master
connect((sri_router, get_tlm_slave_interface(), 0), (dma, 'sriInitiator'))
spbClk_Net.append((dma,'mclk_iInPort'))
sriClk_Net.append((dma,'sri_clk_iInPort'))
allCpuEndInit_Net.append((dma,'mfpi_endinit_iInPort'))
safetyEndInit_Net.append((dma,'mfpi_safe_endinit_iInPort'))
applOrSystRst_Net.append((dma,'mreset_n_iInPort'))
connect((ir,'ifxIr3IspStatus_o',1),(dma,'ServiceRequest_i'))
connect((ir,'ifxIr3IspCtrl_i',1),(dma,'ServiceRequest_Ack_o'))
for i in range(0,128):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x370+ i*4)),(dma,'ChannelInterrupt_o',i))
for i in range(0,4):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x340+ i*4)),(dma,'ErrorInterrupt_o',i))


# Interrupt Router
spb_router_connect(ir, 'IR','ir3_intf')
spbClk_Net.append((ir,'busClock_i'))
allCpuEndInit_Net.append((ir,'ifxIr3EndInit_i'))
safetyEndInit_Net.append((ir,'ifxIr3SafeEndInit_i'))
applOrSystRst_Net.append((ir,'resetIf_i'))


# STM
for i in range(NUM_STM):
    model_name = 'STM%i'%i
    if (__args__["iss"]=="fast"):
        stm.append(vlab.instantiate(stm_component,model_name,extensions={"version":"ASTC v1.0.0"},groups="SPB_domain"))
    else:
        stm.append(vlab.instantiate(stm_component,model_name,args=[model_name, aurix.common.get_debug_level(__args__["debug-level"],'STM_%i'%i)],extensions={"version":"INFINEON v1.0.0"},groups="SPB_domain"))
    spb_router_connect(stm[i], model_name,'stmTargetSocket')
    connect((stm[i],'stmComp0Match_o'),(scu,'scuStmRstReq_i',i))
    spbClk_Net.append((stm[i],'busClock_i'))
    allCpuEndInit_Net.append((stm[i],'stmEndInit_i'))
    safetyEndInit_Net.append((stm[i],'stmSafeEndInit_i'))
    scuStmClk_Net.append((stm[i],'stmClock_i'))
    applOrSystRst_Net.append((stm[i],'resetIf_i'))
    scuApplStmRst_Net.append((stm[i],'appResetIf_i'))

    # Connect SRC_STMxSR1 to IR
    connect((stm[i],'stmIrq1_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x0304 + i*8)))


# Connect SRC_STMxSR0 to IR and to SCU ERU Input Pins
for (stm_id, eru_channel, eru_port) in STM_SCU_ERU:
    connect((stm[stm_id],'stmIrq0_o'),[(ir,'ifxIr3Irq_i',SRC2IN(0x0300 + stm_id*8)),(scu,eru_channel,eru_port)])

# FlexRay : model is a registers stub

# QSPI
qspi = []
for i in range(0,NUM_QSPI):
    model_name = 'QSPI%i'%i
    qspi.append(vlab.instantiate(qspi_component,model_name,args=[model_name, aurix.common.get_debug_level(__args__["debug-level"],model_name)],
                extensions={"version":"INFINEON V1.0.0"},groups="SPB_domain"))
    spb_router_connect(qspi[i], model_name,'qspi_ifc')
    expose_alternate_name((qspi[i], 'ifxQspiMrst_o'), name = 'O_QSPI%i_MRST'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstA_i'), name = 'I_QSPI%i_MRSTA'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstB_i'), name = 'I_QSPI%i_MRSTB'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstC_i'), name = 'I_QSPI%i_MRSTC'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstD_i'), name = 'I_QSPI%i_MRSTD'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstE_i'), name = 'I_QSPI%i_MRSTE'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstF_i'), name = 'I_QSPI%i_MRSTF'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstG_i'), name = 'I_QSPI%i_MRSTG'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMrstH_i'), name = 'I_QSPI%i_MRSTH'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsr_o'), name = 'O_QSPI%i_MTSR'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrA_i'), name = 'I_QSPI%i_MTSRA'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrB_i'), name = 'I_QSPI%i_MTSRB'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrC_i'), name = 'I_QSPI%i_MTSRC'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrD_i'), name = 'I_QSPI%i_MTSRD'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrE_i'), name = 'I_QSPI%i_MTSRE'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrF_i'), name = 'I_QSPI%i_MTSRF'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrG_i'), name = 'I_QSPI%i_MTSRG'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiMtsrH_i'), name = 'I_QSPI%i_MTSRH'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclk_o'), name = 'O_QSPI%i_SCLK'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkA_i'), name = 'I_QSPI%i_SCLKA'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkB_i'), name = 'I_QSPI%i_SCLKB'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkC_i'), name = 'I_QSPI%i_SCLKC'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkD_i'), name = 'I_QSPI%i_SCLKD'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkE_i'), name = 'I_QSPI%i_SCLKE'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkF_i'), name = 'I_QSPI%i_SCLKF'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkG_i'), name = 'I_QSPI%i_SCLKG'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSclkH_i'), name = 'I_QSPI%i_SCLKH'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'StdSpiControl_o'), name = 'O_QSPI%i_STDSPICONTROL'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'StdSpiControl_i'), name = 'I_QSPI%i_STDSPICONTROL'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiA_i'), name = 'I_QSPI%i_SLSIA'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiB_i'), name = 'I_QSPI%i_SLSIB'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiC_i'), name = 'I_QSPI%i_SLSIC'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiD_i'), name = 'I_QSPI%i_SLSID'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiE_i'), name = 'I_QSPI%i_SLSIE'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiF_i'), name = 'I_QSPI%i_SLSIF'%i, groups='QSPI')
    expose_alternate_name((qspi[i], 'ifxQspiSlsiG_i'), name = 'I_QSPI%i_SLSIG'%i, groups='QSPI')
    spbClk_Net.append((qspi[i],'busClock_i'))
    scuQspiClk_Net.append((qspi[i],'qspiClock_i'))
    allCpuEndInit_Net.append((qspi[i],'ifxQspiEndInit_i'))
    safetyEndInit_Net.append((qspi[i],'ifxQspiSafeEndInit_i'))
    applOrSystRst_Net.append((qspi[i],'resetIf_i'))
    connect((qspi[i],'ifxQspiTirInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x0F0 + i*0x14)))
    connect((qspi[i],'ifxQspiRirInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x0F4 + i*0x14)))
    connect((qspi[i],'ifxQspiEirInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x0F8 + i*0x14)))
    connect((qspi[i],'ifxQspiPtInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x0FC + i*0x14)))
    connect((qspi[i],'ifxQspiUsrInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x100 + i*0x14)))

connect((qspi[2],'ifxQspiHcInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x178)))
connect((qspi[3],'ifxQspiHcInt_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x17C)))

# SLSO to PORT conenction
# (PORT, index, Alt, QSPI, SLSO)
slso_port_connections = [
    ("P00", 2, "Alt6", "O_QSPI3_SLSO",  4),
    ("P00", 5, "Alt3", "O_QSPI3_SLSO",  3),
    ("P00", 8, "Alt2", "O_QSPI3_SLSO",  6),
    ("P00", 9, "Alt2", "O_QSPI3_SLSO",  7),
    ("P01", 3, "Alt4", "O_QSPI3_SLSO",  9),
    ("P01", 4, "Alt4", "O_QSPI3_SLSO", 10),
    ("P02", 0, "Alt3", "O_QSPI3_SLSO",  1),
    ("P02", 1, "Alt2", "O_QSPI4_SLSO",  7),
    ("P02", 1, "Alt3", "O_QSPI3_SLSO",  2),
    ("P02", 2, "Alt3", "O_QSPI3_SLSO",  3),
    ("P02", 3, "Alt3", "O_QSPI3_SLSO",  4),
    ("P02", 4, "Alt3", "O_QSPI3_SLSO",  0),
    ("P02", 8, "Alt2", "O_QSPI3_SLSO",  5),
    ("P02",12, "Alt2", "O_QSPI3_SLSO",  5),
    ("P02",12, "Alt3", "O_QSPI4_SLSO",  4),
    ("P02",13, "Alt2", "O_QSPI3_SLSO",  7),
    ("P02",13, "Alt3", "O_QSPI4_SLSO",  6),
    ("P02",15, "Alt2", "O_QSPI3_SLSO",  6),
    ("P02",15, "Alt3", "O_QSPI4_SLSO",  5),
    ("P10", 0, "Alt3", "O_QSPI1_SLSO", 10),
    ("P10", 4, "Alt3", "O_QSPI1_SLSO",  8),
    ("P10", 5, "Alt3", "O_QSPI3_SLSO",  8),
    ("P10", 5, "Alt4", "O_QSPI1_SLSO",  9),
    ("P11", 2, "Alt3", "O_QSPI0_SLSO",  5),
    ("P11", 2, "Alt4", "O_QSPI1_SLSO",  5),
    ("P11",10, "Alt3", "O_QSPI0_SLSO",  3),
    ("P11",10, "Alt4", "O_QSPI1_SLSO",  3),
    ("P11",11, "Alt3", "O_QSPI0_SLSO",  4),
    ("P11",11, "Alt4", "O_QSPI1_SLSO",  4),
    ("P14", 2, "Alt3", "O_QSPI2_SLSO",  1),
    ("P14", 3, "Alt3", "O_QSPI2_SLSO",  3),
    ("P14", 6, "Alt3", "O_QSPI2_SLSO",  2),
    ("P14", 7, "Alt3", "O_QSPI2_SLSO",  4),
    ("P15", 0, "Alt3", "O_QSPI0_SLSO", 13),
    ("P15", 1, "Alt3", "O_QSPI2_SLSO",  5),
    ("P15", 2, "Alt3", "O_QSPI2_SLSO",  0),
    ("P20", 3, "Alt3", "O_QSPI0_SLSO",  9),
    ("P20", 3, "Alt4", "O_QSPI2_SLSO",  9),
    ("P20", 6, "Alt3", "O_QSPI0_SLSO",  8),
    ("P20", 6, "Alt4", "O_QSPI2_SLSO",  8),
    ("P20", 8, "Alt3", "O_QSPI0_SLSO",  0),
    ("P20", 8, "Alt4", "O_QSPI1_SLSO",  0),
    ("P20", 9, "Alt3", "O_QSPI0_SLSO",  1),
    ("P20", 9, "Alt4", "O_QSPI1_SLSO",  1),
    ("P20",10 ,"Alt3", "O_QSPI0_SLSO",  6),
    ("P20",10 ,"Alt4", "O_QSPI2_SLSO",  7),
    ("P20",13 ,"Alt3", "O_QSPI0_SLSO",  2),
    ("P20",13 ,"Alt4", "O_QSPI1_SLSO",  2),
    ("P22", 2, "Alt3", "O_QSPI4_SLSO",  3),
    ("P22", 4, "Alt4", "O_QSPI0_SLSO", 12),
    ("P22",11, "Alt4", "O_QSPI0_SLSO", 10),
    ("P23", 1, "Alt3", "O_QSPI4_SLSO",  6),
    ("P23", 4, "Alt3", "O_QSPI4_SLSO",  5),
    ("P23", 5, "Alt3", "O_QSPI4_SLSO",  4),
    ("P23", 6, "Alt4", "O_QSPI0_SLSO", 11),
    ("P32", 6, "Alt4", "O_QSPI2_SLSO", 12),
    ("P33", 2, "Alt3", "O_QSPI2_SLSO", 10),
    ("P33", 3, "Alt3", "O_QSPI4_SLSO",  2),
    ("P33", 4, "Alt3", "O_QSPI2_SLSO", 12),
    ("P33", 5, "Alt2", "O_QSPI0_SLSO",  7),
    ("P33", 5, "Alt3", "O_QSPI1_SLSO",  7),
    ("P33", 6, "Alt3", "O_QSPI2_SLSO", 11),
    ("P33", 7, "Alt3", "O_QSPI4_SLSO",  7),
    ("P33", 8, "Alt3", "O_QSPI4_SLSO",  2),
    ("P33", 9, "Alt3", "O_QSPI4_SLSO",  1),
    ("P33",10, "Alt2", "O_QSPI1_SLSO",  6),
    ("P33",10, "Alt3", "O_QSPI4_SLSO",  0),
    ("P33",13, "Alt4", "O_QSPI2_SLSO",  6),
    ("P33",15, "Alt3", "O_QSPI2_SLSO", 11),
    ("P34", 3, "Alt4", "O_QSPI2_SLSO", 10),
]

# The very same QSPI port can be configured to different pins of the PORTs according the configurations.
# e.g. ("P00", 2, "Alt6", "O_QSPI3_SLSO",  4) and ("P00", 2, "Alt6", "O_QSPI3_SLSO",  4).
# They are collected into the same list and then connect to the exposed QSPI port together.
slso_port_map = {}
for (port_name, port_index, alt_name, qspi_name, slso_index) in slso_port_connections:
    if (qspi_name, slso_index) in slso_port_map:
        slso_port_map[(qspi_name, slso_index)].append((ports[port_name], "IfxPorts{0}_i".format(alt_name), port_index))
    else:
        slso_port_map[(qspi_name, slso_index)] = [(ports[port_name], "IfxPorts{0}_i".format(alt_name), port_index)]

for i in range(0,NUM_QSPI):
    qspi_expose = []
    qspi_name = 'O_QSPI%i_SLSO'%i
    for j in range(0, 16):
        if (qspi_name, j) in slso_port_map:
            splitter_targets = slso_port_map[(qspi_name, j)]
            splitter_name = "qspi_splitter_%i_%i"%(i,j)
            instantiate(component('sc_splitter_bool', module='aurix.sc_splitter'), splitter_name, args=[splitter_name, len(splitter_targets) + 1], visibility="hidden")
            connect((qspi[i], 'ifxQspiSlso_o', j), (splitter_name, 'input'))
            for k in range(len(splitter_targets)):
                connect((splitter_name, 'output', k+1), splitter_targets[k])
            qspi_expose.append((splitter_name, 'output', 0))
        else:
            qspi_expose.append((qspi[i], 'ifxQspiSlso_o', j))
    expose(qspi_expose, name = qspi_name, array = True, groups="QSPI")

# MSC
msc = []
for i in range(0,NUM_MSC):
    model_name = 'MSC%i'%i
    msc.append( vlab.instantiate(msc_component,model_name,args=[model_name, aurix.common.get_debug_level(__args__["debug-level"],model_name)],extensions={"version":"INFINEON V0.1"},groups="SPB_domain"))
    spb_router_connect(msc[i], model_name,'msc_intf')
    expose_alternate_name((msc[i], 'mscDscCh_o'), name = 'O_MSC%i_DSCCH'%i, groups='MSC', alt_name='MSC%i_SOP'%i) # Use positive name
    expose_alternate_name((msc[i], 'mscDscCtrl_o'), name = 'O_MSC%i_DSCCTRL'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscDscClk_o'), name = 'O_MSC%i_DSCCLOCK'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscDscEn0_o'), name = 'O_MSC%i_DSCEN0'%i, groups='MSC', alt_name='MSC%i_EN0'%i)
    expose_alternate_name((msc[i], 'mscDscEn1_o'), name = 'O_MSC%i_DSCEN1'%i, groups='MSC', alt_name='MSC%i_EN1'%i)
    expose_alternate_name((msc[i], 'mscDscEn2_o'), name = 'O_MSC%i_DSCEN2'%i, groups='MSC', alt_name='MSC%i_EN2'%i)
    expose_alternate_name((msc[i], 'mscDscEn3_o'), name = 'O_MSC%i_DSCEN3'%i, groups='MSC', alt_name='MSC%i_EN3'%i)
    expose_alternate_name((msc[i], 'mscUscDataCtrl0_i'), name = 'I_MSC%i_UscDataCtrl0'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl1_i'), name = 'I_MSC%i_UscDataCtrl1'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl2_i'), name = 'I_MSC%i_UscDataCtrl2'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl3_i'), name = 'I_MSC%i_UscDataCtrl3'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl4_i'), name = 'I_MSC%i_UscDataCtrl4'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl5_i'), name = 'I_MSC%i_UscDataCtrl5'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl6_i'), name = 'I_MSC%i_UscDataCtrl6'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscUscDataCtrl7_i'), name = 'I_MSC%i_UscDataCtrl7'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscInj0_i'), name = 'I_MSC%i_INJ0'%i, groups='MSC')
    expose_alternate_name((msc[i], 'mscInj1_i'), name = 'I_MSC%i_INJ1'%i, groups='MSC')
    spbClk_Net.append((msc[i],'mclk_iInPort'))
    allCpuEndInit_Net.append((msc[i],'mfpi_endinit_iInPort'))
    safetyEndInit_Net.append((msc[i],'mfpi_safe_endinit_iInPort'))
    applOrSystRst_Net.append((msc[i],'mreset_n_iInPort'))
    scuSleep_Net.append((msc[i],'mscSleepMode_i'))
    emStop_Net.append((msc[i],'mscEmgStopMsc_i'))
    connect((msc[i],'mscSrn0_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x270 + i*0x14)))
    connect((msc[i],'mscSrn1_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x274 + i*0x14)))
    connect((msc[i],'mscSrn2_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x278 + i*0x14)))
    connect((msc[i],'mscSrn3_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x27C + i*0x14)))
    connect((msc[i],'mscSrn4_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x280 + i*0x14)))
    connect((msc[i],'mscAltInh_i'),(gtm_wrapper, 'msc%iAltInH_o'%i))
    connect((msc[i],'mscAltInl_i'),(gtm_wrapper, 'msc%iAltInL_o'%i))



#GTM Debug
if __args__["astc-gtm-mcs"] == False:
    connect((spb_router, 'target_socket', spb_master_index), (gtm_debug, 'initiator'))
    spb_master_index += 1
    applOrSystRst_Net.append((gtm_debug, 'reset'))

# GTMWrapper
spb_router_connect(gtm_wrapper, 'GTMWRAPPER', 'gtm_intf')

if not __args__["gtm-stub"]:
    if __args__["astc-gtm-mcs"]:
        connect((gtm_wrapper,'gtmClk_o'),(gtm,'SYS_CLK'), default=BACKUP_CLK)
    else:
        connect((gtm_wrapper,'gtmClk_o'),[(gtm,'SYS_CLK'),(gtm_debug,'gtmClock')], default=BACKUP_CLK)

applOrSystRst_Net.append((gtm_wrapper,'mmreset_n_iInPort'))
allCpuEndInit_Net.append((gtm_wrapper,'mmfpi_endinit_iInPort'))
safetyEndInit_Net.append((gtm_wrapper,'mmfpi_safe_endinit_iInPort'))

spb_router_connect(gtm, 'GTM', 'peripheral_bus')
applOrSystRst_Net.append((gtm,'RST_N'))
connect((ir,'ifxIr3Irq_i',SRC2IN(0x0A70)),(gtm,'AEI_IRQ'))
connect((ir,'ifxIr3Irq_i',SRC2IN(0x0A80)),(gtm,'BRC_IRQ'))
connect((ir,'ifxIr3Irq_i',SRC2IN(0x0A84)),(gtm,'CMP_IRQ'))
connect((ir,'ifxIr3Irq_i',SRC2IN(0x0B70)),(gtm,'ERR_IRQ'))

for i in range(0,3):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x0A74 + i*4)),(gtm,'ARU_IRQ', i))

for i in range(0,NUM_SPE):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x0A88 + i*4)),(gtm,'SPE%d_IRQ'%(i)))

for j in range(3):
    for i in range(8):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x0AA0 + 0x20*j + i*4)),(gtm,'PSM%d_IRQ'%(j),i))

for i in range(0,27):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x0B00 + i*4)),(gtm,'DPLL_IRQ',i))

# gtm_tim_irq is 64 bits length = 8 * 8 bits
# we use 8 * 8 bits
# => 8 irqs / 8 irqs / ... 8 times
for j in range(NUM_TIM):
    for i in range(8):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x0B90 + 0x20*j + i*4)),(gtm,'TIM%d_IRQ'%(j), i))

# gtm_mcs_irq is 320 bits length = 10 * 32 bits
# we use only 10 * 8 bits
# => 8 irqs / 24 unused / 8 irqs / 24 unused / ... 10 times
for j in range(NUM_MCS):
    for i in range(8):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x0CB0 + 0x20*j + i*4)),(gtm,'MCS%d_IRQ'%(j),i))

# gtm_tom_irq is 96 bits length = 6 * 16 bits
# we use only 6 * 8 bits
# => 8 irqs / 8 unused / 8 irqs / 8 unused / ... 6 times
for j in range(NUM_TOM):
    for i in range(8):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x0E10 + 0x20*j + i*4)),(gtm,'TOM%d_IRQ'%(j),i))

# gtm_atom_irq is 96 bits length = 12 * 8 bits
# we use only 12 * 4 bits
# => 4 irqs / 4 unused / 4 irqs / 4 unused / ... 12 times
for j in range(NUM_ATOM):
    for i in range(4):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x0EF0 + 0x10*j + i*4)),(gtm,'ATOM%d_IRQ'%(j),i))

# Missing : SRC_GTMMCSWx

# From page 78, section 28 of [TS 2.5.1], it shows the output of the DS ADC IMUX goes into TIM IMUX.
# From page 848, section 28.25.8.1 of [TS 2.5.1], timy_muxout_x are the output from DSADC_IMUX.
# timy_muxout_x are with the naming convention `tim%dmuxout` % x, where y is the index of the port.
# From page 492, section 23.3.2 of [TS APP 2.3.0], the index 0xE indicates port of TIM0 CH0 IMUX connects to IMUX0_0.
# TIM0 CH0 IMUX index 0xE is present as (gtm_wrapper, 'tim_0_muxin_0_i',  14) in this model.
# The following connections are generated by parsing MCSFR with scripts/create_tim_dsadc_imux_description.py
connect((gtm_wrapper, 'tim_0_muxin_0_i', 14), (gtm_wrapper, 'tim0muxout', 0))
connect((gtm_wrapper, 'tim_0_muxin_1_i', 14), (gtm_wrapper, 'tim0muxout', 1))
connect((gtm_wrapper, 'tim_0_muxin_2_i', 14), (gtm_wrapper, 'tim0muxout', 2))
connect((gtm_wrapper, 'tim_0_muxin_3_i', 14), (gtm_wrapper, 'tim0muxout', 3))
connect((gtm_wrapper, 'tim_0_muxin_4_i', 14), (gtm_wrapper, 'tim0muxout', 4))
connect((gtm_wrapper, 'tim_0_muxin_5_i', 14), (gtm_wrapper, 'tim0muxout', 5))
connect((gtm_wrapper, 'tim_0_muxin_6_i', 14), (gtm_wrapper, 'tim0muxout', 6))
connect((gtm_wrapper, 'tim_0_muxin_7_i', 14), (gtm_wrapper, 'tim0muxout', 7))
connect((gtm_wrapper, 'tim_1_muxin_0_i', 11), (gtm_wrapper, 'tim1muxout', 0))
connect((gtm_wrapper, 'tim_1_muxin_1_i', 11), (gtm_wrapper, 'tim1muxout', 1))
connect((gtm_wrapper, 'tim_1_muxin_2_i', 11), (gtm_wrapper, 'tim1muxout', 2))
connect((gtm_wrapper, 'tim_1_muxin_3_i', 14), (gtm_wrapper, 'tim1muxout', 3))
connect((gtm_wrapper, 'tim_1_muxin_4_i', 14), (gtm_wrapper, 'tim1muxout', 4))
connect((gtm_wrapper, 'tim_1_muxin_5_i', 14), (gtm_wrapper, 'tim1muxout', 5))
connect((gtm_wrapper, 'tim_1_muxin_6_i', 14), (gtm_wrapper, 'tim1muxout', 6))
connect((gtm_wrapper, 'tim_1_muxin_7_i', 14), (gtm_wrapper, 'tim1muxout', 7))
connect((gtm_wrapper, 'tim_2_muxin_0_i', 11), (gtm_wrapper, 'tim2muxout', 0))
connect((gtm_wrapper, 'tim_2_muxin_1_i', 11), (gtm_wrapper, 'tim2muxout', 1))
connect((gtm_wrapper, 'tim_2_muxin_2_i', 11), (gtm_wrapper, 'tim2muxout', 2))
connect((gtm_wrapper, 'tim_2_muxin_3_i', 11), (gtm_wrapper, 'tim2muxout', 3))
connect((gtm_wrapper, 'tim_2_muxin_4_i', 11), (gtm_wrapper, 'tim2muxout', 4))
connect((gtm_wrapper, 'tim_2_muxin_5_i', 11), (gtm_wrapper, 'tim2muxout', 5))
connect((gtm_wrapper, 'tim_2_muxin_6_i', 11), (gtm_wrapper, 'tim2muxout', 6))
connect((gtm_wrapper, 'tim_2_muxin_7_i', 11), (gtm_wrapper, 'tim2muxout', 7))
connect((gtm_wrapper, 'tim_3_muxin_0_i', 15), (gtm_wrapper, 'tim3muxout', 0))
connect((gtm_wrapper, 'tim_3_muxin_1_i', 0), (gtm_wrapper, 'tim3muxout', 1))
connect((gtm_wrapper, 'tim_3_muxin_2_i', 15), (gtm_wrapper, 'tim3muxout', 2))
connect((gtm_wrapper, 'tim_3_muxin_3_i', 14), (gtm_wrapper, 'tim3muxout', 3))
connect((gtm_wrapper, 'tim_3_muxin_4_i', 14), (gtm_wrapper, 'tim3muxout', 4))
connect((gtm_wrapper, 'tim_3_muxin_5_i', 14), (gtm_wrapper, 'tim3muxout', 5))
connect((gtm_wrapper, 'tim_3_muxin_6_i', 15), (gtm_wrapper, 'tim3muxout', 6))
connect((gtm_wrapper, 'tim_3_muxin_7_i', 14), (gtm_wrapper, 'tim3muxout', 7))
connect((gtm_wrapper, 'tim_4_muxin_0_i', 14), (gtm_wrapper, 'tim4muxout', 0))
connect((gtm_wrapper, 'tim_4_muxin_1_i', 15), (gtm_wrapper, 'tim4muxout', 1))
connect((gtm_wrapper, 'tim_4_muxin_2_i', 14), (gtm_wrapper, 'tim4muxout', 2))
connect((gtm_wrapper, 'tim_4_muxin_3_i', 14), (gtm_wrapper, 'tim4muxout', 3))
connect((gtm_wrapper, 'tim_4_muxin_4_i', 13), (gtm_wrapper, 'tim4muxout', 4))
connect((gtm_wrapper, 'tim_4_muxin_5_i', 13), (gtm_wrapper, 'tim4muxout', 5))
connect((gtm_wrapper, 'tim_4_muxin_6_i', 11), (gtm_wrapper, 'tim4muxout', 6))
connect((gtm_wrapper, 'tim_4_muxin_7_i', 11), (gtm_wrapper, 'tim4muxout', 7))
connect((gtm_wrapper, 'tim_5_muxin_0_i', 11), (gtm_wrapper, 'tim5muxout', 0))
connect((gtm_wrapper, 'tim_5_muxin_1_i', 12), (gtm_wrapper, 'tim5muxout', 1))
connect((gtm_wrapper, 'tim_5_muxin_2_i', 10), (gtm_wrapper, 'tim5muxout', 2))
connect((gtm_wrapper, 'tim_5_muxin_3_i', 12), (gtm_wrapper, 'tim5muxout', 3))
connect((gtm_wrapper, 'tim_5_muxin_4_i', 3), (gtm_wrapper, 'tim5muxout', 4))
connect((gtm_wrapper, 'tim_5_muxin_5_i', 13), (gtm_wrapper, 'tim5muxout', 5))
connect((gtm_wrapper, 'tim_5_muxin_6_i', 13), (gtm_wrapper, 'tim5muxout', 6))
connect((gtm_wrapper, 'tim_5_muxin_7_i', 12), (gtm_wrapper, 'tim5muxout', 7))

#GTM wrapper tim_in out port to GTM tim_in in port
for j in range(NUM_TIM):
    for i in range(NUM_TIM_CHANNEL):
        connect((gtm,'TIM%d_IN'%(j),i),[(gtm_wrapper,'tim_in',i + j*8)])

#GTM tom_out out port to GTM wrapper tom_out in port
for i in range(0,NUM_TOM):
    for j in range(0,NUM_TOM_CHANNEL):
        connect((gtm,'TOM%d_OUT'%(i),j),(gtm_wrapper,'out_tom%i'%i,j))
        connect((gtm,'TOM%d_OUT_N'%(i),j),(gtm_wrapper,'out_tom%i_n'%i,j))

#GTM atom_out out port to GTM Wrapper atoum_out in port
for i in range(0,NUM_ATOM):
    for j in range(0,NUM_ATOM_CHANNEL):
        connect((gtm,'ATOM%d_OUT'%(i),j),(gtm_wrapper,'out_atom%i'%i,j))
        connect((gtm,'ATOM%d_OUT_N'%(i),j),(gtm_wrapper,'out_atom%i_n'%i,j))

# GTM Outputs to Port Connections : GTM_TOUT
# This part has been automatically generated by scripts/create_tout_description_from_ifxgtm_pinmap_c.py
connect_digital_port('P00', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 9))
connect_digital_port('P00', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 10))
connect_digital_port('P00', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 11))
connect_digital_port('P00', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 12))
connect_digital_port('P00', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 13))
connect_digital_port('P00', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 14))
connect_digital_port('P00', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 15))
connect_digital_port('P00', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 16))
connect_digital_port('P00', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 17))
connect_digital_port('P00', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 18))
connect_digital_port('P00', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 19))
connect_digital_port('P00', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 20))
connect_digital_port('P00', 'Alt1', 12, (gtm_wrapper, 'gtm_tout', 21))

connect_digital_port('P01', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 111))
connect_digital_port('P01', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 112))
connect_digital_port('P01', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 113))
connect_digital_port('P01', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 114))
connect_digital_port('P01', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 115))

connect_digital_port('P02', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 0))
connect_digital_port('P02', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 1))
connect_digital_port('P02', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 2))
connect_digital_port('P02', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 3))
connect_digital_port('P02', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 4))
connect_digital_port('P02', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 5))
connect_digital_port('P02', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 6))
connect_digital_port('P02', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 7))
connect_digital_port('P02', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 8))
connect_digital_port('P02', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 116))
connect_digital_port('P02', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 117))
connect_digital_port('P02', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 118))

connect_digital_port('P10', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 102))
connect_digital_port('P10', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 103))
connect_digital_port('P10', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 104))
connect_digital_port('P10', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 105))
connect_digital_port('P10', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 106))
connect_digital_port('P10', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 107))
connect_digital_port('P10', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 108))
connect_digital_port('P10', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 109))
connect_digital_port('P10', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 110))

connect_digital_port('P11', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 119))
connect_digital_port('P11', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 120))
connect_digital_port('P11', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 95))
connect_digital_port('P11', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 96))
connect_digital_port('P11', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 121))
connect_digital_port('P11', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 122))
connect_digital_port('P11', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 97))
connect_digital_port('P11', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 123))
connect_digital_port('P11', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 124))
connect_digital_port('P11', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 98))
connect_digital_port('P11', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 99))
connect_digital_port('P11', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 100))
connect_digital_port('P11', 'Alt1', 12, (gtm_wrapper, 'gtm_tout', 101))
connect_digital_port('P11', 'Alt1', 13, (gtm_wrapper, 'gtm_tout', 125))
connect_digital_port('P11', 'Alt1', 14, (gtm_wrapper, 'gtm_tout', 126))
connect_digital_port('P11', 'Alt1', 15, (gtm_wrapper, 'gtm_tout', 127))

connect_digital_port('P12', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 128))
connect_digital_port('P12', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 129))

connect_digital_port('P13', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 91))
connect_digital_port('P13', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 92))
connect_digital_port('P13', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 93))
connect_digital_port('P13', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 94))

connect_digital_port('P14', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 80))
connect_digital_port('P14', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 81))
connect_digital_port('P14', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 82))
connect_digital_port('P14', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 83))
connect_digital_port('P14', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 84))
connect_digital_port('P14', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 85))
connect_digital_port('P14', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 86))
connect_digital_port('P14', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 87))
connect_digital_port('P14', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 88))
connect_digital_port('P14', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 89))
connect_digital_port('P14', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 90))

connect_digital_port('P15', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 71))
connect_digital_port('P15', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 72))
connect_digital_port('P15', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 73))
connect_digital_port('P15', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 74))
connect_digital_port('P15', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 75))
connect_digital_port('P15', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 76))
connect_digital_port('P15', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 77))
connect_digital_port('P15', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 78))
connect_digital_port('P15', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 79))

connect_digital_port('P20', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 59))
connect_digital_port('P20', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 60))
connect_digital_port('P20', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 61))
connect_digital_port('P20', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 62))
connect_digital_port('P20', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 63))
connect_digital_port('P20', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 64))
connect_digital_port('P20', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 65))
connect_digital_port('P20', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 66))
connect_digital_port('P20', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 67))
connect_digital_port('P20', 'Alt1', 12, (gtm_wrapper, 'gtm_tout', 68))
connect_digital_port('P20', 'Alt1', 13, (gtm_wrapper, 'gtm_tout', 69))
connect_digital_port('P20', 'Alt1', 14, (gtm_wrapper, 'gtm_tout', 70))

connect_digital_port('P21', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 51))
connect_digital_port('P21', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 52))
connect_digital_port('P21', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 53))
connect_digital_port('P21', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 54))
connect_digital_port('P21', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 55))
connect_digital_port('P21', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 56))
connect_digital_port('P21', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 57))
connect_digital_port('P21', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 58))

connect_digital_port('P22', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 47))
connect_digital_port('P22', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 48))
connect_digital_port('P22', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 49))
connect_digital_port('P22', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 50))
connect_digital_port('P22', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 130))
connect_digital_port('P22', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 131))
connect_digital_port('P22', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 132))
connect_digital_port('P22', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 133))
connect_digital_port('P22', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 134))
connect_digital_port('P22', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 135))
connect_digital_port('P22', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 136))
connect_digital_port('P22', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 137))

connect_digital_port('P23', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 41))
connect_digital_port('P23', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 42))
connect_digital_port('P23', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 43))
connect_digital_port('P23', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 44))
connect_digital_port('P23', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 45))
connect_digital_port('P23', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 46))
connect_digital_port('P23', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 138))
connect_digital_port('P23', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 139))

connect_digital_port('P32', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 36))
connect_digital_port('P32', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 37))
connect_digital_port('P32', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 38))
connect_digital_port('P32', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 39))
connect_digital_port('P32', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 40))
connect_digital_port('P32', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 140))
connect_digital_port('P32', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 141))
connect_digital_port('P32', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 142))

connect_digital_port('P33', 'Alt1', 0 , (gtm_wrapper, 'gtm_tout', 22))
connect_digital_port('P33', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 23))
connect_digital_port('P33', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 24))
connect_digital_port('P33', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 25))
connect_digital_port('P33', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 26))
connect_digital_port('P33', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 27))
connect_digital_port('P33', 'Alt1', 6 , (gtm_wrapper, 'gtm_tout', 28))
connect_digital_port('P33', 'Alt1', 7 , (gtm_wrapper, 'gtm_tout', 29))
connect_digital_port('P33', 'Alt1', 8 , (gtm_wrapper, 'gtm_tout', 30))
connect_digital_port('P33', 'Alt1', 9 , (gtm_wrapper, 'gtm_tout', 31))
connect_digital_port('P33', 'Alt1', 10, (gtm_wrapper, 'gtm_tout', 32))
connect_digital_port('P33', 'Alt1', 11, (gtm_wrapper, 'gtm_tout', 33))
connect_digital_port('P33', 'Alt1', 12, (gtm_wrapper, 'gtm_tout', 34))
connect_digital_port('P33', 'Alt1', 13, (gtm_wrapper, 'gtm_tout', 35))
connect_digital_port('P33', 'Alt1', 14, (gtm_wrapper, 'gtm_tout', 143))
connect_digital_port('P33', 'Alt1', 15, (gtm_wrapper, 'gtm_tout', 144))

connect_digital_port('P34', 'Alt1', 1 , (gtm_wrapper, 'gtm_tout', 146))
connect_digital_port('P34', 'Alt1', 2 , (gtm_wrapper, 'gtm_tout', 147))
connect_digital_port('P34', 'Alt1', 3 , (gtm_wrapper, 'gtm_tout', 148))
connect_digital_port('P34', 'Alt1', 4 , (gtm_wrapper, 'gtm_tout', 149))
connect_digital_port('P34', 'Alt1', 5 , (gtm_wrapper, 'gtm_tout', 150))

# GPIO to GTM connections
# This part has been automatically generated by scripts/create_tin_description_from_ifxgtm_pinmap_c.py
# expose_atlernate_name() will directly expose the connection if alternate names aren't used
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',7), (gtm_wrapper,'tim_2_muxin_3_i',7), (gtm_wrapper,'tim_5_muxin_3_i',2)]), name='I_GTM_TIN113', groups='GTM')
connect_digital_port('P01', 'AltIn', 5, (this(), 'I_GTM_TIN113'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',8), (gtm_wrapper,'tim_2_muxin_1_i',14), (gtm_wrapper,'tim_4_muxin_6_i',2)]), name='I_GTM_TIN112', groups='GTM')
connect_digital_port('P01', 'AltIn', 4, (this(), 'I_GTM_TIN112'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',8), (gtm_wrapper,'tim_2_muxin_0_i',14), (gtm_wrapper,'tim_4_muxin_5_i',2)]), name='I_GTM_TIN111', groups='GTM')
connect_digital_port('P01', 'AltIn', 3, (this(), 'I_GTM_TIN111'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',2), (gtm_wrapper,'tim_1_muxin_5_i',2), (gtm_wrapper,'tim_4_muxin_0_i',13)]), name='I_GTM_TIN110', groups='GTM')
connect_digital_port('P10', 'AltIn', 8, (this(), 'I_GTM_TIN110'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',10), (gtm_wrapper,'tim_3_muxin_4_i',11), (gtm_wrapper,'tim_4_muxin_3_i',2)]), name='I_GTM_TIN117', groups='GTM')
connect_digital_port('P02', 'AltIn', 10, (this(), 'I_GTM_TIN117'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',10), (gtm_wrapper,'tim_3_muxin_3_i',10), (gtm_wrapper,'tim_4_muxin_2_i',2)]), name='I_GTM_TIN116', groups='GTM')
connect_digital_port('P02', 'AltIn', 9, (this(), 'I_GTM_TIN116'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',7), (gtm_wrapper,'tim_5_muxin_7_i',2)]), name='I_GTM_TIN115', groups='GTM')
connect_digital_port('P01', 'AltIn', 7, (this(), 'I_GTM_TIN115'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',7), (gtm_wrapper,'tim_5_muxin_5_i',3), (gtm_wrapper,'tim_5_muxin_6_i',2)]), name='I_GTM_TIN114', groups='GTM')
connect_digital_port('P01', 'AltIn', 6, (this(), 'I_GTM_TIN114'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',7), (gtm_wrapper,'tim_4_muxin_0_i',4)]), name='I_GTM_TIN119', groups='GTM')
connect_digital_port('P11', 'AltIn', 0, (this(), 'I_GTM_TIN119'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',7), (gtm_wrapper,'tim_3_muxin_5_i',12), (gtm_wrapper,'tim_4_muxin_4_i',3)]), name='I_GTM_TIN118', groups='GTM')
connect_digital_port('P02', 'AltIn', 11, (this(), 'I_GTM_TIN118'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',5), (gtm_wrapper,'tim_3_muxin_0_i',5)]), name='I_GTM_TIN68', groups='GTM')
connect_digital_port('P20', 'AltIn', 12, (this(), 'I_GTM_TIN68'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',4), (gtm_wrapper,'tim_3_muxin_1_i',4)]), name='I_GTM_TIN69', groups='GTM')
connect_digital_port('P20', 'AltIn', 13, (this(), 'I_GTM_TIN69'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',5), (gtm_wrapper,'tim_3_muxin_6_i',5)]), name='I_GTM_TIN62', groups='GTM')
connect_digital_port('P20', 'AltIn', 6, (this(), 'I_GTM_TIN62'))
expose(connect([(gtm_wrapper,'tim_1_muxin_5_i',8), (gtm_wrapper,'tim_2_muxin_7_i',5), (gtm_wrapper,'tim_3_muxin_7_i',5)]), name='I_GTM_TIN63', groups='GTM')
connect_digital_port('P20', 'AltIn', 7, (this(), 'I_GTM_TIN63'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',5), (gtm_wrapper,'tim_3_muxin_3_i',5), (gtm_wrapper,'tim_4_muxin_4_i',11)]), name='I_GTM_TIN60', groups='GTM')
connect_digital_port('P20', 'AltIn', 1, (this(), 'I_GTM_TIN60'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',5), (gtm_wrapper,'tim_3_muxin_4_i',5), (gtm_wrapper,'tim_4_muxin_5_i',11)]), name='I_GTM_TIN61', groups='GTM')
connect_digital_port('P20', 'AltIn', 3, (this(), 'I_GTM_TIN61'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',6), (gtm_wrapper,'tim_3_muxin_6_i',6)]), name='I_GTM_TIN66', groups='GTM')
connect_digital_port('P20', 'AltIn', 10, (this(), 'I_GTM_TIN66'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',6), (gtm_wrapper,'tim_3_muxin_7_i',6)]), name='I_GTM_TIN67', groups='GTM')
connect_digital_port('P20', 'AltIn', 11, (this(), 'I_GTM_TIN67'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',3), (gtm_wrapper,'tim_1_muxin_7_i',3)]), name='I_GTM_TIN64', groups='GTM')
connect_digital_port('P20', 'AltIn', 8, (this(), 'I_GTM_TIN64'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',5), (gtm_wrapper,'tim_3_muxin_5_i',5)]), name='I_GTM_TIN65', groups='GTM')
connect_digital_port('P20', 'AltIn', 9, (this(), 'I_GTM_TIN65'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',1), (gtm_wrapper,'tim_1_muxin_7_i',1), (gtm_wrapper,'tim_3_muxin_1_i',10)]), name='I_GTM_TIN7', groups='GTM')
connect_digital_port('P02', 'AltIn', 7, (this(), 'I_GTM_TIN7'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',1), (gtm_wrapper,'tim_1_muxin_6_i',1), (gtm_wrapper,'tim_3_muxin_0_i',10)]), name='I_GTM_TIN6', groups='GTM')
connect_digital_port('P02', 'AltIn', 6, (this(), 'I_GTM_TIN6'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',1), (gtm_wrapper,'tim_1_muxin_5_i',1)]), name='I_GTM_TIN5', groups='GTM')
connect_digital_port('P02', 'AltIn', 5, (this(), 'I_GTM_TIN5'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',1), (gtm_wrapper,'tim_1_muxin_4_i',1)]), name='I_GTM_TIN4', groups='GTM')
connect_digital_port('P02', 'AltIn', 4, (this(), 'I_GTM_TIN4'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',2), (gtm_wrapper,'tim_1_muxin_3_i',2)]), name='I_GTM_TIN3', groups='GTM')
connect_digital_port('P02', 'AltIn', 3, (this(), 'I_GTM_TIN3'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',2), (gtm_wrapper,'tim_1_muxin_2_i',2)]), name='I_GTM_TIN2', groups='GTM')
connect_digital_port('P02', 'AltIn', 2, (this(), 'I_GTM_TIN2'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',2), (gtm_wrapper,'tim_1_muxin_1_i',2)]), name='I_GTM_TIN1', groups='GTM')
connect_digital_port('P02', 'AltIn', 1, (this(), 'I_GTM_TIN1'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',2), (gtm_wrapper,'tim_1_muxin_0_i',2)]), name='I_GTM_TIN0', groups='GTM')
connect_digital_port('P02', 'AltIn', 0, (this(), 'I_GTM_TIN0'))
expose(connect([(gtm_wrapper,'tim_3_muxin_0_i',7), (gtm_wrapper,'tim_4_muxin_0_i',5)]), name='I_GTM_TIN128', groups='GTM')
connect_digital_port('P12', 'AltIn', 0, (this(), 'I_GTM_TIN128'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',1), (gtm_wrapper,'tim_3_muxin_0_i',1), (gtm_wrapper,'tim_5_muxin_4_i',10)]), name='I_GTM_TIN9', groups='GTM')
connect_digital_port('P00', 'AltIn', 0, (this(), 'I_GTM_TIN9'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',2), (gtm_wrapper,'tim_3_muxin_0_i',2), (gtm_wrapper,'tim_3_muxin_2_i',10)]), name='I_GTM_TIN8', groups='GTM')
connect_digital_port('P02', 'AltIn', 8, (this(), 'I_GTM_TIN8'))
expose(connect([(gtm_wrapper,'tim_3_muxin_1_i',6), (gtm_wrapper,'tim_4_muxin_1_i',6)]), name='I_GTM_TIN129', groups='GTM')
connect_digital_port('P12', 'AltIn', 1, (this(), 'I_GTM_TIN129'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',8), (gtm_wrapper,'tim_1_muxin_4_i',8), (gtm_wrapper,'tim_4_muxin_2_i',12)]), name='I_GTM_TIN57', groups='GTM')
connect_digital_port('P21', 'AltIn', 6, (this(), 'I_GTM_TIN57'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',6), (gtm_wrapper,'tim_1_muxin_3_i',6), (gtm_wrapper,'tim_5_muxin_7_i',11)]), name='I_GTM_TIN56', groups='GTM')
connect_digital_port('P21', 'AltIn', 5, (this(), 'I_GTM_TIN56'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',6), (gtm_wrapper,'tim_1_muxin_2_i',6), (gtm_wrapper,'tim_5_muxin_6_i',12)]), name='I_GTM_TIN55', groups='GTM')
connect_digital_port('P21', 'AltIn', 4, (this(), 'I_GTM_TIN55'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',6), (gtm_wrapper,'tim_1_muxin_1_i',6), (gtm_wrapper,'tim_5_muxin_5_i',12)]), name='I_GTM_TIN54', groups='GTM')
connect_digital_port('P21', 'AltIn', 3, (this(), 'I_GTM_TIN54'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',7), (gtm_wrapper,'tim_1_muxin_0_i',7), (gtm_wrapper,'tim_5_muxin_4_i',11)]), name='I_GTM_TIN53', groups='GTM')
connect_digital_port('P21', 'AltIn', 2, (this(), 'I_GTM_TIN53'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',6), (gtm_wrapper,'tim_3_muxin_5_i',6), (gtm_wrapper,'tim_4_muxin_1_i',13)]), name='I_GTM_TIN52', groups='GTM')
connect_digital_port('P21', 'AltIn', 1, (this(), 'I_GTM_TIN52'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',6), (gtm_wrapper,'tim_3_muxin_4_i',6), (gtm_wrapper,'tim_4_muxin_0_i',11)]), name='I_GTM_TIN51', groups='GTM')
connect_digital_port('P21', 'AltIn', 0, (this(), 'I_GTM_TIN51'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',4), (gtm_wrapper,'tim_1_muxin_4_i',4)]), name='I_GTM_TIN50', groups='GTM')
connect_digital_port('P22', 'AltIn', 3, (this(), 'I_GTM_TIN50'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',7), (gtm_wrapper,'tim_1_muxin_4_i',9), (gtm_wrapper,'tim_1_muxin_6_i',7)]), name='I_GTM_TIN59', groups='GTM')
connect_digital_port('P20', 'AltIn', 0, (this(), 'I_GTM_TIN59'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',7), (gtm_wrapper,'tim_1_muxin_5_i',7), (gtm_wrapper,'tim_4_muxin_3_i',12)]), name='I_GTM_TIN58', groups='GTM')
connect_digital_port('P21', 'AltIn', 7, (this(), 'I_GTM_TIN58'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',3), (gtm_wrapper,'tim_3_muxin_7_i',3)]), name='I_GTM_TIN93', groups='GTM')
connect_digital_port('P13', 'AltIn', 2, (this(), 'I_GTM_TIN93'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',3), (gtm_wrapper,'tim_3_muxin_6_i',3)]), name='I_GTM_TIN92', groups='GTM')
connect_digital_port('P13', 'AltIn', 1, (this(), 'I_GTM_TIN92'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',3), (gtm_wrapper,'tim_3_muxin_5_i',3)]), name='I_GTM_TIN91', groups='GTM')
connect_digital_port('P13', 'AltIn', 0, (this(), 'I_GTM_TIN91'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',3), (gtm_wrapper,'tim_3_muxin_4_i',3)]), name='I_GTM_TIN90', groups='GTM')
connect_digital_port('P14', 'AltIn', 10, (this(), 'I_GTM_TIN90'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',8), (gtm_wrapper,'tim_4_muxin_7_i',4)]), name='I_GTM_TIN126', groups='GTM')
connect_digital_port('P11', 'AltIn', 14, (this(), 'I_GTM_TIN126'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',2), (gtm_wrapper,'tim_3_muxin_2_i',2)]), name='I_GTM_TIN96', groups='GTM')
connect_digital_port('P11', 'AltIn', 3, (this(), 'I_GTM_TIN96'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',8), (gtm_wrapper,'tim_4_muxin_5_i',5)]), name='I_GTM_TIN124', groups='GTM')
connect_digital_port('P11', 'AltIn', 8, (this(), 'I_GTM_TIN124'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',7), (gtm_wrapper,'tim_4_muxin_6_i',5)]), name='I_GTM_TIN125', groups='GTM')
connect_digital_port('P11', 'AltIn', 13, (this(), 'I_GTM_TIN125'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',5), (gtm_wrapper,'tim_1_muxin_5_i',5)]), name='I_GTM_TIN40', groups='GTM')
connect_digital_port('P32', 'AltIn', 4, (this(), 'I_GTM_TIN40'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',4), (gtm_wrapper,'tim_1_muxin_5_i',4)]), name='I_GTM_TIN41', groups='GTM')
connect_digital_port('P23', 'AltIn', 0, (this(), 'I_GTM_TIN41'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',4), (gtm_wrapper,'tim_1_muxin_6_i',4)]), name='I_GTM_TIN42', groups='GTM')
connect_digital_port('P23', 'AltIn', 1, (this(), 'I_GTM_TIN42'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',5), (gtm_wrapper,'tim_1_muxin_6_i',5)]), name='I_GTM_TIN43', groups='GTM')
connect_digital_port('P23', 'AltIn', 2, (this(), 'I_GTM_TIN43'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',4), (gtm_wrapper,'tim_1_muxin_7_i',4)]), name='I_GTM_TIN44', groups='GTM')
connect_digital_port('P23', 'AltIn', 3, (this(), 'I_GTM_TIN44'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',5), (gtm_wrapper,'tim_1_muxin_7_i',5)]), name='I_GTM_TIN45', groups='GTM')
connect_digital_port('P23', 'AltIn', 4, (this(), 'I_GTM_TIN45'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',7), (gtm_wrapper,'tim_1_muxin_2_i',7)]), name='I_GTM_TIN46', groups='GTM')
connect_digital_port('P23', 'AltIn', 5, (this(), 'I_GTM_TIN46'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',7), (gtm_wrapper,'tim_1_muxin_1_i',7)]), name='I_GTM_TIN47', groups='GTM')
connect_digital_port('P22', 'AltIn', 0, (this(), 'I_GTM_TIN47'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',8), (gtm_wrapper,'tim_1_muxin_0_i',8)]), name='I_GTM_TIN48', groups='GTM')
connect_digital_port('P22', 'AltIn', 1, (this(), 'I_GTM_TIN48'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',7), (gtm_wrapper,'tim_1_muxin_3_i',7)]), name='I_GTM_TIN49', groups='GTM')
connect_digital_port('P22', 'AltIn', 2, (this(), 'I_GTM_TIN49'))
expose(connect([(gtm_wrapper,'tim_3_muxin_5_i',8), (gtm_wrapper,'tim_4_muxin_1_i',14), (gtm_wrapper,'tim_5_muxin_5_i',9)]), name='I_GTM_TIN140', groups='GTM')
connect_digital_port('P32', 'AltIn', 5, (this(), 'I_GTM_TIN140'))
expose(connect([(gtm_wrapper,'tim_3_muxin_6_i',8), (gtm_wrapper,'tim_4_muxin_4_i',15), (gtm_wrapper,'tim_5_muxin_6_i',9)]), name='I_GTM_TIN141', groups='GTM')
connect_digital_port('P32', 'AltIn', 6, (this(), 'I_GTM_TIN141'))
expose(connect([(gtm_wrapper,'tim_3_muxin_7_i',8), (gtm_wrapper,'tim_4_muxin_0_i',15), (gtm_wrapper,'tim_5_muxin_7_i',8)]), name='I_GTM_TIN142', groups='GTM')
connect_digital_port('P32', 'AltIn', 7, (this(), 'I_GTM_TIN142'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',8), (gtm_wrapper,'tim_4_muxin_5_i',14), (gtm_wrapper,'tim_5_muxin_0_i',8)]), name='I_GTM_TIN143', groups='GTM')
connect_digital_port('P33', 'AltIn', 14, (this(), 'I_GTM_TIN143'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',7), (gtm_wrapper,'tim_4_muxin_6_i',12), (gtm_wrapper,'tim_5_muxin_1_i',9)]), name='I_GTM_TIN144', groups='GTM')
connect_digital_port('P33', 'AltIn', 15, (this(), 'I_GTM_TIN144'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',9), (gtm_wrapper,'tim_3_muxin_4_i',12), (gtm_wrapper,'tim_5_muxin_3_i',9)]), name='I_GTM_TIN146', groups='GTM')
connect_digital_port('P34', 'AltIn', 1, (this(), 'I_GTM_TIN146'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',8), (gtm_wrapper,'tim_3_muxin_5_i',13), (gtm_wrapper,'tim_5_muxin_4_i',9)]), name='I_GTM_TIN147', groups='GTM')
connect_digital_port('P34', 'AltIn', 2, (this(), 'I_GTM_TIN147'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',9), (gtm_wrapper,'tim_3_muxin_6_i',13), (gtm_wrapper,'tim_5_muxin_5_i',10)]), name='I_GTM_TIN148', groups='GTM')
connect_digital_port('P34', 'AltIn', 3, (this(), 'I_GTM_TIN148'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',8), (gtm_wrapper,'tim_3_muxin_7_i',12), (gtm_wrapper,'tim_5_muxin_6_i',10)]), name='I_GTM_TIN149', groups='GTM')
connect_digital_port('P34', 'AltIn', 4, (this(), 'I_GTM_TIN149'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',5), (gtm_wrapper,'tim_3_muxin_1_i',5)]), name='I_GTM_TIN35', groups='GTM')
connect_digital_port('P33', 'AltIn', 13, (this(), 'I_GTM_TIN35'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',6), (gtm_wrapper,'tim_3_muxin_0_i',6)]), name='I_GTM_TIN34', groups='GTM')
connect_digital_port('P33', 'AltIn', 12, (this(), 'I_GTM_TIN34'))
expose(connect([(gtm_wrapper,'tim_3_muxin_3_i',15)]), name='I_GTM_TIN37', groups='GTM')
connect_digital_port('P32', 'AltIn', 1, (this(), 'I_GTM_TIN37'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',5), (gtm_wrapper,'tim_3_muxin_2_i',5)]), name='I_GTM_TIN36', groups='GTM')
connect_digital_port('P32', 'AltIn', 0, (this(), 'I_GTM_TIN36'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',9), (gtm_wrapper,'tim_1_muxin_1_i',9)]), name='I_GTM_TIN31', groups='GTM')
connect_digital_port('P33', 'AltIn', 9, (this(), 'I_GTM_TIN31'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',7), (gtm_wrapper,'tim_1_muxin_4_i',7)]), name='I_GTM_TIN30', groups='GTM')
connect_digital_port('P33', 'AltIn', 8, (this(), 'I_GTM_TIN30'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',8), (gtm_wrapper,'tim_1_muxin_2_i',8)]), name='I_GTM_TIN33', groups='GTM')
connect_digital_port('P33', 'AltIn', 11, (this(), 'I_GTM_TIN33'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',9), (gtm_wrapper,'tim_1_muxin_0_i',9), (gtm_wrapper,'tim_4_muxin_4_i',14)]), name='I_GTM_TIN32', groups='GTM')
connect_digital_port('P33', 'AltIn', 10, (this(), 'I_GTM_TIN32'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',5), (gtm_wrapper,'tim_1_muxin_4_i',5)]), name='I_GTM_TIN39', groups='GTM')
connect_digital_port('P32', 'AltIn', 3, (this(), 'I_GTM_TIN39'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',8), (gtm_wrapper,'tim_1_muxin_3_i',8)]), name='I_GTM_TIN38', groups='GTM')
connect_digital_port('P32', 'AltIn', 2, (this(), 'I_GTM_TIN38'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',9), (gtm_wrapper,'tim_4_muxin_7_i',12), (gtm_wrapper,'tim_5_muxin_7_i',9)]), name='I_GTM_TIN150', groups='GTM')
connect_digital_port('P34', 'AltIn', 5, (this(), 'I_GTM_TIN150'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',10), (gtm_wrapper,'tim_1_muxin_0_i',10), (gtm_wrapper,'tim_4_muxin_4_i',10)]), name='I_GTM_TIN26', groups='GTM')
connect_digital_port('P33', 'AltIn', 4, (this(), 'I_GTM_TIN26'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',8), (gtm_wrapper,'tim_1_muxin_1_i',8), (gtm_wrapper,'tim_4_muxin_5_i',10)]), name='I_GTM_TIN27', groups='GTM')
connect_digital_port('P33', 'AltIn', 5, (this(), 'I_GTM_TIN27'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',6), (gtm_wrapper,'tim_1_muxin_6_i',6), (gtm_wrapper,'tim_3_muxin_2_i',14)]), name='I_GTM_TIN24', groups='GTM')
connect_digital_port('P33', 'AltIn', 2, (this(), 'I_GTM_TIN24'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',6), (gtm_wrapper,'tim_1_muxin_7_i',6), (gtm_wrapper,'tim_3_muxin_3_i',12)]), name='I_GTM_TIN25', groups='GTM')
connect_digital_port('P33', 'AltIn', 3, (this(), 'I_GTM_TIN25'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',6), (gtm_wrapper,'tim_1_muxin_4_i',6), (gtm_wrapper,'tim_3_muxin_0_i',13)]), name='I_GTM_TIN22', groups='GTM')
connect_digital_port('P33', 'AltIn', 0, (this(), 'I_GTM_TIN22'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',6), (gtm_wrapper,'tim_1_muxin_5_i',6), (gtm_wrapper,'tim_3_muxin_1_i',15)]), name='I_GTM_TIN23', groups='GTM')
connect_digital_port('P33', 'AltIn', 1, (this(), 'I_GTM_TIN23'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',1), (gtm_wrapper,'tim_1_muxin_2_i',1), (gtm_wrapper,'tim_4_muxin_2_i',11)]), name='I_GTM_TIN20', groups='GTM')
connect_digital_port('P00', 'AltIn', 11, (this(), 'I_GTM_TIN20'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',1), (gtm_wrapper,'tim_1_muxin_3_i',1), (gtm_wrapper,'tim_4_muxin_3_i',11)]), name='I_GTM_TIN21', groups='GTM')
connect_digital_port('P00', 'AltIn', 12, (this(), 'I_GTM_TIN21'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',9), (gtm_wrapper,'tim_1_muxin_2_i',9)]), name='I_GTM_TIN28', groups='GTM')
connect_digital_port('P33', 'AltIn', 6, (this(), 'I_GTM_TIN28'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',9), (gtm_wrapper,'tim_1_muxin_3_i',9)]), name='I_GTM_TIN29', groups='GTM')
connect_digital_port('P33', 'AltIn', 7, (this(), 'I_GTM_TIN29'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',9), (gtm_wrapper,'tim_2_muxin_5_i',2), (gtm_wrapper,'tim_3_muxin_5_i',2)]), name='I_GTM_TIN99', groups='GTM')
connect_digital_port('P11', 'AltIn', 10, (this(), 'I_GTM_TIN99'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',2), (gtm_wrapper,'tim_3_muxin_4_i',2)]), name='I_GTM_TIN98', groups='GTM')
connect_digital_port('P11', 'AltIn', 9, (this(), 'I_GTM_TIN98'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',8), (gtm_wrapper,'tim_4_muxin_3_i',5)]), name='I_GTM_TIN122', groups='GTM')
connect_digital_port('P11', 'AltIn', 5, (this(), 'I_GTM_TIN122'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',7), (gtm_wrapper,'tim_4_muxin_4_i',5)]), name='I_GTM_TIN123', groups='GTM')
connect_digital_port('P11', 'AltIn', 7, (this(), 'I_GTM_TIN123'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',6), (gtm_wrapper,'tim_4_muxin_1_i',5)]), name='I_GTM_TIN120', groups='GTM')
connect_digital_port('P11', 'AltIn', 1, (this(), 'I_GTM_TIN120'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',6), (gtm_wrapper,'tim_4_muxin_2_i',5)]), name='I_GTM_TIN121', groups='GTM')
connect_digital_port('P11', 'AltIn', 4, (this(), 'I_GTM_TIN121'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',2), (gtm_wrapper,'tim_3_muxin_3_i',2)]), name='I_GTM_TIN97', groups='GTM')
connect_digital_port('P11', 'AltIn', 6, (this(), 'I_GTM_TIN97'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',8), (gtm_wrapper,'tim_4_muxin_7_i',5)]), name='I_GTM_TIN127', groups='GTM')
connect_digital_port('P11', 'AltIn', 15, (this(), 'I_GTM_TIN127'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',3), (gtm_wrapper,'tim_3_muxin_1_i',3)]), name='I_GTM_TIN95', groups='GTM')
connect_digital_port('P11', 'AltIn', 2, (this(), 'I_GTM_TIN95'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',3), (gtm_wrapper,'tim_3_muxin_0_i',3)]), name='I_GTM_TIN94', groups='GTM')
connect_digital_port('P13', 'AltIn', 3, (this(), 'I_GTM_TIN94'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',1), (gtm_wrapper,'tim_3_muxin_3_i',1)]), name='I_GTM_TIN13', groups='GTM')
connect_digital_port('P00', 'AltIn', 4, (this(), 'I_GTM_TIN13'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',1), (gtm_wrapper,'tim_3_muxin_2_i',1), (gtm_wrapper,'tim_5_muxin_7_i',10)]), name='I_GTM_TIN12', groups='GTM')
connect_digital_port('P00', 'AltIn', 3, (this(), 'I_GTM_TIN12'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',2), (gtm_wrapper,'tim_3_muxin_1_i',2), (gtm_wrapper,'tim_5_muxin_6_i',11)]), name='I_GTM_TIN11', groups='GTM')
connect_digital_port('P00', 'AltIn', 2, (this(), 'I_GTM_TIN11'))
expose(connect([(gtm_wrapper,'tim_2_muxin_1_i',1), (gtm_wrapper,'tim_3_muxin_1_i',1), (gtm_wrapper,'tim_5_muxin_5_i',11)]), name='I_GTM_TIN10', groups='GTM')
connect_digital_port('P00', 'AltIn', 1, (this(), 'I_GTM_TIN10'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',1), (gtm_wrapper,'tim_3_muxin_3_i',11), (gtm_wrapper,'tim_3_muxin_7_i',1)]), name='I_GTM_TIN17', groups='GTM')
connect_digital_port('P00', 'AltIn', 8, (this(), 'I_GTM_TIN17'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',1), (gtm_wrapper,'tim_3_muxin_2_i',11), (gtm_wrapper,'tim_3_muxin_6_i',1)]), name='I_GTM_TIN16', groups='GTM')
connect_digital_port('P00', 'AltIn', 7, (this(), 'I_GTM_TIN16'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',1), (gtm_wrapper,'tim_3_muxin_1_i',14), (gtm_wrapper,'tim_3_muxin_5_i',1)]), name='I_GTM_TIN15', groups='GTM')
connect_digital_port('P00', 'AltIn', 6, (this(), 'I_GTM_TIN15'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',1), (gtm_wrapper,'tim_3_muxin_0_i',11), (gtm_wrapper,'tim_3_muxin_4_i',1)]), name='I_GTM_TIN14', groups='GTM')
connect_digital_port('P00', 'AltIn', 5, (this(), 'I_GTM_TIN14'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',1), (gtm_wrapper,'tim_1_muxin_1_i',1), (gtm_wrapper,'tim_4_muxin_1_i',11)]), name='I_GTM_TIN19', groups='GTM')
connect_digital_port('P00', 'AltIn', 10, (this(), 'I_GTM_TIN19'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',1), (gtm_wrapper,'tim_1_muxin_0_i',1), (gtm_wrapper,'tim_4_muxin_0_i',7)]), name='I_GTM_TIN18', groups='GTM')
connect_digital_port('P00', 'AltIn', 9, (this(), 'I_GTM_TIN18'))
expose(connect([(gtm_wrapper,'tim_0_muxin_7_i',2), (gtm_wrapper,'tim_1_muxin_7_i',2)]), name='I_GTM_TIN84', groups='GTM')
connect_digital_port('P14', 'AltIn', 4, (this(), 'I_GTM_TIN84'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',4), (gtm_wrapper,'tim_1_muxin_0_i',4)]), name='I_GTM_TIN85', groups='GTM')
connect_digital_port('P14', 'AltIn', 5, (this(), 'I_GTM_TIN85'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',4), (gtm_wrapper,'tim_1_muxin_1_i',4)]), name='I_GTM_TIN86', groups='GTM')
connect_digital_port('P14', 'AltIn', 6, (this(), 'I_GTM_TIN86'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',5), (gtm_wrapper,'tim_1_muxin_0_i',5), (gtm_wrapper,'tim_4_muxin_7_i',10)]), name='I_GTM_TIN87', groups='GTM')
connect_digital_port('P14', 'AltIn', 7, (this(), 'I_GTM_TIN87'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',5), (gtm_wrapper,'tim_1_muxin_3_i',5)]), name='I_GTM_TIN80', groups='GTM')
connect_digital_port('P14', 'AltIn', 0, (this(), 'I_GTM_TIN80'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',3), (gtm_wrapper,'tim_1_muxin_4_i',3)]), name='I_GTM_TIN81', groups='GTM')
connect_digital_port('P14', 'AltIn', 1, (this(), 'I_GTM_TIN81'))
expose(connect([(gtm_wrapper,'tim_0_muxin_5_i',3), (gtm_wrapper,'tim_1_muxin_5_i',3)]), name='I_GTM_TIN82', groups='GTM')
connect_digital_port('P14', 'AltIn', 2, (this(), 'I_GTM_TIN82'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',3), (gtm_wrapper,'tim_1_muxin_6_i',3)]), name='I_GTM_TIN83', groups='GTM')
connect_digital_port('P14', 'AltIn', 3, (this(), 'I_GTM_TIN83'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',3), (gtm_wrapper,'tim_3_muxin_2_i',3)]), name='I_GTM_TIN88', groups='GTM')
connect_digital_port('P14', 'AltIn', 8, (this(), 'I_GTM_TIN88'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',3), (gtm_wrapper,'tim_3_muxin_3_i',3)]), name='I_GTM_TIN89', groups='GTM')
connect_digital_port('P14', 'AltIn', 9, (this(), 'I_GTM_TIN89'))
expose(connect([(gtm_wrapper,'tim_1_muxin_3_i',10), (gtm_wrapper,'tim_4_muxin_3_i',7)]), name='I_GTM_TIN139', groups='GTM')
connect_digital_port('P23', 'AltIn', 7, (this(), 'I_GTM_TIN139'))
expose(connect([(gtm_wrapper,'tim_1_muxin_2_i',10), (gtm_wrapper,'tim_4_muxin_2_i',7)]), name='I_GTM_TIN138', groups='GTM')
connect_digital_port('P23', 'AltIn', 6, (this(), 'I_GTM_TIN138'))
expose(connect([(gtm_wrapper,'tim_3_muxin_1_i',7)]), name='I_GTM_TIN131', groups='GTM')
connect_digital_port('P22', 'AltIn', 5, (this(), 'I_GTM_TIN131'))
expose(connect([(gtm_wrapper,'tim_3_muxin_0_i',8)]), name='I_GTM_TIN130', groups='GTM')
connect_digital_port('P22', 'AltIn', 4, (this(), 'I_GTM_TIN130'))
expose(connect([(gtm_wrapper,'tim_3_muxin_3_i',7)]), name='I_GTM_TIN133', groups='GTM')
connect_digital_port('P22', 'AltIn', 7, (this(), 'I_GTM_TIN133'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',14), (gtm_wrapper,'tim_3_muxin_2_i',6)]), name='I_GTM_TIN132', groups='GTM')
connect_digital_port('P22', 'AltIn', 6, (this(), 'I_GTM_TIN132'))
expose(connect([(gtm_wrapper,'tim_3_muxin_5_i',7), (gtm_wrapper,'tim_5_muxin_1_i',10)]), name='I_GTM_TIN135', groups='GTM')
connect_digital_port('P22', 'AltIn', 9, (this(), 'I_GTM_TIN135'))
expose(connect([(gtm_wrapper,'tim_3_muxin_4_i',7), (gtm_wrapper,'tim_5_muxin_0_i',4)]), name='I_GTM_TIN134', groups='GTM')
connect_digital_port('P22', 'AltIn', 8, (this(), 'I_GTM_TIN134'))
expose(connect([(gtm_wrapper,'tim_3_muxin_7_i',7), (gtm_wrapper,'tim_5_muxin_3_i',10)]), name='I_GTM_TIN137', groups='GTM')
connect_digital_port('P22', 'AltIn', 11, (this(), 'I_GTM_TIN137'))
expose(connect([(gtm_wrapper,'tim_3_muxin_6_i',7), (gtm_wrapper,'tim_5_muxin_2_i',8)]), name='I_GTM_TIN136', groups='GTM')
connect_digital_port('P22', 'AltIn', 10, (this(), 'I_GTM_TIN136'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',3), (gtm_wrapper,'tim_1_muxin_2_i',3), (gtm_wrapper,'tim_4_muxin_5_i',12)]), name='I_GTM_TIN104', groups='GTM')
connect_digital_port('P10', 'AltIn', 2, (this(), 'I_GTM_TIN104'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',3), (gtm_wrapper,'tim_1_muxin_3_i',3), (gtm_wrapper,'tim_4_muxin_6_i',10)]), name='I_GTM_TIN105', groups='GTM')
connect_digital_port('P10', 'AltIn', 3, (this(), 'I_GTM_TIN105'))
expose(connect([(gtm_wrapper,'tim_0_muxin_6_i',2), (gtm_wrapper,'tim_1_muxin_6_i',2), (gtm_wrapper,'tim_4_muxin_7_i',3)]), name='I_GTM_TIN106', groups='GTM')
connect_digital_port('P10', 'AltIn', 4, (this(), 'I_GTM_TIN106'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',4), (gtm_wrapper,'tim_1_muxin_2_i',4), (gtm_wrapper,'tim_4_muxin_3_i',13)]), name='I_GTM_TIN107', groups='GTM')
connect_digital_port('P10', 'AltIn', 5, (this(), 'I_GTM_TIN107'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',2), (gtm_wrapper,'tim_3_muxin_0_i',14), (gtm_wrapper,'tim_3_muxin_6_i',2)]), name='I_GTM_TIN100', groups='GTM')
connect_digital_port('P11', 'AltIn', 11, (this(), 'I_GTM_TIN100'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',2), (gtm_wrapper,'tim_3_muxin_7_i',2)]), name='I_GTM_TIN101', groups='GTM')
connect_digital_port('P11', 'AltIn', 12, (this(), 'I_GTM_TIN101'))
expose(connect([(gtm_wrapper,'tim_0_muxin_4_i',2), (gtm_wrapper,'tim_1_muxin_4_i',2), (gtm_wrapper,'tim_4_muxin_0_i',12)]), name='I_GTM_TIN102', groups='GTM')
connect_digital_port('P10', 'AltIn', 0, (this(), 'I_GTM_TIN102'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',3), (gtm_wrapper,'tim_1_muxin_1_i',3), (gtm_wrapper,'tim_4_muxin_4_i',12)]), name='I_GTM_TIN103', groups='GTM')
connect_digital_port('P10', 'AltIn', 1, (this(), 'I_GTM_TIN103'))
expose(connect([(gtm_wrapper,'tim_0_muxin_3_i',4), (gtm_wrapper,'tim_1_muxin_3_i',4), (gtm_wrapper,'tim_4_muxin_2_i',13)]), name='I_GTM_TIN108', groups='GTM')
connect_digital_port('P10', 'AltIn', 6, (this(), 'I_GTM_TIN108'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',3), (gtm_wrapper,'tim_1_muxin_0_i',3)]), name='I_GTM_TIN109', groups='GTM')
connect_digital_port('P10', 'AltIn', 7, (this(), 'I_GTM_TIN109'))
expose(connect([(gtm_wrapper,'tim_0_muxin_2_i',5), (gtm_wrapper,'tim_1_muxin_2_i',5)]), name='I_GTM_TIN79', groups='GTM')
connect_digital_port('P15', 'AltIn', 8, (this(), 'I_GTM_TIN79'))
expose(connect([(gtm_wrapper,'tim_0_muxin_1_i',5), (gtm_wrapper,'tim_1_muxin_1_i',5)]), name='I_GTM_TIN78', groups='GTM')
connect_digital_port('P15', 'AltIn', 7, (this(), 'I_GTM_TIN78'))
expose(connect([(gtm_wrapper,'tim_2_muxin_3_i',4), (gtm_wrapper,'tim_3_muxin_3_i',4)]), name='I_GTM_TIN71', groups='GTM')
connect_digital_port('P15', 'AltIn', 0, (this(), 'I_GTM_TIN71'))
expose(connect([(gtm_wrapper,'tim_2_muxin_2_i',4), (gtm_wrapper,'tim_3_muxin_2_i',4)]), name='I_GTM_TIN70', groups='GTM')
connect_digital_port('P20', 'AltIn', 14, (this(), 'I_GTM_TIN70'))
expose(connect([(gtm_wrapper,'tim_2_muxin_5_i',4), (gtm_wrapper,'tim_3_muxin_5_i',4)]), name='I_GTM_TIN73', groups='GTM')
connect_digital_port('P15', 'AltIn', 2, (this(), 'I_GTM_TIN73'))
expose(connect([(gtm_wrapper,'tim_2_muxin_4_i',4), (gtm_wrapper,'tim_3_muxin_4_i',4)]), name='I_GTM_TIN72', groups='GTM')
connect_digital_port('P15', 'AltIn', 1, (this(), 'I_GTM_TIN72'))
expose(connect([(gtm_wrapper,'tim_2_muxin_7_i',4), (gtm_wrapper,'tim_3_muxin_7_i',4)]), name='I_GTM_TIN75', groups='GTM')
connect_digital_port('P15', 'AltIn', 4, (this(), 'I_GTM_TIN75'))
expose(connect([(gtm_wrapper,'tim_2_muxin_6_i',4), (gtm_wrapper,'tim_3_muxin_6_i',4)]), name='I_GTM_TIN74', groups='GTM')
connect_digital_port('P15', 'AltIn', 3, (this(), 'I_GTM_TIN74'))
expose(connect([(gtm_wrapper,'tim_0_muxin_0_i',6), (gtm_wrapper,'tim_1_muxin_0_i',6), (gtm_wrapper,'tim_2_muxin_2_i',14)]), name='I_GTM_TIN77', groups='GTM')
connect_digital_port('P15', 'AltIn', 6, (this(), 'I_GTM_TIN77'))
expose(connect([(gtm_wrapper,'tim_2_muxin_0_i',4), (gtm_wrapper,'tim_3_muxin_0_i',4)]), name='I_GTM_TIN76', groups='GTM')
connect_digital_port('P15', 'AltIn', 5, (this(), 'I_GTM_TIN76'))

#EVADC
#connect SPB slave
spb_router_connect(evadc, 'EVADC','evadc')
spbClk_Net.append((evadc,'SysClk_InPort'))
allCpuEndInit_Net.append((evadc,'ifxEvadcEndInit_InPort'))
safetyEndInit_Net.append((evadc,'ifxEvadcSafeEndInit_InPort'))
applOrSystRst_Net.append((evadc,'Reset_InPort'))

# section 26.16.4 in User Manual
NUM_GT_CHANNEL_PER_GROUP = 16
NUM_TR_CHANNEL_PER_GROUP_0_11 = 18
NUM_TR_CHANNEL_PER_GROUP_12_19 = 16
NUM_GROUP = 20

# helpers for index computing
REQGTA_INDEX = 0 ; REQTRA_INDEX = 0
REQGTB_INDEX = 1 ; REQTRB_INDEX = 1
REQGTC_INDEX = 2 ; REQTRC_INDEX = 2
REQGTD_INDEX = 3 ; REQTRD_INDEX = 3
REQGTE_INDEX = 4 ; REQTRE_INDEX = 4
REQGTF_INDEX = 5 ; REQTRF_INDEX = 5
REQGTG_INDEX = 6 ; REQTRG_INDEX = 6
REQGTH_INDEX = 7 ; REQTRH_INDEX = 7
REQGTI_INDEX = 8 ; REQTRI_INDEX = 8
REQGTJ_INDEX = 9 ; REQTRJ_INDEX = 9
REQGTK_INDEX = 10; REQTRK_INDEX = 10
REQGTL_INDEX = 11; REQTRL_INDEX = 11
REQGTM_INDEX = 12; REQTRM_INDEX = 12
REQGTN_INDEX = 13; REQTRN_INDEX = 13
REQGTO_INDEX = 14; REQTRO_INDEX = 14
REQGTP_INDEX = 15; REQTRP_INDEX = 15

INDEX_G12_TR = 216 #(NUM_TR_CHANNEL_PER_GROUP_0_11 * 12)

#each sr0 could be connected to several component signals
for i in range(0,NUM_GROUP):
    evadc_GxSR0_Net.append([])
    evadc_GxSR1_Net.append([])
    evadc_GxSR2_Net.append([])
    evadc_GxSR3_Net.append([])


# Gate Inputs for Primary and Secondary Groups
# (x = 0-7, 8-11, input line selected via bitfield GTSEL = [yyyyB])
# adcReqGt_i is a vector of size 192 = 16*12
for x in range(0,12):
    adc_trig0_out_Net.insert(x, [(evadc,'adcReqGt_i', REQGTA_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqTr_i', REQTRI_INDEX + x * NUM_TR_CHANNEL_PER_GROUP_0_11)]) # GxREQGTA & GxREQTRI
    adc_trig1_out_Net.insert(x, [(evadc,'adcReqGt_i', REQGTB_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqTr_i', REQTRJ_INDEX + x * NUM_TR_CHANNEL_PER_GROUP_0_11)]) # GxREQGTB & GxREQTRJ
    # connect((evadc,'adcReqGt_i', REQGTC_INDEX + x),(ccu,'ccu_trig0_out',x))  # GxREQGTC
    # connect((evadc,'adcReqGt_i', REQGTD_INDEX + x),(ccu,'ccu_trig1_out',x))  # GxREQGTD
    # connect((evadc,'adcReqGt_i', REQGTE_INDEX + x),(ccu,'ccu_trig2_out',x))  # GxREQGTE
    # GxREQGTF : no connection
    expose_alternate_name((evadc,'adcReqGt_i', REQGTF_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), name="I_EVADC_G%iREQGTF"%x, groups='EVADC')
    adc_trig4_out_Net.insert(x, [(evadc,'adcReqGt_i', REQGTG_INDEX + x * NUM_GT_CHANNEL_PER_GROUP),(evadc,'adcReqTr_i', REQTRG_INDEX + x * NUM_TR_CHANNEL_PER_GROUP_0_11)]) # GxREQGTG & GxREQTRG
    # GxREQGTH : no connection
    # GxREQGTI : no connection
    # GxREQGTJ : no connection
    expose_alternate_name((evadc,'adcReqGt_i', REQGTH_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), name="I_EVADC_G%iREQGTH"%x, groups="EVADC")
    expose_alternate_name((evadc,'adcReqGt_i', REQGTI_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), name="I_EVADC_G%iREQGTI"%x, groups="EVADC")
    expose_alternate_name((evadc,'adcReqGt_i', REQGTJ_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), name="I_EVADC_G%iREQGTJ"%x, groups="EVADC")
    adc_trig2_out_Net.insert(x, [(evadc,'adcReqGt_i', REQGTK_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqTr_i', REQTRK_INDEX + x * NUM_TR_CHANNEL_PER_GROUP_0_11)]) # GxREQGTK & GxREQTRK
    adc_trig3_out_Net.insert(x, [(evadc,'adcReqGt_i', REQGTL_INDEX + x * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqTr_i', REQTRL_INDEX + x * NUM_TR_CHANNEL_PER_GROUP_0_11)]) # GxREQGTL & GxREQTRL
    if x in (4, 5, 6, 7):
        connect((evadc,'adcReqGt_i', REQGTM_INDEX + x * NUM_GT_CHANNEL_PER_GROUP),(scu,'scuEruPDOUT_o',x)) # GyREQGTM
     # GxREQGTN : no connection
     # GXREQGTO : no connection
     # GxREQGTP : no connection (internal)

# GxREQGTM
connect([(evadc,'adcReqGt_i', REQGTM_INDEX + 0 * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqGt_i', REQGTM_INDEX + 8 * NUM_GT_CHANNEL_PER_GROUP)], (scu,'scuEruPDOUT_o',0)) # G8REQGTM
connect([(evadc,'adcReqGt_i', REQGTM_INDEX + 1 * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqGt_i', REQGTM_INDEX + 9 * NUM_GT_CHANNEL_PER_GROUP)], (scu,'scuEruPDOUT_o',1)) # G9REQGTM
connect([(evadc,'adcReqGt_i', REQGTM_INDEX + 2 * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqGt_i', REQGTM_INDEX + 10 * NUM_GT_CHANNEL_PER_GROUP)],(scu,'scuEruPDOUT_o',2)) # G10REQGTM
connect([(evadc,'adcReqGt_i', REQGTM_INDEX + 3 * NUM_GT_CHANNEL_PER_GROUP), (evadc,'adcReqGt_i', REQGTM_INDEX + 11 * NUM_GT_CHANNEL_PER_GROUP)],(scu,'scuEruPDOUT_o',3)) # G11REQGTM

# GxREQGTP
for x in range(0,12):
    for y in range(0,3):
        connect((evadc,'adcReqGtSel_o', x * 3 + y), (evadc,'adcReqTr_i', x * NUM_TR_CHANNEL_PER_GROUP_0_11 + y  + REQTRP_INDEX))

##############################
# GxREQGTySEL to GxREQTRyP????
##############################

# adcReqTr_i is a vector of size 344 = 16*20 + 24
#GxREQTRA : TODO : TO UPDATE when CCU model is available
# for x in range(0,12):
    # connect((evadc,'adcReqTr_i', REQTRA_INDEX + x),(ccu,'ccu60_sr3_out',x))


#GxREQTRB : TODO : TO UPDATE when CCU model is available
# for x in range(0,12):
    # connect((evadc,'adcReqTr_i', REQTRB_INDEX + x),(ccu,'ccu61_sr3_out',x))


#GxREQTRC : HSPDM_adc_trig
#GxREQTRD : no connection
#GxREQTRE : no connection
#GxREQTRF : no connection
#GxREQTRG I GTM_adcx_trig4 is connected above with GxREQGT
for channel in range(0,12):
    expose_alternate_name((evadc,'adcReqTr_i', REQTRC_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11), name="I_EVADC_G%iREQTRC"%channel, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRD_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11), name="I_EVADC_G%iREQTRD"%channel, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRE_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11), name="I_EVADC_G%iREQTRE"%channel, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRF_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11), name="I_EVADC_G%iREQTRF"%channel, groups="EVADC")

#GxREQTRH
for channel in (4, 5, 6, 7):
    connect((evadc,'adcReqTr_i', REQTRH_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11),(scu,'scuEruIOUT_o',channel))
connect([(evadc,'adcReqTr_i', REQTRH_INDEX + 0 * NUM_TR_CHANNEL_PER_GROUP_0_11),(evadc,'adcReqTr_i', REQTRH_INDEX + 8 * NUM_TR_CHANNEL_PER_GROUP_0_11) ],(scu,'scuEruIOUT_o',0))
connect([(evadc,'adcReqTr_i', REQTRH_INDEX + 1 * NUM_TR_CHANNEL_PER_GROUP_0_11),(evadc,'adcReqTr_i', REQTRH_INDEX + 9 * NUM_TR_CHANNEL_PER_GROUP_0_11) ],(scu,'scuEruIOUT_o',1))
connect([(evadc,'adcReqTr_i', REQTRH_INDEX + 2 * NUM_TR_CHANNEL_PER_GROUP_0_11),(evadc,'adcReqTr_i', REQTRH_INDEX + 10 * NUM_TR_CHANNEL_PER_GROUP_0_11)],(scu,'scuEruIOUT_o',2))
connect([(evadc,'adcReqTr_i', REQTRH_INDEX + 3 * NUM_TR_CHANNEL_PER_GROUP_0_11),(evadc,'adcReqTr_i', REQTRH_INDEX + 11 * NUM_TR_CHANNEL_PER_GROUP_0_11)],(scu,'scuEruIOUT_o',3))


#GxREQTRI I GTM_adcx_trig0 is connected above with GxREQGT
#GxREQTRJ I GTM_adcx_trig1 is connected above with GxREQGT
#GxREQTRK I GTM_adcx_trig2 is connected above with GxREQGT
#GxREQTRL I GTM_adcx_trig3 is connected above with GxREQGT

#GxREQTRM: GxREQTRM I vadc_gxsr1 [1100B] Service request 1, group x
#GxREQTRN: GxREQTRN I vadc_c0sr1 [1101B] Service request 1, common group 0
#GxREQTRO: GxREQTRO I vadc_c1sr1 [1110B] Service request 1, common group 1

for channel in range(0,12):
    evadc_GxSR1_Net[channel].append((evadc,'adcReqTr_i', REQTRM_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11))
    evadc_C0SR1_Net.append((evadc,'adcReqTr_i', REQTRN_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11))
    evadc_C1SR1_Net.append((evadc,'adcReqTr_i', REQTRO_INDEX + channel * NUM_TR_CHANNEL_PER_GROUP_0_11))


################################
# GxREQTRyP to GxREQGTySEL1) ???
################################

for x in range(0,3):
    z = x + 12
    expose_alternate_name((evadc,'adcReqTr_i', REQTRA_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRA"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRB_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRB"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRC_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRC"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRD_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRD"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRE_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRE"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRF_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRF"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRG_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRG"%z, groups="EVADC")
    expose_alternate_name((evadc,'adcReqTr_i', REQTRH_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19), name="I_EVADC_G%iREQTRH"%z, groups="EVADC")
    #GxREQTRI
    adc_trig0_out_Net[x].append((evadc,'adcReqTr_i', REQTRI_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19))
    #GxREQTRJ
    adc_trig1_out_Net[x].append((evadc,'adcReqTr_i', REQTRJ_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19))
    #GxREQTRK
    adc_trig2_out_Net[x].append((evadc,'adcReqTr_i', REQTRK_INDEX + INDEX_G12_TR + x * NUM_TR_CHANNEL_PER_GROUP_12_19))

#GxREQTRL
adc_trig3_out_Net[8].append((evadc,'adcReqTr_i', REQTRL_INDEX +  INDEX_G12_TR + 0 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig3_out_Net[9].append((evadc,'adcReqTr_i', REQTRL_INDEX +  INDEX_G12_TR + 1 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig1_out_Net[8].append((evadc,'adcReqTr_i', REQTRL_INDEX +  INDEX_G12_TR + 2 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig1_out_Net[9].append((evadc,'adcReqTr_i', REQTRL_INDEX +  INDEX_G12_TR + 3 * NUM_TR_CHANNEL_PER_GROUP_12_19))

#GxREQTRM :  Service request 1, group x : see below
adc_trig4_out_Net[8].append((evadc,'adcReqTr_i', REQTRM_INDEX + INDEX_G12_TR +  0 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig4_out_Net[9].append((evadc,'adcReqTr_i', REQTRM_INDEX + INDEX_G12_TR +  1 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig2_out_Net[8].append((evadc,'adcReqTr_i', REQTRM_INDEX + INDEX_G12_TR +  2 * NUM_TR_CHANNEL_PER_GROUP_12_19))
adc_trig2_out_Net[9].append((evadc,'adcReqTr_i', REQTRM_INDEX + INDEX_G12_TR +  3 * NUM_TR_CHANNEL_PER_GROUP_12_19))

# Global Signals and Service Request Lines
# For Primary/Secondary Groups: x=0-7, 8-11, for Fast Compare Channels: z=12-19

#CBFLOUT
connect((evadc, 'ifxEvadcCBflOut_o', 0), [(gtm_wrapper, 'tim_1_muxin_0_i', 13),(gtm_wrapper, 'tim_1_muxin_4_i', 11),(gtm_wrapper, 'tim_2_muxin_0_i', 15),(gtm_wrapper, 'tim_2_muxin_4_i', 15)])
connect((evadc, 'ifxEvadcCBflOut_o', 1), [(gtm_wrapper, 'tim_1_muxin_1_i', 14),(gtm_wrapper, 'tim_1_muxin_5_i', 9),(gtm_wrapper, 'tim_2_muxin_1_i', 15),(gtm_wrapper, 'tim_2_muxin_5_i', 15)])
connect((evadc, 'ifxEvadcCBflOut_o', 2), [(gtm_wrapper, 'tim_1_muxin_2_i', 14),(gtm_wrapper, 'tim_1_muxin_6_i', 8),(gtm_wrapper, 'tim_2_muxin_2_i', 15),(gtm_wrapper, 'tim_2_muxin_6_i', 15)])
connect((evadc, 'ifxEvadcCBflOut_o', 3), [(gtm_wrapper, 'tim_1_muxin_3_i', 11),(gtm_wrapper, 'tim_1_muxin_7_i', 7),(gtm_wrapper, 'tim_2_muxin_3_i', 15),(gtm_wrapper, 'tim_2_muxin_7_i', 15)])

# GxBFL, GxBFSEL, GxBDAT
# => Add connections to GTM_stat_in and GTM_mcs_trigout signals when supported by GTM model
#G12BFL
connect((evadc, 'adcBfl_o', 0), [(gtm_wrapper, 'tim_0_muxin_0_i', 0),
                                 (gtm_wrapper, 'tim_1_muxin_0_i', 0),
                                 (gtm_wrapper, 'tim_2_muxin_0_i', 0),
                                 (gtm_wrapper, 'tim_4_muxin_0_i', 0)])
#G13BFL
connect((evadc, 'adcBfl_o', 1), [(gtm_wrapper, 'tim_0_muxin_1_i', 0),
                                 (gtm_wrapper, 'tim_1_muxin_1_i', 0),
                                 (gtm_wrapper, 'tim_2_muxin_1_i', 0),
                                 (gtm_wrapper, 'tim_4_muxin_1_i', 0)])
#G14BFL
connect((evadc, 'adcBfl_o', 2), [(gtm_wrapper, 'tim_0_muxin_2_i', 0),
                                 (gtm_wrapper, 'tim_1_muxin_2_i', 0),
                                 (gtm_wrapper, 'tim_2_muxin_2_i', 0),
                                 (gtm_wrapper, 'tim_4_muxin_2_i', 0)])
#G15BFL
connect((evadc, 'adcBfl_o', 3), [(gtm_wrapper, 'tim_0_muxin_3_i', 0),
                                 (gtm_wrapper, 'tim_1_muxin_3_i', 0),
                                 (gtm_wrapper, 'tim_2_muxin_3_i', 0),
                                 (gtm_wrapper, 'tim_3_muxin_3_i', 0),
                                 (gtm_wrapper, 'tim_4_muxin_3_i', 0)])
#GxSRm
for x in range(0,12):
    evadc_GxSR0_Net[x].append((ir, 'ifxIr3Irq_i', SRC2IN(0x0670 + 0x10*x)))
    evadc_GxSR1_Net[x].append((ir, 'ifxIr3Irq_i', SRC2IN(0x0670 + 0x10*x + 0x4)))
    evadc_GxSR2_Net[x].append((ir, 'ifxIr3Irq_i', SRC2IN(0x0670 + 0x10*x + 0x8)))
    evadc_GxSR3_Net[x].append((ir, 'ifxIr3Irq_i', SRC2IN(0x0670 + 0x10*x + 0xC)))

for x in range(12,12+NUM_FAST_GROUP):
    evadc_GxSR0_Net[x].append((ir, 'ifxIr3Irq_i', SRC2IN(0x0730 + 0x4*(x-12)))) # SR0 of group x

for x in range(0,12):
    connect((evadc, 'adcSR_o', x * 4), evadc_GxSR0_Net[x])
    connect((evadc, 'adcSR_o', x * 4 + 1), evadc_GxSR1_Net[x])
    connect((evadc, 'adcSR_o', x * 4 + 2), evadc_GxSR2_Net[x])
    connect((evadc, 'adcSR_o', x * 4 + 3), evadc_GxSR3_Net[x])

for x in range(0,4): #G12 to G15
    connect((evadc, 'adcSR_o', 48 + x), evadc_GxSR0_Net[12 + x])

#C0SRm and C1SRm
evadc_C0SR0_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0750))) # C0SR0
evadc_C0SR0_Net.extend([(gtm_wrapper, 'tim_0_muxin_0_i', 15),(gtm_wrapper, 'tim_1_muxin_4_i', 10),(gtm_wrapper, 'tim_2_muxin_0_i', 10)])
evadc_C0SR1_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0754))) # C0SR1
evadc_C0SR1_Net.extend([(gtm_wrapper, 'tim_0_muxin_2_i', 15),(gtm_wrapper, 'tim_1_muxin_6_i', 10),(gtm_wrapper, 'tim_2_muxin_2_i', 10)])
evadc_C0SR2_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0758))) # C0SR2
evadc_C0SR2_Net.extend([(gtm_wrapper, 'tim_0_muxin_4_i', 15),(gtm_wrapper, 'tim_1_muxin_0_i', 12),(gtm_wrapper, 'tim_2_muxin_4_i', 10)])
evadc_C0SR3_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x075C))) # C0SR3
evadc_C0SR3_Net.extend([(gtm_wrapper, 'tim_0_muxin_6_i', 15),(gtm_wrapper, 'tim_1_muxin_2_i', 12),(gtm_wrapper, 'tim_2_muxin_6_i', 10)])
evadc_C1SR0_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0760))) # C1SR0
evadc_C1SR0_Net.extend([(gtm_wrapper, 'tim_0_muxin_1_i', 15),(gtm_wrapper, 'tim_1_muxin_5_i', 10),(gtm_wrapper, 'tim_2_muxin_1_i', 10)])
evadc_C1SR1_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0764))) # C1SR1
evadc_C1SR1_Net.extend([(gtm_wrapper, 'tim_0_muxin_3_i', 15),(gtm_wrapper, 'tim_1_muxin_7_i', 10),(gtm_wrapper, 'tim_2_muxin_3_i', 10)])
evadc_C1SR2_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x0768))) # C1SR2
evadc_C1SR2_Net.extend([(gtm_wrapper, 'tim_0_muxin_5_i', 15),(gtm_wrapper, 'tim_1_muxin_1_i', 12),(gtm_wrapper, 'tim_2_muxin_5_i', 10)])
evadc_C1SR3_Net.append((ir, 'ifxIr3Irq_i', SRC2IN(0x076C))) # C1SR3
evadc_C1SR3_Net.extend([(gtm_wrapper, 'tim_0_muxin_7_i', 15),(gtm_wrapper, 'tim_1_muxin_3_i', 15),(gtm_wrapper, 'tim_2_muxin_7_i', 10)])
connect((evadc, 'ifxEvadcC0SR_o', 0), evadc_C0SR0_Net)
connect((evadc, 'ifxEvadcC0SR_o', 1), evadc_C0SR1_Net)
connect((evadc, 'ifxEvadcC0SR_o', 2), evadc_C0SR2_Net)
connect((evadc, 'ifxEvadcC0SR_o', 3), evadc_C0SR3_Net)
connect((evadc, 'ifxEvadcC1SR_o', 0), evadc_C1SR0_Net)
connect((evadc, 'ifxEvadcC1SR_o', 1), evadc_C1SR1_Net)
connect((evadc, 'ifxEvadcC1SR_o', 2), evadc_C1SR2_Net)
connect((evadc, 'ifxEvadcC1SR_o', 3), evadc_C1SR3_Net)

#GxARBCNT
connect((evadc, 'adcArbCnt_o', 0),  (gtm_wrapper, 'tim_1_muxin_1_i', 15))
connect((evadc, 'adcArbCnt_o', 1),  (gtm_wrapper, 'tim_2_muxin_0_i', 12))
connect((evadc, 'adcArbCnt_o', 2),  (gtm_wrapper, 'tim_1_muxin_4_i', 15))
connect((evadc, 'adcArbCnt_o', 3),  (gtm_wrapper, 'tim_2_muxin_1_i', 12))
connect((evadc, 'adcArbCnt_o', 4),  (gtm_wrapper, 'tim_1_muxin_5_i', 15))
connect((evadc, 'adcArbCnt_o', 5),  (gtm_wrapper, 'tim_2_muxin_2_i', 12))
connect((evadc, 'adcArbCnt_o', 6),  (gtm_wrapper, 'tim_1_muxin_6_i', 15)) #, (gtm_wrapper, 'tim_1_muxin_3_i', )]
connect((evadc, 'adcArbCnt_o', 7),  (gtm_wrapper, 'tim_2_muxin_3_i', 12))
connect((evadc, 'adcArbCnt_o', 8),  (gtm_wrapper, 'tim_3_muxin_1_i', 12))
connect((evadc, 'adcArbCnt_o', 9),  (gtm_wrapper, 'tim_4_muxin_1_i', 12))
connect((evadc, 'adcArbCnt_o', 10), (gtm_wrapper, 'tim_3_muxin_2_i', 12))
connect((evadc, 'adcArbCnt_o', 11), (gtm_wrapper, 'tim_4_muxin_2_i', 15))


#exposed Analog connections, use analog port model for better lisibility of analog values
for i in range(0, NUMBER_OF_EVADC_GROUPS):
    connect((evadc,'adcVRef_i',i),(analog_ports,'vadcVRef_o',i))
    connect((evadc,'adcVGnd_i',i),(analog_ports,'vadcVGnd_o',i))

# The following table is the master table of EVADC among all variants
# Compute ADC groups indexes for ease of use
# Primary
G0CH0=0*8; G0CH1=G0CH0+1; G0CH2=G0CH0+2; G0CH3=G0CH0+3; G0CH4=G0CH0+4; G0CH5=G0CH0+5; G0CH6=G0CH0+6; G0CH7=G0CH0+7;
G1CH0=1*8; G1CH1=G1CH0+1; G1CH2=G1CH0+2; G1CH3=G1CH0+3; G1CH4=G1CH0+4; G1CH5=G1CH0+5; G1CH6=G1CH0+6; G1CH7=G1CH0+7;
G2CH0=2*8; G2CH1=G2CH0+1; G2CH2=G2CH0+2; G2CH3=G2CH0+3; G2CH4=G2CH0+4; G2CH5=G2CH0+5; G2CH6=G2CH0+6; G2CH7=G2CH0+7;
G3CH0=3*8; G3CH1=G3CH0+1; G3CH2=G3CH0+2; G3CH3=G3CH0+3; G3CH4=G3CH0+4; G3CH5=G3CH0+5; G3CH6=G3CH0+6; G3CH7=G3CH0+7;
G4CH0=4*8; G4CH1=G4CH0+1; G4CH2=G4CH0+2; G4CH3=G4CH0+3; G4CH4=G4CH0+4; G4CH5=G4CH0+5; G4CH6=G4CH0+6; G4CH7=G4CH0+7;
G5CH0=5*8; G5CH1=G5CH0+1; G5CH2=G5CH0+2; G5CH3=G5CH0+3; G5CH4=G5CH0+4; G5CH5=G5CH0+5; G5CH6=G5CH0+6; G5CH7=G5CH0+7;
G6CH0=6*8; G6CH1=G6CH0+1; G6CH2=G6CH0+2; G6CH3=G6CH0+3; G6CH4=G6CH0+4; G6CH5=G6CH0+5; G6CH6=G6CH0+6; G6CH7=G6CH0+7;
G7CH0=7*8; G7CH1=G7CH0+1; G7CH2=G7CH0+2; G7CH3=G7CH0+3; G7CH4=G7CH0+4; G7CH5=G7CH0+5; G7CH6=G7CH0+6; G7CH7=G7CH0+7;
# Secondary
G8CH0 = 64; G8CH1=G8CH0+1; G8CH2=G8CH0+2; G8CH3=G8CH0+3; G8CH4=G8CH0+4; G8CH5=G8CH0+5; G8CH6=G8CH0+6; G8CH7=G8CH0+7; G8CH8=G8CH0+8; G8CH9=G8CH0+9; G8CH10=G8CH0+10; G8CH11=G8CH0+11; G8CH12=G8CH0+12; G8CH13=G8CH0+13; G8CH14=G8CH0+14; G8CH15=G8CH0+15;
G9CH0 = G8CH0+16; G9CH1=G9CH0+1; G9CH2=G9CH0+2; G9CH3=G9CH0+3; G9CH4=G9CH0+4; G9CH5=G9CH0+5; G9CH6=G9CH0+6; G9CH7=G9CH0+7; G9CH8=G9CH0+8; G9CH9=G9CH0+9; G9CH10=G9CH0+10; G9CH11=G9CH0+11; G9CH12=G9CH0+12; G9CH13=G9CH0+13; G9CH14=G9CH0+14; G9CH15=G9CH0+15;
G10CH0 = G8CH0+32; G10CH1=G10CH0+1; G10CH2=G10CH0+2; G10CH3=G10CH0+3; G10CH4=G10CH0+4; G10CH5=G10CH0+5; G10CH6=G10CH0+6; G10CH7=G10CH0+7; G10CH8=G10CH0+8; G10CH9=G10CH0+9; G10CH10=G10CH0+10; G10CH11=G10CH0+11; G10CH12=G10CH0+12; G10CH13=G10CH0+13; G10CH14=G10CH0+14; G10CH15=G10CH0+15;
G11CH0 = G8CH0+48; G11CH1=G11CH0+1; G11CH2=G11CH0+2; G11CH3=G11CH0+3; G11CH4=G11CH0+4; G11CH5=G11CH0+5; G11CH6=G11CH0+6; G11CH7=G11CH0+7; G11CH8=G11CH0+8; G11CH9=G11CH0+9; G11CH10=G11CH0+10; G11CH11=G11CH0+11; G11CH12=G11CH0+12; G11CH13=G11CH0+13; G11CH14=G11CH0+14; G11CH15=G11CH0+15;
# Fast
G12CH0 = 128; G13CH0 = G12CH0+1; G14CH0 = G12CH0+2; G15CH0 = G12CH0+3; G16CH0 = G12CH0+4; G17CH0 = G12CH0+5; G18CH0 = G12CH0+6; G19CH0 = G12CH0+7

# p.682 of TC37X_ts_appx_V2.5.1.pdf
connect_evadc_to_analog_pin(0, G0CH0)
connect_evadc_to_analog_pin(1, G0CH1)
connect_evadc_to_analog_pin(2, G0CH2)
connect_evadc_to_analog_pin(3, G0CH3)
connect_evadc_to_analog_pin(4, G0CH4, G11CH0)
connect_evadc_to_analog_pin(5, G0CH5, G11CH1)
connect_evadc_to_analog_pin(6, G0CH6, G11CH2)
connect_evadc_to_analog_pin(7, G0CH7, G11CH3)
connect_evadc_to_analog_pin(8, G1CH0, G11CH4)
connect_evadc_to_analog_pin(9, G1CH1, G11CH5)
connect_evadc_to_analog_pin(10, G1CH2, G11CH6)
connect_evadc_to_analog_pin(11, G1CH3, G11CH7)
connect_evadc_to_analog_pin(12, G1CH4)
connect_evadc_to_analog_pin(13, G1CH5)
connect_evadc_to_analog_pin(14, G1CH6)
connect_evadc_to_analog_pin(15, G1CH7)
connect_evadc_to_analog_pin(16, G2CH0, G12CH0)
connect_evadc_to_analog_pin(17, G2CH1, G13CH0)
connect_evadc_to_analog_pin(18, G2CH2, G11CH8)
connect_evadc_to_analog_pin(19, G2CH3, G11CH9)
connect_evadc_to_analog_pin(20, G2CH4)
connect_evadc_to_analog_pin(21, G2CH5)
connect_evadc_to_analog_pin(22, G2CH6)
connect_evadc_to_analog_pin(23, G2CH7)
connect_evadc_to_analog_pin(24, G3CH0)
connect_evadc_to_analog_pin(25, G3CH1)
connect_evadc_to_analog_pin(26, G3CH2, G11CH10)
connect_evadc_to_analog_pin(27, G3CH3, G11CH11)
connect_evadc_to_analog_pin(28, G3CH4)
connect_evadc_to_analog_pin(29, G3CH5)
connect_evadc_to_analog_pin(30, G3CH6)
connect_evadc_to_analog_pin(31, G3CH7)
connect_evadc_to_analog_pin(32, G8CH0, G11CH12)
connect_evadc_to_analog_pin(33, G8CH1, G11CH13)
connect_evadc_to_analog_pin(34, G8CH2, G11CH14)
connect_evadc_to_analog_pin(35, G8CH3, G11CH15)
connect_evadc_to_analog_pin(36, G8CH4)
connect_evadc_to_analog_pin(37, G8CH5)
connect_evadc_to_analog_pin(38, G8CH6)
connect_evadc_to_analog_pin(39, G8CH7)
connect_evadc_to_analog_pin(40, G8CH8)
connect_evadc_to_analog_pin(41, G8CH9)
connect_evadc_to_analog_pin(42, G8CH10)
connect_evadc_to_analog_pin(43, G8CH11)
connect_evadc_to_analog_pin(44, G8CH12)
connect_evadc_to_analog_pin(45, G8CH13)
connect_evadc_to_analog_pin(46, G8CH14)
connect_evadc_to_analog_pin(47, G8CH15)

#expose AN pins
expose_alternate_name((analog_ports, 'anPins_i'), name='I_AN', groups="ANALOG", alt_name="AN%s", idx=range(72))

#connect and expose the pXX.Y analog input pins to EVADC groups and channels
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 0, G9CH11) #P00.1
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 1, G9CH10) #P00.2
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 2, G9CH9) #P00.3
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 3, G9CH8) #P00.4
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 4, G9CH7) #P00.5
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 5, G9CH6) #P00.6
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 6, G9CH5) #P00.7
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 7, G9CH4) #P00.8
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 8, G9CH3) #P00.9
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 9, G9CH2) #P00.10
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 10, G9CH1,G15CH0) #P00.11
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 11, G9CH0,G14CH0) #P00.12
expose_alternate_name((analog_ports,'pAiPins_i',0),name='I_P00_1_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',1),name='I_P00_2_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',2),name='I_P00_3_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',3),name='I_P00_4_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',4),name='I_P00_5_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',5),name='I_P00_6_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',6),name='I_P00_7_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',7),name='I_P00_8_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',8),name='I_P00_9_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',9),name='I_P00_10_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',10),name='I_P00_11_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',11),name='I_P00_12_AI', groups="ANALOG")
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 12, G9CH14) #P01.3
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 13, G9CH13) #P01.4
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 14, G9CH12) #P01.5
expose_alternate_name((analog_ports,'pAiPins_i',12),name='I_P01_3_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',13),name='I_P01_4_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',14),name='I_P01_5_AI', groups="ANALOG")
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 15, G9CH15) #P02.11
expose_alternate_name((analog_ports,'pAiPins_i',15),name='I_P02_11_AI', groups="ANALOG", alt_name='P02_11_AI')
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 16, G10CH7) #P33.0
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 17, G10CH6) #P33.1
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 18, G10CH5) #P33.2
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 19, G10CH4) #P33.3
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 20, G10CH3) #P33.4
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 21, G10CH2) #P33.5
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 22, G10CH1) #P33.6
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 23, G10CH0) #P33.7
expose_alternate_name((analog_ports,'pAiPins_i',16),name='I_P33_0_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',17),name='I_P33_1_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',18),name='I_P33_2_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',19),name='I_P33_3_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',20),name='I_P33_4_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',21),name='I_P33_5_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',22),name='I_P33_6_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',23),name='I_P33_7_AI', groups="ANALOG")
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 24, G10CH11) #P34.1
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 25, G10CH10) #P34.2
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 26, G10CH9) #P34.3
connect_evadc_to_analog_pin(NUMBER_OF_AN_PINS + 27, G10CH8) #P34.4
expose_alternate_name((analog_ports,'pAiPins_i',24),name='I_P34_1_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',25),name='I_P34_2_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',26),name='I_P34_3_AI', groups="ANALOG")
expose_alternate_name((analog_ports,'pAiPins_i',27),name='I_P34_4_AI', groups="ANALOG")

def stub_connection(p='bool'):
    return vlab.connect(vlab.STUB, kind='signal', payload=p)

# Group VAREF and VAGND for EVADC and ESADC
ref_gnd_count = analog_ref_gnd['ALL']
for a in range(1, ref_gnd_count+1):
    vref_list = []
    vgnd_list = []
    for p in analog_ref_gnd[a]:
        if p == 'EDSADC':
            for e in range(6):
                vref_list.append(('EDSADC', 'ifxEdsadcVAREF_i', e))
                vgnd_list.append(('EDSADC', 'ifxEdsadcVAGND_i', e))
        else:
            # EVADC, e.g. EVADC_G12
            idx = int(p.replace('EVADC_G', ''))
            vref_list.append((analog_ports, 'vadcVRef_i', idx))
            vgnd_list.append((analog_ports, 'vadcVGnd_i', idx))
    if len(vref_list) == 0:
        vref_list = stub_connection('double')
    if len(vgnd_list) == 0:
        vgnd_list = stub_connection('double')
    vlab.expose(vref_list, array=False, name='I_VAREF%d'%a, groups='ANALOG')
    vlab.expose(vgnd_list, array=False, name='I_VAGND%d'%a, groups='ANALOG')

#EVADC to ports (source: IfxEvadc_PinMap.c)
#connect([(ports["P02"], "IfxPortsAlt5_i", 6), (ports["P33"], "IfxPortsAlt5_i", 3), (ports["P02"], "IfxPortsAlt5_i", 7),
#         (ports["P33"], "IfxPortsAlt5_i", 2), (ports["P02"], "IfxPortsAlt5_i", 8), (ports["P33"], "IfxPortsAlt5_i", 1)], (evadc, 'ifxEvadcEmuxGrp_o', 0)) #EMUX0x
#connect([(ports["P00"], "IfxPortsAlt5_i", 6), (ports["P33"], "IfxPortsAlt5_i", 6), (ports["P00"], "IfxPortsAlt5_i", 7),
#         (ports["P33"], "IfxPortsAlt5_i", 5), (ports["P00"], "IfxPortsAlt5_i", 8), (ports["P33"], "IfxPortsAlt5_i", 4)], (evadc, 'ifxEvadcEmuxGrp_o', 1)) #EMUX1x
connect([(ports["P00"], "IfxPortsAlt5_i", 5),  (ports["P33"], "IfxPortsAlt6_i", 4)], (evadc, 'adcBflOut_o', 0)) #G12BFLOUT
connect([(ports["P10"], "IfxPortsAlt5_i", 1),  (ports["P33"], "IfxPortsAlt6_i", 6)], (evadc, 'adcBflOut_o', 1)) #G13BFLOUT
connect([(ports["P00"], "IfxPortsAlt3_i", 7),  (ports["P33"], "IfxPortsAlt6_i", 0), (ports["P33"], "IfxPortsAlt6_i", 5)], (evadc, 'adcBflOut_o', 2)) #G14BFLOUT
connect([(ports["P10"], "IfxPortsAlt5_i", 2),  (ports["P33"], "IfxPortsAlt6_i", 2), (ports["P33"], "IfxPortsAlt6_i", 7)], (evadc, 'adcBflOut_o', 3)) #G15BFLOUT
connect([(ports["P00"], "IfxPortsAlt5_i", 4),  (ports["P01"], "IfxPortsAlt7_i", 8), (ports["P33"], "IfxPortsAlt6_i", 1)])
connect([(ports["P00"], "IfxPortsAlt3_i", 6),  (ports["P01"], "IfxPortsAlt7_i", 9), (ports["P33"], "IfxPortsAlt6_i", 3)])
connect([(ports["P01"], "IfxPortsAlt7_i", 10), (ports["P10"], "IfxPortsAlt5_i", 0), (ports["P34"], "IfxPortsAlt6_i", 4)])
connect([(ports["P01"], "IfxPortsAlt7_i", 11), (ports["P10"], "IfxPortsAlt7_i", 6), (ports["P34"], "IfxPortsAlt6_i", 5)])


# SENT
spb_router_connect(sent, "SENT",'sent_intf')
spbClk_Net.append((sent,'mclk_i'))
allCpuEndInit_Net.append((sent,'mfpi_endinit_i'))
safetyEndInit_Net.append((sent,'mfpi_safe_endinit_i'))
applOrSystRst_Net.append((sent,'mreset_n_i'))
for i in range(0,10):
    connect((sent,'IntrTrigger_o',i),(ir,'ifxIr3Irq_i',SRC2IN(0x240 + i*0x4)))
for i in range(0,12):
     adc_trig0_out_Net[i].append((sent,'GTMTrigger_i',i))
for i in range(0,4):
     dsadc_trig0_out_Net.insert(i,[(sent,'GTMTrigger_i',i+12)])

for i in range(0,25):
    expose_alternate_name((sent,'SENTRxData%i_0_i'%i),name='I_SENT%iA'%i, groups="SENT", alt_name="SENT_SENT%iA"%i)
    expose_alternate_name((sent,'SENTRxData%i_1_i'%i),name='I_SENT%iB'%i, groups="SENT", alt_name="SENT_SENT%iB"%i)
    expose_alternate_name((sent,'SENTRxData%i_2_i'%i),name='I_SENT%iC'%i, groups="SENT", alt_name="SENT_SENT%iC"%i)
    expose_alternate_name((sent,'SENTRxData%i_3_i'%i),name='I_SENT%iD'%i, groups="SENT", alt_name="SENT_SENT%iD"%i)
    expose_alternate_name((sent,'SENTTxData%i_o'%i),name='O_SPC%i'%i, groups="SENT", alt_name="SENT_SPC%i"%i)


# Finally, actually connect EVADC and SENT to GTM ADC Triggers
for x in range(0,12):
    connect(adc_trig0_out_Net[x], (gtm_wrapper,'adc_trig0_out',x))
    connect(adc_trig1_out_Net[x], (gtm_wrapper,'adc_trig1_out',x))
    connect(adc_trig2_out_Net[x], (gtm_wrapper,'adc_trig2_out',x))
    connect(adc_trig3_out_Net[x], (gtm_wrapper,'adc_trig3_out',x))
    connect(adc_trig4_out_Net[x], (gtm_wrapper,'adc_trig4_out',x))


# (EDSADC) -> (DS ADC IMUX of GTM) at page 78 of [TS 2.5.1]
for x in range(0,4):
    connect(dsadc_trig0_out_Net[x], (gtm_wrapper,'dsadc_trig0_out',x))


#PORTS Connections
counter = 0
for port_name in ports:
    port_instance = ports[port_name]
    spb_router_connect(port_instance, port_name,'ports_ifc')
    spbClk_Net.append((port_instance,'busClock_i'))
    applOrSystRst_Net.append((port_instance,'resetIf_i'))
    allCpuEndInit_Net.append((port_instance,'IfxPortEndInit_i'))
    safetyEndInit_Net.append((port_instance,'IfxPortSafeEndInit_i'))
    emStop_Net.append((port_instance,'IfxPortEmStop_i'))
    expose_alternate_name((port_instance,'IfxPortsData_io'), name='IO_'+port_name, groups="PORTS", alt_name='{}_%s'.format(port_name), idx=range(16))
# expose HWCFG6
expose(hwcfg6_net, name='HWCFG6', groups="PORTS")

# GPIOs to SCU ERU
connect_digital_port("P15", "AltIn", 4, (scu,"scuEruChannelIn0_i",0))
connect_digital_port("P10", "AltIn", 7, (scu,"scuEruChannelIn0_i",2))
connect_digital_port("P14", "AltIn", 3, (scu,"scuEruChannelIn1_i",0))
connect_digital_port("P10", "AltIn", 8, (scu,"scuEruChannelIn1_i",2))
connect_digital_port("P10", "AltIn", 2, (scu,"scuEruChannelIn2_i",0))
connect_digital_port("P02", "AltIn", 1, (scu,"scuEruChannelIn2_i",1))
connect_digital_port("P00", "AltIn", 4, (scu,"scuEruChannelIn2_i",2))
connect_digital_port("P10", "AltIn", 3, (scu,"scuEruChannelIn3_i",0))
connect_digital_port("P14", "AltIn", 1, (scu,"scuEruChannelIn3_i",1))
connect_digital_port("P02", "AltIn", 0, (scu,"scuEruChannelIn3_i",2))
connect_digital_port("P33", "AltIn", 7, (scu,"scuEruChannelIn4_i",0))
connect_digital_port("P15", "AltIn", 5, (scu,"scuEruChannelIn4_i",3))
connect_digital_port("P15", "AltIn", 8, (scu,"scuEruChannelIn5_i",0))
connect_digital_port("P20", "AltIn", 0, (scu,"scuEruChannelIn6_i",0))
connect_digital_port("P11", "AltIn", 10, (scu,"scuEruChannelIn6_i",3))
connect_digital_port("P20", "AltIn", 9, (scu,"scuEruChannelIn7_i",0))
connect_digital_port("P15", "AltIn", 1, (scu,"scuEruChannelIn7_i",2))


##################################
#             MCMCANs            #
##################################
mcan_clk_net = []
mcan_hclk_net = []
def convert_ord_to_letter(idx):
    return chr(ord('A')+idx)

for i in range (NUM_MCMCAN):
    # connect to SPB bus
    spb_router_connect(mcmcan[i], 'MCMCAN%i'%i, 'TargetSocket')
    spbClk_Net.append((mcmcan[i], "fclk_scan"))
    mcan_clk_net.append((mcmcan[i], "fclk_acan"))
    allCpuEndInit_Net.append((mcmcan[i], "mcmcan_endInit_i"))
    safetyEndInit_Net.append((mcmcan[i], "mcmcan_safe_endInit_i"))
    applOrSystRst_Net.append((mcmcan[i], "reset"))
    ############ Connect MCMCANs <---> MCANs ############
    mcmcan_reset_net = []

    mcmcan_master_index = 0
    mcmcan_slave_index = 0

    mcmcan_to_mcan_router= instantiate(router_component, 'MCMCAN%i_TO_MCAN'%i,
                            args=[vlab.NAME, 1, 4],groups="SPB_domain")#, visibility="hidden")
    connect((mcmcan[i], "mcan_master"), (mcmcan_to_mcan_router, 'target_socket', mcmcan_master_index))
    mcan_txd_output = []
    mcan_txd_ctrl_output = []
    mcan_txd_data_output = []
    for j in range (NUM_MCAN):
        connect((mcmcan[i], "fsyn",j), (mcmcan_mcan[i][j], "HCLK"))
        connect((mcmcan[i], "fasyn",j), (mcmcan_mcan[i][j], "CCLK"))
        mcmcan_reset_net.append((mcmcan_mcan[i][j], "reset"))
        ## --> mcmcani --> mcani
        connect((mcmcan[i], "MCAN_RX_OUT",j), (mcmcan_mcan[i][j], "RX"))
        connect((mcmcan[i], "MCAN_RX_TOKEN_DATA_OUT",j), (mcmcan_mcan[i][j], "TOKEN_RX_DATA"))
        connect((mcmcan[i], "MCAN_RX_TOKEN_CTRL_OUT",j), (mcmcan_mcan[i][j], "TOKEN_RX_CTRL"))
        ## mcani --> mcmcani -->
        mcan_txd_output.append((mcmcan_mcan[i][j],"TX"))
        mcan_txd_data_output.append((mcmcan_mcan[i][j], "TOKEN_TX_DATA"))
        mcan_txd_ctrl_output.append((mcmcan_mcan[i][j], "TOKEN_TX_CTRL"))
        connect((mcmcan[i], "MCAN_INT",j), (mcmcan_mcan[i][j], "INT0"))
        connect((mcmcan_mcan[i][j], "slave"), (mcmcan_to_mcan_router, 'initiator_socket', mcmcan_slave_index))
        mcmcan_to_mcan_router.obj.add_address_mapping(mcmcan_slave_index, 0x100 + j * 0x400, 0x200,  0x100 + j * 0x400)
        mcmcan_slave_index += 1
        connect((mcmcan[i], "mcan_slave",j), (mcmcan_mcan[i][j], "master"))
        applOrSystRst_Net.append((mcmcan_mcan[i][j], "reset"))

    #export external interfaces
    if alt_io_name:
        #TX
        for x in range(4):
            expose_alternate_name(mcan_txd_output[x], name="O_MCMCAN%i_TXD_%i"%(i,x), groups="MCMCAN%i"%i,
                                  alt_name='CAN%i%i_TXD'%(i,x))
            expose_alternate_name(mcan_txd_ctrl_output[x], name="O_MCMCAN%i_TXD_TOKEN_CTRL_%i"%(i,x), groups="MCMCAN%i"%i,
                                  alt_name='CAN%i%i_TXD_TOKEN_CTRL'%(i,x))
            expose_alternate_name(mcan_txd_data_output[x], name="O_MCMCAN%i_TXD_TOKEN_DATA_%i"%(i,x), groups="MCMCAN%i"%i,
                                  alt_name='CAN%i%i_TXD_TOKEN_DATA'%(i,x))

        #RX
        for j in range (NUM_MCAN):
            expose_alternate_name((mcmcan[i], "CAN%i_RXD"%j), name="I_MCMCAN%i%i_RXD"%(i,j), groups="MCMCAN%i"%i,
                                  alt_name='CAN{}{}_RXD%s'.format(i,j), idx=range(8), idx_func=convert_ord_to_letter)
            expose_alternate_name((mcmcan[i], "CAN%i_RXD_TOKEN_DATA"%j), name="I_MCMCAN%i%i_RXD_TOKEN_DATA"%(i,j), groups="MCMCAN%i"%i,
                                  alt_name='CAN{}{}_RXD%s_TOKEN_DATA'.format(i,j), idx=range(8), idx_func=convert_ord_to_letter)
            expose_alternate_name((mcmcan[i], "CAN%i_RXD_TOKEN_CTRL"%j, x), name="I_MCMCAN%i%i_RXD_TOKEN_CTRL"%(i,j), groups="MCMCAN%i"%i,
                                  alt_name='CAN{}{}_RXD%s_TOKEN_CTRL'.format(i,j), idx=range(8), idx_func=convert_ord_to_letter)
    else:
        #TX
        expose(mcan_txd_output, name="O_MCMCAN%i_TXD"%i, groups="MCMCAN%i"%i)
        expose(mcan_txd_ctrl_output, name="O_MCMCAN%i_TXD_TOKEN_CTRL"%i, groups="MCMCAN%i"%i)
        expose(mcan_txd_data_output, name="O_MCMCAN%i_TXD_TOKEN_DATA"%i, groups="MCMCAN%i"%i)

        #RX
        for j in range (NUM_MCAN):
            expose((mcmcan[i], "CAN%i_RXD"%j), name="I_MCMCAN%i%i_RXD"%(i,j), groups="MCMCAN%i"%i)

            expose((mcmcan[i], "CAN%i_RXD_TOKEN_DATA"%j), name="I_MCMCAN%i%i_RXD_TOKEN_DATA"%(i,j), groups="MCMCAN%i"%i)
            expose((mcmcan[i], "CAN%i_RXD_TOKEN_CTRL"%j), name="I_MCMCAN%i%i_RXD_TOKEN_CTRL"%(i,j), groups="MCMCAN%i"%i)

#connect interrupts
for i in range (NUM_MCMCAN): #FOR MCMCAN0, MCMCAN1, MCMCAN2
    # MCMCAN to IR
    for y in range(16):
        connect((ir, 'ifxIr3Irq_i', SRC2IN(0x005B0 + 0x40*i + 4*y)),(mcmcan[i],'INT_O',y))

# MCMCAN from SCU
connect((scu, "scuMcanClk_o"),mcan_clk_net)
connect((scu, "scuMcanhClk_o"),mcan_hclk_net)

# GETH
# Connect SRI master
# As described in section 4.5.1, page 29, of [TS APP 2.3.0], GETH is associated with MCI9 in Domain 0
connect((sri_router, get_tlm_slave_interface(), 9), (geth, 'dma_master'))
#connect SPB router
spb_router_connect(geth, 'GETH','peripheral_bus')
spb_router_connect(geth, 'GETH_SNPS','synopsys_ethernet_peripheral_bus')

# Connections to IR
connect((ir,'ifxIr3Irq_i',SRC2IN(0x580)),(geth,'sbd_intr'))
for i in range(4):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x588 + (i * 4))),(geth,'sbd_perch_tx_intr', i))

for i in range(4):
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x598 + (i * 4))),(geth,'sbd_perch_rx_intr', i))
applOrSystRst_Net.append((geth, "reset"))
expose((geth,"RX"),name="I_GETH_RX", groups="GETH")
expose((geth,"TX"),name="O_GETH_TX", groups="GETH")
expose((geth,"MDIO_in"),name="I_MDIO_in", groups="GETH")
expose((geth,"MDIO_out"),name="O_MDIO_out", groups="GETH")


if tc37xext:
    # ---- GETH1 ----
    # As described in section 4.5.1, page 30, of [TS APP 2.3.0], GETH1 is associated with MCI12 in Domain 0
    connect((sri_router, get_tlm_slave_interface(), 12), (geth1, 'dma_master'))
    
    spb_router_connect(geth1, 'GETH1','peripheral_bus')
    spb_router_connect(geth1, 'GETH1_SNPS','synopsys_ethernet_peripheral_bus')
    # Connections to IR
    connect((ir,'ifxIr3Irq_i',SRC2IN(0x1D4)),(geth1,'sbd_intr'))
    for i in range(4):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x1D8 + (i * 4))),(geth1,'sbd_perch_tx_intr', i))

    for i in range(4):
        connect((ir,'ifxIr3Irq_i',SRC2IN(0x1E8 + (i * 4))),(geth1,'sbd_perch_rx_intr', i))
    applOrSystRst_Net.append((geth1, "reset"))
    expose((geth1,"RX"),name="I_GETH1_RX", groups="GETH1")
    expose((geth1,"TX"),name="O_GETH1_TX", groups="GETH1")
    expose((geth1,"MDIO_in"),name="I_MDIO1_in", groups="GETH1")
    expose((geth1,"MDIO_out"),name="O_MDIO1_out", groups="GETH1")

# ASCLIN
asclin = []
asclin_component = component('IfxAscLinWrapper', module='aurix.IfxAscLin_TC3xx', kind='leaf', description='aurix.metadata_common_tc3xx.metadata_ASCLIN')
for i in range(0, NUM_ASCLIN):
    # Naming convention follows page 11 of TC39x_A_v1_2_4_Platform_User_Manual_v1_2_4.pdf
    model_name = 'ASCLIN_%i_%i'%(i*2, i*2+1)
    asclin.append(vlab.instantiate(asclin_component,model_name,args=[model_name, False, aurix.common.get_debug_level(__args__["debug-level"],model_name)],extensions={"version":"INFINEON V20210713"},groups="SPB_domain"))
    spb_router_connect(asclin[i],model_name,'asclin_ifc')
    spbClk_Net.append((asclin[i],'busClock_i'))                     # f_SPB
    allCpuEndInit_Net.append((asclin[i],'IfxAscLinEndInit_i'))
    safetyEndInit_Net.append((asclin[i],'IfxAscLinSafeEndInit_i'))
    applOrSystRst_Net.append((asclin[i],'resetIf_i'))
    scuAsclinClk_Net.append((asclin[i],'asclinClock_i'))
    scuAsclinSClk_Net.append((asclin[i],'asclinSClock_i'))
    # page 22 of TC39x_A_v1_2_4_Platform_User_Manual_v1_2_4.pdf
    # ASC0
    expose((asclin[i], 'IfxAscLin0RxData_i'), name = 'I_ASCLIN%i_RXDATA'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0RxCtrl_i'), name = 'I_ASCLIN%i_RXCTRL'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0TxData_o'), name = 'O_ASCLIN%i_TXDATA'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0TxCtrl_o'), name = 'O_ASCLIN%i_TXCTRL'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0Sclk_o'), name = 'O_ASCLIN%i_SYNC_CLK'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0Mtsr_o'), name = 'O_ASCLIN%i_MTSR'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0Mrst_i'), name = 'I_ASCLIN%i_MRST'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0StdSpiControl_o'), name = 'O_ASCLIN%i_SPICONTROL'%(i*2), groups="ASCLIN")
    # ASC1
    expose((asclin[i], 'IfxAscLin1RxData_i'), name = 'I_ASCLIN%i_RXDATA'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1RxCtrl_i'), name = 'I_ASCLIN%i_RXCTRL'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1TxData_o'), name = 'O_ASCLIN%i_TXDATA'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1TxCtrl_o'), name = 'O_ASCLIN%i_TXCTRL'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1Sclk_o'), name = 'O_ASCLIN%i_SYNC_CLK'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1Mtsr_o'), name = 'O_ASCLIN%i_MTSR'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1Mrst_i'), name = 'I_ASCLIN%i_MRST'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1StdSpiControl_o'), name = 'O_ASCLin%i_SPICONTROL'%(i*2+1), groups="ASCLIN")
    # page 567 of TC39XB_ts_appx_V2.3.0.pdf
    # ASC0
    connect((asclin[i],'IfxAscLin0TXSR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x50 + i*2*12)))
    connect((asclin[i],'IfxAscLin0RXSR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x54 + i*2*12)))
    connect((asclin[i],'IfxAscLin0ESR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x58 + i*2*12)))
    # ASC1
    connect((asclin[i],'IfxAscLin1TXSR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x50 + (i*2+1)*12)))
    connect((asclin[i],'IfxAscLin1RXSR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x54 + (i*2+1)*12)))
    connect((asclin[i],'IfxAscLin1ESR_o'),(ir,'ifxIr3Irq_i',SRC2IN(0x58 + (i*2+1)*12)))
    # Other pins
    # TODO: connection to PORTS
    expose((asclin[i], 'IfxAscLin0Slso_o'), name = 'O_ASCLIN%i_SLSO'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0RTS_o'), name = 'O_ASCLIN%i_RTS'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin0CTS_i'), name = 'I_ASCLIN%i_CTS'%(i*2), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1Slso_o'), name = 'O_ASCLIN%i_SLSO'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1RTS_o'), name = 'O_ASCLIN%i_RTS'%(i*2+1), groups="ASCLIN")
    expose((asclin[i], 'IfxAscLin1CTS_i'), name = 'I_ASCLIN%i_CTS'%(i*2+1), groups="ASCLIN")

# SCU is the last peripheral to connect, because it manages several connections to different peripherals
# force_sync is set to True to ensure any modification on its registers are effective immediately.
spb_router_connect(scu, 'SCU','TargetSocket', force_sync=True)
#export external interfaces
expose((scu,'scuXtalOscClk_i'), name='I_OSCCLK', groups="SCU")
expose((scu,'scuSysClk_i'),     name='I_SCUSYSCLK', groups="SCU")
expose_alternate_name((scu,'scuEsr_io',0), name='IO_ESR0_NOT', groups="SCU", alt_name='ESR0')
expose_alternate_name((scu,'scuEsr_io',1), name='IO_ESR1_NOT', groups="SCU", alt_name='ESR1')
if alt_io_name:
    # Expose reset with both names
    instantiate(component('OrGate', module='aurix.OrGate'), 'I_RESET_N_or', visibility='hidden')
    expose(('I_RESET_N_or', 'input1'), name='I_RESET_N', groups="SCU")
    expose_alternate_name(('I_RESET_N_or', 'input2'), name="", alt_name='PORST', groups="SCU")
    connect(('I_RESET_N_or', 'output'), (scu, 'scuPowerOnRst_i'))
else:
    expose((scu,'scuPowerOnRst_i'), name='I_RESET_N', groups="SCU")

#connect SCU to tricores
for i in range(0,NUM_CORES):
    connect((scu,'scuCpuClk_o',i),      (cores[i],'CPU_Clock'),default=BACKUP_CLK)
    connect((scu,'scuCpuEndInitCe_o',i),(cores[i],'CPU_EndInit'))
    connect((scu,'scuOvcEnable_o',i),   (cores[i],'CPU_OVC_Enable'))
    connect((scu,'scuOvcStart_o',i),    (cores[i],'CPU_OVC_Start'))
    connect((scu,'scuOvcStop_o',i),     (cores[i],'CPU_OVC_Stop'))
    connect((scu,'scuOvcDcinv_o',i),    (cores[i],'CPU_OVC_Dcinv'))
    connect((scu,'scuCpuIdleReq_o',i),  (cores[i],'CPU_IdleReq'))
    connect((scu,'scuCpuIdleAck_i',i),  (cores[i],'CPU_IdleAck'),default=False)
    if i == 0 :
        connect((scu,'scuNmiTrap_o'), (cores[0],'CPU_NMI'))
    else:
        connect((cores[i],'CPU_CoreHalt'),(scu,'scuCore%iHalt_i'%i),default=True)


#connect SCU to ASCLIN
#scuOsc0Clk_Net.append([(asclin_0_1,'asclinOsc0_i'),(asclin_2_3,'asclinOsc0_i')])
#connect((scu,'scuErayClk_o'),[(asclin_0_1,'asclinErayClock_i'),(asclin_2_3,'asclinErayClock_i')],default=BACKUP_CLK)
#SCU to GTM
connect((scu,'scuGtmClk_o'),[(gtm_wrapper,'mmclk_iInPort')],default=BACKUP_CLK)
#SCU to EVADC
connect((scu,'scuAdcClk_o'),[(evadc,'ScuClk_InPort')],default=BACKUP_CLK)
#multiple connections
spbClk_Net.append((scu,'TargetSocketClock_i'))
scu_sys_rst_net.append((scu,'Reset'))
allCpuEndInit_Net.append((scu,'ScuEndInit_i'))
safetyEndInit_Net.append((scu,'SafeEndInit_i'))

connect_digital_port("P00", "Alt1", 3, (scu,'scuEruChannelIn4_i',1)) # because this pin is connected to gtm_tout 12 = TOM0_12
connect_digital_port("P33", "Alt1", 6, (scu,'scuEruChannelIn5_i',1)) # because this pin is connected to gtm_tout 28 = TOM1_12
connect_digital_port("P23", "Alt1", 3, (scu,'scuEruChannelIn6_i',5)) # because this pin is connected to gtm_tout 44 = TOM2_12
connect_digital_port("P20", "Alt1", 1, (scu,'scuEruChannelIn7_i',5)) # because this pin is connected to gtm_tout 60 = TOM3_12

#SMU
spb_router_connect(smu, 'SMU','SmuTargetSocket')
spbClk_Net.append((smu,'SmuTargetSocketClock'))
applOrSystRst_Net.append((smu,'Reset_i'))
allCpuEndInit_Net.append((smu,'EndInit_i'))
safetyEndInit_Net.append((smu,'SafeEndInit_i'))
powerOnRst_Net.append((smu,'PowerOnReset_i'))
#applOrSystRst_Net.append((smu, 'SystemReset_i'))
#applOrSystRst_Net.append((smu,'ApplicationReset_i'))            ### TODO to confirm
scu_sys_rst_net.append((smu, 'SystemReset_i'))
scu_app_rst_net.append((smu,'ApplicationReset_i'))
#applOrSystRst_Net.append((smu,'DebugReset_i'))                  ### TODO to confirm
scuOsc0Clk_Net.append((smu, 'Osc_Clk_i'))

# Interfaces to IR
connect((smu, 'SMU_IntReq_o', 0), (ir,'ifxIr3Irq_i',SRC2IN(0x08D0 + 0*4)))
connect((smu, 'SMU_IntReq_o', 1), (ir,'ifxIr3Irq_i',SRC2IN(0x08D0 + 1*4)))
connect((smu, 'SMU_IntReq_o', 2), (ir,'ifxIr3Irq_i',SRC2IN(0x08D0 + 2*4)))

# Interfaces to SCU
connect((smu, 'SMU_EmgStopReq_o'),        (scu, 'scuSmuEmgStopReq_i'))
connect((smu, 'SMU_ResetReq_o'),          (scu, 'scuSmuRstReq_i'))
connect((smu, 'SMU_RunStateIndicator_o'), (scu, 'scuSmuRunStateInd_i'))
# connect((smu, ), (scu, 'scuSmuAlarmReq_o'))
# connect((smu, ), (scu, 'scuSmuCpuIdleReq_i'))
# SW/HW alarm loopbacks, page 1369 of AURIXTC3XX_ts_part1_V2.5.1.pdf
# SW generated alarms wired to 320th alarm input and more
for i in range(16):
    connect((smu, 'SMU_SwAlarm_o', i), (smu, 'SMU_AlarmGroup_i', 320+i))
# SMU generated alarms wired to 336th alarm input and more
# From IFX only the first 3 pins are supported, ref. MODELS-10242
# SMU_Generated_Alarm_o[0], Recovery Timer-0 timeout alarm, connects to SMU_AlarmGroup_i[336]
# SMU_Generated_Alarm_o[1], Recovery Timer-1 timeout alarm, connects to SMU_AlarmGroup_i[337]
# SMU_Generated_Alarm_o[2], FSP Fault State Activation alarm, connects to SMU_AlarmGroup_i[338]
for i in range(3):
    connect((smu, 'SMU_Generated_Alarm_o', i), (smu, 'SMU_AlarmGroup_i', 336+i))


# AND gate for system reset and application reset from SCU, which are both active low
scu_resets_and = instantiate(component("AndGate", module="aurix.AndGate"), "scu_resets_and", visibility="hidden")
scu_app_rst_net.append((scu_resets_and,'input1'))
scu_sys_rst_net.append((scu_resets_and,'input2'))
connect((scu_resets_and, "output"), applOrSystRst_Net)


# Actual SCU connections
connect((scu,'scuStmClk_o'),         scuStmClk_Net,default=BACKUP_CLK)
connect((scu,'scuPowerOnRst_o'),     powerOnRst_Net,default=True)
connect((scu,'scuApplStmRst_o',0),   scuApplStmRst_Net)
connect((scu,'scuSleep_o'),          scuSleep_Net)
connect((scu,'scuSpbClk_o'),         spbClk_Net,default=BACKUP_CLK)
connect((scu,'scuSriClk_o'),         sriClk_Net,default=BACKUP_CLK)
connect((scu,'scuQspiClk_o'),       scuQspiClk_Net,default=BACKUP_CLK)
connect((scu,'scuAllCpuEndInitE_o'), allCpuEndInit_Net)
connect((scu,'scuSafetyEndInitSe_o'),safetyEndInit_Net)
connect((scu, 'scuApplClass3Rst_o'), scu_app_rst_net)
connect((scu, 'scuSystemClass0Rst_o'), scu_sys_rst_net)
connect((scu,'scuAsclinFClk_o'),     scuAsclinClk_Net,default=BACKUP_CLK)
connect((scu,'scuAsclinSClk_o'),     scuAsclinSClk_Net,default=BACKUP_CLK)
connect((scu,'scuEmgStop_o'),        emStop_Net)
connect((scu, 'scuOsc0Clk_o'), scuOsc0Clk_Net)
"""
connect((scu,'scuEruPDOUT_o',0),[(gtm_wrapper,'tim_0_muxin_0_i',14)])
connect((scu,'scuEruPDOUT_o',1),[(gtm_wrapper,'tim_0_muxin_1_i',14)])
connect((scu,'scuEruPDOUT_o',2),[(gtm_wrapper,'tim_0_muxin_2_i',14)])
for i in range(3,8):
    connect((scu,'scuEruPDOUT_o',i),[(gtm_wrapper,'tim_0_muxin_%i_i'%i,14)])
"""

# Actually connect the ports netlists to PORTS instances
connect_all_digital_ports()

# free some memory now that the ports netlists are used
del Ports_Netlist

#
# Console
#

# connect to SPB master bus
spb_router_connect(console, 'CONSOLE', 'slave')

# Instantiation and router mapping of stubbed models
# SPB
# Discard the real models
models_ = ["SCU" , "GTM_part1", "GTM_part2", "GTMWRAPPER", "STM0", "STM1", "STM2", "STM3", "STM4", "STM5", "CONSOLE", "IR", "EVADC", "SMU","QSPI0","QSPI1","QSPI2","QSPI3","QSPI4","QSPI5",
        "P00", "P01", "P02", "P10", "P11", "P12", "P13", "P14", "P15", "P20", "P21", "P22", "P23", "P24", "P25", "P26", "P30", "P31", "P32", "P33", "P34", "P40", "P41", "P50", "P51", "DMA", "MSC0",
        "MSC1", "MSC2", "MSC3", "SENT", "MCMCAN0", "MCMCAN1", "MCMCAN2", "MCMCAN3", "MCMCAN4", "GETH", "GETH_SNPS",
        "ASCLIN_0_1", "ASCLIN_2_3", "ASCLIN_4_5", "ASCLIN_6_7", "ASCLIN_8_9", "ASCLIN_10_11", "ASCLIN_12_13", "ASCLIN_14_15", "ASCLIN_16_17", "ASCLIN_18_19", "ASCLIN_20_21", "ASCLIN_22_23"]
if tc37xext:
    models_.append("GETH1")
    models_.append("GETH1_SNPS")

for stub in SPB_MEMORY_MAP:
    if stub not in tuple(models_):
        size    = SPB_MEMORY_MAP[stub][1]
        if len(SPB_MEMORY_MAP[stub]) == 3 :
            # A register description is available, use it
            address = SPB_MEMORY_MAP[stub][0]
            stub_initiator((spb_router, 'initiator_socket', spb_slave_index), SPB_MEMORY_MAP[stub][2], stub,"SPB_domain")
            spb_router.obj.add_address_mapping(spb_slave_index, address, size, address)
            # Table 60 on p. 179 of AURIXTC3XX_ts_part1_V2.5.1.pdf
            module_wait_state = 2
            spb_router.obj.set_read_latency(spb_slave_index, spb_bus_byte_latency_calculation(module_wait_state))
            spb_router.obj.set_write_latency(spb_slave_index, spb_bus_byte_latency_calculation(module_wait_state))
            spb_slave_index += 1
        else:
            # no register description available
            memory = instantiate(component("tlm_memory_32", module="vlab.components"), stub, args=[vlab.NAME, size, 0, False], doc="Stub model (Memory block)",groups="SPB_domain")
            spb_router_connect(memory, stub,'target_socket')

# Memory controllers
mc_base_address = 0xF0061000
for x in range(96):
    # remove the ones not supported on TC39x
    if x not in (34, 35, 36, 37, 82, 83, 84, 86, 87):
        unit = "MC{0}".format(x)
        address = mc_base_address + x * 0x100
        stub_initiator((spb_router, 'initiator_socket', spb_slave_index), "MTU_MEMORY_CONTROLLER", unit,"SPB_domain")
        spb_router.obj.add_address_mapping(spb_slave_index, address, MEMORY_SIZE_256B, address)
        spb_slave_index += 1

# Process the renamed IO ports
aurix.common._process_renamed_ports()

vlab.stub()
