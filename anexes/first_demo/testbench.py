# python libraries
import os

# vlab toolboxes
import vlab
import sysc
import can
import lin

can_files = os.path.dirname(__file__)
vlab.path.append(can_files)

# Create bus can
CanBus = vlab.component(name="CANTokenBusRouter", module="can.CANTokenBusRouter")
Can = vlab.instantiate(CanBus, "CanBus", args=[vlab.NAME, 10])
# -------- RESET CONNECTIONS --------
vlab.connect(vlab.STUB, ("CanBus","RESETN"), default=True)
vlab.connect(vlab.STUB, ("CanBus","RESET"), default=False)

# Create UART bus
vlab.component('bus_router', module='lin.bus_router')
uart_bus = vlab.instantiate('bus_router', 'UartBus', args=[vlab.NAME, 2])
uart_rx_control_conn = vlab.connect((uart_bus, 'OUT_RX_CONTROL'))
uart_rx_data_conn = vlab.connect((uart_bus, 'OUT_RX_DATA'))

# ------ Components instantiation ------
#vlab.instantiate("transceiver", "CustomCanNode")
vlab.instantiate("hybrid_node", "HybridNode0", args=[vlab.NAME, 0x234])

vlab.component('uart_terminal_adapter', module='lin.uart_terminal_adapter')
hybrid_adapter = vlab.instantiate('uart_terminal_adapter', "HybridUartAdapter")


# -------------------
# | CAN CONNECTIONS |
# -------------------

# -------- TOKEN CTRL CONNECTIONS --------
# CAN0
for i in range(4):
    vlab.connect(
            ("tc37x", "O_MCMCAN0_TXD_TOKEN_CTRL",i),
            ("CanBus", "IN_TX_CTRL", i)
            )

#CAN1
for i in range(4):
    vlab.connect(
            ("tc37x", "O_MCMCAN1_TXD_TOKEN_CTRL",i),
            ("CanBus", "IN_TX_CTRL", i+4)
            )
vlab.connect(
        ("HybridNode0", "CAN_TOKEN_TX_CTRL"),
        ("CanBus", "IN_TX_CTRL", 8)
        )

vlab.connect(
        ("CanBus", "OUT_RX_CTRL"),
        ([  #CAN0
            ("tc37x", "I_MCMCAN00_RXD_TOKEN_CTRL",0),#RXDA
            ("tc37x", "I_MCMCAN01_RXD_TOKEN_CTRL",2),#RXDC
            ("tc37x", "I_MCMCAN02_RXD_TOKEN_CTRL",1),#RXDB
            ("tc37x", "I_MCMCAN03_RXD_TOKEN_CTRL",0),#RXDA
            #CAN1
            ("tc37x", "I_MCMCAN10_RXD_TOKEN_CTRL",0),#RXDA
            ("tc37x", "I_MCMCAN11_RXD_TOKEN_CTRL",0),#RXDA
            ("tc37x", "I_MCMCAN12_RXD_TOKEN_CTRL",1),#RXDB
            ("tc37x", "I_MCMCAN13_RXD_TOKEN_CTRL",1),#RXDB
            #My Node
            ("HybridNode0", "CAN_TOKEN_RX_CTRL"),
            ]
            ),
        )
# -------- TOKEN DATA CONNECTIONS --------
# CAN0
for i in range(4):
    vlab.connect(
            ("tc37x", "O_MCMCAN0_TXD_TOKEN_DATA",i),
            ("CanBus", "IN_TX_DATA", i)
            )

#CAN1
for i in range(4):
    vlab.connect(
            ("tc37x", "O_MCMCAN1_TXD_TOKEN_DATA",i),
            ("CanBus", "IN_TX_DATA", i+4)
            )
vlab.connect(
        ("HybridNode0", "CAN_TOKEN_TX_DATA"),
        ("CanBus", "IN_TX_DATA", 8)
        )

vlab.connect(
        ("CanBus", "OUT_RX_DATA"),
        ([  #CAN0
            ("tc37x", "I_MCMCAN00_RXD_TOKEN_DATA",0),#RXDA
            ("tc37x", "I_MCMCAN01_RXD_TOKEN_DATA",2),#RXDC
            ("tc37x", "I_MCMCAN02_RXD_TOKEN_DATA",1),#RXDB
            ("tc37x", "I_MCMCAN03_RXD_TOKEN_DATA",0),#RXDA
            #CAN1
            ("tc37x", "I_MCMCAN10_RXD_TOKEN_DATA",0),#RXDA
            ("tc37x", "I_MCMCAN11_RXD_TOKEN_DATA",0),#RXDA
            ("tc37x", "I_MCMCAN12_RXD_TOKEN_DATA",1),#RXDB
            ("tc37x", "I_MCMCAN13_RXD_TOKEN_DATA",1),#RXDB
            #My Node
            ("HybridNode0", "CAN_TOKEN_RX_DATA"),
            ]
            ),
        )
# --------------------
# | UART CONNECTIONS |
# --------------------
# Hybrid node --> hybrid adapter
vlab.connect(
        ("HybridNode0", 'UART_RX_CONTROL'),
        (hybrid_adapter, 'OUT_RX_CONTROL')
        )
vlab.connect(
        ("HybridNode0", 'UART_RX_DATA'),
        (hybrid_adapter, 'OUT_RX_DATA')
        )
vlab.connect(
        ("HybridNode0", 'UART_TX_CONTROL'),
        (hybrid_adapter, 'IN_TX_CONTROL')
        )
vlab.connect(
        ("HybridNode0", 'UART_TX_DATA'),
        (hybrid_adapter, 'IN_TX_DATA')
        )
vlab.connect(
        vlab.STUB,
        (hybrid_adapter, 'RX_DATA'),
        kind='buffer'
        )
vlab.connect(
        vlab.STUB,
        (hybrid_adapter, 'TX_DATA'),
        kind='buffer'
        )
# hybrid adapter --> uart bus
vlab.connect(
        (hybrid_adapter, 'OUT_TX_CONTROL'),
        (uart_bus, 'IN_TX_CONTROL', 1)
        )
vlab.connect(
        (hybrid_adapter, 'OUT_TX_DATA'),
        (uart_bus, 'IN_TX_DATA', 1)
        )
vlab.connect(
        uart_rx_control_conn,
        (hybrid_adapter, 'IN_RX_CONTROL')
        )
vlab.connect(
        uart_rx_data_conn,
        (hybrid_adapter, 'IN_RX_DATA')
        )

# Change mcan engine
for mcan in range(2):
    for i in range(4):
        attribute_name = 'tc37x.mcan%d%d.ENGINE'%(mcan, i)
        vlab.write_attribute(attribute_name,  'token')

vlab.stub()