# python libraries
import os

# vlab toolboxes
import vlab
import sysc
import can
import lin
import ethernet.VLANBridge as VLANBridge
#import MDIO_bus
import aurix
#import swt88q5050

# aurix variant name
from run_microsar import AURIX_MODEL

can_files = os.path.dirname(__file__)
vlab.path.append(can_files)

# Create can bus
CanBus1 = vlab.component(
        name = "CANTokenBusRouter",
        module = "can.CANTokenBusRouter"
        )
CanBus2 = vlab.component(
        name = "CANTokenBusRouter",
        module = "can.CANTokenBusRouter"
        )

Can1 = vlab.instantiate(CanBus1, "CAN1", args=[vlab.NAME, 4])
Can2 = vlab.instantiate(CanBus2, "CAN2", args=[vlab.NAME, 4])

# -------- RESET CONNECTIONS --------
vlab.connect(vlab.STUB, ("CAN1", "RESETN"), default = True)
vlab.connect(vlab.STUB, ("CAN1", "RESET"), default=False)

vlab.connect(vlab.STUB, ("CAN2", "RESETN"), default = True)
vlab.connect(vlab.STUB, ("CAN2", "RESET"), default=False)

# UART components
vlab.component('uart_terminal_adapter', module='lin.uart_terminal_adapter')

# ------ Components instantiation ------
# Hybrid Nodes
MAC_ECU2 = 0x771122354455
MAC_TC39X = 0x771122354410
vlab.instantiate("hybrid_node", "Ecu2Can2", args=[vlab.NAME, 0x123, MAC_ECU2])
vlab.instantiate("hybrid_node", "Tc39x", args=[vlab.NAME, 0x325, MAC_TC39X])

# UART components
ecu2_term = vlab.instantiate('uart_terminal_adapter', "ECU2Term")
tc39x_term = vlab.instantiate('uart_terminal_adapter', "Tc39xTerm")

#MDIO_BUS
mdio_bus = vlab.component("MDIO_bus", module="aurix.MDIO_bus")
vlab.instantiate(mdio_bus, "MDIO_bus_", args=[vlab.NAME, 2, 2])
#Switch marvel
swt_component = vlab.component("marvell_88Q5050", module='aurix.marvell_88Q5050')
marvell_88Q5050 = vlab.instantiate(
        swt_component,
        "Marvell_88Q5050",
        args=[vlab.NAME]
        )
aurix_model = AURIX_MODEL

# -------------------
# | CAN CONNECTIONS |
# -------------------
# Ecu2Can2 --CAN2-- tc37xGW
# -------- TOKEN CTRL CONNECTIONS --------
# CAN2

for i in range(3):
    vlab.connect(
            (aurix_model, "O_MCMCAN2_TXD_TOKEN_CTRL",i),
            ("CAN2", "IN_TX_CTRL", i)
            )

vlab.connect(
        ("Ecu2Can2", "CAN_TOKEN_TX_CTRL"),
        ("CAN2", "IN_TX_CTRL", 3)
        )

vlab.connect(
        ("CAN2", "OUT_RX_CTRL"),
        ([  #CAN2
            (aurix_model, "I_MCMCAN20_RXD_TOKEN_CTRL", 2),#RXDC
            (aurix_model, "I_MCMCAN21_RXD_TOKEN_CTRL", 2),#RXDC
            (aurix_model, "I_MCMCAN22_RXD_TOKEN_CTRL", 0),#RXDA
            #My Node
            ("Ecu2Can2", "CAN_TOKEN_RX_CTRL"),
            ]
            ),
        )
# -------- TOKEN DATA CONNECTIONS --------
for i in range(3):
    vlab.connect(
            (aurix_model, "O_MCMCAN2_TXD_TOKEN_DATA",i),
            ("CAN2", "IN_TX_DATA", i)
            )

vlab.connect(
        ("Ecu2Can2", "CAN_TOKEN_TX_DATA"),
        ("CAN2", "IN_TX_DATA", 3)
        )

vlab.connect(
        ("CAN2", "OUT_RX_DATA"),
        ([  #CAN2
            (aurix_model, "I_MCMCAN20_RXD_TOKEN_DATA", 2),#RXDC
            (aurix_model, "I_MCMCAN21_RXD_TOKEN_DATA", 2),#RXDC
            (aurix_model, "I_MCMCAN22_RXD_TOKEN_DATA", 0),#RXDA
            #My Node
            ("Ecu2Can2", "CAN_TOKEN_RX_DATA"),
            ]
            ),
        )

# tc39x --CAN1-- tc37xGW
# -------- TOKEN CTRL CONNECTIONS --------
# CAN1
for i in range(3):
    vlab.connect(
            (aurix_model, "O_MCMCAN1_TXD_TOKEN_CTRL",i),
            ("CAN1", "IN_TX_CTRL", i)
            )

vlab.connect(
        ("Tc39x", "CAN_TOKEN_TX_CTRL"),
        ("CAN1", "IN_TX_CTRL", 3)
        )

vlab.connect(
        ("CAN1", "OUT_RX_CTRL"),
        ([  #CAN1
            (aurix_model, "I_MCMCAN10_RXD_TOKEN_CTRL", 2),#RXDC
            (aurix_model, "I_MCMCAN11_RXD_TOKEN_CTRL", 2),#RXDC
            (aurix_model, "I_MCMCAN12_RXD_TOKEN_CTRL", 0),#RXDA
            #My Node
            ("Tc39x", "CAN_TOKEN_RX_CTRL"),
            ]
            ),
        )
# -------- TOKEN DATA CONNECTIONS --------
for i in range(3):
    vlab.connect(
            (aurix_model, "O_MCMCAN1_TXD_TOKEN_DATA",i),
            ("CAN1", "IN_TX_DATA", i)
            )

vlab.connect(
        ("Tc39x", "CAN_TOKEN_TX_DATA"),
        ("CAN1", "IN_TX_DATA", 3)
        )

vlab.connect(
        ("CAN1", "OUT_RX_DATA"),
        ([  #CAN1
            (aurix_model, "I_MCMCAN10_RXD_TOKEN_DATA", 2),#RXDC
            (aurix_model, "I_MCMCAN11_RXD_TOKEN_DATA", 2),#RXDC
            (aurix_model, "I_MCMCAN12_RXD_TOKEN_DATA", 0),#RXDA
            #My Node
            ("Tc39x", "CAN_TOKEN_RX_DATA"),
            ]
            ),
        )

# Change mcan engine
for mcan in range(3):
    for i in range(4):
        attribute_name = '{}.mcan{}{}.ENGINE'.format(aurix_model, mcan, i)
        vlab.write_attribute(attribute_name,  'token')
        
# --------------------
# | UART CONNECTIONS |
# --------------------
# Ecu2Can2 --> ECU2Term
vlab.connect(
        ("Ecu2Can2", 'UART_RX_CONTROL'),
        (ecu2_term, 'OUT_RX_CONTROL')
        )
vlab.connect(
        ("Ecu2Can2", 'UART_RX_DATA'),
        (ecu2_term, 'OUT_RX_DATA')
        )
vlab.connect(
        ("Ecu2Can2", 'UART_TX_CONTROL'),
        (ecu2_term, 'IN_TX_CONTROL')
        )
vlab.connect(
        ("Ecu2Can2", 'UART_TX_DATA'),
        (ecu2_term, 'IN_TX_DATA')
        )
vlab.connect(
        vlab.STUB,
        (ecu2_term, 'RX_DATA'),
        kind='buffer'
        )
vlab.connect(
        vlab.STUB,
        (ecu2_term, 'TX_DATA'),
        kind='buffer'
        )

# Tc39x --> Tc39xTerm
vlab.connect(
        ("Tc39x", 'UART_RX_CONTROL'),
        (tc39x_term, 'OUT_RX_CONTROL')
        )
vlab.connect(
        ("Tc39x", 'UART_RX_DATA'),
        (tc39x_term, 'OUT_RX_DATA')
        )
vlab.connect(
        ("Tc39x", 'UART_TX_CONTROL'),
        (tc39x_term, 'IN_TX_CONTROL')
        )
vlab.connect(
        ("Tc39x", 'UART_TX_DATA'),
        (tc39x_term, 'IN_TX_DATA')
        )
vlab.connect(
        vlab.STUB,
        (tc39x_term, 'RX_DATA'),
        kind='buffer'
        )

# --------------------
# | GETH CONNECTIONS |
# --------------------

vlab.connect((marvell_88Q5050, "TX", 8), (aurix_model, "I_GETH_RX"), kind="buffer")
vlab.connect((marvell_88Q5050, "RX", 8), (aurix_model, "O_GETH_TX"), kind="buffer")

vlab.connect((marvell_88Q5050, "TX", 1), (aurix_model, "I_GETH1_RX"), kind="buffer")
vlab.connect((marvell_88Q5050, "RX", 1), (aurix_model, "O_GETH1_TX"), kind="buffer")

vlab.connect((marvell_88Q5050, "TX", 2), ("Tc39x", "ETH_RX"), kind="buffer")
vlab.connect((marvell_88Q5050, "RX", 2), ("Tc39x", "ETH_TX"), kind="buffer")

vlab.connect((marvell_88Q5050, "TX", 3), ("Ecu2Can2", "ETH_RX"), kind="buffer")
vlab.connect((marvell_88Q5050, "RX", 3), ("Ecu2Can2", "ETH_TX"), kind="buffer")

vlab.connect(
        ('MDIO_bus_', 'MDIO_STA_out', 0),
        (aurix_model, 'I_MDIO_in'),
        kind='buffer'
        )
vlab.connect(
        ('MDIO_bus_', 'MDIO_STA_in', 0),
        (aurix_model, 'O_MDIO_out'),
        kind='buffer'
        )

vlab.connect(
        ('MDIO_bus_', 'MDIO_MMD_out', 1),
        (marvell_88Q5050, 'MDIO_in'),
        kind='buffer'
        )
vlab.connect(
        ('MDIO_bus_', 'MDIO_MMD_in', 1),
        (marvell_88Q5050, 'MDIO_out'),
        kind='buffer'
        )

vlab.stub()
