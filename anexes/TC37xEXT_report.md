# TC37EXT Vs TC37X

## Memory Map

AR = Access Range
AT = Access Type

### 2.3 Bus Fabric SRI
| TC37EXT |||||| TC37X ||||||
| ---- |----|----|----|----|----|----| ---- |----|----|----|----|
| AR from | AR to | Size | Unit | AT Read | AT Write | AR from | AR to | Size | Unit | AT Read | AT Write |
| 90408000H | 98FFFFFFH | - | Reserved | BE | BE | 90408000H | 97FFFFFFH | - | Reserved | BE | BE |
| 99000000H | 990FFFFFH | 1Mbyte | SRI slave interface 0 (access to EMEM module RAM, cached segment) (EMEMRAM0) | ok | ok | 98000000H | 98001FFFH | 8Kbyte | TRAM cached access via SRI (MINIMCDS) | ok | ok |
| 99100000H | 991FFFFFH | 1Mbyte | SRI slave interface 1 (access to EMEM module RAM, cached segment) (EMEMRAM1) | ok | ok | | | | | | |
| 99200000H | 992FFFFFH | 1Mbyte | SRI slave interface 2 (access to EMEM module RAM, cached segment) (EMEMRAM2) | ok | ok | | | | | | |
| 99300000H | 9FFFFFFFH | - | Reserved | BE | BE | 98002000H | 9FFFFFFFH | - | Reserved | BE | BE |
| B0408000H | B8FFFFFFH | - | Reserved | BE | BE | B0408000H | B7FFFFFFH | - | Reserved | BE | BE |
| B9000000H | B90FFFFFH | 1Mbyte | SRI slave interface 0 (access to EMEM module RAM, non-cached segment) (EMEMRAM0_NC) | ok | ok | B8000000H | B8001FFFH | 8Kbyte | TRAM non cached access via SRI (MINIMCDS) | ok | ok |
| B9100000H | B91FFFFFH | 1Mbyte | SRI slave interface 1 (access to EMEM module RAM, non-cached segment) (EMEMRAM1_NC) | ok | ok | | | | | | |
| B9200000H | B92FFFFFH | 1Mbyte | SRI slave interface 2 (access to EMEM module RAM, non-cached segment) (EMEMRAM2_NC) | ok | ok | | | | | | |
| B9300000H | B93FFFFFH | - | Reserved | BE | BE | | | | | | |
| B9400000H | B947FFFFH | 512Kbyte | Non-Cached XTM Ram addess range (SFIBRIDGE2) Bridge to Bus BBB (SFIBRIDGE2) | ok | ok | | | | | | |
| B9480000H | F801FFFFH | - | Reserved | BE | BE | B8002000H | F801FFFFH | - | Reserved | BE | BE |
| F8860000H | F9FFFFFFH | - | Reserved | BE | BE | F8860000H | FB717FFFH | - | Reserved | BE | BE |
| FA000000H | FAFFFFFFH | 16 Mbyte | Non-Cached XTM Ram address range (SFIBRIDGE2) | ok | ok | | | | | | |
| FB000000H	| FB00FFFFH | 64 Kbyte | EMEM RAM Interface Control Registers (EMEMMPU0) | ok | ok | | | | | | |
| FB010000H	| FB010000H | 64 Kbyte | EMEM RAM Interface Control Registers (EMEMMPU1) | ok | ok | | | | | | |
| FB020000H	| FB02FFFFH | 64 Kbyte | EMEM RAM Interface Control Registers (EMEMMPU2) | ok | ok | | | | | | |
| FB030000H | FB6FFFFFH | - | Reserved | BE | BE | | | | | | |
| FB700000H | FB70FFFFH | 64 Kbyte | sri slave interface (DOM2) | ok | ok | FB718000H | FB71FFFFH | 32 Kbyte | sri slave interface (MINIMCDS) | ok | ok |
| FB710000H | FFBFFFFFH | - | Reserved | BE | BE | FB720000H | FFBFFFFFH | - | Reserved | BE | BE |

### 2.4 Bus Instance SPB


| TC37EXT |||||| TC37X ||||||
| ---- |----|----|----|----|----|----| ---- |----|----|----|----|
| AR from | AR to | Size | Unit | AT Read | AT Write | AR from | AR to | Size | Unit | AT Read | AT Write |
| F0014000H | F0018FFFH | - | Reserved | BE | BE | F0014000H | F001BFFFH | - | Reserved | BE | BE |
| F0019000H	| F001B0FFH | 8.2 Kbyte | FPI bus interface (GETH1) FPI bus interface (GETH1) | ok | ok | | | | | | |
| F001B100H | F001BFFFH | - | Reserved | BE | BE | | | | | | |
| F0219000H | F021FFFFH | - | Reserved | BE | BE | F0219000H | F023FFFFH | - | Reserved | BE | BE |
| F0220000H	| F0228FFFH | 36 Kbyte | RAM Area (CAN2) Register Area (CAN2) | ok | ok | | | | | | |
| F0229000H | F0229000H | - | Reserved | BE | BE | | | | | | |
| F0248200H | F02AFFFFH | - | Reserved | BE | BE | F0248200H | F02C09FFH | - | Reserved | BE | BE |
| F02B0000H	| F02B0FFFH | 4 Kbyte | FPI slave interface (SDMMC0) | ok | ok | | | | | | |
| F02B1000H | F02C09FFH | - | Reserved | BE | BE | | | | | | |
| F02B1000H | F02C09FFH | - | Reserved | BE | BE | | | | | | |

### 2.5 Bus Instance BBB

| TC37EXT |||||| TC37X ||||||
| ---- |----|----|----|----|----|----| ---- |----|----|----|----|
| 00000000H | 98FFFFFFH | - | Reserved | BE | BE | | | | | | |
| 99000000H	| 990FFFFFH | 1 Mbyte |  BBB slave interface 0 (access to EMEM module RAM, cached segment) (EMEMRAM0) | ok | ok | | | | | | |
| 99100000H	| 991FFFFFH | 1 Mbyte |  BBB slave interface 1 (access to EMEM module RAM, cached segment) (EMEMRAM1) | ok | ok | | | | | | |
| 99200000H	| 992FFFFFH | 1 Mbyte |  BBB slave interface 2 (access to EMEM module RAM, cached segment) (EMEMRAM2) | ok | ok | | | | | | |
| 99300000H | B8FFFFFFH | - | Reserved | BE | BE | | | | | | |
| B9000000H	| B90FFFFFH | 1 Mbyte |  BBB slave interface 0 (access to EMEM module RAM, non-cached segment) (EMEMRAM0_NC) | ok | ok | | | | | | |
| B9100000H	| B91FFFFFH | 1 Mbyte |  BBB slave interface 1 (access to EMEM module RAM, non-cached segment) (EMEMRAM1_NC) | ok | ok | | | | | | |
| B9200000H	| B92FFFFFH | 1 Mbyte |  BBB slave interface 2 (access to EMEM module RAM, non-cached segment) (EMEMRAM2_NC) | ok | ok | | | | | | |
| B9300000H | B93FFFFFH | - | Reserved | BE | BE | | | | | | |
| B9400000H	| B947FFFFH | 512 Kbyte | XTM FPI slave interface (XTM) | ok | ok | | | | | | |
| B9480000H | EFFFFFFFH | - | Reserved | BE | BE | | | | | | |
| F0000000H | FA0000FFH | - | Reserved | BE | BE | | | | | | |
| FA000100H	| FA0001FFH | 256 byte | BCU Registers (EBCU) | ok | ok | | | | | | |
| FA000200H | FA000FFFH | - | Reserved | BE | BE | | | | | | |
| FA001000H	| FA0010FFH | 256 byte | FPI slave interface (AGBT) | ok | ok | | | | | | |
| FA001100H | FA001EFFH | - | Reserved | BE | BE | | | | | | |
| FA001F00H	| FA005FFFH | 16.2 Kbyte | FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) FPI slave interface (CIF) | ok | ok | | | | | | |
| FA006000H	| FA0060FFH | 256 byte | BUS SFF (access to EMEM core resgisters) (EMEM) | ok | ok | | | | | | |
| FA006100H | FA00FFFFH | - | Reserved | BE | BE | | | | | | |
| FA010000H	| FA01FFFFH | 64 Kbyte | FPI slave interface (MCDS) | ok | ok | | | | | | |
| FA020000H | FFFFFFFFH | - | Reserved | BE | BE | | | | | | |

## 3 Firmware

### 3.1 Checker software  exit inforamtion by CHSW for microcontroller
"ALL CHECKS PASSED" indication by CHSW for microcontroller

| Reset Type | TC37EXT ||||| TC37X ||||||
| ---- |----|----|----|----|----|----| ---- |----|----|----|----|
|| Additional conditions | SCU_STMEM3 | SCU_STMEM4 | SCU_STMEMS5 | SCU_STMEM6 | Additional conditions | SCU_STMEM3 | SCU_STMEM4 | SCU_STMEMS5 | SCU_STMEM6 |
| Cold power-on | - | A133FB1FH | 00000001H | A133FB1FH | A133FB1FH | - | A030FB1FH | 00000001H | A030FB1FH | A030FB1FH |
| Warm power-on | - | A123F82FH | 00000001H | A123F82FH | A123F82FH | - | A020F82FH | 00000001H | A020F82FH | A020F82FH |
| System Reset | - | 2120B84FH | 00000001H | 2120B84FH | 2120B84FH | - | 2020B84FH | 00000001H | 2020B84FH | 2020B84FH |
| Application Reset | CCUCON5.GETHDIV<>0 CCUCON5.GETHDIV=0 | 2120088FH | 01200001H | 2000088FH | 2120088FH | CCUCON5.GETHDIV<>0 CCUCON5.GETHDIV=0  | 2020088FH | 00200001H | 2000088FH | 2020088FH |

## 4. On system connectivity and bridges
### 4.1 Specific Ip configuration
TC37EXT has `DOM2` interface. Its parameters are exactly the same of `DOM0` except for `OLDA base address1`, `OLDA range`, `OLDA base address (non-cached)` and `OLDA range (non-cached)` which has no values for DOM2.
### 4.2 Register set
TC37EXT has extra resgister set for  DOM2

| Base Address | End Address | Note |
| ---- | ---- | ---- |
| FB700000H | FB70FFFFH | sri slave interface |

Register overview of `DOM2` has the same values of DOM0 but their names changes, for instance, `DOM0_PECONx` is changed to `DOM2_PECONx`. Offset addresses and access modes are the same as `DOM0`.
Domain 2 control register ( 00430h ) Application Reset Value = 0000 0000h

| 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 09 | 08 | 07 | 06 | 05 | 04 | 03 | 02 | 01 | 00 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |


| Field | Bit | Type | Description |
| ---- | ---- | ---- | ---- |
| 0 | 31:0 | r | reserved; Read as 0; Shall be written with 0 |

### 4.5.1 DOM0 Interconnection Matrix
Matrix interconnection is basically the same but TC37EXT adds a `GETH1` port and changes the port `Mini MCDS` present in TC37x for `S2S1 D0D2` and `S2S0 D0D2`.

||| S2S0 D0D2 | S2S1 D0D2 |
| ---- | ---- | ---- | ---- |
| | | SCI12 | SCI13 |
| DMA MIFO | MCI0 | r/w | x |
| SFI F2S | MCI1 | r/w | x |
| CPU0 | MCI2 | r/w | x |
| CPU1 | MCI3 | r/w | x |
| CPU2 | MCI4 | x | r/w |
| HSSL0 | MCI8 | x | r/w |
| GETH | MCI9 | x | r/w |
| GETH1 | MCI12 | r/w | x |

### 4.5.2 DOM2 Interconnection Matrix

||| EMEM2 | EMEM1 | EMEM0 | SFI_S2F BBB | Default Slave |
| ---- | ---- | ---- | ---- |  ---- | ---- | ---- |
||| SCI4 | SCI3 | SCI2 | SCI1 | SCI0 |
| S2S0 DOD2 | MCI0 | r/w | r/w | r/w | r/w | r/w |
| S2S1 DOD2 | MCI1 | r/w | r/w | r/w | r/w | r/w |
| DMA MIF1 | MCI3 | r/w | x | r/w | x | r/w |
| DMA MIF2 | MCI4 | r/w | x | x | r/w | x |

### 4.7 FPI Bus Control Units 
TC37EXT has an aditional EBCU Unit instead of TC37X which has only the SBCU. SBCU registers space are the same in both microcontrollers, here the table of EBCU.

| Module | Base Address | End Address | Note |
| ---- | ---- | ---- | ---- |
| (EBCU) | F0000000H | FFFFFFFFH | FPI default slave |
| EBCU | FA000100H | FA0001FFH | BCU Registers |
| (SBCU) | F0000000H | F7FFFFFFH | FPI default slave |
| SBCU | F0030000H | F00300FFH | BCU Registers |

### SBCU Control Unit Registers

Some registers like `SBCU_PRIOL`, `SBCU_DBGRNT` and `SBCU_DBGRNT` has bits named differently.

### EBCU Control Unit Registers

Registers for EBCU have the same offset but they work differently. Read the [TC37Ext user manual](https://www.infineon.com/dgdl/Infineon-AURIX_TC37xEXT-UserManual-v02_00-EN.pdf?fileId=5546d4627506bb32017527203f913b3d) (p48 - 58) to have more information.

### Connectivity
SBUC has the same connection in both microcontrollers. But TC37EXT has the connectivity of EBCU, shown below.

| Interface Signals | connects | Description |
| ---- | ---- | ---- |
| EBCU:INT | to  INT:bbbcu_INT | Bus Control Unit BBB Service Request

### LIBST

The `LBIST` function can be controlled via four registers at SCU level. Their configs changes between microcontrollers, please read documentation for this.

## System control Unit

According to documentation, TC37EXT do not have the register `SCU_LCLCON0` (p 120)

## Power management

SRAMs with Address ECC
On this device (TC37EXT), in the EMEM0-2 SRAMs, the ECC is calculated over the data as well as the address. This means, that
for the same data word at different addresses, the corresponding ECC value will be different.
For these SRAMs/SSHs, initializing the SRAM with ECC correct data using MCONTROL.DINIT is not supported. The
SRAMs can be still completely initialized via the MCONTROL.SRAM_CLR bit (Refer platform specification chapter
on Filling a Memory with Defined Contents).

## Memory Test Unit

Registers `MTU_MEMTEST1`, `MTU_MEMTEST2`, `MTU_MEMDONE1`, `MTU_MEMDONE2`, `MTU_MEMFDA1` and `MTU_MEMFDA2` within TC37EXT, have some bits that are named differently. More info in the doc p.155

There are some new elements in table `SSH instances`.

Ganging for SRAM tables changes as well.

## 14. GPIO

`P22_IOCR12`, `P22_OMCR12`, do not exist in TC37X. p22 does not work the same way in TC37EXT, some of its registers are different. `P22_PCSR` and `P23_PCSR` works differently.

## 15. Safety management Unit
 
Alarm Configurator Registers (`SMU_AGiCFj`), Alarm Status Registers (`SMU_AGi`), Alarm Debug Registers (`SMU_ADi`), has some bits named differently. 

MTU Pre-Alarm Mapping changes also, some errors do not appear in both microcontrollers.

Alarm Mapping related to ALM0, ALM1 group has different module names.

## 16. Interupt Router (IR)

TC37EXT adds some new register to the Interrupt Router.


| Short Name | Long Name | Offset Address | Access Mode Read | Access Mode Write | Reset |
| ---- | ---- | ---- | ---- | ---- | ---- |
| SRC_BCUBBB | EBCU Service Request (BBB Bus control Unit, on ED and ADAS devices only) | 00024H | U, SV | SV, P1, P2| Debug, Reset |
| SRC_AGBT | AGBT Service Request (on ED devices only) | 0002CH | U, SV | SV, P1, P2| Debug, Reset |
| SRC_XBAR2 | SRI Domain 2 Service Request | 00038H | U, SV | SV, P1, P2| Debug, Reset |
| SRC_GETH1y (y=0-9) | GETH1 Service Request y | 001D4H + y\*4 | U, SV | SV, P1, P2| Application, Reset |
| SRC_CANxINTy (x=0-2;y=0-15) | CANx Service Request y | 0x5B0+ x\* 40H+ y\* 4 | U, SV | SV, P1, P2| Application, Reset |
| SRC_SDMMCERR | SDMCC Error Service Request | 00570H | U, SV | SV, P1, P2| Application, Reset |
| SRC_SDMMCDNA | SDMCC DMA Error Service Request | 00574H | U, SV | SV, P1, P2| Application, Reset |
| SRC_CIFMI | CIF MI Service Request | 00940H | U, SV | SV, P1, P2| Application, Reset |
| SRC_CIFMIEP | CIF MI EP Service Request | 00944H | U, SV | SV, P1, P2| Application, Reset |
| SRC_CIFISP | CIF ISP Service Request | 00948H | U, SV | SV, P1, P2| Application, Reset |
| SRC_CIFMJPEG | CIF MJPEG Service Request | 0094CH | U, SV | SV, P1, P2| Application, Reset |

## 21. Extended Memory (EMEM)

The whole Extended Memory (EMEM) is only present in TC37EXT.

## 24. Camera Interface (CIF)

Camera Interface module is only present in TC37EXT

## 25. System Timer (STM)

In TC37EXT booth timer have additional connections to the extra CAN bus included on the extended version.

## 38. Can Interface (MCMCAN)

TC37EXT has an additional CAN interface.

| Module | Base Address | End Address | Note |
| ---- | ---- | ---- | ---- |
| CAN2 | F0220000H | F0228FFFH | Bus Interface |

Register overview

| Short Name | Long Name | Offset Address | 
| ---- | ---- | ---- |
| CAN2_RAM | Embedded SRAM for messages (004000H Byte) | 000000H |
| CAN2_CLC | Can Clock Register | 008000H |
| CAN2_ID | Module Identification Register | 008008H |
| CAN2_MCR | Module Control Register | 008030H |
| CAN2_ACCENCTR0 | Access Enable Register Control 0 | 0080DCH |
| CAN2_OCS | OCDS Control and Status | 0080E8H |
| CAN2_KRSTCLR | Kernel Status Clear Register | 0080ECH |
| CAN2_KRST1 | Kernel Reset Register 1 | 0080F0H |
| CAN2_KRST0 | Kernel Reset Register 0 | 0080F4H |
| CAN2_ACCEN0 | Access Enable Register 0 | 0080FCH |
| CAN2_ACCENNODEi0 (i=0-3) | Acces Enable Register Can Node i 0 | 008100H + i\* 400H |
| CAN2_STARTADRi (i=0-3) | Start Address Node i | 008108H + i\*400H |
| CAN2_ENDADRi (i=0-3) | End Address Node i | 00810CF + i\* 400H |
| CAN2_ISREGi (i=0-3) | Interrupt signalling Register i | 008110H + i\* 400H |
| CAN2_GRINT1i (i=0-3) | Interrupt routing for Groups 1 i | 008114H + i\* 400H |
| CAN2_GRINT2i (i=0-3) | Interrupt routing for Groups 2 i | 008118H + i\* 400H |
| CAN2_NTCCRi (i=0-3) | Node i Timer Clock Control Register | 008120H + i\* 400H |
| CAN2_NTATTRi (i=0-3) | Node i Timer A Transmit Trigger Register | 008124H + i\* 400H |
| CAN2_NTBTTRi (i=0-3) | Node i Timer B Transmit Trigger Register | 008128H + i\* 400H |
| CAN2_NTCTTRi (i=0-3) | Node i Timer C Transmit Trigger Register | 00812CH + i\* 400H |
| CAN2_NTRTRi (i=0-3) | Node i Timer Receive Timeout Register | 008130H + i\* 400H |
| CAN2_CRELi (i=0-3) | Core Release Register i | 008200H + i\* 400H |
| CAN2_ENDNi (i=0-3) | Endian Register i | 008204H + i\* 400H |
| CAN2_DBTPi (i=0-3) | Data Bit Timing & Prescaler Register i  | 00820cH + i\* 400H |
| CAN2_TESTi (i=0-3) | Test Register i  | 008210H + i\* 400H |
| CAN2_RWDi (i=0-3) | RAM Watchdog i  | 008214H + i\* 400H |
| CAN2_CCCRi (i=0-3) | CC Control Register i  | 008218H + i\* 400H |
| CAN2_NBTPi (i=0-3) | Nominal Bit Timing & Prescaler Register i  | 00821CH + i\* 400H |
| CAN2_TSCCi (i=0-3) | Timestamp Counter Configuration i  | 008220H + i\* 400H |
| CAN2_TSCVi (i=0-3) | Timestamp Counter Value i  | 008224H + i\* 400H |
| CAN2_TOCCi (i=0-3) | Timeout Counter Configuration i | 008228H + i\* 400H |
| CAN2_TOCVi (i=0-3) | Timeout Counter Value i | 00822cH + i\* 400H |
| CAN2_ECRi (i=0-3) | Error Counter Register i | 008240H + i\* 400H |
| CAN2_PSRi (i=0-3) | Protocol Status Register i | 008244H + i\* 400H |
| CAN2_TDCRi (i=0-3) | Transmitter Delay Compensation Register i | 008248H + i\* 400H |
| CAN2_IRi (i=0-3) | Interrupt Register i | 008250H + i\* 400H |
| CAN2_IEi (i=0-3) | Interrupt Enable i | 008254H + i\* 400H |
| CAN2_GFCi (i=0-3) | Global Filter Configuration i | 008280H + i\* 400H |
| CAN2_SIDFCi (i=0-3) | Standard ID Filter Configuration i | 008284H + i\* 400H |
| CAN2_XIDFCi (i=0-3) | Extended ID Filter Configuration i | 008288H + i\* 400H |
| CAN2_XIDAMi (i=0-3) | Extended ID AND Mask i | 008290H + i\* 400H |
| CAN2_HPMSi (i=0-3) | High Priority Message Status i | 008294H + i\* 400H |
| CAN2_NDAT1i (i=0-3) | New Data 1 i | 008298H + i\* 400H |
| CAN2_NDAT2i (i=0-3) | New Data 2 i | 00829CH + i\* 400H |
| CAN2_RXF0Ci (i=0-3) | Rx FIFO 0 Configuration i | 0082A0H + i\* 400H |
| CAN2_RXF0Si (i=0-3) | Rx FIFO 0 Status i | 0082A4H + i\* 400H |
| CAN2_RXF0Ai (i=0-3) | Rx FIFO 0 Acknowledge i | 0082A8H + i\* 400H |
| CAN2_RXBCi (i=0-3) | Rx Buffer Configuration i | 0082ACH + i\* 400H |
| CAN2_RXF1Ci (i=0-3) | Rx FIFO 1 Configuration i  | 0082B0H + i\* 400H |
| CAN2_RXF1Si (i=0-3) | Rx FIFO 1 Status i | 0082B4H + i\* 400H |
| CAN2_RXF1Ai (i=0-3) | Rx FIFO 1 Acknowledge i | 0082B8H + i\* 400H |
| CAN2_RXESCi (i=0-3) | Rx Buffer/FIFO Element Size Configuration i | 0082BCH + i\* 400H |
| CAN2_TXBCi (i=0-3) | Tx Buffer Configuration i | 0082C0H + i\* 400H |
| CAN2_TXFQSi (i=0-3) | Tx FIFO/Queue Status i | 0082C4H + i\* 400H |
| CAN2_TXESCi (i=0-3) | Tx Buffer Element Size Configuration i | 0082C8H + i\* 400H |
| CAN2_TXBRPi (i=0-3) | Tx Buffer Request Pending i | 0082CCH + i\* 400H |
| CAN2_TXBARi (i=0-3) | Tx Buffer Add Request i | 0082D0H + i\* 400H |
| CAN2_TXBCRi (i=0-3) | Tx Buffer Cancellation Request i | 0082D4H + i\* 400H |
| CAN2_TXBTOi (i=0-3) | Tx Buffer Transmission Occurred i| 0082D8H + i\* 400H |
| CAN2_TXBCFi (i=0-3) | Tx Buffer Cancellation Finished i | 0082DCH + i\* 400H |
| CAN2_TXBTIEi (i=0-3) | Tx Buffer Transmission Interrupt Enable i | 0082E0H + i\* 400H |
| CAN2_TXBCIEi (i=0-3) | Tx Buffer Cancellation Finished Interrupt Enable i | 0082E4H + i\* 400H |
| CAN2_TXEFCi (i=0-3) | Tx Event FIFO Configuration i | 0082F0H + i\* 400H |
| CAN2_TXEFSi (i=0-3) | Tx Event FIFO Status i | 0082F4H + i\* 400H |
| CAN2_TXEFAi (i=0-3) | Tx Event FIFO Acknowledge i | 0082F8H + i\* 400H |

## 42. Gigabit Ethernet MAC (GETH)

TC37EXT has an additional ethernet interface.

| Module | Base Address | End Address | Note |
| ---- | ---- | ---- | ---- |
| GETH1 | F0019000H | F001B0FFH | FPI Bus Interface |

Master TAG ID for `GETH1`

| GETH1_DMA | Master TAG ID |
| ---- | ---- | 
| DMA0 | 0x2CH |
| DMA1 | 0x2DH |
| DMA2 | 0x2EH |
| DMA3 | 0x2FH |

There are new interruptions for the new interface.

| IR SRC | GETH1 IP signal | GETH1 IP function | Description |
| ---- | ---- | ---- | ---- |                            
| SRC_GETH10 |GETH1_TRIGO0 | GETH1_INTR | DMA functions (sbd_intr_o), this internal line is connected via OR gate to GETH1.SR0 wake up on LAN (pmt_intr_o), this internal line is connected via OR gate to GETH1.SR0 wake up on EEE - LPI (lpi_intr_o), this internal line is connected via OR gate to GETH1.SR0 |
| SRC_GETH11 | GETH1_TRIGO1 | GETH1_PPS | Pulse Per Second signal from Precision Time Protocol (ptp_pps_o) |
| SRC_GETH12 | GETH1_TRIGO2 | GETH1_TX_DMA0 | TX interrupt from DMA 0 (sbd_perch_tx_intr_o[0]) |
| SRC_GETH13 | GETH1_TRIGO3 | GETH1_TX_DMA1 | TX interrupt from DMA 1(sbd_perch_tx_intr_o[1]) |
| SRC_GETH14 | GETH1_TRIGO4 | GETH1_TX_DMA2 | TX interrupt from DMA 2(sbd_perch_tx_intr_o[2]) |
| SRC_GETH15 | GETH1_TRIGO4 | GETH1_TX_DMA3 | TX interrupt from DMA 3(sbd_perch_tx_intr_o[3]) |
| SRC_GETH16 | GETH1_TRIGO6 | GETH1_RX_DMA0 | RX interrupt from DMA 0 (sbd_perch_rx_intr_o[0]) |
| SRC_GETH17 | GETH1_TRIGO7 | GETH1_RX_DMA1 | RX interrupt from DMA 1(sbd_perch_rx_intr_o[1]) |
| SRC_GETH18 | GETH1_TRIGO8 | GETH1_RX_DMA2 | RX interrupt from DMA 2(sbd_perch_rx_intr_o[2]) |
| SRC_GETH19 | GETH1_TRIGO9 | GETH1_RX_DMA3 | RX interrupt from DMA 3(sbd_perch_rx_intr_o[3]) |

## 44. SD- and eMMC Interface (SDMMC)

SDMMC interface is only present in TC37EXT.