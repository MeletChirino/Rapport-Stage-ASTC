import collections
import sysc
import can
from can.CANNode import CANNode
from can.Frame import Frame

class transceiver(sysc.sc_module):
    """Can transceiver for gateway"""
    def __init__(self, name):
        sysc.sc_module.__init__(self, name)
        self.can = CANNode(
                "Node",
                can.CANNode.ENGINE_TYPE_TOKEN
                )
        self.id = 0x00
        #create token ports
        self.CAN_TOKEN_TX_CTRL = self.can.TOKEN_TX_CTRL
        self.CAN_TOKEN_RX_CTRL = self.can.TOKEN_RX_CTRL
        self.CAN_TOKEN_TX_DATA = self.can.TOKEN_TX_DATA
        self.CAN_TOKEN_RX_DATA = self.can.TOKEN_RX_DATA

        self.rx_frames_queue = collections.deque([])

        self.spawn_method(
                "can_frame_received",
                self.can.on_frame_received_event,
                True
                )
        self.spawn_method(
                "can_frame_mirror",
                self.can.on_frame_received_event,
                False
                )
    def can_frame_mirror(self):
        pass
        #print("Sending Msgs")
        #sysc.wait(10, sysc.SC_MS)
        #self.can.transmit_frame(self.can.get_latest_received_frame())

    def set_can_id(self, id_):
        self.can_id = id_
        print self.name(), ".id set to ", hex(self.can_id)

    def can_frame_received(self):
        rx_frame = self.can.get_latest_received_frame()
        '''
        print(
                self.name(),
                ": Frame is received at",
                sysc.sc_time_stamp().to_seconds(),
                "s\nID:",
                hex(rx_frame.get_id()),
                "\nData:",
                rx_frame.get_data()
                )
        '''

        if(rx_frame.get_id() == self.can_id):
            #print self.name(),": This one is for me!"
            self.rx_frames_queue.append(rx_frame)

            #rx_frame.show()
