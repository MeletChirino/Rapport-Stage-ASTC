# Run file for GW demo
import os
import random

# vlab toolboxes
import vlab
import sysc
import can
import can.CANNode as CANNode
from ethernet.frame import Ethernet as EthFrame

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
 
AURIX_MODEL = 'tc37xext'

def set_breakpoint_symbol(symbol_name, **kwargs):
    symbol_ = vlab.get_symbol(symbol_name)
    symbol_trig = vlab.trigger.execute(symbol_)
    if kwargs.get('action'):
        func = kwargs['action']
        vlab.add_breakpoint(symbol_trig, action=func)
        return 0
    vlab.add_breakpoint(symbol_trig)

def wait_node0_tx(count):
    """Wait until node0 transmits specified number of bytes."""
    while bp_0_tx_done.hits < count:
        vlab.run(1, "ms", True)

def display_ecu2can2(bp):
    """Display hybrid response in terminal."""
    vlab.disable_breakpoint(bp)
    rx = ecu2can2_uart.obj.get_uart_response()
    vlab.print_in_terminal(vlab.terminal.ecu2term, rx)
    ecu2_uart.obj.clear_uart_response()
    vlab.enable_breakpoint(bp)

def display_tc39x(bp):
    """Display hybrid response in terminal."""
    vlab.disable_breakpoint(bp)
    rx = tc39x_uart.obj.get_uart_response()
    vlab.print_in_terminal(vlab.terminal.tc39xterm, rx)
    tc39x_uart.obj.clear_uart_response()
    vlab.enable_breakpoint(bp)

def dump_eth_frame(frame):
    in_msg = vlab.read_port('tc37ex.O_GETH_TX').GetData()
    print "\n\n====> Original frame <==== \n "
    for pdu in in_msg:
        print "0x{:X},".format(pdu),

    print "\n\n====> GETH_IN <====  "
    print "dest = 0x{:X} 0x{:X} 0x{:X} 0x{:X} 0x{:X} 0x{:X}".format(
        in_msg[0], in_msg[1], in_msg[2],
        in_msg[3], in_msg[4], in_msg[5])

    print "source = 0x{:X} 0x{:X} 0x{:X} 0x{:X} 0x{:X} 0x{:X}".format(
        in_msg[6], in_msg[7], in_msg[8],
        in_msg[9], in_msg[10], in_msg[11])

    print "Tag = 0x{:X} 0x{:X} 0x{:X} 0x{:X}".format(
        in_msg[12], in_msg[13], in_msg[14], in_msg[15])

    print("EtherType = 0x{:X} 0x{:X}".format(
        in_msg[16], in_msg[17]))

    print("Request Format = 0x{:X} 0x{:X}".format(
        in_msg[18], in_msg[19]))

    print("Pad = 0x{:X} 0x{:X}".format(
        in_msg[20], in_msg[21]))

    print("Request code = 0x{:X} 0x{:X}".format(
        in_msg[22], in_msg[23]))
    offset = 24
    frame_size = len(in_msg)
    while(offset + 4 < frame_size):
        print "Octet = 0x{:X} 0x{:X} 0x{:X} 0x{:X}".format(
            in_msg[offset + 0],
            in_msg[offset + 1],
            in_msg[offset + 2],
            in_msg[offset + 3])
        offset += 4

    print "\n\n====> GETH_IN2 <====  "
    offset = 0
    while(offset + 4 < frame_size):
        print "Octet = 0x{:X} 0x{:X} 0x{:X} 0x{:X}".format(
            in_msg[offset + 0],
            in_msg[offset + 1],
            in_msg[offset + 2],
            in_msg[offset + 3])
        offset += 4
    #vlab.pause()

def enable_mdio_bp(bp):
    vlab.add_breakpoint(vlab.trigger.port('tc37ex.GETH.MDIO_in'))
    vlab.pause()

if __name__ == '__main__':
    # Load VP
    testbench_file = "--testbench={}\\{}".format(hybrid_node_files, "testbench.py")
    vlab.load(
        "aurix.{}.sim".format(AURIX_MODEL),
        args=[
            testbench_file,
            '--debugger-config=all:trace32mcd',
            #"--iss=fast",
            "--quantum-period=500",#quantum in nanoseconds => 1us
            '--debugger=all']
        )


    # Load image to VP
    folder_name = os.path.basename(file_path)
    parent_folder = file_path.replace('\\{}'.format(folder_name), '')

    image_path = os.path.join(parent_folder, 'TestSuit.elf')
    vlab.load_image(
        image_path,
        subject="{}.CPU0_SUBSYSTEM.CPU0".format(AURIX_MODEL) 
        )
    vlab.enable_analysis(vlab.analysis.view.function_trace)
    vlab.add_trace(subject='{}.GETH.MDIO_out'.format(AURIX_MODEL) , sink=vlab.sink.vtf, verbose=False)
    vlab.add_trace(subject='{}.GETH.MDIO_in'.format(AURIX_MODEL) , sink=vlab.sink.vtf, verbose=False)
    vlab.add_trace(subject='{}.I_GETH_RX'.format(AURIX_MODEL) , sink=vlab.sink.vtf, verbose=False)
    vlab.add_trace(subject='{}.O_GETH_TX'.format(AURIX_MODEL) , sink=vlab.sink.vtf, verbose=False)
    #vlab.add_trace(subject='tc37ex.GETH', sink=vlab.sink.vtf, verbose=False)
    #vlab.add_trace(subject=AURIX_MODEL, sink=vlab.sink.vtf, verbose=False)

    #-----------------------------
    #|------- BREAKPOINTS -------|
    #-----------------------------
    #vlab.add_breakpoint(vlab.trigger.execute(0xa00dddf0, core="tc37ex.CPU0_SUBSYSTEM.CPU0"))
    #vlab.add_breakpoint(vlab.trigger.execute(0xa00e5d9a, core="tc37ex.CPU0_SUBSYSTEM.CPU0"))#SoAd_RouteGrp_CheckAnyRoutGrpOnPduRouteDestEnabled
    #vlab.add_breakpoint(vlab.trigger.execute(0xa00e60b2, core="tc37ex.CPU0_SUBSYSTEM.CPU0"))#inside SoAd_TxIf_TransmitPduRouteDest

    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('SoAd_SoCon_HandleSoConStates')))
    vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('Det_ReportError')))
    vlab.add_breakpoint(
        vlab.trigger.execute(vlab.get_symbol('SoAd_RouteGrp_CheckAnyRoutGrpOnPduRouteDestEnabled'))
        )
    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('SoAd_MainFunctionState')))
    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('SoAd_IfTransmit')))
    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('SoAd_Init')))
    vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('SoAd_MainFunctionState')))

    vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('EthSwt_30_88Q5050_VSwitchInit')))
    #vlab.add_breakpoint(vlab.trigger.execute(0xa00d2bcc, core="tc37ex.CPU0_SUBSYSTEM.CPU0"))
    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('Eth_30_Tc3xx_ReadMii')))
    #vlab.add_breakpoint(vlab.trigger.execute(vlab.get_symbol('Eth_30_Tc3xx_WriteMii')))
    '''
    vlab.add_breakpoint(
        vlab.trigger.port('tc37ex.O_GETH_TX'),
        action = dump_eth_frame
        )
    '''
    #vlab.add_breakpoint(vlab.trigger.execute(0xa00cd6a0, core="tc37ex.CPU0_SUBSYSTEM.CPU0"))

    #-----------------------------
    #|------- CAN CONFIGS -------|
    #-----------------------------
    clk = 900000L

    ecu2can2 = vlab.get_instance("Ecu2Can2").obj
    ecu2can2.can.set_bit_time_segment(CANNode.PROP_SEG, 2)
    ecu2can2.can.set_bit_time_segment(CANNode.PHASE_SEG1, 3)
    ecu2can2.can.set_bit_time_segment(CANNode.PHASE_SEG2, 3)
    ecu2can2.can.set_clock_freq(clk)
    ecu2can2.can.activate()

    tc39x = vlab.get_instance("Tc39x").obj
    tc39x.can.set_bit_time_segment(CANNode.PROP_SEG, 2)
    tc39x.can.set_bit_time_segment(CANNode.PHASE_SEG1, 3)
    tc39x.can.set_bit_time_segment(CANNode.PHASE_SEG2, 3)
    tc39x.can.set_clock_freq(clk)
    tc39x.can.activate()

    #------------------------------
    #|------- UART CONFIGS -------|
    #------------------------------
    ecu2can2_uart = vlab.get_instance("Ecu2Can2")
    tc39x_uart = vlab.get_instance("Tc39x")

    ecu2_term = vlab.get_instance("ECU2Term")
    tc39x_term = vlab.get_instance("Tc39xTerm")

    # --- Add virtual terminals ---
    ecu2can2.add_terminal(
            ecu2_term,
            name='ecu2term',
            msg = 'This is ECU2 Terminal',
            display = False
            )
    tc39x.add_terminal(
            tc39x_term,
            name='tc39xterm',
            msg = 'This is TC39X terminal',
            display = False
            )

    #----------------------------------
    #|------- LIN & UART  Init -------|
    #----------------------------------

    # --- DISABLE NODES ---
    #uart nodes
    ecu2can2_uart.obj.uart_node.deactivate()
    tc39x_uart.obj.uart_node.deactivate()

    #RUN 0 TIME
    vlab.run(sysc.SC_ZERO_TIME, blocking=True)

    # --- SET CLOCK FREQS ---
    #uart nodes
    uart_clk = 100000000
    ecu2_term.obj.set_clock_freq(uart_clk)
    tc39x_term.obj.set_clock_freq(uart_clk)
    ecu2can2_uart.obj.uart_node.set_clock_freq(uart_clk)
    tc39x_uart.obj.uart_node.set_clock_freq(uart_clk)

    # uart breakpoints
    trig_0_tx_done = vlab.trigger.port(
        (ecu2can2_uart, "count_event_tx_data")
        )
    bp_0_tx_done = vlab.add_breakpoint(
        trig_0_tx_done,
        persist = False
        )

    # --- ACTIVATE NODES ---

    #uart nodes
    ecu2can2_uart.obj.uart_node.activate(upec.UART_TRANSCEIVER)
    tc39x_uart.obj.uart_node.activate(upec.UART_TRANSCEIVER)


    #RUN 0 TIME
    vlab.run(sysc.SC_ZERO_TIME, blocking=True)

    is_gui = (vlab.get_properties()["interface_mode"] == "graphical")
    if not is_gui:
        vlab.exit()
        
    #This breakpoint shows what was written in out_term
    trig_ecu2can2_rec = vlab.trigger.port(
        (ecu2can2_uart, "uart_event_received_command")
        )
    bp_ecu2can2_rec = vlab.add_breakpoint(
        trig_ecu2can2_rec,
        action=display_ecu2can2
        )

    trig_tc39x_rec = vlab.trigger.port(
        (tc39x_uart, "uart_event_received_command")
        )
    bp_tc39x_rec = vlab.add_breakpoint(
        trig_tc39x_rec,
        action=display_tc39x
        )
    '''
    while not (tc39x.finish or ecu2can2.finish):
        vlab.run(blocking=True)
    vlab.exit()
    '''
        
    print """
    ---------------------
    | Ready to simulate |
    ---------------------
    """
    vlab.run(5000, 'ms')
    #vlab.exit()
