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

MAC_ECU2 = 0x771122354455
MAC_TC39X = 0x771122354410

class GateWayHub(sysc.sc_module):
    def __init__(self, name):
        # ------ CAN settings ------
        #sysc.sc_module.__init__(self, name)
        super(GateWayHub, self).__init__(name)
        self.can = [
                CANNode(
                    "NodeCAN0",
                    can.CANNode.ENGINE_TYPE_TOKEN
                    ),
                CANNode(
                    "NodeCAN1",
                    can.CANNode.ENGINE_TYPE_TOKEN
                    ),
                ]


        self.data_log = []
        self.CAN_TOKEN_TX_CTRL = [
                self.can[0].TOKEN_TX_CTRL,
                self.can[1].TOKEN_TX_CTRL,
                ]
        self.CAN_TOKEN_RX_CTRL = [
                self.can[0].TOKEN_RX_CTRL,
                self.can[1].TOKEN_RX_CTRL,
                ]
        self.CAN_TOKEN_TX_DATA = [
                self.can[0].TOKEN_TX_DATA,
                self.can[1].TOKEN_TX_DATA,
                ]
        self.CAN_TOKEN_RX_DATA = [
                self.can[0].TOKEN_RX_DATA,
                self.can[1].TOKEN_RX_DATA,
                ]
        self.can_id = [0x324, 0x202]

        self.spawn_method(
                "finished_activation",
                self.can[0].on_finished_activation_event,
                True
                )
        self.spawn_method(
                "receive0_data",
                self.can[0].on_frame_received_event,
                True
                )
        self.spawn_method(
                "receive1_data",
                self.can[1].on_frame_received_event,
                True
                )
        #method when receiving data

        # ------ ETH settings ------
        self.eth_nodes = [
                EthernetNode.EthernetNode(sysc.sc_module_name('node0')),
                EthernetNode.EthernetNode(sysc.sc_module_name('node1')),
                ]
        self.mac_add1 = 0x001122334455 #GWMAC1
        self.mac_add2 = 0x001122334457 #GWMAC2
        self.ether_type = 0xfeed
        
        self.ETH_RX = [self.eth_nodes[0].RX, self.eth_nodes[1].RX]
        self.ETH_TX = [self.eth_nodes[0].TX, self.eth_nodes[1].TX]


        self.spawn_method(#on receive GWMAC1
                self.on_eth_receive0,
                self.eth_nodes[0].on_frame_received_event,
                dont_initialize=True
                )
        self.spawn_method(#on receive GWMAC2
                self.on_eth_receive1,
                self.eth_nodes[1].on_frame_received_event,
                dont_initialize=True
                )
        self.eth_nodes[0].activate()
        self.eth_nodes[1].activate()
            
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
        
    # -----------------------------
    # |------- CAN METHODS -------|
    # -----------------------------
    def set_clock_freq(self, freq):
        self.can[0].set_clock_freq(freq)
        self.can[1].set_clock_freq(freq)
                
    def set_id(self, id_):
        if not len(id_) == 2:
            raise Exception("You must write a list of two elements")
        self.can_id = id_
        print self.name(), ": can1 id set to ", self.can_id," at", sysc.sc_time_stamp().to_seconds(), "sec"

    def finished_activation(self):
        print self.name(), ": Finished activation at", sysc.sc_time_stamp().to_seconds(), "sec"

    def receive0_data(self):
        frame = self.can[0].get_latest_received_frame()
        if frame.get_id() == self.can_id[0]:
                print self.name(), ":Got frame @{} ms\n DATA: {}".format(self.sim_time(), frame.get_data())
                frame.set_id(0x325)
                #from ecu2 -> tc39x
                #self.can[1].transmit_frame(frame)
                prototype_frame = Ethernet(
                    destination = MAC_TC39X,
                    source=self.mac_add1,
                    typeid=self.ether_type)
                eth_frame = Ethernet(prototype_frame, payload=frame.get_data())
                print self.name(), ":  frame CAN0 -> ETH1"
                self.eth_nodes[1].transmit_frame(eth_frame)
                
    def receive1_data(self):
        #from tc39x -> ecu2
        frame = self.can[1].get_latest_received_frame()
        if frame.get_id() == self.can_id[1]:
                print self.name(), ":Got frame @{} ms\n DATA: {}".format(self.sim_time(), frame.get_data())
                frame.set_id(0x123)
                prototype_frame = Ethernet(
                    destination = MAC_ECU2,
                    source = self.mac_add2,
                    typeid=self.ether_type)
                eth_frame = Ethernet(prototype_frame, payload=frame.get_data())
                print(self.name(), " frame CAN1 -> ETH0")
                self.eth_nodes[0].transmit_frame(eth_frame)

    def activate(self):
        self.can.activate()
    # -----------------------------
    # |------- ETH METHODS -------|
    # -----------------------------
    def sim_time(self):
        return vlab.simulation_time().to_seconds() * 1000          

    def on_eth_receive0(self):
        if not self.eth_nodes[0].has_received_new_frame():
            vlab.activate_probepoint(self.msg_queue_empty)
        while self.eth_nodes[0].has_received_new_frame():
            frame = Ethernet(self.eth_nodes[0].get_latest_received_frame())
            if frame.destination == self.mac_add1:
                if frame.typeid == self.ether_type:
                    print self.name(), "Got something {}".format(str(frame.payload))

                
    def on_eth_receive1(self):
        if not self.eth_nodes[1].has_received_new_frame():
            vlab.activate_probepoint(self.msg_queue_empty)
        while self.eth_nodes[1].has_received_new_frame():
            frame = Ethernet(self.eth_nodes[1].get_latest_received_frame())
            if frame.destination == self.mac_add2:
                if frame.typeid == self.ether_type:
                    print self.name(), "Got something {}".format(str(frame.payload))