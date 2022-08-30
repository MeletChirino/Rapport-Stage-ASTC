import os

# vlab toolboxes
import vlab
import sysc
import can
import can.CANNode as CANNode

# LIN toolbox
from lin.lin_protocol_engine import lin_protocol_engine_common as engine

# Uart
from lin.uart_protocol_engine import uart_protocol_engine_common as upec


file_path = os.path.dirname(__file__)
vlab.path.append(file_path)
hybrid_node_files = os.path.join(file_path, 'hybrid_node_demo')

vlab.path.append(hybrid_node_files)

global old_sim_time
old_sim_time = 0

def sim_time(descriptor):
    # Shows executions times of StartApplicationCycli250ms
    global old_sim_time
    old_sim_time_ = old_sim_time
    new_sim_time = vlab.simulation_time().to_seconds() * 1000
    delta = new_sim_time - old_sim_time
    print "\n----\ncyclic 250 @" +
                new_sim_time +
                "\ndelta = " +
                delta +
                "\n----\n"
    old_sim_time = new_sim_time

# ---- Set breakpoint in funciton execution ----
def set_breakpoint_symbol(symbol_name, **kwargs):
    symbol_ = vlab.get_symbol(symbol_name)
    symbol_trig = vlab.trigger.execute(symbol_)
    if kwargs.get('action'):
        func = kwargs['action']
        vlab.add_breakpoint(symbol_trig, action=func)
        return 0
    vlab.add_breakpoint(symbol_trig)

def switch_cyclic(descriptor):
    # Shows executions times of StartApplicationCycli250ms
    global old_sim_time
    old_sim_time_ = old_sim_time
    new_sim_time = vlab.simulation_time().to_seconds() * 1000
    delta = new_sim_time - old_sim_time
    print "\n----\nStartApplication_COM_RXTX_Cyclic @" +
                new_sim_time +
                "\ndelta = " +
                delta +
                "\n----\n"
    old_sim_time = new_sim_time


def fr_init_fix(descriptor):
    # Fix Fr_Init configs
    print "\n----\nFixing Fr_Init configs\n----\n"
    print "Time => %f ms" % (vlab.simulation_time().to_seconds()*1000)
    #vlab.pause()
    register_name = 'tc37x.ERAY0.SUCC1'
    succ1_ori = vlab.read_register(register_name)
    mask = 0xffffff7f
    new_value = succ1_ori & mask


    print "vlab.write_register('%s', %d)" % (register_name, new_value)
    print "vlab.write_register('tc37x.ERAY0.CCSV.POCS', 0x4)"
    vlab.write_register(register_name, new_value)
    vlab.write_register('tc37x.ERAY0.CCSV.POCS', 0x4)

def os_api_writeperipheral32(PeripheralID, Address, Value):
    print "\n----\nWrite peripherals\n----\n"
    print "PeripheralID = ", PeripheralID
    print "Address = ", hex(Address)
    print "Value = ", hex(Value)
    print " --- Time => ", vlab.simulation_time()
    address_p = vlab.get_symbol('Address')
    if Address >= 0xf001c000 and Address <= 0xf001cfff:
        print "This is the flexray"
    elif Address >= 0xf0000800 and Address <= 0xf00008ff:
        print "This is the Asynchronous/Synchronous Serial\n" +
                "Controller with LIN 2 (ASCLIN2)"
        vlab.write_memory(
                Address,
                Value,
                pack = '<L',
                core = 'tc37x.CPU0_SUBSYSTEM.CPU0
                )
    elif Address >= 0xf0218000 and Address <= 0xf0218fff:
        print "This is the MCMCAN1 SFR (CAN1)"
        vlab.write_memory(
                Address,
                Value,
                pack = '<L',
                core='tc37x.CPU0_SUBSYSTEM.CPU0'
                )
    else:
        vlab.write_memory(
                Address,
                Value,
                pack = '<L',
                core = 'tc37x.CPU0_SUBSYSTEM.CPU0'
                )


def fr_sendwup_fix(x):
    # Fix Fr_SendWUP configs
    print "\n----\nStub Fr_SendWUP configs\n----\n"
    print "Time => ", vlab.simulation_time()
    yield 0

def display_hybrid(bp):
    """Display hybrid response in terminal."""
    vlab.disable_breakpoint(bp)
    rx = hybrid_uart.obj.get_uart_response()
    vlab.print_in_terminal(vlab.terminal.hybrid_node_terminal, rx)
    hybrid_uart.obj.clear_uart_response()
    vlab.enable_breakpoint(bp)

# Load VP
testbench_file = "--testbench=%s\\%s" % (
        file_path,
        "startapp\\testbench.py"
        )
vlab.load(
    "aurix.tc37x.sim",
    args = [
        "--iss=fast",
        testbench_file,
        '--debugger-config=all:trace32mcd',
        '--debugger=all',
        "--quantum-period=500"
        ]
    )

# Load image to VP
image_path = u"D:\\ifx_aurix_software_packages\\Aurix2G\\" +
    "Vector_MICROSAR\\CBD2000456_D02\\Applications\\" +
    "SipAddon\\StartApplication\\Appl\\TestSuit.elf"
vlab.load_image(
    image_path,
    subject="tc37x.CPU0_SUBSYSTEM.CPU0"
    )
vlab.enable_analysis(vlab.analysis.view.function_trace)
vlab.add_trace(subject='tc37x', sink=vlab.sink.vtf, verbose=False)

# ---- Fix FlexRay hardware failure ----
symbol_ = vlab.get_symbol("Fr_Init")
symbol_trig = vlab.trigger.execute(symbol_)
vlab.add_breakpoint(symbol_trig, action=fr_init_fix)

# ---- Stub flexRay functions ----
vlab.add_software_stub('Fr_SendWUP', fr_sendwup_fix)
vlab.add_software_stub('Fr_StartCommunication', fr_sendwup_fix)
vlab.add_software_stub('Fr_AllowColdstart', fr_sendwup_fix)

def bp_fun(bp):
    print "---\n Com_RxIndication\n---\n"

set_breakpoint_symbol('Com_RxIndication')

#bp before set deferred handle
vlab.add_breakpoint(
        vlab.trigger.execute(
            0xa00af606,
            core = "tc37x.CPU0_SUBSYSTEM.CPU0"
            )
        )
# bp before the callback
vlab.add_breakpoint(
        vlab.trigger.execute(
            0xa00aeec4,
            core = "tc37x.CPU0_SUBSYSTEM.CPU0"
            )
        )

set_breakpoint_symbol(
    'StartApplication_OnDataRec_RxData',
    action = switch_cyclic
    )
set_breakpoint_symbol('StartApplication_Cyclic250ms', action = sim_time)

#-----------------------------
#|------- CAN CONFIGS -------|
#-----------------------------

hybrid_node = vlab.get_instance("HybridNode0").obj
hybrid_node.set_id(0x268)
hybrid_node.can.set_bit_time_segment(CANNode.PROP_SEG, 2)
hybrid_node.can.set_bit_time_segment(CANNode.PHASE_SEG1, 3)
hybrid_node.can.set_bit_time_segment(CANNode.PHASE_SEG2, 3)
hybrid_node.can.set_clock_freq(900000L)
hybrid_node.can.activate()

#------------------------------
#|------- UART CONFIGS -------|
#------------------------------
hybrid_uart = vlab.get_instance("HybridNode0")
hybrid_adapter = vlab.get_instance("HybridUartAdapter")
# ---- Add virtual terminal ----
hybrid_node.add_terminal(hybrid_adapter)

#----------------------------------
#|------- LIN & UART  Init -------|
#----------------------------------
#Uart must be initialized to work with virtual terminal
# --- DISABLE NODES ---
#lin nodes
hybrid_node.lin_node.deactivate()
#uart nodes
hybrid_uart.obj.uart_node.deactivate()

#RUN 0 TIME
vlab.run(sysc.SC_ZERO_TIME, blocking=True)

# --- SET CLOCK FREQS ---
#lin nodes
lin_clk = 10000
hybrid_node.lin_node.set_clock_freq(lin_clk)
#uart nodes
uart_clk = 100000000
hybrid_adapter.obj.set_clock_freq(uart_clk)
hybrid_uart.obj.uart_node.set_clock_freq(uart_clk)

# uart breakpoints
trig_0_tx_done = vlab.trigger.port(
    (hybrid_uart, "count_event_tx_data")
    )
bp_0_tx_done = vlab.add_breakpoint(
    trig_0_tx_done,
    persist = False
    )

# --- ACTIVATE NODES ---
#lin nodes
hybrid_node.lin_node.activate(engine.LIN_MASTER)
vlab.run(sysc.SC_ZERO_TIME, blocking=True)

#uart nodes
hybrid_uart.obj.uart_node.activate(upec.UART_TRANSCEIVER)


#RUN 0 TIME
vlab.run(sysc.SC_ZERO_TIME, blocking=True)

is_gui = (vlab.get_properties()["interface_mode"] == "graphical")
if not is_gui:
    vlab.exit()

#This breakpoint shows what was written in out_term
trig_hybrid_rec = vlab.trigger.port(
    (hybrid_uart, "uart_event_received_command")
    )
bp_hybrid_rec = vlab.add_breakpoint(
    trig_hybrid_rec,
    action=display_hybrid
    )

print """
---------------------
| Ready to simulate |
---------------------
"""
vlab.run(5000, 'ms')
