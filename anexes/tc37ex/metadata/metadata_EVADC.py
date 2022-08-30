import vlab
from vlab import *

vlab.properties(name="IfxEvadcWrapper", kind="leaf")
evadcTargetSocket = vlab.bus("evadc", kind="target", width=32)
    
r = register('CLC', width=32, block=evadcTargetSocket, offset=0x0000,
             access='read-only', reset=0x00000003,
             doc='Clock Control Register')
field(name='DISR', register=r, offset=0, width=1, access='read-write',
      doc='Module Disable Request Bit')
field(name='DISS', register=r, offset=1, width=1, access='read-only',
      doc='Module Disable Status Bit')
field(name='EDIS', register=r, offset=3, width=1, access='read-write',
      doc='Sleep Mode Enable Control')

r = register('ID', width=32, block=evadcTargetSocket, offset=0x0008,
             access='read-only', reset=0x00C5C013,
             doc='Module Identification Register')
field(name='MOD_REV', register=r, offset=0, width=8, access='read-only',
      doc='Module Revision')
field(name='MOD_TYPE', register=r, offset=8, width=8, access='read-only',
      doc='Module Type')
field(name='MOD_NUMBER', register=r, offset=16, width=16, access='read-only',
      doc='Module Number')

r = register('OCS', width=32, block=evadcTargetSocket, offset=0x0028,
             access='read-only', reset=0x00000000,
             doc='OCDS Control and Status Register')
field(name='TGS', register=r, offset=0, width=2, access='read-write',
      doc='Trigger Set for OTGB0/1')
field(name='TGB', register=r, offset=2, width=1, access='read-write',
      doc='OTGB0/1 Bus Select')
field(name='TG_P', register=r, offset=3, width=1, access='write-only',
      doc='TGS, TGB Write Protection')
field(name='SUS', register=r, offset=24, width=4, access='read-write',
      doc='OCDS Suspend Control')
field(name='SUS_P', register=r, offset=28, width=1, access='write-only',
      doc='SUS Write Protection')
field(name='SUSSTA', register=r, offset=29, width=1, access='read-only',
      doc='Suspend State')

r = register('KRSTCLR', width=32, block=evadcTargetSocket, offset=0x002c,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Status Clear Register')
field(name='CLR', register=r, offset=0, width=1, access='write-only',
      doc='Kernel Reset Status Clear')

r = register('KRST1', width=32, block=evadcTargetSocket, offset=0x0030,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Register 1')
field(name='RST', register=r, offset=0, width=1, access='read-write',
      doc='Kernel Reset')

r = register('KRST0', width=32, block=evadcTargetSocket, offset=0x0034,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Register 0')
field(name='RST', register=r, offset=0, width=1, access='read-write',
      doc='Kernel Reset')
field(name='RSTSTAT', register=r, offset=1, width=1, access='read-only',
      doc='Kernel Reset Status')

r = register('ACCEN0', width=32, block=evadcTargetSocket, offset=0x003c,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable Register 0')
field(name='EN0', register=r, offset=0, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 0')
field(name='EN1', register=r, offset=1, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 1')
field(name='EN2', register=r, offset=2, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 2')
field(name='EN3', register=r, offset=3, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 3')
field(name='EN4', register=r, offset=4, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 4')
field(name='EN5', register=r, offset=5, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 5')
field(name='EN6', register=r, offset=6, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 6')
field(name='EN7', register=r, offset=7, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 7')
field(name='EN8', register=r, offset=8, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 8')
field(name='EN9', register=r, offset=9, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 9')
field(name='EN10', register=r, offset=10, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 10')
field(name='EN11', register=r, offset=11, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 11')
field(name='EN12', register=r, offset=12, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 12')
field(name='EN13', register=r, offset=13, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 13')
field(name='EN14', register=r, offset=14, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 14')
field(name='EN15', register=r, offset=15, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 15')
field(name='EN16', register=r, offset=16, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 16')
field(name='EN17', register=r, offset=17, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 17')
field(name='EN18', register=r, offset=18, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 18')
field(name='EN19', register=r, offset=19, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 19')
field(name='EN20', register=r, offset=20, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 20')
field(name='EN21', register=r, offset=21, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 21')
field(name='EN22', register=r, offset=22, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 22')
field(name='EN23', register=r, offset=23, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 23')
field(name='EN24', register=r, offset=24, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 24')
field(name='EN25', register=r, offset=25, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 25')
field(name='EN26', register=r, offset=26, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 26')
field(name='EN27', register=r, offset=27, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 27')
field(name='EN28', register=r, offset=28, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 28')
field(name='EN29', register=r, offset=29, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 29')
field(name='EN30', register=r, offset=30, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 30')
field(name='EN31', register=r, offset=31, width=1, access='read-write',
      doc='Access Enable for Master TAG ID 31')

r = register('GLOBCFG', width=32, block=evadcTargetSocket, offset=0x0080,
             access='read-only', reset=0x00000000,
             doc='Global Configuration Register')
field(name='USC', register=r, offset=12, width=1, access='read-write',
      doc='Unsynchronized Clock Generation')
field(name='SUPLEV', register=r, offset=13, width=2, access='read-write',
      doc='Supply Voltage Level')
field(name='CPWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Control Parameters')
field(name='SUCAL', register=r, offset=31, width=1, access='write-only',
      doc='Start-Up Calibration')

r = register('ACCPROT0', width=32, block=evadcTargetSocket, offset=0x0088,
             access='read-only', reset=0x00000000,
             doc='Access Protection Register 0')
field(name='APCP', register=r, offset=0, width=4, access='read-write',
      doc='Access Protection Channel Control, Primary Groups')
field(name='APCS', register=r, offset=8, width=4, access='read-write',
      doc='Access Protection Channel Control, Secondary Groups')
field(name='APIP', register=r, offset=16, width=4, access='read-write',
      doc='Access Protection Initialization, Primary Groups')
field(name='APIS', register=r, offset=24, width=4, access='read-write',
      doc='Access Protection Initialization, Secondary Groups')

r = register('ACCPROT1', width=32, block=evadcTargetSocket, offset=0x008c,
             access='read-only', reset=0x00000000,
             doc='Access Protection Register 1')
field(name='APSP', register=r, offset=0, width=4, access='read-write',
      doc='Access Protection Service Request, Primary Groups')
field(name='APSS', register=r, offset=8, width=4, access='read-write',
      doc='Access Protection Service Request, Secondary Groups')
field(name='APRP', register=r, offset=16, width=4, access='read-write',
      doc='Access Protection Result Registers, Primary Groups')
field(name='APRS', register=r, offset=24, width=4, access='read-write',
      doc='Access Protection Result Registers, Secondary Groups')

r = register('ACCPROT2', width=32, block=evadcTargetSocket, offset=0x0090,
             access='read-only', reset=0x00000000,
             doc='Access Protection Register 2')
field(name='APF', register=r, offset=0, width=4, access='read-write',
      doc='Access Protection Fast Compare Channels')
field(name='APGC', register=r, offset=16, width=1, access='read-write',
      doc='Access Protection Global Configuration')
field(name='APEM', register=r, offset=17, width=1, access='read-write',
      doc='Access Protection External Multiplexer')
field(name='APTF', register=r, offset=18, width=1, access='read-write',
      doc='Access Protection Test Function')

r = register('GLOBICLASS0', width=32, block=evadcTargetSocket, offset=0x00a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Global')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('GLOBICLASS1', width=32, block=evadcTargetSocket, offset=0x00a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Global')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('GLOBBOUND', width=32, block=evadcTargetSocket, offset=0x00b8,
             access='read-only', reset=0x00000000,
             doc='Global Boundary Select Register')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('GLOBEFLAG', width=32, block=evadcTargetSocket, offset=0x00e0,
             access='read-only', reset=0x00000000,
             doc='Global Event Flag Register')
field(name='REVGLB', register=r, offset=8, width=1, access='read-write',
      doc='Global Result Event')
field(name='REVGLBCLR', register=r, offset=24, width=1, access='write-only',
      doc='Clear Global Result Event')

r = register('GLOBEVNP', width=32, block=evadcTargetSocket, offset=0x0140,
             access='read-only', reset=0x00000000,
             doc='Global Event Node Pointer Register')
field(name='REV0NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Global Result')

r = register('GLOBTF', width=32, block=evadcTargetSocket, offset=0x0160,
             access='read-only', reset=0x00000000,
             doc='Global Test Functions Register')
field(name='CDCH', register=r, offset=0, width=4, access='read-write',
      doc='Conversion Diagnostics Channel')
field(name='CDGR', register=r, offset=4, width=4, access='read-write',
      doc='Conversion Diagnostics Group')
field(name='CDEN', register=r, offset=8, width=1, access='read-write',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=9, width=2, access='read-write',
      doc='Converter Diagnostics Pull-Devices Select')
field(name='CDWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Conversion Diagnostics')
field(name='PDD', register=r, offset=16, width=1, access='read-write',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=17, width=1, access='read-write',
      doc='Multiplexer Diagnostics Pull-Down-Devices Enable')
field(name='MDPU', register=r, offset=18, width=1, access='read-write',
      doc='Multiplexer Diagnostics Pull-Up-Devices Enable')
field(name='MDWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Multiplexer Diagnostics')

r = register('GLOBTE', width=32, block=evadcTargetSocket, offset=0x0164,
             access='read-only', reset=0x00000000,
             doc='Global Test Enable Register')
field(name='TFEP', register=r, offset=0, width=4, access='read-write',
      doc='Test Function Enable, Primary Groups')
field(name='TFES', register=r, offset=8, width=4, access='read-write',
      doc='Test Function Enable, Secondary Groups')

r = register('GLOBRCR', width=32, block=evadcTargetSocket, offset=0x0280,
             access='read-only', reset=0x00000000,
             doc='Global Result Control Register')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('GLOBRES', width=32, block=evadcTargetSocket, offset=0x0300,
             access='read-only', reset=0x00000000,
             doc='Global Result Register')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of most recent conversion')
field(name='GNR', register=r, offset=16, width=4, access='read-only',
      doc='Group Number')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-write',
      doc='Valid Flag')

r = register('GLOBRESD', width=32, block=evadcTargetSocket, offset=0x0380,
             access='read-only', reset=0x00000000,
             doc='Global Result Register, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of most recent conversion')
field(name='GNR', register=r, offset=16, width=4, access='read-only',
      doc='Group Number')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('EMUXSEL', width=32, block=evadcTargetSocket, offset=0x03f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Interface Select Register')
field(name='EMUXGRP0', register=r, offset=0, width=4, access='read-write',
      doc='External Multiplexer Group for Interface 0')
field(name='EMUXGRP1', register=r, offset=4, width=4, access='read-write',
      doc='External Multiplexer Group for Interface 1')

r = register('G0TRCTR', width=32, block=evadcTargetSocket, offset=0x0410,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 0')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G1TRCTR', width=32, block=evadcTargetSocket, offset=0x0810,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 1')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G2TRCTR', width=32, block=evadcTargetSocket, offset=0x0c10,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 2')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G3TRCTR', width=32, block=evadcTargetSocket, offset=0x1010,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 3')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G8TRCTR', width=32, block=evadcTargetSocket, offset=0x2410,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 8')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G9TRCTR', width=32, block=evadcTargetSocket, offset=0x2810,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 9')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G10TRCTR', width=32, block=evadcTargetSocket, offset=0x2c10,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 10')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G11TRCTR', width=32, block=evadcTargetSocket, offset=0x3010,
             access='read-only', reset=0x00000000,
             doc='Trigger Control Register, Group 11')
field(name='TSC', register=r, offset=0, width=6, access='read-only',
      doc='Trigger Sequence Counter')
field(name='QACT', register=r, offset=14, width=1, access='read-only',
      doc='Queue Active')
field(name='OV', register=r, offset=15, width=1, access='read-only',
      doc='Overflow Detected')
field(name='TSCSET', register=r, offset=16, width=6, access='read-write',
      doc='Trigger Sequence Counter Start Value')
field(name='ITSEL', register=r, offset=24, width=2, access='read-write',
      doc='Internal Trigger Input Selection')
field(name='SRDIS', register=r, offset=28, width=1, access='read-write',
      doc='Service Request Disable')
field(name='COV', register=r, offset=31, width=1, access='write-only',
      doc='Clear Overflow Flag')

r = register('G0ARBCFG', width=32, block=evadcTargetSocket, offset=0x0480,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 0')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G1ARBCFG', width=32, block=evadcTargetSocket, offset=0x0880,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 1')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G2ARBCFG', width=32, block=evadcTargetSocket, offset=0x0c80,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 2')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G3ARBCFG', width=32, block=evadcTargetSocket, offset=0x1080,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 3')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G8ARBCFG', width=32, block=evadcTargetSocket, offset=0x2480,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 8')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G9ARBCFG', width=32, block=evadcTargetSocket, offset=0x2880,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 9')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G10ARBCFG', width=32, block=evadcTargetSocket, offset=0x2c80,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 10')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G11ARBCFG', width=32, block=evadcTargetSocket, offset=0x3080,
             access='read-only', reset=0x00000000,
             doc='Arbitration Config. Register, Group 11')
field(name='ANONC', register=r, offset=0, width=2, access='read-write',
      doc='Analog Converter Control')
field(name='ANONS', register=r, offset=16, width=2, access='read-only',
      doc='Analog Converter Control Status')
field(name='CSRC', register=r, offset=18, width=2, access='read-only',
      doc='Currently Converted Request Source')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='SYNRUN', register=r, offset=25, width=1, access='read-only',
      doc='Synchronous Conversion Running')
field(name='CAL', register=r, offset=28, width=1, access='read-only',
      doc='Start-Up Calibration Active Indication')
field(name='BUSY', register=r, offset=30, width=1, access='read-only',
      doc='Converter Busy Flag')
field(name='SAMPLE', register=r, offset=31, width=1, access='read-only',
      doc='Sample Phase Flag')

r = register('G0ARBPR', width=32, block=evadcTargetSocket, offset=0x0484,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 0')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G1ARBPR', width=32, block=evadcTargetSocket, offset=0x0884,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 1')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G2ARBPR', width=32, block=evadcTargetSocket, offset=0x0c84,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 2')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G3ARBPR', width=32, block=evadcTargetSocket, offset=0x1084,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 3')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G8ARBPR', width=32, block=evadcTargetSocket, offset=0x2484,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 8')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G9ARBPR', width=32, block=evadcTargetSocket, offset=0x2884,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 9')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G10ARBPR', width=32, block=evadcTargetSocket, offset=0x2c84,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 10')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G11ARBPR', width=32, block=evadcTargetSocket, offset=0x3084,
             access='read-only', reset=0x00000000,
             doc='Arbitration Priority Register, Group 11')
field(name='PRIO0', register=r, offset=0, width=2, access='read-write',
      doc='Priority of Request Source 0')
field(name='PRIO1', register=r, offset=4, width=2, access='read-write',
      doc='Priority of Request Source 1')
field(name='PRIO2', register=r, offset=8, width=2, access='read-write',
      doc='Priority of Request Source 2')
field(name='CSM0', register=r, offset=3, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 0')
field(name='CSM1', register=r, offset=7, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 1')
field(name='CSM2', register=r, offset=11, width=1, access='read-write',
      doc='Conversion Start Mode of Request Source 2')
field(name='ASEN0', register=r, offset=24, width=1, access='read-write',
      doc='Arbitration Source Input 0 Enable')
field(name='ASEN1', register=r, offset=25, width=1, access='read-write',
      doc='Arbitration Source Input 1 Enable')
field(name='ASEN2', register=r, offset=26, width=1, access='read-write',
      doc='Arbitration Source Input 2 Enable')

r = register('G0ANCFG', width=32, block=evadcTargetSocket, offset=0x0488,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 0')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G1ANCFG', width=32, block=evadcTargetSocket, offset=0x0888,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 1')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G2ANCFG', width=32, block=evadcTargetSocket, offset=0x0c88,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 2')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G3ANCFG', width=32, block=evadcTargetSocket, offset=0x1088,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 3')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G8ANCFG', width=32, block=evadcTargetSocket, offset=0x2488,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 8')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G9ANCFG', width=32, block=evadcTargetSocket, offset=0x2888,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 9')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G10ANCFG', width=32, block=evadcTargetSocket, offset=0x2c88,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 10')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G11ANCFG', width=32, block=evadcTargetSocket, offset=0x3088,
             access='read-only', reset=0x00300004,
             doc='Analog Fct. Config. Register, Group 11')
field(name='IPE', register=r, offset=0, width=1, access='read-write',
      doc='Idle Precharge Enable')
field(name='BE', register=r, offset=1, width=1, access='read-write',
      doc='Input Buffer Enable')
field(name='RPE', register=r, offset=2, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='RPC', register=r, offset=3, width=1, access='read-write',
      doc='Reference Precharge Control')
field(name='CALSTC', register=r, offset=4, width=2, access='read-write',
      doc='Calibration Sample Time Control')
field(name='DPCAL', register=r, offset=6, width=1, access='read-write',
      doc='Disable Post-Calibration')
field(name='ACSD', register=r, offset=16, width=3, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='SSE', register=r, offset=19, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='DIVA', register=r, offset=20, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='DCMSB', register=r, offset=25, width=1, access='read-write',
      doc='Double Clock for the MSB Conversion')

r = register('G0ICLASS0', width=32, block=evadcTargetSocket, offset=0x04a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 0')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G1ICLASS0', width=32, block=evadcTargetSocket, offset=0x08a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 1')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G2ICLASS0', width=32, block=evadcTargetSocket, offset=0x0ca0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 2')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G3ICLASS0', width=32, block=evadcTargetSocket, offset=0x10a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 3')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G8ICLASS0', width=32, block=evadcTargetSocket, offset=0x24a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 8')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G9ICLASS0', width=32, block=evadcTargetSocket, offset=0x28a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 9')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G10ICLASS0', width=32, block=evadcTargetSocket, offset=0x2ca0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 10')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G11ICLASS0', width=32, block=evadcTargetSocket, offset=0x30a0,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 0, Group 11')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G0ICLASS1', width=32, block=evadcTargetSocket, offset=0x04a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 0')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G1ICLASS1', width=32, block=evadcTargetSocket, offset=0x08a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 1')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G2ICLASS1', width=32, block=evadcTargetSocket, offset=0x0ca4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 2')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G3ICLASS1', width=32, block=evadcTargetSocket, offset=0x10a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 3')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G8ICLASS1', width=32, block=evadcTargetSocket, offset=0x24a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 8')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G9ICLASS1', width=32, block=evadcTargetSocket, offset=0x28a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 9')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G10ICLASS1', width=32, block=evadcTargetSocket, offset=0x2ca4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 10')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G11ICLASS1', width=32, block=evadcTargetSocket, offset=0x30a4,
             access='read-only', reset=0x00000000,
             doc='Input Class Register 1, Group 11')
field(name='STCS', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Standard Conversions')
field(name='AIPS', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Control for Standard Conversions')
field(name='CMS', register=r, offset=8, width=2, access='read-write',
      doc='Conversion Mode for Standard Conversions')
field(name='SESPS', register=r, offset=10, width=1, access='read-write',
      doc='Spread Early Sample Point for Standard Conversions')
field(name='STCE', register=r, offset=16, width=5, access='read-write',
      doc='Sample Time Control for EMUX Conversions')
field(name='AIPE', register=r, offset=22, width=2, access='read-write',
      doc='Analog Input Precharge Control for EMUX Conversions')
field(name='CME', register=r, offset=24, width=2, access='read-write',
      doc='Conversion Mode for EMUX Conversions')
field(name='SESPE', register=r, offset=26, width=1, access='read-write',
      doc='Spread Early Sample Point for EMUX Conversions')

r = register('G0ALIAS', width=32, block=evadcTargetSocket, offset=0x04b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 0')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G1ALIAS', width=32, block=evadcTargetSocket, offset=0x08b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 1')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G2ALIAS', width=32, block=evadcTargetSocket, offset=0x0cb0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 2')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G3ALIAS', width=32, block=evadcTargetSocket, offset=0x10b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 3')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G8ALIAS', width=32, block=evadcTargetSocket, offset=0x24b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 8')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G9ALIAS', width=32, block=evadcTargetSocket, offset=0x28b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 9')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G10ALIAS', width=32, block=evadcTargetSocket, offset=0x2cb0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 10')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G11ALIAS', width=32, block=evadcTargetSocket, offset=0x30b0,
             access='read-only', reset=0x00000100,
             doc='Alias Register, Group 11')
field(name='ALIAS0', register=r, offset=0, width=5, access='read-write',
      doc='Alias Value for CH0 Conversion Requests')
field(name='ALIAS1', register=r, offset=8, width=5, access='read-write',
      doc='Alias Value for CH1 Conversion Requests')

r = register('G0BOUND', width=32, block=evadcTargetSocket, offset=0x04b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 0')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G1BOUND', width=32, block=evadcTargetSocket, offset=0x08b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 1')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G2BOUND', width=32, block=evadcTargetSocket, offset=0x0cb8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 2')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G3BOUND', width=32, block=evadcTargetSocket, offset=0x10b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 3')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G8BOUND', width=32, block=evadcTargetSocket, offset=0x24b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 8')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G9BOUND', width=32, block=evadcTargetSocket, offset=0x28b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 9')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G10BOUND', width=32, block=evadcTargetSocket, offset=0x2cb8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 10')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G11BOUND', width=32, block=evadcTargetSocket, offset=0x30b8,
             access='read-only', reset=0x00000000,
             doc='Boundary Select Register, Group 11')
field(name='BOUNDARY0', register=r, offset=0, width=12, access='read-write',
      doc='Boundary Value 0 for Limit Checking')
field(name='BOUNDARY1', register=r, offset=16, width=12, access='read-write',
      doc='Boundary Value 1 for Limit Checking')

r = register('G0SYNCTR', width=32, block=evadcTargetSocket, offset=0x04c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 0')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G1SYNCTR', width=32, block=evadcTargetSocket, offset=0x08c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 1')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G2SYNCTR', width=32, block=evadcTargetSocket, offset=0x0cc0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 2')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G3SYNCTR', width=32, block=evadcTargetSocket, offset=0x10c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 3')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G8SYNCTR', width=32, block=evadcTargetSocket, offset=0x24c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 8')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G9SYNCTR', width=32, block=evadcTargetSocket, offset=0x28c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 9')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G10SYNCTR', width=32, block=evadcTargetSocket, offset=0x2cc0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 10')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G11SYNCTR', width=32, block=evadcTargetSocket, offset=0x30c0,
             access='read-only', reset=0x00000000,
             doc='Synchronization Control Register, Group 11')
field(name='STSEL', register=r, offset=0, width=2, access='read-write',
      doc='Start Selection')
field(name='EVALR1', register=r, offset=4, width=1, access='read-write',
      doc='Evaluate Ready Input R1')
field(name='EVALR2', register=r, offset=5, width=1, access='read-write',
      doc='Evaluate Ready Input R2')
field(name='EVALR3', register=r, offset=6, width=1, access='read-write',
      doc='Evaluate Ready Input R3')

r = register('G0QCTRL0', width=32, block=evadcTargetSocket, offset=0x0500,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 0')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G1QCTRL0', width=32, block=evadcTargetSocket, offset=0x0900,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 1')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G2QCTRL0', width=32, block=evadcTargetSocket, offset=0x0d00,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 2')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G3QCTRL0', width=32, block=evadcTargetSocket, offset=0x1100,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 3')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G8QCTRL0', width=32, block=evadcTargetSocket, offset=0x2500,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 8')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G9QCTRL0', width=32, block=evadcTargetSocket, offset=0x2900,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 9')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G10QCTRL0', width=32, block=evadcTargetSocket, offset=0x2d00,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 10')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G11QCTRL0', width=32, block=evadcTargetSocket, offset=0x3100,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Source Contr. Register, Group 11')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G0QCTRL1', width=32, block=evadcTargetSocket, offset=0x0520,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 0')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G1QCTRL1', width=32, block=evadcTargetSocket, offset=0x0920,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 1')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G2QCTRL1', width=32, block=evadcTargetSocket, offset=0x0d20,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 2')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G3QCTRL1', width=32, block=evadcTargetSocket, offset=0x1120,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 3')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G8QCTRL1', width=32, block=evadcTargetSocket, offset=0x2520,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 8')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G9QCTRL1', width=32, block=evadcTargetSocket, offset=0x2920,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 9')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G10QCTRL1', width=32, block=evadcTargetSocket, offset=0x2d20,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 10')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G11QCTRL1', width=32, block=evadcTargetSocket, offset=0x3120,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Source Contr. Register, Group 11')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G0QCTRL2', width=32, block=evadcTargetSocket, offset=0x0540,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 0')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G1QCTRL2', width=32, block=evadcTargetSocket, offset=0x0940,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 1')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G2QCTRL2', width=32, block=evadcTargetSocket, offset=0x0d40,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 2')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G3QCTRL2', width=32, block=evadcTargetSocket, offset=0x1140,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 3')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G8QCTRL2', width=32, block=evadcTargetSocket, offset=0x2540,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 8')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G9QCTRL2', width=32, block=evadcTargetSocket, offset=0x2940,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 9')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G10QCTRL2', width=32, block=evadcTargetSocket, offset=0x2d40,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 10')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G11QCTRL2', width=32, block=evadcTargetSocket, offset=0x3140,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Source Contr. Register, Group 11')
field(name='SRCRESREG', register=r, offset=0, width=4, access='read-write',
      doc='Source-specific Result Register')
field(name='TRSEL', register=r, offset=6, width=2, access='read-write',
      doc='Trigger Source Selection')
field(name='XTSEL', register=r, offset=8, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=12, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=13, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Trigger Configuration')
field(name='GTSEL', register=r, offset=16, width=4, access='read-write',
      doc='Gate Input Selection')
field(name='GTLVL', register=r, offset=20, width=1, access='read-only',
      doc='Gate Input Level')
field(name='GTWC', register=r, offset=23, width=1, access='write-only',
      doc='Write Control for Gate Configuration')
field(name='TMEN', register=r, offset=28, width=1, access='read-write',
      doc='Timer Mode Enable')
field(name='TMWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Timer Mode')

r = register('G0QMR0', width=32, block=evadcTargetSocket, offset=0x0504,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 0')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G1QMR0', width=32, block=evadcTargetSocket, offset=0x0904,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 1')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G2QMR0', width=32, block=evadcTargetSocket, offset=0x0d04,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 2')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G3QMR0', width=32, block=evadcTargetSocket, offset=0x1104,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 3')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G8QMR0', width=32, block=evadcTargetSocket, offset=0x2504,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 8')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G9QMR0', width=32, block=evadcTargetSocket, offset=0x2904,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 9')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G10QMR0', width=32, block=evadcTargetSocket, offset=0x2d04,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 10')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G11QMR0', width=32, block=evadcTargetSocket, offset=0x3104,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Mode Register, Group 11')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G0QMR1', width=32, block=evadcTargetSocket, offset=0x0524,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 0')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G1QMR1', width=32, block=evadcTargetSocket, offset=0x0924,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 1')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G2QMR1', width=32, block=evadcTargetSocket, offset=0x0d24,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 2')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G3QMR1', width=32, block=evadcTargetSocket, offset=0x1124,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 3')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G8QMR1', width=32, block=evadcTargetSocket, offset=0x2524,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 8')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G9QMR1', width=32, block=evadcTargetSocket, offset=0x2924,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 9')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G10QMR1', width=32, block=evadcTargetSocket, offset=0x2d24,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 10')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G11QMR1', width=32, block=evadcTargetSocket, offset=0x3124,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Mode Register, Group 11')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G0QMR2', width=32, block=evadcTargetSocket, offset=0x0544,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 0')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G1QMR2', width=32, block=evadcTargetSocket, offset=0x0944,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 1')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G2QMR2', width=32, block=evadcTargetSocket, offset=0x0d44,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 2')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G3QMR2', width=32, block=evadcTargetSocket, offset=0x1144,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 3')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G8QMR2', width=32, block=evadcTargetSocket, offset=0x2544,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 8')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G9QMR2', width=32, block=evadcTargetSocket, offset=0x2944,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 9')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G10QMR2', width=32, block=evadcTargetSocket, offset=0x2d44,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 10')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G11QMR2', width=32, block=evadcTargetSocket, offset=0x3144,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Mode Register, Group 11')
field(name='ENGT', register=r, offset=0, width=2, access='read-write',
      doc='Enable Gate')
field(name='ENTR', register=r, offset=2, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='CLRV', register=r, offset=8, width=1, access='write-only',
      doc='Clear Valid Bit')
field(name='TREV', register=r, offset=9, width=1, access='write-only',
      doc='Trigger Event')
field(name='FLUSH', register=r, offset=10, width=1, access='write-only',
      doc='Flush Queue')
field(name='CEV', register=r, offset=11, width=1, access='write-only',
      doc='Clear Event Flag')
field(name='RPTDIS', register=r, offset=16, width=1, access='read-write',
      doc='Repeat Disable')

r = register('G0QSR0', width=32, block=evadcTargetSocket, offset=0x0508,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 0')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G1QSR0', width=32, block=evadcTargetSocket, offset=0x0908,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 1')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G2QSR0', width=32, block=evadcTargetSocket, offset=0x0d08,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 2')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G3QSR0', width=32, block=evadcTargetSocket, offset=0x1108,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 3')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G8QSR0', width=32, block=evadcTargetSocket, offset=0x2508,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 8')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G9QSR0', width=32, block=evadcTargetSocket, offset=0x2908,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 9')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G10QSR0', width=32, block=evadcTargetSocket, offset=0x2d08,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 10')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G11QSR0', width=32, block=evadcTargetSocket, offset=0x3108,
             access='read-only', reset=0x00000020,
             doc='Queue 0 Status Register, Group 11')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G0QSR1', width=32, block=evadcTargetSocket, offset=0x0528,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 0')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G1QSR1', width=32, block=evadcTargetSocket, offset=0x0928,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 1')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G2QSR1', width=32, block=evadcTargetSocket, offset=0x0d28,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 2')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G3QSR1', width=32, block=evadcTargetSocket, offset=0x1128,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 3')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G8QSR1', width=32, block=evadcTargetSocket, offset=0x2528,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 8')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G9QSR1', width=32, block=evadcTargetSocket, offset=0x2928,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 9')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G10QSR1', width=32, block=evadcTargetSocket, offset=0x2d28,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 10')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G11QSR1', width=32, block=evadcTargetSocket, offset=0x3128,
             access='read-only', reset=0x00000020,
             doc='Queue 1 Status Register, Group 11')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G0QSR2', width=32, block=evadcTargetSocket, offset=0x0548,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 0')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G1QSR2', width=32, block=evadcTargetSocket, offset=0x0948,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 1')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G2QSR2', width=32, block=evadcTargetSocket, offset=0x0d48,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 2')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G3QSR2', width=32, block=evadcTargetSocket, offset=0x1148,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 3')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G8QSR2', width=32, block=evadcTargetSocket, offset=0x2548,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 8')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G9QSR2', width=32, block=evadcTargetSocket, offset=0x2948,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 9')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G10QSR2', width=32, block=evadcTargetSocket, offset=0x2d48,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 10')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G11QSR2', width=32, block=evadcTargetSocket, offset=0x3148,
             access='read-only', reset=0x00000020,
             doc='Queue 2 Status Register, Group 11')
field(name='FILL', register=r, offset=0, width=4, access='read-only',
      doc='Filling Level for Queue')
field(name='EMPTY', register=r, offset=5, width=1, access='read-only',
      doc='Queue Empty')
field(name='REQGT', register=r, offset=7, width=1, access='read-only',
      doc='Request Gate Level')
field(name='EV', register=r, offset=8, width=1, access='read-only',
      doc='Event Detected')

r = register('G0Q0R0', width=32, block=evadcTargetSocket, offset=0x050c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1Q0R0', width=32, block=evadcTargetSocket, offset=0x090c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2Q0R0', width=32, block=evadcTargetSocket, offset=0x0d0c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3Q0R0', width=32, block=evadcTargetSocket, offset=0x110c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8Q0R0', width=32, block=evadcTargetSocket, offset=0x250c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9Q0R0', width=32, block=evadcTargetSocket, offset=0x290c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10Q0R0', width=32, block=evadcTargetSocket, offset=0x2d0c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11Q0R0', width=32, block=evadcTargetSocket, offset=0x310c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Register 0, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0Q0R1', width=32, block=evadcTargetSocket, offset=0x052c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1Q0R1', width=32, block=evadcTargetSocket, offset=0x092c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2Q0R1', width=32, block=evadcTargetSocket, offset=0x0d2c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3Q0R1', width=32, block=evadcTargetSocket, offset=0x112c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8Q0R1', width=32, block=evadcTargetSocket, offset=0x252c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9Q0R1', width=32, block=evadcTargetSocket, offset=0x292c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10Q0R1', width=32, block=evadcTargetSocket, offset=0x2d2c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11Q0R1', width=32, block=evadcTargetSocket, offset=0x312c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Register 0, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0Q0R2', width=32, block=evadcTargetSocket, offset=0x054c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1Q0R2', width=32, block=evadcTargetSocket, offset=0x094c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2Q0R2', width=32, block=evadcTargetSocket, offset=0x0d4c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3Q0R2', width=32, block=evadcTargetSocket, offset=0x114c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8Q0R2', width=32, block=evadcTargetSocket, offset=0x254c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9Q0R2', width=32, block=evadcTargetSocket, offset=0x294c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10Q0R2', width=32, block=evadcTargetSocket, offset=0x2d4c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11Q0R2', width=32, block=evadcTargetSocket, offset=0x314c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Register 0, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QINR0', width=32, block=evadcTargetSocket, offset=0x0510,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QINR0', width=32, block=evadcTargetSocket, offset=0x0910,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QINR0', width=32, block=evadcTargetSocket, offset=0x0d10,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QINR0', width=32, block=evadcTargetSocket, offset=0x1110,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QINR0', width=32, block=evadcTargetSocket, offset=0x2510,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QINR0', width=32, block=evadcTargetSocket, offset=0x2910,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QINR0', width=32, block=evadcTargetSocket, offset=0x2d10,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QINR0', width=32, block=evadcTargetSocket, offset=0x3110,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Input Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QINR1', width=32, block=evadcTargetSocket, offset=0x0530,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QINR1', width=32, block=evadcTargetSocket, offset=0x0930,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QINR1', width=32, block=evadcTargetSocket, offset=0x0d30,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QINR1', width=32, block=evadcTargetSocket, offset=0x1130,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QINR1', width=32, block=evadcTargetSocket, offset=0x2530,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QINR1', width=32, block=evadcTargetSocket, offset=0x2930,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QINR1', width=32, block=evadcTargetSocket, offset=0x2d30,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QINR1', width=32, block=evadcTargetSocket, offset=0x3130,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Input Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QINR2', width=32, block=evadcTargetSocket, offset=0x0550,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QINR2', width=32, block=evadcTargetSocket, offset=0x0950,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QINR2', width=32, block=evadcTargetSocket, offset=0x0d50,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QINR2', width=32, block=evadcTargetSocket, offset=0x1150,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QINR2', width=32, block=evadcTargetSocket, offset=0x2550,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QINR2', width=32, block=evadcTargetSocket, offset=0x2950,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QINR2', width=32, block=evadcTargetSocket, offset=0x2d50,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QINR2', width=32, block=evadcTargetSocket, offset=0x3150,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Input Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='write-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='write-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='write-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='write-only',
      doc='External Trigger')
field(name='PDD', register=r, offset=9, width=1, access='write-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='write-only',
      doc='Multiplexer Diagnostics Pull-Devices Enable - MDPD,MDPU')
field(name='CDEN', register=r, offset=12, width=1, access='write-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='write-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QBUR0', width=32, block=evadcTargetSocket, offset=0x0514,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QBUR0', width=32, block=evadcTargetSocket, offset=0x0914,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QBUR0', width=32, block=evadcTargetSocket, offset=0x0d14,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QBUR0', width=32, block=evadcTargetSocket, offset=0x1114,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QBUR0', width=32, block=evadcTargetSocket, offset=0x2514,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QBUR0', width=32, block=evadcTargetSocket, offset=0x2914,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QBUR0', width=32, block=evadcTargetSocket, offset=0x2d14,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QBUR0', width=32, block=evadcTargetSocket, offset=0x3114,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Backup Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QBUR1', width=32, block=evadcTargetSocket, offset=0x0534,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QBUR1', width=32, block=evadcTargetSocket, offset=0x0934,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QBUR1', width=32, block=evadcTargetSocket, offset=0x0d34,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QBUR1', width=32, block=evadcTargetSocket, offset=0x1134,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QBUR1', width=32, block=evadcTargetSocket, offset=0x2534,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QBUR1', width=32, block=evadcTargetSocket, offset=0x2934,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QBUR1', width=32, block=evadcTargetSocket, offset=0x2d34,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QBUR1', width=32, block=evadcTargetSocket, offset=0x3134,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Backup Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0QBUR2', width=32, block=evadcTargetSocket, offset=0x0554,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 0')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G1QBUR2', width=32, block=evadcTargetSocket, offset=0x0954,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 1')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G2QBUR2', width=32, block=evadcTargetSocket, offset=0x0d54,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 2')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G3QBUR2', width=32, block=evadcTargetSocket, offset=0x1154,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 3')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G8QBUR2', width=32, block=evadcTargetSocket, offset=0x2554,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 8')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G9QBUR2', width=32, block=evadcTargetSocket, offset=0x2954,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 9')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G10QBUR2', width=32, block=evadcTargetSocket, offset=0x2d54,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 10')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G11QBUR2', width=32, block=evadcTargetSocket, offset=0x3154,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Backup Register, Group 11')
field(name='REQCHNR', register=r, offset=0, width=5, access='read-only',
      doc='Request Channel Number')
field(name='RF', register=r, offset=5, width=1, access='read-only',
      doc='Refill')
field(name='ENSI', register=r, offset=6, width=1, access='read-only',
      doc='Enable Source Interrupt')
field(name='EXTR', register=r, offset=7, width=1, access='read-only',
      doc='External Trigger')
field(name='V', register=r, offset=8, width=1, access='read-only',
      doc='Request Channel Number Valid')
field(name='PDD', register=r, offset=9, width=1, access='read-only',
      doc='Pull-Down Diagnostics Enable')
field(name='MDPD', register=r, offset=10, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Down Devices Enable')
field(name='MDPU', register=r, offset=11, width=1, access='read-only',
      doc='Multiplexer Diagnostics Pull-Up Devices Enable')
field(name='CDEN', register=r, offset=12, width=1, access='read-only',
      doc='Converter Diagnostics Enable')
field(name='CDSEL', register=r, offset=13, width=2, access='read-only',
      doc='Converter Diagnostics Pull-Devices Select')

r = register('G0REQTM0', width=32, block=evadcTargetSocket, offset=0x0518,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 0')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G1REQTM0', width=32, block=evadcTargetSocket, offset=0x0918,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 1')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G2REQTM0', width=32, block=evadcTargetSocket, offset=0x0d18,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 2')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G3REQTM0', width=32, block=evadcTargetSocket, offset=0x1118,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 3')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G8REQTM0', width=32, block=evadcTargetSocket, offset=0x2518,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 8')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G9REQTM0', width=32, block=evadcTargetSocket, offset=0x2918,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 9')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G10REQTM0', width=32, block=evadcTargetSocket, offset=0x2d18,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 10')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G11REQTM0', width=32, block=evadcTargetSocket, offset=0x3118,
             access='read-only', reset=0xFFC00000,
             doc='Queue 0 Requ. Timer Mode Reg., Group 11')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G0REQTM1', width=32, block=evadcTargetSocket, offset=0x0538,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 0')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G1REQTM1', width=32, block=evadcTargetSocket, offset=0x0938,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 1')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G2REQTM1', width=32, block=evadcTargetSocket, offset=0x0d38,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 2')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G3REQTM1', width=32, block=evadcTargetSocket, offset=0x1138,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 3')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G8REQTM1', width=32, block=evadcTargetSocket, offset=0x2538,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 8')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G9REQTM1', width=32, block=evadcTargetSocket, offset=0x2938,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 9')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G10REQTM1', width=32, block=evadcTargetSocket, offset=0x2d38,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 10')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G11REQTM1', width=32, block=evadcTargetSocket, offset=0x3138,
             access='read-only', reset=0xFFC00000,
             doc='Queue 1 Requ. Timer Mode Reg., Group 11')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G0REQTM2', width=32, block=evadcTargetSocket, offset=0x0558,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 0')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G1REQTM2', width=32, block=evadcTargetSocket, offset=0x0958,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 1')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G2REQTM2', width=32, block=evadcTargetSocket, offset=0x0d58,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 2')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G3REQTM2', width=32, block=evadcTargetSocket, offset=0x1158,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 3')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G8REQTM2', width=32, block=evadcTargetSocket, offset=0x2558,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 8')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G9REQTM2', width=32, block=evadcTargetSocket, offset=0x2958,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 9')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G10REQTM2', width=32, block=evadcTargetSocket, offset=0x2d58,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 10')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G11REQTM2', width=32, block=evadcTargetSocket, offset=0x3158,
             access='read-only', reset=0xFFC00000,
             doc='Queue 2 Requ. Timer Mode Reg., Group 11')
field(name='SEQMOD', register=r, offset=0, width=2, access='read-write',
      doc='Sequence Mode')
field(name='SEQTIMSET', register=r, offset=6, width=10, access='read-write',
      doc='Sequence Timer, Set Value')
field(name='REQTS', register=r, offset=16, width=1, access='write-only',
      doc='Request Timer Start Trigger')
field(name='ENTR', register=r, offset=17, width=1, access='read-write',
      doc='Enable External Trigger')
field(name='SEQTIMOFF', register=r, offset=22, width=10, access='read-write',
      doc='Sequence Timer, Switch Off Value')

r = register('G0REQTS0', width=32, block=evadcTargetSocket, offset=0x051c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 0')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G1REQTS0', width=32, block=evadcTargetSocket, offset=0x091c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 1')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G2REQTS0', width=32, block=evadcTargetSocket, offset=0x0d1c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 2')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G3REQTS0', width=32, block=evadcTargetSocket, offset=0x111c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 3')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G8REQTS0', width=32, block=evadcTargetSocket, offset=0x251c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 8')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G9REQTS0', width=32, block=evadcTargetSocket, offset=0x291c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 9')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G10REQTS0', width=32, block=evadcTargetSocket, offset=0x2d1c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 10')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G11REQTS0', width=32, block=evadcTargetSocket, offset=0x311c,
             access='read-only', reset=0x00000000,
             doc='Queue 0 Requ. Timer Status Reg., Group 11')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G0REQTS1', width=32, block=evadcTargetSocket, offset=0x053c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 0')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G1REQTS1', width=32, block=evadcTargetSocket, offset=0x093c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 1')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G2REQTS1', width=32, block=evadcTargetSocket, offset=0x0d3c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 2')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G3REQTS1', width=32, block=evadcTargetSocket, offset=0x113c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 3')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G8REQTS1', width=32, block=evadcTargetSocket, offset=0x253c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 8')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G9REQTS1', width=32, block=evadcTargetSocket, offset=0x293c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 9')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G10REQTS1', width=32, block=evadcTargetSocket, offset=0x2d3c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 10')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G11REQTS1', width=32, block=evadcTargetSocket, offset=0x313c,
             access='read-only', reset=0x00000000,
             doc='Queue 1 Requ. Timer Status Reg., Group 11')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G0REQTS2', width=32, block=evadcTargetSocket, offset=0x055c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 0')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G1REQTS2', width=32, block=evadcTargetSocket, offset=0x095c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 1')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G2REQTS2', width=32, block=evadcTargetSocket, offset=0x0d5c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 2')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G3REQTS2', width=32, block=evadcTargetSocket, offset=0x115c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 3')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G8REQTS2', width=32, block=evadcTargetSocket, offset=0x255c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 8')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G9REQTS2', width=32, block=evadcTargetSocket, offset=0x295c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 9')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G10REQTS2', width=32, block=evadcTargetSocket, offset=0x2d5c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 10')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G11REQTS2', width=32, block=evadcTargetSocket, offset=0x315c,
             access='read-only', reset=0x00000000,
             doc='Queue 2 Requ. Timer Status Reg., Group 11')
field(name='SEQTIMER', register=r, offset=6, width=10, access='read-only',
      doc='Sequence Timer')

r = register('G0CEFLAG', width=32, block=evadcTargetSocket, offset=0x0580,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 0')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')

r = register('G1CEFLAG', width=32, block=evadcTargetSocket, offset=0x0980,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 1')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')

r = register('G2CEFLAG', width=32, block=evadcTargetSocket, offset=0x0d80,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 2')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')

r = register('G3CEFLAG', width=32, block=evadcTargetSocket, offset=0x1180,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 3')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')

r = register('G8CEFLAG', width=32, block=evadcTargetSocket, offset=0x2580,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 8')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='read-write',
      doc='Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='read-write',
      doc='Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='read-write',
      doc='Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='read-write',
      doc='Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='read-write',
      doc='Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='read-write',
      doc='Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='read-write',
      doc='Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='read-write',
      doc='Channel Event for Channel 15')

r = register('G9CEFLAG', width=32, block=evadcTargetSocket, offset=0x2980,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 9')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='read-write',
      doc='Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='read-write',
      doc='Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='read-write',
      doc='Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='read-write',
      doc='Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='read-write',
      doc='Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='read-write',
      doc='Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='read-write',
      doc='Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='read-write',
      doc='Channel Event for Channel 15')

r = register('G10CEFLAG', width=32, block=evadcTargetSocket, offset=0x2d80,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 10')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='read-write',
      doc='Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='read-write',
      doc='Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='read-write',
      doc='Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='read-write',
      doc='Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='read-write',
      doc='Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='read-write',
      doc='Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='read-write',
      doc='Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='read-write',
      doc='Channel Event for Channel 15')

r = register('G11CEFLAG', width=32, block=evadcTargetSocket, offset=0x3180,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Register, Group 11')
field(name='CEV0', register=r, offset=0, width=1, access='read-write',
      doc='Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='read-write',
      doc='Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='read-write',
      doc='Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='read-write',
      doc='Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='read-write',
      doc='Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='read-write',
      doc='Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='read-write',
      doc='Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='read-write',
      doc='Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='read-write',
      doc='Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='read-write',
      doc='Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='read-write',
      doc='Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='read-write',
      doc='Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='read-write',
      doc='Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='read-write',
      doc='Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='read-write',
      doc='Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='read-write',
      doc='Channel Event for Channel 15')

r = register('G0REFLAG', width=32, block=evadcTargetSocket, offset=0x0584,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 0')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G1REFLAG', width=32, block=evadcTargetSocket, offset=0x0984,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 1')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G2REFLAG', width=32, block=evadcTargetSocket, offset=0x0d84,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 2')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G3REFLAG', width=32, block=evadcTargetSocket, offset=0x1184,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 3')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G8REFLAG', width=32, block=evadcTargetSocket, offset=0x2584,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 8')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G9REFLAG', width=32, block=evadcTargetSocket, offset=0x2984,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 9')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G10REFLAG', width=32, block=evadcTargetSocket, offset=0x2d84,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 10')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G11REFLAG', width=32, block=evadcTargetSocket, offset=0x3184,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Register, Group 11')
field(name='REV0', register=r, offset=0, width=1, access='read-write',
      doc='Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='read-write',
      doc='Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='read-write',
      doc='Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='read-write',
      doc='Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='read-write',
      doc='Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='read-write',
      doc='Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='read-write',
      doc='Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='read-write',
      doc='Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='read-write',
      doc='Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='read-write',
      doc='Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='read-write',
      doc='Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='read-write',
      doc='Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='read-write',
      doc='Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='read-write',
      doc='Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='read-write',
      doc='Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='read-write',
      doc='Result Event for Result Register 15')

r = register('G0SEFLAG', width=32, block=evadcTargetSocket, offset=0x0588,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 0')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G1SEFLAG', width=32, block=evadcTargetSocket, offset=0x0988,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 1')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G2SEFLAG', width=32, block=evadcTargetSocket, offset=0x0d88,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 2')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G3SEFLAG', width=32, block=evadcTargetSocket, offset=0x1188,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 3')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G8SEFLAG', width=32, block=evadcTargetSocket, offset=0x2588,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 8')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G9SEFLAG', width=32, block=evadcTargetSocket, offset=0x2988,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 9')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G10SEFLAG', width=32, block=evadcTargetSocket, offset=0x2d88,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 10')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G11SEFLAG', width=32, block=evadcTargetSocket, offset=0x3188,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Register, Group 11')
field(name='SEV0', register=r, offset=0, width=1, access='read-write',
      doc='Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='read-write',
      doc='Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='read-write',
      doc='Source Event 2')

r = register('G0CEFCLR', width=32, block=evadcTargetSocket, offset=0x0590,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 0')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')

r = register('G1CEFCLR', width=32, block=evadcTargetSocket, offset=0x0990,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 1')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')

r = register('G2CEFCLR', width=32, block=evadcTargetSocket, offset=0x0d90,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 2')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')

r = register('G3CEFCLR', width=32, block=evadcTargetSocket, offset=0x1190,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 3')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')

r = register('G8CEFCLR', width=32, block=evadcTargetSocket, offset=0x2590,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 8')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Channel Event for Channel 15')

r = register('G9CEFCLR', width=32, block=evadcTargetSocket, offset=0x2990,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 9')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Channel Event for Channel 15')

r = register('G10CEFCLR', width=32, block=evadcTargetSocket, offset=0x2d90,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 10')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Channel Event for Channel 15')

r = register('G11CEFCLR', width=32, block=evadcTargetSocket, offset=0x3190,
             access='read-only', reset=0x00000000,
             doc='Channel Event Flag Clear Register, Group 11')
field(name='CEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Channel Event for Channel 0')
field(name='CEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Channel Event for Channel 1')
field(name='CEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Channel Event for Channel 2')
field(name='CEV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Channel Event for Channel 3')
field(name='CEV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Channel Event for Channel 4')
field(name='CEV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Channel Event for Channel 5')
field(name='CEV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Channel Event for Channel 6')
field(name='CEV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Channel Event for Channel 7')
field(name='CEV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Channel Event for Channel 8')
field(name='CEV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Channel Event for Channel 9')
field(name='CEV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Channel Event for Channel 10')
field(name='CEV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Channel Event for Channel 11')
field(name='CEV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Channel Event for Channel 12')
field(name='CEV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Channel Event for Channel 13')
field(name='CEV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Channel Event for Channel 14')
field(name='CEV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Channel Event for Channel 15')

r = register('G0REFCLR', width=32, block=evadcTargetSocket, offset=0x0594,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 0')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G1REFCLR', width=32, block=evadcTargetSocket, offset=0x0994,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 1')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G2REFCLR', width=32, block=evadcTargetSocket, offset=0x0d94,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 2')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G3REFCLR', width=32, block=evadcTargetSocket, offset=0x1194,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 3')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G8REFCLR', width=32, block=evadcTargetSocket, offset=0x2594,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 8')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G9REFCLR', width=32, block=evadcTargetSocket, offset=0x2994,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 9')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G10REFCLR', width=32, block=evadcTargetSocket, offset=0x2d94,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 10')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G11REFCLR', width=32, block=evadcTargetSocket, offset=0x3194,
             access='read-only', reset=0x00000000,
             doc='Result Event Flag Clear Register, Group 11')
field(name='REV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Result Event for Result Register 0')
field(name='REV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Result Event for Result Register 1')
field(name='REV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Result Event for Result Register 2')
field(name='REV3', register=r, offset=3, width=1, access='write-only',
      doc='Clear Result Event for Result Register 3')
field(name='REV4', register=r, offset=4, width=1, access='write-only',
      doc='Clear Result Event for Result Register 4')
field(name='REV5', register=r, offset=5, width=1, access='write-only',
      doc='Clear Result Event for Result Register 5')
field(name='REV6', register=r, offset=6, width=1, access='write-only',
      doc='Clear Result Event for Result Register 6')
field(name='REV7', register=r, offset=7, width=1, access='write-only',
      doc='Clear Result Event for Result Register 7')
field(name='REV8', register=r, offset=8, width=1, access='write-only',
      doc='Clear Result Event for Result Register 8')
field(name='REV9', register=r, offset=9, width=1, access='write-only',
      doc='Clear Result Event for Result Register 9')
field(name='REV10', register=r, offset=10, width=1, access='write-only',
      doc='Clear Result Event for Result Register 10')
field(name='REV11', register=r, offset=11, width=1, access='write-only',
      doc='Clear Result Event for Result Register 11')
field(name='REV12', register=r, offset=12, width=1, access='write-only',
      doc='Clear Result Event for Result Register 12')
field(name='REV13', register=r, offset=13, width=1, access='write-only',
      doc='Clear Result Event for Result Register 13')
field(name='REV14', register=r, offset=14, width=1, access='write-only',
      doc='Clear Result Event for Result Register 14')
field(name='REV15', register=r, offset=15, width=1, access='write-only',
      doc='Clear Result Event for Result Register 15')

r = register('G0SEFCLR', width=32, block=evadcTargetSocket, offset=0x0598,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 0')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G1SEFCLR', width=32, block=evadcTargetSocket, offset=0x0998,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 1')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G2SEFCLR', width=32, block=evadcTargetSocket, offset=0x0d98,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 2')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G3SEFCLR', width=32, block=evadcTargetSocket, offset=0x1198,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 3')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G8SEFCLR', width=32, block=evadcTargetSocket, offset=0x2598,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 8')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G9SEFCLR', width=32, block=evadcTargetSocket, offset=0x2998,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 9')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G10SEFCLR', width=32, block=evadcTargetSocket, offset=0x2d98,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 10')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G11SEFCLR', width=32, block=evadcTargetSocket, offset=0x3198,
             access='read-only', reset=0x00000000,
             doc='Source Event Flag Clear Reg., Group 11')
field(name='SEV0', register=r, offset=0, width=1, access='write-only',
      doc='Clear Source Event 0')
field(name='SEV1', register=r, offset=1, width=1, access='write-only',
      doc='Clear Source Event 1')
field(name='SEV2', register=r, offset=2, width=1, access='write-only',
      doc='Clear Source Event 2')

r = register('G0CEVNP0', width=32, block=evadcTargetSocket, offset=0x05a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 0')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G1CEVNP0', width=32, block=evadcTargetSocket, offset=0x09a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 1')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G2CEVNP0', width=32, block=evadcTargetSocket, offset=0x0da0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 2')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G3CEVNP0', width=32, block=evadcTargetSocket, offset=0x11a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 3')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G8CEVNP0', width=32, block=evadcTargetSocket, offset=0x25a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 8')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G9CEVNP0', width=32, block=evadcTargetSocket, offset=0x29a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 9')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G10CEVNP0', width=32, block=evadcTargetSocket, offset=0x2da0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 10')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G11CEVNP0', width=32, block=evadcTargetSocket, offset=0x31a0,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 0, Group 11')
field(name='CEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 0')
field(name='CEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 1')
field(name='CEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 2')
field(name='CEV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 3')
field(name='CEV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 4')
field(name='CEV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 5')
field(name='CEV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 6')
field(name='CEV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 7')

r = register('G8CEVNP1', width=32, block=evadcTargetSocket, offset=0x25a4,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 1, Group 8')
field(name='CEV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 8')
field(name='CEV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 9')
field(name='CEV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 10')
field(name='CEV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 11')
field(name='CEV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 12')
field(name='CEV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 13')
field(name='CEV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 14')
field(name='CEV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 15')

r = register('G9CEVNP1', width=32, block=evadcTargetSocket, offset=0x29a4,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 1, Group 9')
field(name='CEV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 8')
field(name='CEV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 9')
field(name='CEV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 10')
field(name='CEV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 11')
field(name='CEV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 12')
field(name='CEV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 13')
field(name='CEV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 14')
field(name='CEV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 15')

r = register('G10CEVNP1', width=32, block=evadcTargetSocket, offset=0x2da4,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 1, Group 10')
field(name='CEV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 8')
field(name='CEV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 9')
field(name='CEV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 10')
field(name='CEV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 11')
field(name='CEV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 12')
field(name='CEV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 13')
field(name='CEV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 14')
field(name='CEV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 15')

r = register('G11CEVNP1', width=32, block=evadcTargetSocket, offset=0x31a4,
             access='read-only', reset=0x00000000,
             doc='Channel Event Node Pointer Reg. 1, Group 11')
field(name='CEV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 8')
field(name='CEV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 9')
field(name='CEV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 10')
field(name='CEV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 11')
field(name='CEV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 12')
field(name='CEV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 13')
field(name='CEV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 14')
field(name='CEV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Channel Event 15')

r = register('G0REVNP0', width=32, block=evadcTargetSocket, offset=0x05b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 0')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G1REVNP0', width=32, block=evadcTargetSocket, offset=0x09b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 1')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G2REVNP0', width=32, block=evadcTargetSocket, offset=0x0db0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 2')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G3REVNP0', width=32, block=evadcTargetSocket, offset=0x11b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 3')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G8REVNP0', width=32, block=evadcTargetSocket, offset=0x25b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 8')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G9REVNP0', width=32, block=evadcTargetSocket, offset=0x29b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 9')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G10REVNP0', width=32, block=evadcTargetSocket, offset=0x2db0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 10')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G11REVNP0', width=32, block=evadcTargetSocket, offset=0x31b0,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 0, Group 11')
field(name='REV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 0')
field(name='REV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 1')
field(name='REV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 2')
field(name='REV3NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 3')
field(name='REV4NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 4')
field(name='REV5NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 5')
field(name='REV6NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 6')
field(name='REV7NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 7')

r = register('G0REVNP1', width=32, block=evadcTargetSocket, offset=0x05b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 0')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G1REVNP1', width=32, block=evadcTargetSocket, offset=0x09b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 1')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G2REVNP1', width=32, block=evadcTargetSocket, offset=0x0db4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 2')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G3REVNP1', width=32, block=evadcTargetSocket, offset=0x11b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 3')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G8REVNP1', width=32, block=evadcTargetSocket, offset=0x25b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 8')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G9REVNP1', width=32, block=evadcTargetSocket, offset=0x29b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 9')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G10REVNP1', width=32, block=evadcTargetSocket, offset=0x2db4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 10')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G11REVNP1', width=32, block=evadcTargetSocket, offset=0x31b4,
             access='read-only', reset=0x00000000,
             doc='Result Event Node Pointer Reg. 1, Group 11')
field(name='REV8NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 8')
field(name='REV9NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 9')
field(name='REV10NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 10')
field(name='REV11NP', register=r, offset=12, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 11')
field(name='REV12NP', register=r, offset=16, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 12')
field(name='REV13NP', register=r, offset=20, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 13')
field(name='REV14NP', register=r, offset=24, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 14')
field(name='REV15NP', register=r, offset=28, width=4, access='read-write',
      doc='Service Request Node Pointer Result Event 15')

r = register('G0SEVNP', width=32, block=evadcTargetSocket, offset=0x05c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 0')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G1SEVNP', width=32, block=evadcTargetSocket, offset=0x09c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 1')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G2SEVNP', width=32, block=evadcTargetSocket, offset=0x0dc0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 2')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G3SEVNP', width=32, block=evadcTargetSocket, offset=0x11c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 3')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G8SEVNP', width=32, block=evadcTargetSocket, offset=0x25c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 8')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G9SEVNP', width=32, block=evadcTargetSocket, offset=0x29c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 9')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G10SEVNP', width=32, block=evadcTargetSocket, offset=0x2dc0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 10')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G11SEVNP', width=32, block=evadcTargetSocket, offset=0x31c0,
             access='read-only', reset=0x00000000,
             doc='Source Event Node Pointer Reg., Group 11')
field(name='SEV0NP', register=r, offset=0, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 0')
field(name='SEV1NP', register=r, offset=4, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 1')
field(name='SEV2NP', register=r, offset=8, width=4, access='read-write',
      doc='Service Request Node Pointer Source Event 2')

r = register('G0SRACT', width=32, block=evadcTargetSocket, offset=0x05c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 0')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G1SRACT', width=32, block=evadcTargetSocket, offset=0x09c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 1')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G2SRACT', width=32, block=evadcTargetSocket, offset=0x0dc8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 2')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G3SRACT', width=32, block=evadcTargetSocket, offset=0x11c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 3')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G8SRACT', width=32, block=evadcTargetSocket, offset=0x25c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 8')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G9SRACT', width=32, block=evadcTargetSocket, offset=0x29c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 9')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G10SRACT', width=32, block=evadcTargetSocket, offset=0x2dc8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 10')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G11SRACT', width=32, block=evadcTargetSocket, offset=0x31c8,
             access='read-only', reset=0x00000000,
             doc='Service Request Software Activation Trigger, Group 11')
field(name='AGSR0', register=r, offset=0, width=1, access='write-only',
      doc='Activate Group Service Request Node 0')
field(name='AGSR1', register=r, offset=1, width=1, access='write-only',
      doc='Activate Group Service Request Node 1')
field(name='AGSR2', register=r, offset=2, width=1, access='write-only',
      doc='Activate Group Service Request Node 2')
field(name='AGSR3', register=r, offset=3, width=1, access='write-only',
      doc='Activate Group Service Request Node 3')
field(name='ASSR0', register=r, offset=8, width=1, access='write-only',
      doc='Activate Shared Service Request Node 0')
field(name='ASSR1', register=r, offset=9, width=1, access='write-only',
      doc='Activate Shared Service Request Node 1')
field(name='ASSR2', register=r, offset=10, width=1, access='write-only',
      doc='Activate Shared Service Request Node 2')
field(name='ASSR3', register=r, offset=11, width=1, access='write-only',
      doc='Activate Shared Service Request Node 3')

r = register('G0EMUXCTR', width=32, block=evadcTargetSocket, offset=0x05f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 0')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G1EMUXCTR', width=32, block=evadcTargetSocket, offset=0x09f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 1')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G2EMUXCTR', width=32, block=evadcTargetSocket, offset=0x0df0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 2')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G3EMUXCTR', width=32, block=evadcTargetSocket, offset=0x11f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 3')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G8EMUXCTR', width=32, block=evadcTargetSocket, offset=0x25f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 8')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G9EMUXCTR', width=32, block=evadcTargetSocket, offset=0x29f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 9')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G10EMUXCTR', width=32, block=evadcTargetSocket, offset=0x2df0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 10')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G11EMUXCTR', width=32, block=evadcTargetSocket, offset=0x31f0,
             access='read-only', reset=0x00000000,
             doc='External Multiplexer Control Reg., Group 11')
field(name='EMUXSET', register=r, offset=0, width=3, access='read-write',
      doc='External Multiplexer Start Selection')
field(name='EMUXMODE', register=r, offset=4, width=3, access='read-write',
      doc='External Multiplexer Mode')
field(name='EMXCOD', register=r, offset=12, width=1, access='read-write',
      doc='External Multiplexer Coding Scheme')
field(name='EMXST', register=r, offset=13, width=1, access='read-write',
      doc='External Multiplexer Sample Time Control')
field(name='EMXCSS', register=r, offset=14, width=1, access='read-write',
      doc='External Multiplexer Channel Selection Style')
field(name='EMXWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for EMUX Configuration')
field(name='EMUXACT', register=r, offset=16, width=3, access='read-only',
      doc='External Multiplexer Actual Selection')
field(name='EMUXCCB', register=r, offset=20, width=5, access='read-write',
      doc='External Multiplexer Channel Selection for Block Mode')

r = register('G0EMUXCS', width=32, block=evadcTargetSocket, offset=0x05f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 0')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G1EMUXCS', width=32, block=evadcTargetSocket, offset=0x09f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 1')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G2EMUXCS', width=32, block=evadcTargetSocket, offset=0x0df4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 2')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G3EMUXCS', width=32, block=evadcTargetSocket, offset=0x11f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 3')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G8EMUXCS', width=32, block=evadcTargetSocket, offset=0x25f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 8')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G9EMUXCS', width=32, block=evadcTargetSocket, offset=0x29f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 9')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G10EMUXCS', width=32, block=evadcTargetSocket, offset=0x2df4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 10')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G11EMUXCS', width=32, block=evadcTargetSocket, offset=0x31f4,
             access='read-only', reset=0x00000000,
             doc='Ext. Multiplexer Channel Select Reg., Group 11')
field(name='EMUXCH', register=r, offset=0, width=16, access='read-write',
      doc='External Multiplexer Channel Select')

r = register('G0VFR', width=32, block=evadcTargetSocket, offset=0x05f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 0')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 0 15')

r = register('G1VFR', width=32, block=evadcTargetSocket, offset=0x09f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 1')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 1 15')

r = register('G2VFR', width=32, block=evadcTargetSocket, offset=0x0df8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 2')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 2 15')

r = register('G3VFR', width=32, block=evadcTargetSocket, offset=0x11f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 3')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 3 15')

r = register('G8VFR', width=32, block=evadcTargetSocket, offset=0x25f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 8')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 8 15')

r = register('G9VFR', width=32, block=evadcTargetSocket, offset=0x29f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 9')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 9 15')

r = register('G10VFR', width=32, block=evadcTargetSocket, offset=0x2df8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 10')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 10 15')

r = register('G11VFR', width=32, block=evadcTargetSocket, offset=0x31f8,
             access='read-only', reset=0x00000000,
             doc='Valid Flag Register, Group 11')
field(name='VF0', register=r, offset=0, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 0')
field(name='VF1', register=r, offset=1, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 1')
field(name='VF2', register=r, offset=2, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 2')
field(name='VF3', register=r, offset=3, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 3')
field(name='VF4', register=r, offset=4, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 4')
field(name='VF5', register=r, offset=5, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 5')
field(name='VF6', register=r, offset=6, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 6')
field(name='VF7', register=r, offset=7, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 7')
field(name='VF8', register=r, offset=8, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 8')
field(name='VF9', register=r, offset=9, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 9')
field(name='VF10', register=r, offset=10, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 10')
field(name='VF11', register=r, offset=11, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 11')
field(name='VF12', register=r, offset=12, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 12')
field(name='VF13', register=r, offset=13, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 13')
field(name='VF14', register=r, offset=14, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 14')
field(name='VF15', register=r, offset=15, width=1, access='read-write',
      doc='Valid Flag of Result Register 11 15')

r = register('G0CHCTR0', width=32, block=evadcTargetSocket, offset=0x0600,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR1', width=32, block=evadcTargetSocket, offset=0x0604,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR2', width=32, block=evadcTargetSocket, offset=0x0608,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR3', width=32, block=evadcTargetSocket, offset=0x060c,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR4', width=32, block=evadcTargetSocket, offset=0x0610,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR5', width=32, block=evadcTargetSocket, offset=0x0614,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR6', width=32, block=evadcTargetSocket, offset=0x0618,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0CHCTR7', width=32, block=evadcTargetSocket, offset=0x061c,
             access='read-only', reset=0x00000000,
             doc='Group 0, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR0', width=32, block=evadcTargetSocket, offset=0x0a00,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR1', width=32, block=evadcTargetSocket, offset=0x0a04,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR2', width=32, block=evadcTargetSocket, offset=0x0a08,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR3', width=32, block=evadcTargetSocket, offset=0x0a0c,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR4', width=32, block=evadcTargetSocket, offset=0x0a10,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR5', width=32, block=evadcTargetSocket, offset=0x0a14,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR6', width=32, block=evadcTargetSocket, offset=0x0a18,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G1CHCTR7', width=32, block=evadcTargetSocket, offset=0x0a1c,
             access='read-only', reset=0x00000000,
             doc='Group 1, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR0', width=32, block=evadcTargetSocket, offset=0x0e00,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR1', width=32, block=evadcTargetSocket, offset=0x0e04,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR2', width=32, block=evadcTargetSocket, offset=0x0e08,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR3', width=32, block=evadcTargetSocket, offset=0x0e0c,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR4', width=32, block=evadcTargetSocket, offset=0x0e10,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR5', width=32, block=evadcTargetSocket, offset=0x0e14,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR6', width=32, block=evadcTargetSocket, offset=0x0e18,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G2CHCTR7', width=32, block=evadcTargetSocket, offset=0x0e1c,
             access='read-only', reset=0x00000000,
             doc='Group 2, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR0', width=32, block=evadcTargetSocket, offset=0x1200,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR1', width=32, block=evadcTargetSocket, offset=0x1204,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR2', width=32, block=evadcTargetSocket, offset=0x1208,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR3', width=32, block=evadcTargetSocket, offset=0x120c,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR4', width=32, block=evadcTargetSocket, offset=0x1210,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR5', width=32, block=evadcTargetSocket, offset=0x1214,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR6', width=32, block=evadcTargetSocket, offset=0x1218,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G3CHCTR7', width=32, block=evadcTargetSocket, offset=0x121c,
             access='read-only', reset=0x00000000,
             doc='Group 3, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR0', width=32, block=evadcTargetSocket, offset=0x2600,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR1', width=32, block=evadcTargetSocket, offset=0x2604,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR2', width=32, block=evadcTargetSocket, offset=0x2608,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR3', width=32, block=evadcTargetSocket, offset=0x260c,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR4', width=32, block=evadcTargetSocket, offset=0x2610,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR5', width=32, block=evadcTargetSocket, offset=0x2614,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR6', width=32, block=evadcTargetSocket, offset=0x2618,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR7', width=32, block=evadcTargetSocket, offset=0x261c,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR8', width=32, block=evadcTargetSocket, offset=0x2620,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 8 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR9', width=32, block=evadcTargetSocket, offset=0x2624,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 9 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR10', width=32, block=evadcTargetSocket, offset=0x2628,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 10 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR11', width=32, block=evadcTargetSocket, offset=0x262c,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 11 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR12', width=32, block=evadcTargetSocket, offset=0x2630,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 12 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR13', width=32, block=evadcTargetSocket, offset=0x2634,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 13 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR14', width=32, block=evadcTargetSocket, offset=0x2638,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 14 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G8CHCTR15', width=32, block=evadcTargetSocket, offset=0x263c,
             access='read-only', reset=0x00000000,
             doc='Group 8, Channel 15 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR0', width=32, block=evadcTargetSocket, offset=0x2a00,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR1', width=32, block=evadcTargetSocket, offset=0x2a04,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR2', width=32, block=evadcTargetSocket, offset=0x2a08,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR3', width=32, block=evadcTargetSocket, offset=0x2a0c,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR4', width=32, block=evadcTargetSocket, offset=0x2a10,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR5', width=32, block=evadcTargetSocket, offset=0x2a14,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR6', width=32, block=evadcTargetSocket, offset=0x2a18,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR7', width=32, block=evadcTargetSocket, offset=0x2a1c,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR8', width=32, block=evadcTargetSocket, offset=0x2a20,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 8 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR9', width=32, block=evadcTargetSocket, offset=0x2a24,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 9 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR10', width=32, block=evadcTargetSocket, offset=0x2a28,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 10 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR11', width=32, block=evadcTargetSocket, offset=0x2a2c,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 11 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR12', width=32, block=evadcTargetSocket, offset=0x2a30,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 12 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR13', width=32, block=evadcTargetSocket, offset=0x2a34,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 13 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR14', width=32, block=evadcTargetSocket, offset=0x2a38,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 14 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G9CHCTR15', width=32, block=evadcTargetSocket, offset=0x2a3c,
             access='read-only', reset=0x00000000,
             doc='Group 9, Channel 15 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR0', width=32, block=evadcTargetSocket, offset=0x2e00,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR1', width=32, block=evadcTargetSocket, offset=0x2e04,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR2', width=32, block=evadcTargetSocket, offset=0x2e08,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR3', width=32, block=evadcTargetSocket, offset=0x2e0c,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR4', width=32, block=evadcTargetSocket, offset=0x2e10,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR5', width=32, block=evadcTargetSocket, offset=0x2e14,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR6', width=32, block=evadcTargetSocket, offset=0x2e18,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR7', width=32, block=evadcTargetSocket, offset=0x2e1c,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR8', width=32, block=evadcTargetSocket, offset=0x2e20,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 8 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR9', width=32, block=evadcTargetSocket, offset=0x2e24,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 9 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR10', width=32, block=evadcTargetSocket, offset=0x2e28,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 10 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR11', width=32, block=evadcTargetSocket, offset=0x2e2c,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 11 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR12', width=32, block=evadcTargetSocket, offset=0x2e30,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 12 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR13', width=32, block=evadcTargetSocket, offset=0x2e34,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 13 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR14', width=32, block=evadcTargetSocket, offset=0x2e38,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 14 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G10CHCTR15', width=32, block=evadcTargetSocket, offset=0x2e3c,
             access='read-only', reset=0x00000000,
             doc='Group 10, Channel 15 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR0', width=32, block=evadcTargetSocket, offset=0x3200,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 0 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR1', width=32, block=evadcTargetSocket, offset=0x3204,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 1 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR2', width=32, block=evadcTargetSocket, offset=0x3208,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 2 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR3', width=32, block=evadcTargetSocket, offset=0x320c,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 3 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR4', width=32, block=evadcTargetSocket, offset=0x3210,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 4 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR5', width=32, block=evadcTargetSocket, offset=0x3214,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 5 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR6', width=32, block=evadcTargetSocket, offset=0x3218,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 6 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR7', width=32, block=evadcTargetSocket, offset=0x321c,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 7 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR8', width=32, block=evadcTargetSocket, offset=0x3220,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 8 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR9', width=32, block=evadcTargetSocket, offset=0x3224,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 9 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR10', width=32, block=evadcTargetSocket, offset=0x3228,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 10 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR11', width=32, block=evadcTargetSocket, offset=0x322c,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 11 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR12', width=32, block=evadcTargetSocket, offset=0x3230,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 12 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR13', width=32, block=evadcTargetSocket, offset=0x3234,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 13 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR14', width=32, block=evadcTargetSocket, offset=0x3238,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 14 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G11CHCTR15', width=32, block=evadcTargetSocket, offset=0x323c,
             access='read-only', reset=0x00000000,
             doc='Group 11, Channel 15 Control Register')
field(name='ICLSEL', register=r, offset=0, width=2, access='read-write',
      doc='Input Class Select')
field(name='BNDSELL', register=r, offset=4, width=2, access='read-write',
      doc='Lower Boundary Select')
field(name='BNDSELU', register=r, offset=6, width=2, access='read-write',
      doc='Upper Boundary Select')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='SYNC', register=r, offset=10, width=1, access='read-write',
      doc='Synchronization Request')
field(name='REFSEL', register=r, offset=11, width=1, access='read-write',
      doc='Reference Input Selection')
field(name='BNDSELX', register=r, offset=12, width=4, access='read-write',
      doc='BoundaryExtension')
field(name='RESREG', register=r, offset=16, width=4, access='read-write',
      doc='Result Register')
field(name='RESTGT', register=r, offset=20, width=1, access='read-write',
      doc='Result Target')
field(name='RESPOS', register=r, offset=21, width=1, access='read-write',
      doc='Result Position')
field(name='BWDCH', register=r, offset=28, width=2, access='read-write',
      doc='Broken Wire Detection Channel')
field(name='BWDEN', register=r, offset=30, width=1, access='read-write',
      doc='Broken Wire Detection Enable')

r = register('G0RCR0', width=32, block=evadcTargetSocket, offset=0x0680,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR1', width=32, block=evadcTargetSocket, offset=0x0684,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR2', width=32, block=evadcTargetSocket, offset=0x0688,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR3', width=32, block=evadcTargetSocket, offset=0x068c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR4', width=32, block=evadcTargetSocket, offset=0x0690,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR5', width=32, block=evadcTargetSocket, offset=0x0694,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR6', width=32, block=evadcTargetSocket, offset=0x0698,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR7', width=32, block=evadcTargetSocket, offset=0x069c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR8', width=32, block=evadcTargetSocket, offset=0x06a0,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR9', width=32, block=evadcTargetSocket, offset=0x06a4,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR10', width=32, block=evadcTargetSocket, offset=0x06a8,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR11', width=32, block=evadcTargetSocket, offset=0x06ac,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR12', width=32, block=evadcTargetSocket, offset=0x06b0,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR13', width=32, block=evadcTargetSocket, offset=0x06b4,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR14', width=32, block=evadcTargetSocket, offset=0x06b8,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RCR15', width=32, block=evadcTargetSocket, offset=0x06bc,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR0', width=32, block=evadcTargetSocket, offset=0x0a80,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR1', width=32, block=evadcTargetSocket, offset=0x0a84,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR2', width=32, block=evadcTargetSocket, offset=0x0a88,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR3', width=32, block=evadcTargetSocket, offset=0x0a8c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR4', width=32, block=evadcTargetSocket, offset=0x0a90,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR5', width=32, block=evadcTargetSocket, offset=0x0a94,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR6', width=32, block=evadcTargetSocket, offset=0x0a98,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR7', width=32, block=evadcTargetSocket, offset=0x0a9c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR8', width=32, block=evadcTargetSocket, offset=0x0aa0,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR9', width=32, block=evadcTargetSocket, offset=0x0aa4,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR10', width=32, block=evadcTargetSocket, offset=0x0aa8,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR11', width=32, block=evadcTargetSocket, offset=0x0aac,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR12', width=32, block=evadcTargetSocket, offset=0x0ab0,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR13', width=32, block=evadcTargetSocket, offset=0x0ab4,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR14', width=32, block=evadcTargetSocket, offset=0x0ab8,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G1RCR15', width=32, block=evadcTargetSocket, offset=0x0abc,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR0', width=32, block=evadcTargetSocket, offset=0x0e80,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR1', width=32, block=evadcTargetSocket, offset=0x0e84,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR2', width=32, block=evadcTargetSocket, offset=0x0e88,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR3', width=32, block=evadcTargetSocket, offset=0x0e8c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR4', width=32, block=evadcTargetSocket, offset=0x0e90,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR5', width=32, block=evadcTargetSocket, offset=0x0e94,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR6', width=32, block=evadcTargetSocket, offset=0x0e98,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR7', width=32, block=evadcTargetSocket, offset=0x0e9c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR8', width=32, block=evadcTargetSocket, offset=0x0ea0,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR9', width=32, block=evadcTargetSocket, offset=0x0ea4,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR10', width=32, block=evadcTargetSocket, offset=0x0ea8,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR11', width=32, block=evadcTargetSocket, offset=0x0eac,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR12', width=32, block=evadcTargetSocket, offset=0x0eb0,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR13', width=32, block=evadcTargetSocket, offset=0x0eb4,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR14', width=32, block=evadcTargetSocket, offset=0x0eb8,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G2RCR15', width=32, block=evadcTargetSocket, offset=0x0ebc,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR0', width=32, block=evadcTargetSocket, offset=0x1280,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR1', width=32, block=evadcTargetSocket, offset=0x1284,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR2', width=32, block=evadcTargetSocket, offset=0x1288,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR3', width=32, block=evadcTargetSocket, offset=0x128c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR4', width=32, block=evadcTargetSocket, offset=0x1290,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR5', width=32, block=evadcTargetSocket, offset=0x1294,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR6', width=32, block=evadcTargetSocket, offset=0x1298,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR7', width=32, block=evadcTargetSocket, offset=0x129c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR8', width=32, block=evadcTargetSocket, offset=0x12a0,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR9', width=32, block=evadcTargetSocket, offset=0x12a4,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR10', width=32, block=evadcTargetSocket, offset=0x12a8,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR11', width=32, block=evadcTargetSocket, offset=0x12ac,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR12', width=32, block=evadcTargetSocket, offset=0x12b0,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR13', width=32, block=evadcTargetSocket, offset=0x12b4,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR14', width=32, block=evadcTargetSocket, offset=0x12b8,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G3RCR15', width=32, block=evadcTargetSocket, offset=0x12bc,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR0', width=32, block=evadcTargetSocket, offset=0x2680,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR1', width=32, block=evadcTargetSocket, offset=0x2684,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR2', width=32, block=evadcTargetSocket, offset=0x2688,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR3', width=32, block=evadcTargetSocket, offset=0x268c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR4', width=32, block=evadcTargetSocket, offset=0x2690,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR5', width=32, block=evadcTargetSocket, offset=0x2694,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR6', width=32, block=evadcTargetSocket, offset=0x2698,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR7', width=32, block=evadcTargetSocket, offset=0x269c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR8', width=32, block=evadcTargetSocket, offset=0x26a0,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR9', width=32, block=evadcTargetSocket, offset=0x26a4,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR10', width=32, block=evadcTargetSocket, offset=0x26a8,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR11', width=32, block=evadcTargetSocket, offset=0x26ac,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR12', width=32, block=evadcTargetSocket, offset=0x26b0,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR13', width=32, block=evadcTargetSocket, offset=0x26b4,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR14', width=32, block=evadcTargetSocket, offset=0x26b8,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G8RCR15', width=32, block=evadcTargetSocket, offset=0x26bc,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR0', width=32, block=evadcTargetSocket, offset=0x2a80,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR1', width=32, block=evadcTargetSocket, offset=0x2a84,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR2', width=32, block=evadcTargetSocket, offset=0x2a88,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR3', width=32, block=evadcTargetSocket, offset=0x2a8c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR4', width=32, block=evadcTargetSocket, offset=0x2a90,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR5', width=32, block=evadcTargetSocket, offset=0x2a94,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR6', width=32, block=evadcTargetSocket, offset=0x2a98,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR7', width=32, block=evadcTargetSocket, offset=0x2a9c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR8', width=32, block=evadcTargetSocket, offset=0x2aa0,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR9', width=32, block=evadcTargetSocket, offset=0x2aa4,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR10', width=32, block=evadcTargetSocket, offset=0x2aa8,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR11', width=32, block=evadcTargetSocket, offset=0x2aac,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR12', width=32, block=evadcTargetSocket, offset=0x2ab0,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR13', width=32, block=evadcTargetSocket, offset=0x2ab4,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR14', width=32, block=evadcTargetSocket, offset=0x2ab8,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G9RCR15', width=32, block=evadcTargetSocket, offset=0x2abc,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR0', width=32, block=evadcTargetSocket, offset=0x2e80,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR1', width=32, block=evadcTargetSocket, offset=0x2e84,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR2', width=32, block=evadcTargetSocket, offset=0x2e88,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR3', width=32, block=evadcTargetSocket, offset=0x2e8c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR4', width=32, block=evadcTargetSocket, offset=0x2e90,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR5', width=32, block=evadcTargetSocket, offset=0x2e94,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR6', width=32, block=evadcTargetSocket, offset=0x2e98,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR7', width=32, block=evadcTargetSocket, offset=0x2e9c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR8', width=32, block=evadcTargetSocket, offset=0x2ea0,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR9', width=32, block=evadcTargetSocket, offset=0x2ea4,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR10', width=32, block=evadcTargetSocket, offset=0x2ea8,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR11', width=32, block=evadcTargetSocket, offset=0x2eac,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR12', width=32, block=evadcTargetSocket, offset=0x2eb0,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR13', width=32, block=evadcTargetSocket, offset=0x2eb4,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR14', width=32, block=evadcTargetSocket, offset=0x2eb8,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G10RCR15', width=32, block=evadcTargetSocket, offset=0x2ebc,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR0', width=32, block=evadcTargetSocket, offset=0x3280,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 0')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR1', width=32, block=evadcTargetSocket, offset=0x3284,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 1')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR2', width=32, block=evadcTargetSocket, offset=0x3288,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 2')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR3', width=32, block=evadcTargetSocket, offset=0x328c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 3')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR4', width=32, block=evadcTargetSocket, offset=0x3290,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 4')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR5', width=32, block=evadcTargetSocket, offset=0x3294,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 5')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR6', width=32, block=evadcTargetSocket, offset=0x3298,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 6')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR7', width=32, block=evadcTargetSocket, offset=0x329c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 7')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR8', width=32, block=evadcTargetSocket, offset=0x32a0,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 8')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR9', width=32, block=evadcTargetSocket, offset=0x32a4,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 9')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR10', width=32, block=evadcTargetSocket, offset=0x32a8,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 10')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR11', width=32, block=evadcTargetSocket, offset=0x32ac,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 11')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR12', width=32, block=evadcTargetSocket, offset=0x32b0,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 12')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR13', width=32, block=evadcTargetSocket, offset=0x32b4,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 13')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR14', width=32, block=evadcTargetSocket, offset=0x32b8,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 14')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G11RCR15', width=32, block=evadcTargetSocket, offset=0x32bc,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Control Register 15')
field(name='DRCTR', register=r, offset=16, width=4, access='read-write',
      doc='Data Reduction Control')
field(name='DMM', register=r, offset=20, width=2, access='read-write',
      doc='Data Modification Mode')
field(name='WFR', register=r, offset=24, width=1, access='read-write',
      doc='Wait-for-Read Mode Enable')
field(name='FEN', register=r, offset=25, width=2, access='read-write',
      doc='FIFO Mode Enable')
field(name='SRGEN', register=r, offset=31, width=1, access='read-write',
      doc='Service Request Generation Enable')

r = register('G0RES0', width=32, block=evadcTargetSocket, offset=0x0700,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES1', width=32, block=evadcTargetSocket, offset=0x0704,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES2', width=32, block=evadcTargetSocket, offset=0x0708,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES3', width=32, block=evadcTargetSocket, offset=0x070c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES4', width=32, block=evadcTargetSocket, offset=0x0710,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES5', width=32, block=evadcTargetSocket, offset=0x0714,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES6', width=32, block=evadcTargetSocket, offset=0x0718,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES7', width=32, block=evadcTargetSocket, offset=0x071c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES8', width=32, block=evadcTargetSocket, offset=0x0720,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES9', width=32, block=evadcTargetSocket, offset=0x0724,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES10', width=32, block=evadcTargetSocket, offset=0x0728,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES11', width=32, block=evadcTargetSocket, offset=0x072c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES12', width=32, block=evadcTargetSocket, offset=0x0730,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES13', width=32, block=evadcTargetSocket, offset=0x0734,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES14', width=32, block=evadcTargetSocket, offset=0x0738,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RES15', width=32, block=evadcTargetSocket, offset=0x073c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES0', width=32, block=evadcTargetSocket, offset=0x0b00,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES1', width=32, block=evadcTargetSocket, offset=0x0b04,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES2', width=32, block=evadcTargetSocket, offset=0x0b08,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES3', width=32, block=evadcTargetSocket, offset=0x0b0c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES4', width=32, block=evadcTargetSocket, offset=0x0b10,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES5', width=32, block=evadcTargetSocket, offset=0x0b14,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES6', width=32, block=evadcTargetSocket, offset=0x0b18,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES7', width=32, block=evadcTargetSocket, offset=0x0b1c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES8', width=32, block=evadcTargetSocket, offset=0x0b20,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES9', width=32, block=evadcTargetSocket, offset=0x0b24,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES10', width=32, block=evadcTargetSocket, offset=0x0b28,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES11', width=32, block=evadcTargetSocket, offset=0x0b2c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES12', width=32, block=evadcTargetSocket, offset=0x0b30,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES13', width=32, block=evadcTargetSocket, offset=0x0b34,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES14', width=32, block=evadcTargetSocket, offset=0x0b38,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RES15', width=32, block=evadcTargetSocket, offset=0x0b3c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES0', width=32, block=evadcTargetSocket, offset=0x0f00,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES1', width=32, block=evadcTargetSocket, offset=0x0f04,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES2', width=32, block=evadcTargetSocket, offset=0x0f08,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES3', width=32, block=evadcTargetSocket, offset=0x0f0c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES4', width=32, block=evadcTargetSocket, offset=0x0f10,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES5', width=32, block=evadcTargetSocket, offset=0x0f14,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES6', width=32, block=evadcTargetSocket, offset=0x0f18,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES7', width=32, block=evadcTargetSocket, offset=0x0f1c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES8', width=32, block=evadcTargetSocket, offset=0x0f20,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES9', width=32, block=evadcTargetSocket, offset=0x0f24,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES10', width=32, block=evadcTargetSocket, offset=0x0f28,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES11', width=32, block=evadcTargetSocket, offset=0x0f2c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES12', width=32, block=evadcTargetSocket, offset=0x0f30,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES13', width=32, block=evadcTargetSocket, offset=0x0f34,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES14', width=32, block=evadcTargetSocket, offset=0x0f38,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RES15', width=32, block=evadcTargetSocket, offset=0x0f3c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES0', width=32, block=evadcTargetSocket, offset=0x1300,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES1', width=32, block=evadcTargetSocket, offset=0x1304,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES2', width=32, block=evadcTargetSocket, offset=0x1308,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES3', width=32, block=evadcTargetSocket, offset=0x130c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES4', width=32, block=evadcTargetSocket, offset=0x1310,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES5', width=32, block=evadcTargetSocket, offset=0x1314,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES6', width=32, block=evadcTargetSocket, offset=0x1318,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES7', width=32, block=evadcTargetSocket, offset=0x131c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES8', width=32, block=evadcTargetSocket, offset=0x1320,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES9', width=32, block=evadcTargetSocket, offset=0x1324,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES10', width=32, block=evadcTargetSocket, offset=0x1328,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES11', width=32, block=evadcTargetSocket, offset=0x132c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES12', width=32, block=evadcTargetSocket, offset=0x1330,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES13', width=32, block=evadcTargetSocket, offset=0x1334,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES14', width=32, block=evadcTargetSocket, offset=0x1338,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RES15', width=32, block=evadcTargetSocket, offset=0x133c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES0', width=32, block=evadcTargetSocket, offset=0x2700,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES1', width=32, block=evadcTargetSocket, offset=0x2704,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES2', width=32, block=evadcTargetSocket, offset=0x2708,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES3', width=32, block=evadcTargetSocket, offset=0x270c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES4', width=32, block=evadcTargetSocket, offset=0x2710,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES5', width=32, block=evadcTargetSocket, offset=0x2714,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES6', width=32, block=evadcTargetSocket, offset=0x2718,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES7', width=32, block=evadcTargetSocket, offset=0x271c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES8', width=32, block=evadcTargetSocket, offset=0x2720,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES9', width=32, block=evadcTargetSocket, offset=0x2724,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES10', width=32, block=evadcTargetSocket, offset=0x2728,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES11', width=32, block=evadcTargetSocket, offset=0x272c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES12', width=32, block=evadcTargetSocket, offset=0x2730,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES13', width=32, block=evadcTargetSocket, offset=0x2734,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES14', width=32, block=evadcTargetSocket, offset=0x2738,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RES15', width=32, block=evadcTargetSocket, offset=0x273c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES0', width=32, block=evadcTargetSocket, offset=0x2b00,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES1', width=32, block=evadcTargetSocket, offset=0x2b04,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES2', width=32, block=evadcTargetSocket, offset=0x2b08,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES3', width=32, block=evadcTargetSocket, offset=0x2b0c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES4', width=32, block=evadcTargetSocket, offset=0x2b10,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES5', width=32, block=evadcTargetSocket, offset=0x2b14,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES6', width=32, block=evadcTargetSocket, offset=0x2b18,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES7', width=32, block=evadcTargetSocket, offset=0x2b1c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES8', width=32, block=evadcTargetSocket, offset=0x2b20,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES9', width=32, block=evadcTargetSocket, offset=0x2b24,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES10', width=32, block=evadcTargetSocket, offset=0x2b28,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES11', width=32, block=evadcTargetSocket, offset=0x2b2c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES12', width=32, block=evadcTargetSocket, offset=0x2b30,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES13', width=32, block=evadcTargetSocket, offset=0x2b34,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES14', width=32, block=evadcTargetSocket, offset=0x2b38,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RES15', width=32, block=evadcTargetSocket, offset=0x2b3c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES0', width=32, block=evadcTargetSocket, offset=0x2f00,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES1', width=32, block=evadcTargetSocket, offset=0x2f04,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES2', width=32, block=evadcTargetSocket, offset=0x2f08,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES3', width=32, block=evadcTargetSocket, offset=0x2f0c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES4', width=32, block=evadcTargetSocket, offset=0x2f10,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES5', width=32, block=evadcTargetSocket, offset=0x2f14,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES6', width=32, block=evadcTargetSocket, offset=0x2f18,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES7', width=32, block=evadcTargetSocket, offset=0x2f1c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES8', width=32, block=evadcTargetSocket, offset=0x2f20,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES9', width=32, block=evadcTargetSocket, offset=0x2f24,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES10', width=32, block=evadcTargetSocket, offset=0x2f28,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES11', width=32, block=evadcTargetSocket, offset=0x2f2c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES12', width=32, block=evadcTargetSocket, offset=0x2f30,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES13', width=32, block=evadcTargetSocket, offset=0x2f34,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES14', width=32, block=evadcTargetSocket, offset=0x2f38,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RES15', width=32, block=evadcTargetSocket, offset=0x2f3c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES0', width=32, block=evadcTargetSocket, offset=0x3300,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 0')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES1', width=32, block=evadcTargetSocket, offset=0x3304,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 1')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES2', width=32, block=evadcTargetSocket, offset=0x3308,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 2')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES3', width=32, block=evadcTargetSocket, offset=0x330c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 3')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES4', width=32, block=evadcTargetSocket, offset=0x3310,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 4')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES5', width=32, block=evadcTargetSocket, offset=0x3314,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 5')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES6', width=32, block=evadcTargetSocket, offset=0x3318,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 6')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES7', width=32, block=evadcTargetSocket, offset=0x331c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 7')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES8', width=32, block=evadcTargetSocket, offset=0x3320,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 8')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES9', width=32, block=evadcTargetSocket, offset=0x3324,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 9')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES10', width=32, block=evadcTargetSocket, offset=0x3328,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 10')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES11', width=32, block=evadcTargetSocket, offset=0x332c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 11')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES12', width=32, block=evadcTargetSocket, offset=0x3330,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 12')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES13', width=32, block=evadcTargetSocket, offset=0x3334,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 13')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES14', width=32, block=evadcTargetSocket, offset=0x3338,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 14')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RES15', width=32, block=evadcTargetSocket, offset=0x333c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Register 15')
field(name='RESULT', register=r, offset=0, width=16, access='read-write',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD0', width=32, block=evadcTargetSocket, offset=0x0780,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD1', width=32, block=evadcTargetSocket, offset=0x0784,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD2', width=32, block=evadcTargetSocket, offset=0x0788,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD3', width=32, block=evadcTargetSocket, offset=0x078c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD4', width=32, block=evadcTargetSocket, offset=0x0790,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD5', width=32, block=evadcTargetSocket, offset=0x0794,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD6', width=32, block=evadcTargetSocket, offset=0x0798,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD7', width=32, block=evadcTargetSocket, offset=0x079c,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD8', width=32, block=evadcTargetSocket, offset=0x07a0,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD9', width=32, block=evadcTargetSocket, offset=0x07a4,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD10', width=32, block=evadcTargetSocket, offset=0x07a8,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD11', width=32, block=evadcTargetSocket, offset=0x07ac,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD12', width=32, block=evadcTargetSocket, offset=0x07b0,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD13', width=32, block=evadcTargetSocket, offset=0x07b4,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD14', width=32, block=evadcTargetSocket, offset=0x07b8,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G0RESD15', width=32, block=evadcTargetSocket, offset=0x07bc,
             access='read-only', reset=0x00000000,
             doc='Group 0 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD0', width=32, block=evadcTargetSocket, offset=0x0b80,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD1', width=32, block=evadcTargetSocket, offset=0x0b84,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD2', width=32, block=evadcTargetSocket, offset=0x0b88,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD3', width=32, block=evadcTargetSocket, offset=0x0b8c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD4', width=32, block=evadcTargetSocket, offset=0x0b90,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD5', width=32, block=evadcTargetSocket, offset=0x0b94,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD6', width=32, block=evadcTargetSocket, offset=0x0b98,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD7', width=32, block=evadcTargetSocket, offset=0x0b9c,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD8', width=32, block=evadcTargetSocket, offset=0x0ba0,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD9', width=32, block=evadcTargetSocket, offset=0x0ba4,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD10', width=32, block=evadcTargetSocket, offset=0x0ba8,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD11', width=32, block=evadcTargetSocket, offset=0x0bac,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD12', width=32, block=evadcTargetSocket, offset=0x0bb0,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD13', width=32, block=evadcTargetSocket, offset=0x0bb4,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD14', width=32, block=evadcTargetSocket, offset=0x0bb8,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G1RESD15', width=32, block=evadcTargetSocket, offset=0x0bbc,
             access='read-only', reset=0x00000000,
             doc='Group 1 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD0', width=32, block=evadcTargetSocket, offset=0x0f80,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD1', width=32, block=evadcTargetSocket, offset=0x0f84,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD2', width=32, block=evadcTargetSocket, offset=0x0f88,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD3', width=32, block=evadcTargetSocket, offset=0x0f8c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD4', width=32, block=evadcTargetSocket, offset=0x0f90,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD5', width=32, block=evadcTargetSocket, offset=0x0f94,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD6', width=32, block=evadcTargetSocket, offset=0x0f98,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD7', width=32, block=evadcTargetSocket, offset=0x0f9c,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD8', width=32, block=evadcTargetSocket, offset=0x0fa0,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD9', width=32, block=evadcTargetSocket, offset=0x0fa4,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD10', width=32, block=evadcTargetSocket, offset=0x0fa8,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD11', width=32, block=evadcTargetSocket, offset=0x0fac,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD12', width=32, block=evadcTargetSocket, offset=0x0fb0,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD13', width=32, block=evadcTargetSocket, offset=0x0fb4,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD14', width=32, block=evadcTargetSocket, offset=0x0fb8,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G2RESD15', width=32, block=evadcTargetSocket, offset=0x0fbc,
             access='read-only', reset=0x00000000,
             doc='Group 2 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD0', width=32, block=evadcTargetSocket, offset=0x1380,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD1', width=32, block=evadcTargetSocket, offset=0x1384,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD2', width=32, block=evadcTargetSocket, offset=0x1388,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD3', width=32, block=evadcTargetSocket, offset=0x138c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD4', width=32, block=evadcTargetSocket, offset=0x1390,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD5', width=32, block=evadcTargetSocket, offset=0x1394,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD6', width=32, block=evadcTargetSocket, offset=0x1398,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD7', width=32, block=evadcTargetSocket, offset=0x139c,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD8', width=32, block=evadcTargetSocket, offset=0x13a0,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD9', width=32, block=evadcTargetSocket, offset=0x13a4,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD10', width=32, block=evadcTargetSocket, offset=0x13a8,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD11', width=32, block=evadcTargetSocket, offset=0x13ac,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD12', width=32, block=evadcTargetSocket, offset=0x13b0,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD13', width=32, block=evadcTargetSocket, offset=0x13b4,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD14', width=32, block=evadcTargetSocket, offset=0x13b8,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G3RESD15', width=32, block=evadcTargetSocket, offset=0x13bc,
             access='read-only', reset=0x00000000,
             doc='Group 3 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD0', width=32, block=evadcTargetSocket, offset=0x2780,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD1', width=32, block=evadcTargetSocket, offset=0x2784,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD2', width=32, block=evadcTargetSocket, offset=0x2788,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD3', width=32, block=evadcTargetSocket, offset=0x278c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD4', width=32, block=evadcTargetSocket, offset=0x2790,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD5', width=32, block=evadcTargetSocket, offset=0x2794,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD6', width=32, block=evadcTargetSocket, offset=0x2798,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD7', width=32, block=evadcTargetSocket, offset=0x279c,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD8', width=32, block=evadcTargetSocket, offset=0x27a0,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD9', width=32, block=evadcTargetSocket, offset=0x27a4,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD10', width=32, block=evadcTargetSocket, offset=0x27a8,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD11', width=32, block=evadcTargetSocket, offset=0x27ac,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD12', width=32, block=evadcTargetSocket, offset=0x27b0,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD13', width=32, block=evadcTargetSocket, offset=0x27b4,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD14', width=32, block=evadcTargetSocket, offset=0x27b8,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G8RESD15', width=32, block=evadcTargetSocket, offset=0x27bc,
             access='read-only', reset=0x00000000,
             doc='Group 8 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD0', width=32, block=evadcTargetSocket, offset=0x2b80,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD1', width=32, block=evadcTargetSocket, offset=0x2b84,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD2', width=32, block=evadcTargetSocket, offset=0x2b88,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD3', width=32, block=evadcTargetSocket, offset=0x2b8c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD4', width=32, block=evadcTargetSocket, offset=0x2b90,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD5', width=32, block=evadcTargetSocket, offset=0x2b94,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD6', width=32, block=evadcTargetSocket, offset=0x2b98,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD7', width=32, block=evadcTargetSocket, offset=0x2b9c,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD8', width=32, block=evadcTargetSocket, offset=0x2ba0,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD9', width=32, block=evadcTargetSocket, offset=0x2ba4,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD10', width=32, block=evadcTargetSocket, offset=0x2ba8,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD11', width=32, block=evadcTargetSocket, offset=0x2bac,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD12', width=32, block=evadcTargetSocket, offset=0x2bb0,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD13', width=32, block=evadcTargetSocket, offset=0x2bb4,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD14', width=32, block=evadcTargetSocket, offset=0x2bb8,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G9RESD15', width=32, block=evadcTargetSocket, offset=0x2bbc,
             access='read-only', reset=0x00000000,
             doc='Group 9 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD0', width=32, block=evadcTargetSocket, offset=0x2f80,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD1', width=32, block=evadcTargetSocket, offset=0x2f84,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD2', width=32, block=evadcTargetSocket, offset=0x2f88,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD3', width=32, block=evadcTargetSocket, offset=0x2f8c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD4', width=32, block=evadcTargetSocket, offset=0x2f90,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD5', width=32, block=evadcTargetSocket, offset=0x2f94,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD6', width=32, block=evadcTargetSocket, offset=0x2f98,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD7', width=32, block=evadcTargetSocket, offset=0x2f9c,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD8', width=32, block=evadcTargetSocket, offset=0x2fa0,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD9', width=32, block=evadcTargetSocket, offset=0x2fa4,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD10', width=32, block=evadcTargetSocket, offset=0x2fa8,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD11', width=32, block=evadcTargetSocket, offset=0x2fac,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD12', width=32, block=evadcTargetSocket, offset=0x2fb0,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD13', width=32, block=evadcTargetSocket, offset=0x2fb4,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD14', width=32, block=evadcTargetSocket, offset=0x2fb8,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G10RESD15', width=32, block=evadcTargetSocket, offset=0x2fbc,
             access='read-only', reset=0x00000000,
             doc='Group 10 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD0', width=32, block=evadcTargetSocket, offset=0x3380,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 0, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD1', width=32, block=evadcTargetSocket, offset=0x3384,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 1, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD2', width=32, block=evadcTargetSocket, offset=0x3388,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 2, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD3', width=32, block=evadcTargetSocket, offset=0x338c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 3, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD4', width=32, block=evadcTargetSocket, offset=0x3390,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 4, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD5', width=32, block=evadcTargetSocket, offset=0x3394,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 5, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD6', width=32, block=evadcTargetSocket, offset=0x3398,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 6, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD7', width=32, block=evadcTargetSocket, offset=0x339c,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 7, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD8', width=32, block=evadcTargetSocket, offset=0x33a0,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 8, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD9', width=32, block=evadcTargetSocket, offset=0x33a4,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 9, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD10', width=32, block=evadcTargetSocket, offset=0x33a8,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 10, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD11', width=32, block=evadcTargetSocket, offset=0x33ac,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 11, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD12', width=32, block=evadcTargetSocket, offset=0x33b0,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 12, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD13', width=32, block=evadcTargetSocket, offset=0x33b4,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 13, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD14', width=32, block=evadcTargetSocket, offset=0x33b8,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 14, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('G11RESD15', width=32, block=evadcTargetSocket, offset=0x33bc,
             access='read-only', reset=0x00000000,
             doc='Group 11 Result Reg. 15, Debug')
field(name='RESULT', register=r, offset=0, width=16, access='read-only',
      doc='Result of Most Recent Conversion')
field(name='DRC', register=r, offset=16, width=4, access='read-only',
      doc='Data Reduction Counter')
field(name='CHNR', register=r, offset=20, width=5, access='read-only',
      doc='Channel Number')
field(name='EMUX', register=r, offset=25, width=3, access='read-only',
      doc='External Multiplexer Setting')
field(name='CRS', register=r, offset=28, width=2, access='read-only',
      doc='Converted Request Source')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('FC0FCCTRL', width=32, block=evadcTargetSocket, offset=0x3400,
             access='read-only', reset=0x00000C20,
             doc='Fast Compare Control Register, FC Channel 0')
field(name='STCF', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Fast Comparisons')
field(name='RPE', register=r, offset=5, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='AIPF', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Enable for Fast Comparisons')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='DIVA', register=r, offset=10, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='CPWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Control Parameters')
field(name='XTSEL', register=r, offset=16, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=20, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=21, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTPOL', register=r, offset=23, width=1, access='read-write',
      doc='External Trigger Polarity')
field(name='GTMODE', register=r, offset=24, width=2, access='read-write',
      doc='Gate Operating Mode')
field(name='FCCHNR', register=r, offset=26, width=5, access='read-write',
      doc='Fast Compare Channel: Cannel Number')
field(name='XTWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Trigger/Gate Configuration')

r = register('FC1FCCTRL', width=32, block=evadcTargetSocket, offset=0x3500,
             access='read-only', reset=0x00000C20,
             doc='Fast Compare Control Register, FC Channel 1')
field(name='STCF', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Fast Comparisons')
field(name='RPE', register=r, offset=5, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='AIPF', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Enable for Fast Comparisons')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='DIVA', register=r, offset=10, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='CPWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Control Parameters')
field(name='XTSEL', register=r, offset=16, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=20, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=21, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTPOL', register=r, offset=23, width=1, access='read-write',
      doc='External Trigger Polarity')
field(name='GTMODE', register=r, offset=24, width=2, access='read-write',
      doc='Gate Operating Mode')
field(name='FCCHNR', register=r, offset=26, width=5, access='read-write',
      doc='Fast Compare Channel: Cannel Number')
field(name='XTWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Trigger/Gate Configuration')

r = register('FC2FCCTRL', width=32, block=evadcTargetSocket, offset=0x3600,
             access='read-only', reset=0x00000C20,
             doc='Fast Compare Control Register, FC Channel 2')
field(name='STCF', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Fast Comparisons')
field(name='RPE', register=r, offset=5, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='AIPF', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Enable for Fast Comparisons')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='DIVA', register=r, offset=10, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='CPWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Control Parameters')
field(name='XTSEL', register=r, offset=16, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=20, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=21, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTPOL', register=r, offset=23, width=1, access='read-write',
      doc='External Trigger Polarity')
field(name='GTMODE', register=r, offset=24, width=2, access='read-write',
      doc='Gate Operating Mode')
field(name='FCCHNR', register=r, offset=26, width=5, access='read-write',
      doc='Fast Compare Channel: Cannel Number')
field(name='XTWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Trigger/Gate Configuration')

r = register('FC3FCCTRL', width=32, block=evadcTargetSocket, offset=0x3700,
             access='read-only', reset=0x00000C20,
             doc='Fast Compare Control Register, FC Channel 3')
field(name='STCF', register=r, offset=0, width=5, access='read-write',
      doc='Sample Time Control for Fast Comparisons')
field(name='RPE', register=r, offset=5, width=1, access='read-write',
      doc='Reference Precharge Enable')
field(name='AIPF', register=r, offset=6, width=2, access='read-write',
      doc='Analog Input Precharge Enable for Fast Comparisons')
field(name='CHEVMODE', register=r, offset=8, width=2, access='read-write',
      doc='Channel Event Mode')
field(name='DIVA', register=r, offset=10, width=5, access='read-write',
      doc='Divider Factor for the Analog Internal Clock')
field(name='CPWC', register=r, offset=15, width=1, access='write-only',
      doc='Write Control for Control Parameters')
field(name='XTSEL', register=r, offset=16, width=4, access='read-write',
      doc='External Trigger Input Selection')
field(name='XTLVL', register=r, offset=20, width=1, access='read-only',
      doc='External Trigger Level')
field(name='XTMODE', register=r, offset=21, width=2, access='read-write',
      doc='Trigger Operating Mode')
field(name='XTPOL', register=r, offset=23, width=1, access='read-write',
      doc='External Trigger Polarity')
field(name='GTMODE', register=r, offset=24, width=2, access='read-write',
      doc='Gate Operating Mode')
field(name='FCCHNR', register=r, offset=26, width=5, access='read-write',
      doc='Fast Compare Channel: Cannel Number')
field(name='XTWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Trigger/Gate Configuration')

r = register('FC0FCM', width=32, block=evadcTargetSocket, offset=0x3404,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Mode Register, FC Channel 0')
field(name='RUNCOMP', register=r, offset=0, width=2, access='read-write',
      doc='Run Control for Compare Channel')
field(name='RUNRAMP', register=r, offset=2, width=2, access='read-write',
      doc='Run Control for Ramp')
field(name='FCRDIR', register=r, offset=4, width=1, access='read-write',
      doc='Fast Compare Ramp Direction')
field(name='ANON', register=r, offset=5, width=1, access='read-write',
      doc='Analog Converter Control')
field(name='ACSD', register=r, offset=6, width=2, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='FCTRIV', register=r, offset=8, width=8, access='read-write',
      doc='Fast Compare Trigger Interval')
field(name='SRG', register=r, offset=16, width=2, access='read-write',
      doc='Service Request Generation')
field(name='AUE', register=r, offset=18, width=2, access='read-write',
      doc='Automatic Update Enable')
field(name='SSE', register=r, offset=20, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='FCMWC', register=r, offset=21, width=1, access='write-only',
      doc='Write Control for Fast Compare Mode Configuration')
field(name='FCREF', register=r, offset=22, width=10, access='read-write',
      doc='Fast Compare Reference Value')

r = register('FC1FCM', width=32, block=evadcTargetSocket, offset=0x3504,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Mode Register, FC Channel 1')
field(name='RUNCOMP', register=r, offset=0, width=2, access='read-write',
      doc='Run Control for Compare Channel')
field(name='RUNRAMP', register=r, offset=2, width=2, access='read-write',
      doc='Run Control for Ramp')
field(name='FCRDIR', register=r, offset=4, width=1, access='read-write',
      doc='Fast Compare Ramp Direction')
field(name='ANON', register=r, offset=5, width=1, access='read-write',
      doc='Analog Converter Control')
field(name='ACSD', register=r, offset=6, width=2, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='FCTRIV', register=r, offset=8, width=8, access='read-write',
      doc='Fast Compare Trigger Interval')
field(name='SRG', register=r, offset=16, width=2, access='read-write',
      doc='Service Request Generation')
field(name='AUE', register=r, offset=18, width=2, access='read-write',
      doc='Automatic Update Enable')
field(name='SSE', register=r, offset=20, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='FCMWC', register=r, offset=21, width=1, access='write-only',
      doc='Write Control for Fast Compare Mode Configuration')
field(name='FCREF', register=r, offset=22, width=10, access='read-write',
      doc='Fast Compare Reference Value')

r = register('FC2FCM', width=32, block=evadcTargetSocket, offset=0x3604,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Mode Register, FC Channel 2')
field(name='RUNCOMP', register=r, offset=0, width=2, access='read-write',
      doc='Run Control for Compare Channel')
field(name='RUNRAMP', register=r, offset=2, width=2, access='read-write',
      doc='Run Control for Ramp')
field(name='FCRDIR', register=r, offset=4, width=1, access='read-write',
      doc='Fast Compare Ramp Direction')
field(name='ANON', register=r, offset=5, width=1, access='read-write',
      doc='Analog Converter Control')
field(name='ACSD', register=r, offset=6, width=2, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='FCTRIV', register=r, offset=8, width=8, access='read-write',
      doc='Fast Compare Trigger Interval')
field(name='SRG', register=r, offset=16, width=2, access='read-write',
      doc='Service Request Generation')
field(name='AUE', register=r, offset=18, width=2, access='read-write',
      doc='Automatic Update Enable')
field(name='SSE', register=r, offset=20, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='FCMWC', register=r, offset=21, width=1, access='write-only',
      doc='Write Control for Fast Compare Mode Configuration')
field(name='FCREF', register=r, offset=22, width=10, access='read-write',
      doc='Fast Compare Reference Value')

r = register('FC3FCM', width=32, block=evadcTargetSocket, offset=0x3704,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Mode Register, FC Channel 3')
field(name='RUNCOMP', register=r, offset=0, width=2, access='read-write',
      doc='Run Control for Compare Channel')
field(name='RUNRAMP', register=r, offset=2, width=2, access='read-write',
      doc='Run Control for Ramp')
field(name='FCRDIR', register=r, offset=4, width=1, access='read-write',
      doc='Fast Compare Ramp Direction')
field(name='ANON', register=r, offset=5, width=1, access='read-write',
      doc='Analog Converter Control')
field(name='ACSD', register=r, offset=6, width=2, access='read-write',
      doc='Analog Clock Synchronization Delay')
field(name='FCTRIV', register=r, offset=8, width=8, access='read-write',
      doc='Fast Compare Trigger Interval')
field(name='SRG', register=r, offset=16, width=2, access='read-write',
      doc='Service Request Generation')
field(name='AUE', register=r, offset=18, width=2, access='read-write',
      doc='Automatic Update Enable')
field(name='SSE', register=r, offset=20, width=1, access='read-write',
      doc='Sample Synchronization Enable')
field(name='FCMWC', register=r, offset=21, width=1, access='write-only',
      doc='Write Control for Fast Compare Mode Configuration')
field(name='FCREF', register=r, offset=22, width=10, access='read-write',
      doc='Fast Compare Reference Value')

r = register('FC0FCRAMP0', width=32, block=evadcTargetSocket, offset=0x3408,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 0, FC Channel 0')
field(name='FCRCOMPA', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value A')
field(name='FCRSTEP', register=r, offset=16, width=8, access='read-write',
      doc='Fast Compare Ramp Step Width')
field(name='FSWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Fast Compare Stepwidth')

r = register('FC1FCRAMP0', width=32, block=evadcTargetSocket, offset=0x3508,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 0, FC Channel 1')
field(name='FCRCOMPA', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value A')
field(name='FCRSTEP', register=r, offset=16, width=8, access='read-write',
      doc='Fast Compare Ramp Step Width')
field(name='FSWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Fast Compare Stepwidth')

r = register('FC2FCRAMP0', width=32, block=evadcTargetSocket, offset=0x3608,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 0, FC Channel 2')
field(name='FCRCOMPA', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value A')
field(name='FCRSTEP', register=r, offset=16, width=8, access='read-write',
      doc='Fast Compare Ramp Step Width')
field(name='FSWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Fast Compare Stepwidth')

r = register('FC3FCRAMP0', width=32, block=evadcTargetSocket, offset=0x3708,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 0, FC Channel 3')
field(name='FCRCOMPA', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value A')
field(name='FCRSTEP', register=r, offset=16, width=8, access='read-write',
      doc='Fast Compare Ramp Step Width')
field(name='FSWC', register=r, offset=31, width=1, access='write-only',
      doc='Write Control for Fast Compare Stepwidth')

r = register('FC0FCRAMP1', width=32, block=evadcTargetSocket, offset=0x340c,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 1, FC Channel 0')
field(name='FCRCOMPB', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value B')

r = register('FC1FCRAMP1', width=32, block=evadcTargetSocket, offset=0x350c,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 1, FC Channel 1')
field(name='FCRCOMPB', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value B')

r = register('FC2FCRAMP1', width=32, block=evadcTargetSocket, offset=0x360c,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 1, FC Channel 2')
field(name='FCRCOMPB', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value B')

r = register('FC3FCRAMP1', width=32, block=evadcTargetSocket, offset=0x370c,
             access='read-only', reset=0x00000000,
             doc='Fast Compare Ramp Register 1, FC Channel 3')
field(name='FCRCOMPB', register=r, offset=0, width=10, access='read-write',
      doc='Fast Compare Ramp Compare Value B')

r = register('FC0FCBFL', width=32, block=evadcTargetSocket, offset=0x3420,
             access='read-only', reset=0x00000000,
             doc='Boundary Flag Register, FC Channel 0')
field(name='BFL', register=r, offset=0, width=1, access='read-only',
      doc='Boundary Flag')
field(name='BFA', register=r, offset=4, width=1, access='read-write',
      doc='Boundary Flag Activation Select')
field(name='BFI', register=r, offset=8, width=1, access='read-write',
      doc='Boundary Flag Inversion Control')
field(name='BFS', register=r, offset=12, width=2, access='write-only',
      doc='Boundary Flag Software Control')
field(name='BFM', register=r, offset=16, width=1, access='read-write',
      doc='Boundary Flag Mode Control')
field(name='BFV', register=r, offset=17, width=1, access='read-write',
      doc='Boundary Flag Value')
field(name='BFLNP', register=r, offset=24, width=4, access='read-write',
      doc='Boundary Flag Node Pointer')
field(name='FCR', register=r, offset=28, width=1, access='read-only',
      doc='Fast Compare Result')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('FC1FCBFL', width=32, block=evadcTargetSocket, offset=0x3520,
             access='read-only', reset=0x00000000,
             doc='Boundary Flag Register, FC Channel 1')
field(name='BFL', register=r, offset=0, width=1, access='read-only',
      doc='Boundary Flag')
field(name='BFA', register=r, offset=4, width=1, access='read-write',
      doc='Boundary Flag Activation Select')
field(name='BFI', register=r, offset=8, width=1, access='read-write',
      doc='Boundary Flag Inversion Control')
field(name='BFS', register=r, offset=12, width=2, access='write-only',
      doc='Boundary Flag Software Control')
field(name='BFM', register=r, offset=16, width=1, access='read-write',
      doc='Boundary Flag Mode Control')
field(name='BFV', register=r, offset=17, width=1, access='read-write',
      doc='Boundary Flag Value')
field(name='BFLNP', register=r, offset=24, width=4, access='read-write',
      doc='Boundary Flag Node Pointer')
field(name='FCR', register=r, offset=28, width=1, access='read-only',
      doc='Fast Compare Result')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('FC2FCBFL', width=32, block=evadcTargetSocket, offset=0x3620,
             access='read-only', reset=0x00000000,
             doc='Boundary Flag Register, FC Channel 2')
field(name='BFL', register=r, offset=0, width=1, access='read-only',
      doc='Boundary Flag')
field(name='BFA', register=r, offset=4, width=1, access='read-write',
      doc='Boundary Flag Activation Select')
field(name='BFI', register=r, offset=8, width=1, access='read-write',
      doc='Boundary Flag Inversion Control')
field(name='BFS', register=r, offset=12, width=2, access='write-only',
      doc='Boundary Flag Software Control')
field(name='BFM', register=r, offset=16, width=1, access='read-write',
      doc='Boundary Flag Mode Control')
field(name='BFV', register=r, offset=17, width=1, access='read-write',
      doc='Boundary Flag Value')
field(name='BFLNP', register=r, offset=24, width=4, access='read-write',
      doc='Boundary Flag Node Pointer')
field(name='FCR', register=r, offset=28, width=1, access='read-only',
      doc='Fast Compare Result')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('FC3FCBFL', width=32, block=evadcTargetSocket, offset=0x3720,
             access='read-only', reset=0x00000000,
             doc='Boundary Flag Register, FC Channel 3')
field(name='BFL', register=r, offset=0, width=1, access='read-only',
      doc='Boundary Flag')
field(name='BFA', register=r, offset=4, width=1, access='read-write',
      doc='Boundary Flag Activation Select')
field(name='BFI', register=r, offset=8, width=1, access='read-write',
      doc='Boundary Flag Inversion Control')
field(name='BFS', register=r, offset=12, width=2, access='write-only',
      doc='Boundary Flag Software Control')
field(name='BFM', register=r, offset=16, width=1, access='read-write',
      doc='Boundary Flag Mode Control')
field(name='BFV', register=r, offset=17, width=1, access='read-write',
      doc='Boundary Flag Value')
field(name='BFLNP', register=r, offset=24, width=4, access='read-write',
      doc='Boundary Flag Node Pointer')
field(name='FCR', register=r, offset=28, width=1, access='read-only',
      doc='Fast Compare Result')
field(name='VF', register=r, offset=31, width=1, access='read-only',
      doc='Valid Flag')

r = register('FC0FCHYST', width=32, block=evadcTargetSocket, offset=0x3424,
             access='read-only', reset=0x00000000,
             doc='Fast Comp. Hysteresis Register, FC Channel 0')
field(name='DELTAMINUS', register=r, offset=2, width=10, access='read-write',
      doc='Lower Delta Value')
field(name='DELTAPLUS', register=r, offset=18, width=10, access='read-write',
      doc='Upper Delta Value')

r = register('FC1FCHYST', width=32, block=evadcTargetSocket, offset=0x3524,
             access='read-only', reset=0x00000000,
             doc='Fast Comp. Hysteresis Register, FC Channel 1')
field(name='DELTAMINUS', register=r, offset=2, width=10, access='read-write',
      doc='Lower Delta Value')
field(name='DELTAPLUS', register=r, offset=18, width=10, access='read-write',
      doc='Upper Delta Value')

r = register('FC2FCHYST', width=32, block=evadcTargetSocket, offset=0x3624,
             access='read-only', reset=0x00000000,
             doc='Fast Comp. Hysteresis Register, FC Channel 2')
field(name='DELTAMINUS', register=r, offset=2, width=10, access='read-write',
      doc='Lower Delta Value')
field(name='DELTAPLUS', register=r, offset=18, width=10, access='read-write',
      doc='Upper Delta Value')

r = register('FC3FCHYST', width=32, block=evadcTargetSocket, offset=0x3724,
             access='read-only', reset=0x00000000,
             doc='Fast Comp. Hysteresis Register, FC Channel 3')
field(name='DELTAMINUS', register=r, offset=2, width=10, access='read-write',
      doc='Lower Delta Value')
field(name='DELTAPLUS', register=r, offset=18, width=10, access='read-write',
      doc='Upper Delta Value')
