# python modules
import random

# vlab toolboxes
from vlab import simulation_time, print_in_terminal
import vlab
import sysc

# can toolbox
import can
from can.CANNode import CANNode
from can.Frame import Frame

# lin toolbox
from lin.lin_node import lin_node
from lin.lin_protocol_engine import lin_protocol_engine_common as engine
from lin.lin_protocol_engine import Response_t
# UART
from lin.uart_node import uart_node
from lin.uart_terminal_adapter import uart_terminal_adapter
from lin.uart_protocol_engine import uart_protocol_engine_common as upec
# Ethernet
import ethernet.EthernetNode as EthernetNode
from ethernet.frame import Ethernet
# local modules
from command_processor import CommandProcessor


class hybrid_node(sysc.sc_module, CommandProcessor):
    def __init__(self, name, id_, mac_add):
        super(hybrid_node, self).__init__(name)
        self._name = name

        # ------ CAN settings ------
        self.can = CANNode(
                "NodeCAN",
                can.CANNode.ENGINE_TYPE_TOKEN
                )
        self.data_log = []
        self.CAN_TOKEN_TX_CTRL = self.can.TOKEN_TX_CTRL
        self.CAN_TOKEN_RX_CTRL = self.can.TOKEN_RX_CTRL
        self.CAN_TOKEN_TX_DATA = self.can.TOKEN_TX_DATA
        self.CAN_TOKEN_RX_DATA = self.can.TOKEN_RX_DATA
        self.can_id = id_

        # spawn CAN methods
        self.spawn_thread("send_frame")
        self.spawn_method(
                "receive_data",
                self.can.on_frame_received_event,
                True
                )
        self.spawn_method(
                "finished_activation",
                self.can.on_finished_activation_event,
                True
                )

        # ------ UART settings ------
        # Monitor terminal

        # Declare ports
        self.UART_RX_CONTROL = sysc.sc_in_sc_uint_32('RX_CONTROL')
        self.UART_RX_DATA = sysc.sc_in_sc_uint_32('RX_DATA')
        self.UART_TX_CONTROL = sysc.sc_out_sc_uint_32('TX_CONTROL')
        self.UART_TX_DATA = sysc.sc_out_sc_uint_32('TX_DATA')
        self.UART_ENABLED = sysc.sc_in_sc_logic("UART_ENABLED")
        self.uart_msg = ''
        self.resp = 'GOT IT'
        self.uart_event_received_command = sysc.sc_out_unsigned_int(
                'uart_event_received_command')
        self.count_event_rx_data = sysc.sc_out_unsigned_int(
                'count_event_rx_data')
        self.count_event_rx_data_start = sysc.sc_out_unsigned_int(
                'count_event_rx_data_start')
        self.count_event_tx_data = sysc.sc_out_unsigned_int(
                'count_event_tx_data')
        self.count_event_tx_data_start = sysc.sc_out_unsigned_int(
                'count_event_tx_data_start')

        # Instantiate basic UART node
        self.uart_node = uart_node(self.name())
        # Bind UART ports
        self.uart_node.RX_CONTROL.bind(self.UART_RX_CONTROL)
        self.uart_node.RX_DATA.bind(self.UART_RX_DATA)
        self.uart_node.TX_CONTROL.bind(self.UART_TX_CONTROL)
        self.uart_node.TX_DATA.bind(self.UART_TX_DATA)
        # Declare event handlers
        self.spawn_method(
                self.on_event_rx_data,
                [self.uart_node.event_rx_data],
                dont_initialize = True
                )
        self.spawn_method(
                self.on_event_rx_data_start,
                [self.uart_node.event_rx_data_start],
                dont_initialize=True
                )
        self.spawn_method(
                self.on_event_tx_data,
                [self.uart_node.event_tx_data],
                dont_initialize = True
                )
        self.spawn_method(
                self.on_event_tx_data_start,
                [self.uart_node.event_tx_data_start],
                dont_initialize = True
                )


        # ------ LIN settings ------
        # Declare ports
        self.LIN_RX_CONTROL = sysc.sc_in_sc_uint_32(
                'LIN_RX_CONTROL'
                )
        self.LIN_RX_DATA = sysc.sc_in_sc_uint_32(
                'LIN_RX_DATA'
                )
        self.LIN_TX_CONTROL = sysc.sc_out_sc_uint_32(
                'LIN_TX_CONTROL'
                )
        self.LIN_TX_DATA = sysc.sc_out_sc_uint_32(
                'LIN_TX_DATA'
                )
        # Instantiate basic LIN node
        self.lin_node = lin_node(self.name())
        self.lin_fid = 0x7

        # Bind LIN ports
        self.lin_node.RX_CONTROL.bind(self.LIN_RX_CONTROL)
        self.lin_node.RX_DATA.bind(self.LIN_RX_DATA)
        self.lin_node.TX_CONTROL.bind(self.LIN_TX_CONTROL)

        self.lin_node.TX_DATA.bind(self.LIN_TX_DATA)

        self.spawn_method(
                self.lin_on_event_rx_data,
                [self.lin_node.event_data],
                dont_initialize=True
                )

        # ------ ETH settings ------
        self.eth_node = EthernetNode.EthernetNode(
                sysc.sc_module_name('eth_node')
                )
        self.mac_add = mac_add
        self.ether_type = 0xfeed

        self.ETH_RX = self.eth_node.RX
        self.ETH_TX = self.eth_node.TX


        self.spawn_method(#on receive
                self.on_eth_receive,
                self.eth_node.on_frame_received_event,
                dont_initialize=True
                )

        self.spawn_thread(self.eth_transmitter)
        self.eth_node.activate()

        self.msg_queue_empty = vlab.add_probepoint(
            source=self.name(),
            name="queue_empty",
            desc="Notified of a new frame, but it isn't on the receive queue",
            group="warning")
        self.msg_time = vlab.add_probepoint(
            source=self.name(),
            name="time",
            desc="A time beacon arrived",
            fields=[(sysc.sc_time, "network time"),
                    (sysc.sc_time, "propagation delay")],
            group="info")
        self.msg_unexpected_type = vlab.add_probepoint(
            source=self.name(),
            name="unexpected_type",
            desc="Received a frame with an unexpected type",
            fields=[(int, "type", "hex")],
            group="info")
        self.msg_unexpected_destination = vlab.add_probepoint(
            source=self.name(),
            name="unexpected_destination",
            desc="Received a frame addressed to someone else",
            fields=[(long, "destination", "hex")],
            group="info")

    def set_clock_freq(self, freq):
        self.can.set_clock_freq(freq)
        self.lin_node.set_clock_freq(freq)

    # ----------------------------------
    # |------- Termimal Monitor -------|
    # ----------------------------------

    def add_terminal(self, terminal_adapter, **kwargs):
        self.terminal_adapter = terminal_adapter
        self.finish = False
        vlab.add_terminal(
                kwargs['name'],
                output_port = (self.terminal_adapter, "TX_DATA"),
                input_port = (self.terminal_adapter, "RX_DATA"),
                baud_rate_func =
                    self.terminal_adapter.obj.get_terminal_clock_freq
                )
        is_gui = (vlab.get_properties()["interface_mode"] == "graphical")
        exec('self.terminal = vlab.terminal.{}'.format(kwargs['name']))
        display = True
        if kwargs.get("display"): display = kwargs['display']
        if is_gui and display:
                vlab.display_terminal(self.terminal)


        # Print test instruction
        MSG = kwargs['msg']
        vlab.print_in_terminal(self.terminal, MSG)
        #this breakpoint is used for showing what youre typing in the terminal
        trig_0_rx_updated = vlab.trigger.port(
                (self.terminal_adapter, "RX_DATA")
                )
        bp_0_rx = vlab.add_breakpoint(trig_0_rx_updated, action=self.echo)

    def echo(self, bp):
        """Send character to terminal 1."""
        vlab.pause()
        port = bp.trigger["port"][0]
        ch = vlab.read_port(port)
        if ch == 0x1A:
        # Ctrl-Z character detected; exit
                self.finish = True
        else:
                vlab.disable_breakpoint(bp)
                if ch == 0x0D:
                        self.send_char('\n')
                else:
                        self.send_char(chr(ch))
                vlab.enable_breakpoint(bp)

    # ------------------------------
    # |------- UART METHODS -------|
    # ------------------------------

    def reset(self, freq):
        self.node.deactivate()
        run(sysc.SC_ZERO_TIME, blocking=True)
        self.node.set_clock_freq(freq)
        self.node.set_data_bits(8)
        self.node.set_stop_bits(1)
        self.node.set_parity_type(upec.UART_PARITY_NONE)
        self.node.set_lsb()
        self.node.activate(upec.UART_TRANSCEIVER)
        run(sysc.SC_ZERO_TIME, blocking=True)

    def get_uart_response(self):
            return self.resp
    def clear_uart_response(self):
            self.resp = ''

    def get_char(self):
        rx = self.uart_node.get_rx_buffer()
        return chr(rx[-1] & 0xFF)

    def send_char(self, ch):
        self.uart_node.transmit(ord(ch))

    def on_event_rx_data(self):
        self.count_event_rx_data.write(self.count_event_rx_data.read() + 1)
        last_char = self.get_char()
        self.uart_msg += last_char
        if last_char == "\n":
                # Uncomment next line only for debug purposes
                self.print_ter(self.name(), "UART", self.uart_msg)
                print self.name(), "transmiting ", self.uart_msg
                self.command = self.uart_msg
                self.uart_msg = ''
                #transmitting character
                for char in self.uart_msg:
                        self.send_char(char)
                print self.command
                self.exec_command(self.command[:-1])
                self.uart_event_received_command.write(
                        self.uart_event_received_command.read() + 1
                        )

    def on_event_rx_data_start(self):
        self.count_event_rx_data_start.write(
                self.count_event_rx_data_start.read() + 1
                )

    def on_event_tx_data(self):
        self.count_event_tx_data.write(
                self.count_event_tx_data.read() + 1
                )

    def on_event_tx_data_start(self):
        self.count_event_tx_data_start.write(
                self.count_event_tx_data_start.read() + 1
                )

    # -----------------------------
    # |------- LIN METHODS -------|
    # -----------------------------
    def lin_on_event_rx_data(self):
        response = Response_t()
        success = self.lin_node.get_latest_response(self.lin_fid, response)


    # -----------------------------
    # |------- ETH METHODS -------|
    # -----------------------------

    def eth_transmitter(self):
        self.wait(1, sysc.SC_SEC)

        prototype_frame = Ethernet(
            destination = 0x0A01A8C0,
            source = 0x001122334490,
            typeid=self.ether_type)
        frame = Frame()
        frame.set_id(0x34)
        frame.set_dlc(8)
        for j in range(8):
                frame.set_data_at_index(j, random.randint(0X1, 0xFF))
        frame = Ethernet(prototype_frame, payload=frame.get_data())
        print self.name(), ": transmiting eth frame {} {}".format(
                frame.destination,
                frame.payload
                )
        self.eth_node.transmit_frame(frame)
        # --- second transmition
        self.wait(1, sysc.SC_SEC)

        prototype_frame = Ethernet(
            destination = 0x0C01A8C0,
            source = 0x001122334490,
            typeid=self.ether_type)
        frame = Frame()
        frame.set_id(0x34)
        frame.set_dlc(8)
        for j in range(8):
                frame.set_data_at_index(j, random.randint(0X1, 0xFF))
        frame = Ethernet(prototype_frame, payload=frame.get_data())
        print self.name(), ": transmiting eth frame {} {}".format(
                hex(frame.destination),
                frame.payload
                )
        self.eth_node.transmit_frame(frame)

    def on_eth_receive(self):
        frame = Ethernet(self.eth_node.get_latest_received_frame())
        print self.name() +
            "Got something \nSOURCE={} \nDATA={} \nDESTINATION={}".format(
            str(hex(frame.source)),
            str(frame.payload),
            str(hex(frame.destination))
            )

        if frame.source ==  0x55361216fa41:
            prototype_frame = Ethernet(
                destination = 0x0C01A8C0,
                source = 0x43,
                typeid=self.ether_type
                )
            payload_data = []
            for j in range(40):
                payload_data.append(random.randint(0X1, 0xFF))
            res_frame = Ethernet(prototype_frame, payload=frame.payload)
            print self.name() +
                ": transmiting eth \nSOURCE={} \nDATA={} \nDESTINATION={}".format(
                hex(res_frame.source),
                frame.payload,
                str(hex(res_frame.destination))
                )
            self.eth_node.transmit_frame(res_frame)


        if not self.eth_node.has_received_new_frame():
            vlab.activate_probepoint(self.msg_queue_empty)

        while self.eth_node.has_received_new_frame():
            if frame.destination == self.mac_add:
                if frame.typeid == self.ether_type:
                    print self.name(), "Got something {}".format(
                            str(frame.payload)
                            )

    # -----------------------------
    # |------- CAN METHODS -------|
    # -----------------------------
    def send_frame(self):
        frame = Frame()
        frames = [
            #CanId,     PduDlc, FD,     ValidDLC
            #(0x0501,   0xf,    True,   1),
            (0x324,     8,      True,   8),
            (0x0101,    8,      False,  4),
            (0x0178,    8,      False,  4),
            (0x0202,    8,      True,   8),
            (0x4501,    8,      False,  4),
            (0x5162,    8,      False,  4),
        ]

        for frame_config in frames:
            frame_conf = {
                'CanId': frame_config[0],
                'PduDlc': frame_config[1],
                'FD': frame_config[2]
                }
            frame = Frame()
            frame.set_fd(frame_conf['FD'])
            frame.set_extended_not_standard(not frame_conf['FD'])
            frame.set_id(frame_conf['CanId'])
            frame.set_dlc(frame_conf['PduDlc'])
            ValidDLC = frame_config[3]
            for j in range(ValidDLC):
                    frame.set_data_at_index(j, random.randint(0X1, 0xFF))
            sysc.wait(1000, sysc.SC_MS)
            if self.can_id == 0x123:
                print "{}:---> transmit_thread started @ {}" +
                "sec\n--> ID:{} {}\n".format(
                    self.name(),
                    sysc.sc_time_stamp().to_seconds(),
                    hex(frame.get_id()),
                    frame.get_data()
                    )
                self.can.transmit_frame(frame)

    def set_id(self, id_):
        self.can_id = id_
        print self.name() +
            ": id set to " +
            self.can_id +
            " at" +
            sysc.sc_time_stamp().to_seconds(), "sec"

    def finished_activation(self):
        print self.name()+
            ": Finished activation at" +
            sysc.sc_time_stamp().to_seconds() +
            "sec"

    def sim_time(self):
        return vlab.simulation_time().to_seconds() * 1000

    def receive_data(self):
        frame = self.can.get_latest_received_frame()
        data_list = frame.get_data()
        empty = True
        for msg in data_list:
            if msg != 0x0:
                empty = False
        if not empty:
            self.display_can()
        if(frame.get_id() == self.can_id):
                print self.name() +
                        ":Got frame @{} ms\n" +
                        "DATA: {}".format(self.sim_time(), frame.get_data())
                self.data_log.append({
                        "bus": "CAN",
                        "data": frame.get_data(),
                        "time": simulation_time().to_seconds() * 1000
                })
                self.display_can()

    def display_can(self):
        frame = self.can.get_latest_received_frame()
        if(frame.get_id() == self.can_id):
                vlab.print_in_terminal(self.terminal,
                        "\n->GOT CAN FRAME:\nCANID: {} DATA: {}"+
                        "@{}\n".format(
                            str(hex(frame.get_id())),
                            str(frame.get_data()),
                            self.sim_time())
                        )

    def activate(self):
        self.can.activate()
        self.lin_node.activate(engine.LIN_MASTER)

    def print_ter(self, node_name, data_bus, data):
        time_ = simulation_time().to_seconds() * 1000
        string_ = "\n>>t = " + str(time_) + "ms >>" +
                  node_name + ">>" + data_bus + " > "
        vlab.print_in_terminal(
                vlab.terminal.hybrid_node_terminal,
                string_
                )
        vlab.print_in_terminal(
                vlab.terminal.hybrid_node_terminal,
                str(data)
                )
        vlab.print_in_terminal(
                vlab.terminal.hybrid_node_terminal,
                "\n$"
                )

    # ----------------------------------
    # |------- COMMANDS METHODS -------|
    # ----------------------------------
    def command_CAN(self):
        super(hybrid_node)
        print self.name(), ":Transmiting frame @", self.sim_time(), "ms"
        frame = raw_data2frame(self.kwargs, "CAN")
        frame.show()
        self.can.transmit_frame(frame)

    def command_LIN(self):
        super(hybrid_node)
        frame, fid = raw_data2frame(self.kwargs, "LIN")
        #test fid 0x7
        self.lin_node.publish(fid,frame.get_data())
        self.lin_node.transmit_header(fid)

    def pause(self):
        self.finish = True

    def command_not_found(self, command):
        super(hybrid_node)
        error = "Command " + command[8:] + " not found"
        self.print_ter(self.name(), "COMMAND_PROCESSOR", error)


def raw_data2frame(kwargs, data_bus):
        is_remote = True
        if kwargs.get('isRemote'):
                is_remote = kwargs['isRemote'] == 'True'
                is_remote = not(kwargs['isRemote'] == 'False')
        is_extended = False
        if kwargs.get('isExtended'):
                is_extended = kwargs['isExtended'] == 'True'
                is_extended = not(kwargs['isExtended'] == 'False')

        raw_data = kwargs['data'].split(',')
        data = []
        for num in raw_data:
                data.append(int(num))

        dlc = len(data)
        if kwargs.get('dlc'):
                dlc = int(kwargs['dlc'])

        frame_type = Frame.FRAME_TYPE_MESSAGE
        if kwargs.get('isExtended'):
                if kwargs['type'] == 'Message' or
                   kwargs['type'] == 'message':
                        frame_type = Frame.FRAME_TYPE_MESSAGE
        frame = Frame(
                frame_type,
                is_remote,
                is_extended,
                0x00,# it is set at the, thats for recycling purposes
                dlc
                )
        frame.set_data(data)

        if data_bus == 'CAN':
                id = int(kwargs['id'], 16)
                frame.set_id(id)
                return frame
        elif data_bus == 'LIN':
                fid = int(kwargs['fid'], 16)
                return frame, fid

def gen_random_frame(isFDEnabled = None, isExtended = None,
                     isRemote = None, dlcMax = None, useDlc = None):
    """
    Returns a random frame taking into
    consideration the constraints provided
    """
    frame = Frame()

    # CAN or CAN FD
    frame.set_fd(False)

    # Standard or Extended
    frame.set_extended_not_standard(False)

    # Data or Remote
    if (frame.is_fd()):
        frame.set_remote_not_data(False)
        frame.set_bit_rate_switched(random.choice([True, False]))
    else:
        frame.set_bit_rate_switched(False)
        if isRemote is None:
            frame.set_remote_not_data(random.choice([True, False]))
        else:
            frame.set_remote_not_data(False)
    # ID
    frame.set_id(0x501)

    # DLC
    if useDlc is None:
        if dlcMax is None:
            frame.set_dlc(random.randint(0, 0xF))
        else:
            frame.set_dlc(random.randint(0, dlcMax&0xF))
    else:
        frame.set_dlc(useDlc)

    # Data
    if (frame.is_data()):
        for i in range(8):
            frame.set_data_at_index(i, random.randint(0X1, 0xFF))

    return frame
