#------------------------------------------------------------------------------
# Copyright (C) Australian Semiconductor Technology Company. 2015.
# All Rights Reserved.
#
# This is unpublished proprietary source code of the Australian Semiconductor
# Technology Company (ASTC). The copyright notice does not evidence any
# actual or intended publication of such source code.
#------------------------------------------------------------------------------

import vlab
from vlab import *
vlab.properties(name="IfxGtm2FpiWrapper", kind="leaf")
gtm_intf = vlab.bus("gtm_intf", kind="target", width=32)

r = register('CLC', width=32, block=gtm_intf, offset=0x00000000,
             access='read-only', reset=0x00000003,
             doc='Clock Control Register')
field(name='DISR', register=r, offset=0, width=1, access='read-write',
      doc='Module Disable Request Bit')
field(name='DISS', register=r, offset=1, width=1, access='read-only',
      doc='Module Disable Status Bit')
field(name='EDIS', register=r, offset=3, width=1, access='read-write',
      doc='Sleep Mode Enable Control')

r = register('RESET_CLR', width=32, block=gtm_intf, offset=0x00000004,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Status Clear Register')
field(name='CLR', register=r, offset=0, width=1, access='write-only',
      doc='Kernel Reset Status Clear')

r = register('RESET1', width=32, block=gtm_intf, offset=0x00000008,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Register 0')
field(name='RST', register=r, offset=0, width=1, access='read-write',
      doc='Kernel Reset')
field(name='RSTSTAT', register=r, offset=1, width=1, access='read-only',
      doc='Kernel Reset Status')

r = register('RESET2', width=32, block=gtm_intf, offset=0x0000000c,
             access='read-only', reset=0x00000000,
             doc='Kernel Reset Register 1')
field(name='RST', register=r, offset=0, width=1, access='read-write',
      doc='Kernel Reset')

r = register('ACCEN0', width=32, block=gtm_intf, offset=0x00000010,
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

r = register('ACCEN1', width=32, block=gtm_intf, offset=0x00000014,
             access='read-only', reset=0x00000000,
             doc='Access Enable Register 1')

r = register('OTBU0T', width=32, block=gtm_intf, offset=0x00000018,
             access='read-only', reset=0x00000000,
             doc='OCDS TBU0 Trigger Register')
field(name='CV', register=r, offset=0, width=27, access='read-write',
      doc='Compare Value')
field(name='CM', register=r, offset=28, width=2, access='read-write',
      doc='Compare Mode')

r = register('OTBU1T', width=32, block=gtm_intf, offset=0x0000001c,
             access='read-only', reset=0x00000000,
             doc='OCDS TBU1 Trigger Register')
field(name='CV', register=r, offset=0, width=24, access='read-write',
      doc='Compare Value')
field(name='EN', register=r, offset=28, width=1, access='read-write',
      doc='Enable')

r = register('OTBU2T', width=32, block=gtm_intf, offset=0x00000020,
             access='read-only', reset=0x00000000,
             doc='OCDS TBU2 Trigger Register')
field(name='CV', register=r, offset=0, width=24, access='read-write',
      doc='Compare Value')
field(name='EN', register=r, offset=28, width=1, access='read-write',
      doc='Enable')

r = register('OTBU3T', width=32, block=gtm_intf, offset=0x00000024,
             access='read-only', reset=0x00000000,
             doc='OCDS TBU3 Trigger Register')
field(name='CV', register=r, offset=0, width=24, access='read-write',
      doc='Compare Value')
field(name='EN', register=r, offset=28, width=1, access='read-write',
      doc='Enable')

r = register('OTSS', width=32, block=gtm_intf, offset=0x00000028,
             access='read-only', reset=0x00000000,
             doc='OCDS Trigger Set Select Register')
field(name='OTGB0', register=r, offset=0, width=4, access='read-write',
      doc='Trigger Set for OTGB0')
field(name='OTGB1', register=r, offset=8, width=4, access='read-write',
      doc='Trigger Set for OTGB1')
field(name='OTGBM0', register=r, offset=16, width=4, access='read-write',
      doc='Trigger Set for OTGBM0')
field(name='OTGBM1', register=r, offset=24, width=4, access='read-write',
      doc='Trigger Set for OTGBM1')

r = register('OTSC0', width=32, block=gtm_intf, offset=0x0000002c,
             access='read-only', reset=0x00000000,
             doc='OCDS Trigger Set Control 0 Register')
field(name='B0LMT', register=r, offset=0, width=3, access='read-write',
      doc='OTGB0 TS16_IOS Low Byte Module Type')
field(name='B0LMI', register=r, offset=4, width=4, access='read-write',
      doc='OTGB0 TS16_IOS Low Byte Module Instance')
field(name='B0HMT', register=r, offset=8, width=3, access='read-write',
      doc='OTGB0 TS16_IOS High Byte Module Type')
field(name='B0HMI', register=r, offset=12, width=4, access='read-write',
      doc='OTGB0 TS16_IOS High Byte Module Instance')
field(name='B1LMT', register=r, offset=16, width=3, access='read-write',
      doc='OTGB1 TS16_IOS Low Byte Module Type')
field(name='B1LMI', register=r, offset=20, width=4, access='read-write',
      doc='OTGB1 TS16_IOS Low Byte Module Instance')
field(name='B1HMT', register=r, offset=24, width=3, access='read-write',
      doc='OTGB1 TS16_IOS High Byte Module Type')
field(name='B1HMI', register=r, offset=28, width=4, access='read-write',
      doc='OTGB1 TS16_IOS High Byte Module Instance')

r = register('OTSC1', width=32, block=gtm_intf, offset=0x00000030,
             access='read-only', reset=0x00000000,
             doc='OCDS Trigger Set Control 1 Register')
field(name='MCS', register=r, offset=0, width=4, access='read-write',
      doc='MCS Channel Selection')
field(name='MI', register=r, offset=4, width=4, access='read-write',
      doc='MCS Instance')
field(name='MOE', register=r, offset=9, width=1, access='read-write',
      doc='MCS Opcode Trace Enable')

r = register('ODA', width=32, block=gtm_intf, offset=0x00000034,
             access='read-only', reset=0x00000000,
             doc='OCDS Debug Access Register')
field(name='DRAC', register=r, offset=0, width=2, access='read-write',
      doc='Debug Read Access Control')

r = register('OCS', width=32, block=gtm_intf, offset=0x00000038,
             access='read-only', reset=0x00000000,
             doc='OCDS Control and Status')
field(name='SUS', register=r, offset=24, width=4, access='read-write',
      doc='OCDS Suspend Control')
field(name='SUS_P', register=r, offset=28, width=1, access='write-only',
      doc='SUS Write Protection')
field(name='SUSSTA', register=r, offset=29, width=1, access='read-only',
      doc='Suspend State')

r = register('TIM0INSEL', width=32, block=gtm_intf, offset=0x00000040,
             access='read-only', reset=0x00000000,
             doc='TIM0 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TIM1INSEL', width=32, block=gtm_intf, offset=0x00000044,
             access='read-only', reset=0x00000000,
             doc='TIM1 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TIM2INSEL', width=32, block=gtm_intf, offset=0x00000048,
             access='read-only', reset=0x00000000,
             doc='TIM2 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TIM3INSEL', width=32, block=gtm_intf, offset=0x0000004c,
             access='read-only', reset=0x00000000,
             doc='TIM3 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TIM4INSEL', width=32, block=gtm_intf, offset=0x00000050,
             access='read-only', reset=0x00000000,
             doc='TIM4 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TIM5INSEL', width=32, block=gtm_intf, offset=0x00000054,
             access='read-only', reset=0x00000000,
             doc='TIM5 Input Select Register')
field(name='CH0SEL', register=r, offset=0, width=4, access='read-write',
      doc='TIM Channel 0 Input Selection')
field(name='CH1SEL', register=r, offset=4, width=4, access='read-write',
      doc='TIM Channel 1 Input Selection')
field(name='CH2SEL', register=r, offset=8, width=4, access='read-write',
      doc='TIM Channel 2 Input Selection')
field(name='CH3SEL', register=r, offset=12, width=4, access='read-write',
      doc='TIM Channel 3 Input Selection')
field(name='CH4SEL', register=r, offset=16, width=4, access='read-write',
      doc='TIM Channel 4 Input Selection')
field(name='CH5SEL', register=r, offset=20, width=4, access='read-write',
      doc='TIM Channel 5 Input Selection')
field(name='CH6SEL', register=r, offset=24, width=4, access='read-write',
      doc='TIM Channel 6 Input Selection')
field(name='CH7SEL', register=r, offset=28, width=4, access='read-write',
      doc='TIM Channel 7 Input Selection')

r = register('TOUTSEL0', width=32, block=gtm_intf, offset=0x00000060,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL1', width=32, block=gtm_intf, offset=0x00000064,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL2', width=32, block=gtm_intf, offset=0x00000068,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL3', width=32, block=gtm_intf, offset=0x0000006c,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL4', width=32, block=gtm_intf, offset=0x00000070,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL5', width=32, block=gtm_intf, offset=0x00000074,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL6', width=32, block=gtm_intf, offset=0x00000078,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL7', width=32, block=gtm_intf, offset=0x0000007c,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL8', width=32, block=gtm_intf, offset=0x00000080,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL9', width=32, block=gtm_intf, offset=0x00000084,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL10', width=32, block=gtm_intf, offset=0x00000088,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL11', width=32, block=gtm_intf, offset=0x0000008c,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL12', width=32, block=gtm_intf, offset=0x00000090,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL13', width=32, block=gtm_intf, offset=0x00000094,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL14', width=32, block=gtm_intf, offset=0x00000098,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL15', width=32, block=gtm_intf, offset=0x0000009c,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL16', width=32, block=gtm_intf, offset=0x000000a0,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL17', width=32, block=gtm_intf, offset=0x000000a4,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')

r = register('TOUTSEL18', width=32, block=gtm_intf, offset=0x000000a8,
             access='read-only', reset=0x00000000,
             doc='Timer Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='TOUT(n*8 + 0) Output Selection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='TOUT(n*8 + 1) Output Selection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='TOUT(n*8 + 7) Output Selection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='TOUT(n*8 + 2) Output Selection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='TOUT(n*8 + 3) Output Selection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='TOUT(n*8 + 4) Output Selection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='TOUT(n*8 + 5) Output Selection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='TOUT(n*8 + 6) Output Selection')

r = register('DSADCINSEL0', width=32, block=gtm_intf, offset=0x00000100,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 0 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCINSEL1', width=32, block=gtm_intf, offset=0x00000104,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 1 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCINSEL2', width=32, block=gtm_intf, offset=0x00000108,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 2 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCINSEL3', width=32, block=gtm_intf, offset=0x0000010c,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 3 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCINSEL4', width=32, block=gtm_intf, offset=0x00000110,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 4 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCINSEL5', width=32, block=gtm_intf, offset=0x00000114,
             access='read-only', reset=0x00000000,
             doc='DSADC Input Select 5 Register')
field(name='INSEL0', register=r, offset=0, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 0')
field(name='INSEL1', register=r, offset=4, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 1')
field(name='INSEL2', register=r, offset=8, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 2')
field(name='INSEL3', register=r, offset=12, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 3')
field(name='INSEL4', register=r, offset=16, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 4')
field(name='INSEL5', register=r, offset=20, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 5')
field(name='INSEL6', register=r, offset=24, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 6')
field(name='INSEL7', register=r, offset=28, width=4, access='read-write',
      doc='In Selection for DSADCn GTM connection 7')

r = register('DSADCOUTSEL00', width=32, block=gtm_intf, offset=0x00000120,
             access='read-only', reset=0x00000000,
             doc='DSADC Output Select 00 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for DSADC0 GTM connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for DSADC1 GTM connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for DSADC2 GTM connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for DSADC3 GTM connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for DSADC4 GTM connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for DSADC5 GTM connection')

r = register('DSADCOUTSEL10', width=32, block=gtm_intf, offset=0x00000128,
             access='read-only', reset=0x00000000,
             doc='DSADC Output Select 10 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for DSADC0 GTM connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for DSADC1 GTM connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for DSADC2 GTM connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for DSADC3 GTM connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for DSADC4 GTM connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for DSADC5 GTM connection')

r = register('DSADCOUTSEL20', width=32, block=gtm_intf, offset=0x00000130,
             access='read-only', reset=0x00000000,
             doc='DSADC Output Select 20 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for DSADC0 GTM connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for DSADC1 GTM connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for DSADC2 GTM connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for DSADC3 GTM connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for DSADC4 GTM connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for DSADC5 GTM connection')

r = register('DSADCOUTSEL30', width=32, block=gtm_intf, offset=0x00000138,
             access='read-only', reset=0x00000000,
             doc='DSADC Output Select 30 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for DSADC0 GTM connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for DSADC1 GTM connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for DSADC2 GTM connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for DSADC3 GTM connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for DSADC4 GTM connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for DSADC5 GTM connection')

r = register('ADCTRIG0OUT0', width=32, block=gtm_intf, offset=0x00000140,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 0 Output Select 0 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to ADC4 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to ADC5 connection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to ADC6 connection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to ADC7 connection')

r = register('ADCTRIG1OUT0', width=32, block=gtm_intf, offset=0x00000148,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 1 Output Select 0 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to ADC4 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to ADC5 connection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to ADC6 connection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to ADC7 connection')

r = register('ADCTRIG2OUT0', width=32, block=gtm_intf, offset=0x00000150,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 2 Output Select 0 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to ADC4 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to ADC5 connection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to ADC6 connection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to ADC7 connection')

r = register('ADCTRIG3OUT0', width=32, block=gtm_intf, offset=0x00000158,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 3 Output Select 0 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to ADC4 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to ADC5 connection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to ADC6 connection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to ADC7 connection')

r = register('ADCTRIG4OUT0', width=32, block=gtm_intf, offset=0x00000160,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 4 Output Select 0 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to ADC4 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to ADC5 connection')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to ADC6 connection')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to ADC7 connection')

r = register('ADCTRIG0OUT1', width=32, block=gtm_intf, offset=0x00000144,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 0 Output Select 1 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')

r = register('ADCTRIG1OUT1', width=32, block=gtm_intf, offset=0x0000014c,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 1 Output Select 1 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')

r = register('ADCTRIG2OUT1', width=32, block=gtm_intf, offset=0x00000154,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 2 Output Select 1 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')

r = register('ADCTRIG3OUT1', width=32, block=gtm_intf, offset=0x0000015c,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 3 Output Select 1 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')

r = register('ADCTRIG4OUT1', width=32, block=gtm_intf, offset=0x00000164,
             access='read-only', reset=0x00000000,
             doc='ADC Trigger 4 Output Select 1 Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to ADC0 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to ADC1 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to ADC2 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to ADC3 connection')

r = register('DXOUTCON', width=32, block=gtm_intf, offset=0x00000170,
             access='read-only', reset=0x00000000,
             doc='Data Exchange Output Control Register')
field(name='OUT0', register=r, offset=0, width=1, access='read-write',
      doc='Output 00 Control')
field(name='OUT1', register=r, offset=1, width=1, access='read-write',
      doc='Output 01 Control')
field(name='OUT2', register=r, offset=2, width=1, access='read-write',
      doc='Output 02 Control')
field(name='OUT3', register=r, offset=3, width=1, access='read-write',
      doc='Output 03 Control')
field(name='OUT4', register=r, offset=4, width=1, access='read-write',
      doc='Output 04 Control')

r = register('TRIGOUT0', width=32, block=gtm_intf, offset=0x00000174,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Register 0')
field(name='TRIG0', register=r, offset=0, width=2, access='write-only',
      doc='Trigger 0')
field(name='TRIG1', register=r, offset=2, width=2, access='write-only',
      doc='Trigger 1')
field(name='TRIG2', register=r, offset=4, width=2, access='write-only',
      doc='Trigger 2')
field(name='TRIG3', register=r, offset=6, width=2, access='write-only',
      doc='Trigger 3')
field(name='TRIG4', register=r, offset=8, width=2, access='write-only',
      doc='Trigger 4')
field(name='TRIG5', register=r, offset=10, width=2, access='write-only',
      doc='Trigger 5')
field(name='TRIG6', register=r, offset=12, width=2, access='write-only',
      doc='Trigger 6')
field(name='TRIG7', register=r, offset=14, width=2, access='write-only',
      doc='Trigger 7')

r = register('TRIGOUT1', width=32, block=gtm_intf, offset=0x00000178,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Register 1')
field(name='TRIG0', register=r, offset=0, width=2, access='write-only',
      doc='Trigger 0')
field(name='TRIG1', register=r, offset=2, width=2, access='write-only',
      doc='Trigger 1')
field(name='TRIG2', register=r, offset=4, width=2, access='write-only',
      doc='Trigger 2')
field(name='TRIG3', register=r, offset=6, width=2, access='write-only',
      doc='Trigger 3')
field(name='TRIG4', register=r, offset=8, width=2, access='write-only',
      doc='Trigger 4')
field(name='TRIG5', register=r, offset=10, width=2, access='write-only',
      doc='Trigger 5')
field(name='TRIG6', register=r, offset=12, width=2, access='write-only',
      doc='Trigger 6')
field(name='TRIG7', register=r, offset=14, width=2, access='write-only',
      doc='Trigger 7')

r = register('TRIGOUT2', width=32, block=gtm_intf, offset=0x0000017c,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Register 2')
field(name='TRIG0', register=r, offset=0, width=2, access='write-only',
      doc='Trigger 0')
field(name='TRIG1', register=r, offset=2, width=2, access='write-only',
      doc='Trigger 1')
field(name='TRIG2', register=r, offset=4, width=2, access='write-only',
      doc='Trigger 2')
field(name='TRIG3', register=r, offset=6, width=2, access='write-only',
      doc='Trigger 3')
field(name='TRIG4', register=r, offset=8, width=2, access='write-only',
      doc='Trigger 4')
field(name='TRIG5', register=r, offset=10, width=2, access='write-only',
      doc='Trigger 5')
field(name='TRIG6', register=r, offset=12, width=2, access='write-only',
      doc='Trigger 6')
field(name='TRIG7', register=r, offset=14, width=2, access='write-only',
      doc='Trigger 7')

r = register('TRIGOUT3', width=32, block=gtm_intf, offset=0x00000180,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Register 3')
field(name='TRIG0', register=r, offset=0, width=2, access='write-only',
      doc='Trigger 0')
field(name='TRIG1', register=r, offset=2, width=2, access='write-only',
      doc='Trigger 1')
field(name='TRIG2', register=r, offset=4, width=2, access='write-only',
      doc='Trigger 2')
field(name='TRIG3', register=r, offset=6, width=2, access='write-only',
      doc='Trigger 3')
field(name='TRIG4', register=r, offset=8, width=2, access='write-only',
      doc='Trigger 4')
field(name='TRIG5', register=r, offset=10, width=2, access='write-only',
      doc='Trigger 5')
field(name='TRIG6', register=r, offset=12, width=2, access='write-only',
      doc='Trigger 6')
field(name='TRIG7', register=r, offset=14, width=2, access='write-only',
      doc='Trigger 7')

r = register('TRIGOUT4', width=32, block=gtm_intf, offset=0x00000184,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Register 4')
field(name='TRIG0', register=r, offset=0, width=2, access='write-only',
      doc='Trigger 0')
field(name='TRIG1', register=r, offset=2, width=2, access='write-only',
      doc='Trigger 1')
field(name='TRIG2', register=r, offset=4, width=2, access='write-only',
      doc='Trigger 2')
field(name='TRIG3', register=r, offset=6, width=2, access='write-only',
      doc='Trigger 3')
field(name='TRIG4', register=r, offset=8, width=2, access='write-only',
      doc='Trigger 4')
field(name='TRIG5', register=r, offset=10, width=2, access='write-only',
      doc='Trigger 5')
field(name='TRIG6', register=r, offset=12, width=2, access='write-only',
      doc='Trigger 6')
field(name='TRIG7', register=r, offset=14, width=2, access='write-only',
      doc='Trigger 7')

r = register('INTOUT0', width=32, block=gtm_intf, offset=0x0000019c,
             access='read-only', reset=0x00000000,
             doc='Interrupt Output Register 0')
field(name='INT0', register=r, offset=0, width=2, access='write-only',
      doc='Interrupt Trigger Request 0')

r = register('INTOUT1', width=32, block=gtm_intf, offset=0x000001a0,
             access='read-only', reset=0x00000000,
             doc='Interrupt Output Register 1')
field(name='INT0', register=r, offset=0, width=2, access='write-only',
      doc='Interrupt Trigger Request 0')

r = register('INTOUT2', width=32, block=gtm_intf, offset=0x000001a4,
             access='read-only', reset=0x00000000,
             doc='Interrupt Output Register 2')
field(name='INT0', register=r, offset=0, width=2, access='write-only',
      doc='Interrupt Trigger Request 0')

r = register('INTOUT3', width=32, block=gtm_intf, offset=0x000001a8,
             access='read-only', reset=0x00000000,
             doc='Interrupt Output Register 3')
field(name='INT0', register=r, offset=0, width=2, access='write-only',
      doc='Interrupt Trigger Request 0')

r = register('INTOUT4', width=32, block=gtm_intf, offset=0x000001ac,
             access='read-only', reset=0x00000000,
             doc='Interrupt Output Register 4')
field(name='INT0', register=r, offset=0, width=2, access='write-only',
      doc='Interrupt Trigger Request 0')

r = register('MCSTRIGOUTSEL', width=32, block=gtm_intf, offset=0x000001c4,
             access='read-only', reset=0x00000000,
             doc='Trigger Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Selects which MCS triggers go to FC0BFDAT/SEL')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Selects which MCS triggers go to FC1BFDAT/SEL')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Selects which MCS triggers go to FC2BFDAT/SEL')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Selects which MCS triggers go to FC3BFDAT/SEL')

r = register('MCSINTSTAT', width=32, block=gtm_intf, offset=0x000001c8,
             access='read-only', reset=0x00000000,
             doc='MCS Interrupt Status Register')
field(name='MCS00', register=r, offset=0, width=1, access='read-only',
      doc='MCS0 RAM0 Interrupt 0 Status Flag')
field(name='MCS10', register=r, offset=1, width=1, access='read-only',
      doc='MCS1 RAM0 Interrupt 0 Status Flag')
field(name='MCS20', register=r, offset=2, width=1, access='read-only',
      doc='MCS2 RAM0 Interrupt 0 Status Flag')
field(name='MCS30', register=r, offset=3, width=1, access='read-only',
      doc='MCS3 RAM0 Interrupt 0 Status Flag')
field(name='MCS40', register=r, offset=4, width=1, access='read-only',
      doc='MCS4 RAM0 Interrupt 0 Status Flag')

r = register('MCSINTCLR', width=32, block=gtm_intf, offset=0x000001cc,
             access='read-only', reset=0x00000000,
             doc='MCS Interrupt Clear Register')
field(name='MCS0', register=r, offset=0, width=1, access='write-only',
      doc='MCSn RAM0 Interrupt 0 Status Clear Bit 0')
field(name='MCS1', register=r, offset=1, width=1, access='write-only',
      doc='MCSn RAM0 Interrupt 0 Status Clear Bit 1')
field(name='MCS2', register=r, offset=2, width=1, access='write-only',
      doc='MCSn RAM0 Interrupt 0 Status Clear Bit 2')
field(name='MCS3', register=r, offset=3, width=1, access='write-only',
      doc='MCSn RAM0 Interrupt 0 Status Clear Bit 3')
field(name='MCS4', register=r, offset=4, width=1, access='write-only',
      doc='MCSn RAM0 Interrupt 0 Status Clear Bit 4')

r = register('DXINCON', width=32, block=gtm_intf, offset=0x000001d0,
             access='read-only', reset=0x00000000,
             doc='Data Exchange Input Control Register')
field(name='IN0', register=r, offset=0, width=1, access='read-write',
      doc='Input 00 Control')
field(name='IN1', register=r, offset=1, width=1, access='read-write',
      doc='Input 01 Control')
field(name='IN2', register=r, offset=2, width=1, access='read-write',
      doc='Input 02 Control')
field(name='IN3', register=r, offset=3, width=1, access='read-write',
      doc='Input 03 Control')
field(name='IN4', register=r, offset=4, width=1, access='read-write',
      doc='Input 04 Control')
field(name='DSS0', register=r, offset=16, width=1, access='read-write',
      doc='Data Source Select 00 Control')
field(name='DSS1', register=r, offset=17, width=1, access='read-write',
      doc='Data Source Select 01 Control')
field(name='DSS2', register=r, offset=18, width=1, access='read-write',
      doc='Data Source Select 02 Control')
field(name='DSS3', register=r, offset=19, width=1, access='read-write',
      doc='Data Source Select 03 Control')
field(name='DSS4', register=r, offset=20, width=1, access='read-write',
      doc='Data Source Select 04 Control')

r = register('DATAIN0', width=32, block=gtm_intf, offset=0x000001d4,
             access='read-only', reset=0x00000000,
             doc='Data Input 0 Register')
field(name='DATA', register=r, offset=0, width=32, access='read-write',
      doc='Data')

r = register('DATAIN1', width=32, block=gtm_intf, offset=0x000001d8,
             access='read-only', reset=0x00000000,
             doc='Data Input 1 Register')
field(name='DATA', register=r, offset=0, width=32, access='read-write',
      doc='Data')

r = register('DATAIN2', width=32, block=gtm_intf, offset=0x000001dc,
             access='read-only', reset=0x00000000,
             doc='Data Input 2 Register')
field(name='DATA', register=r, offset=0, width=32, access='read-write',
      doc='Data')

r = register('DATAIN3', width=32, block=gtm_intf, offset=0x000001e0,
             access='read-only', reset=0x00000000,
             doc='Data Input 3 Register')
field(name='DATA', register=r, offset=0, width=32, access='read-write',
      doc='Data')

r = register('DATAIN4', width=32, block=gtm_intf, offset=0x000001e4,
             access='read-only', reset=0x00000000,
             doc='Data Input 4 Register')
field(name='DATA', register=r, offset=0, width=32, access='read-write',
      doc='Data')

r = register('MSCSET0CON0', width=32, block=gtm_intf, offset=0x00000200,
             access='read-only', reset=0x00000000,
             doc='MSC Set 0 Control 0 Register')
field(name='SEL0', register=r, offset=0, width=5, access='read-write',
      doc='Set 0[0] Input Selection')
field(name='SEL1', register=r, offset=8, width=5, access='read-write',
      doc='Set 0[1] Input Selection')
field(name='SEL2', register=r, offset=16, width=5, access='read-write',
      doc='Set 0[2] Input Selection')
field(name='SEL3', register=r, offset=24, width=5, access='read-write',
      doc='Set 0[3] Input Selection')

r = register('MSCSET1CON0', width=32, block=gtm_intf, offset=0x00000210,
             access='read-only', reset=0x00000000,
             doc='MSC Set 1 Control 0 Register')
field(name='SEL0', register=r, offset=0, width=5, access='read-write',
      doc='Set 1[0] Input Selection')
field(name='SEL1', register=r, offset=8, width=5, access='read-write',
      doc='Set 1[1] Input Selection')
field(name='SEL2', register=r, offset=16, width=5, access='read-write',
      doc='Set 1[2] Input Selection')
field(name='SEL3', register=r, offset=24, width=5, access='read-write',
      doc='Set 1[3] Input Selection')

r = register('MSCSET2CON0', width=32, block=gtm_intf, offset=0x00000220,
             access='read-only', reset=0x00000000,
             doc='MSC Set 2 Control 0 Register')
field(name='SEL0', register=r, offset=0, width=5, access='read-write',
      doc='Set 2[0] Input Selection')
field(name='SEL1', register=r, offset=8, width=5, access='read-write',
      doc='Set 2[1] Input Selection')
field(name='SEL2', register=r, offset=16, width=5, access='read-write',
      doc='Set 2[2] Input Selection')
field(name='SEL3', register=r, offset=24, width=5, access='read-write',
      doc='Set 2[3] Input Selection')

r = register('MSCSET3CON0', width=32, block=gtm_intf, offset=0x00000230,
             access='read-only', reset=0x00000000,
             doc='MSC Set 3 Control 0 Register')
field(name='SEL0', register=r, offset=0, width=5, access='read-write',
      doc='Set 3[0] Input Selection')
field(name='SEL1', register=r, offset=8, width=5, access='read-write',
      doc='Set 3[1] Input Selection')
field(name='SEL2', register=r, offset=16, width=5, access='read-write',
      doc='Set 3[2] Input Selection')
field(name='SEL3', register=r, offset=24, width=5, access='read-write',
      doc='Set 3[3] Input Selection')

r = register('MSCSET0CON1', width=32, block=gtm_intf, offset=0x00000204,
             access='read-only', reset=0x00000000,
             doc='MSC Set 0 Control 1 Register')
field(name='SEL4', register=r, offset=0, width=5, access='read-write',
      doc='Set 0[4] Input Selection')
field(name='SEL5', register=r, offset=8, width=5, access='read-write',
      doc='Set 0[5] Input Selection')
field(name='SEL6', register=r, offset=16, width=5, access='read-write',
      doc='Set 0[6] Input Selection')
field(name='SEL7', register=r, offset=24, width=5, access='read-write',
      doc='Set 0[7] Input Selection')

r = register('MSCSET1CON1', width=32, block=gtm_intf, offset=0x00000214,
             access='read-only', reset=0x00000000,
             doc='MSC Set 1 Control 1 Register')
field(name='SEL4', register=r, offset=0, width=5, access='read-write',
      doc='Set 1[4] Input Selection')
field(name='SEL5', register=r, offset=8, width=5, access='read-write',
      doc='Set 1[5] Input Selection')
field(name='SEL6', register=r, offset=16, width=5, access='read-write',
      doc='Set 1[6] Input Selection')
field(name='SEL7', register=r, offset=24, width=5, access='read-write',
      doc='Set 1[7] Input Selection')

r = register('MSCSET2CON1', width=32, block=gtm_intf, offset=0x00000224,
             access='read-only', reset=0x00000000,
             doc='MSC Set 2 Control 1 Register')
field(name='SEL4', register=r, offset=0, width=5, access='read-write',
      doc='Set 2[4] Input Selection')
field(name='SEL5', register=r, offset=8, width=5, access='read-write',
      doc='Set 2[5] Input Selection')
field(name='SEL6', register=r, offset=16, width=5, access='read-write',
      doc='Set 2[6] Input Selection')
field(name='SEL7', register=r, offset=24, width=5, access='read-write',
      doc='Set 2[7] Input Selection')

r = register('MSCSET3CON1', width=32, block=gtm_intf, offset=0x00000234,
             access='read-only', reset=0x00000000,
             doc='MSC Set 3 Control 1 Register')
field(name='SEL4', register=r, offset=0, width=5, access='read-write',
      doc='Set 3[4] Input Selection')
field(name='SEL5', register=r, offset=8, width=5, access='read-write',
      doc='Set 3[5] Input Selection')
field(name='SEL6', register=r, offset=16, width=5, access='read-write',
      doc='Set 3[6] Input Selection')
field(name='SEL7', register=r, offset=24, width=5, access='read-write',
      doc='Set 3[7] Input Selection')

r = register('MSCSET0CON2', width=32, block=gtm_intf, offset=0x00000208,
             access='read-only', reset=0x00000000,
             doc='MSC Set 0 Control 2 Register')
field(name='SEL8', register=r, offset=0, width=5, access='read-write',
      doc='Set 0[8] Input Selection')
field(name='SEL9', register=r, offset=8, width=5, access='read-write',
      doc='Set 0[9] Input Selection')
field(name='SEL10', register=r, offset=16, width=5, access='read-write',
      doc='Set 0[10] Input Selection')
field(name='SEL11', register=r, offset=24, width=5, access='read-write',
      doc='Set 0[11] Input Selection')

r = register('MSCSET1CON2', width=32, block=gtm_intf, offset=0x00000218,
             access='read-only', reset=0x00000000,
             doc='MSC Set 1 Control 2 Register')
field(name='SEL8', register=r, offset=0, width=5, access='read-write',
      doc='Set 1[8] Input Selection')
field(name='SEL9', register=r, offset=8, width=5, access='read-write',
      doc='Set 1[9] Input Selection')
field(name='SEL10', register=r, offset=16, width=5, access='read-write',
      doc='Set 1[10] Input Selection')
field(name='SEL11', register=r, offset=24, width=5, access='read-write',
      doc='Set 1[11] Input Selection')

r = register('MSCSET2CON2', width=32, block=gtm_intf, offset=0x00000228,
             access='read-only', reset=0x00000000,
             doc='MSC Set 2 Control 2 Register')
field(name='SEL8', register=r, offset=0, width=5, access='read-write',
      doc='Set 2[8] Input Selection')
field(name='SEL9', register=r, offset=8, width=5, access='read-write',
      doc='Set 2[9] Input Selection')
field(name='SEL10', register=r, offset=16, width=5, access='read-write',
      doc='Set 2[10] Input Selection')
field(name='SEL11', register=r, offset=24, width=5, access='read-write',
      doc='Set 2[11] Input Selection')

r = register('MSCSET3CON2', width=32, block=gtm_intf, offset=0x00000238,
             access='read-only', reset=0x00000000,
             doc='MSC Set 3 Control 2 Register')
field(name='SEL8', register=r, offset=0, width=5, access='read-write',
      doc='Set 3[8] Input Selection')
field(name='SEL9', register=r, offset=8, width=5, access='read-write',
      doc='Set 3[9] Input Selection')
field(name='SEL10', register=r, offset=16, width=5, access='read-write',
      doc='Set 3[10] Input Selection')
field(name='SEL11', register=r, offset=24, width=5, access='read-write',
      doc='Set 3[11] Input Selection')

r = register('MSCSET0CON3', width=32, block=gtm_intf, offset=0x0000020c,
             access='read-only', reset=0x00000000,
             doc='MSC Set 0 Control 3 Register')
field(name='SEL12', register=r, offset=0, width=5, access='read-write',
      doc='Set 0[12] Input Selection')
field(name='SEL13', register=r, offset=8, width=5, access='read-write',
      doc='Set 0[13] Input Selection')
field(name='SEL14', register=r, offset=16, width=5, access='read-write',
      doc='Set 0[14] Input Selection')
field(name='SEL15', register=r, offset=24, width=5, access='read-write',
      doc='Set 0[15] Input Selection')

r = register('MSCSET1CON3', width=32, block=gtm_intf, offset=0x0000021c,
             access='read-only', reset=0x00000000,
             doc='MSC Set 1 Control 3 Register')
field(name='SEL12', register=r, offset=0, width=5, access='read-write',
      doc='Set 1[12] Input Selection')
field(name='SEL13', register=r, offset=8, width=5, access='read-write',
      doc='Set 1[13] Input Selection')
field(name='SEL14', register=r, offset=16, width=5, access='read-write',
      doc='Set 1[14] Input Selection')
field(name='SEL15', register=r, offset=24, width=5, access='read-write',
      doc='Set 1[15] Input Selection')

r = register('MSCSET2CON3', width=32, block=gtm_intf, offset=0x0000022c,
             access='read-only', reset=0x00000000,
             doc='MSC Set 2 Control 3 Register')
field(name='SEL12', register=r, offset=0, width=5, access='read-write',
      doc='Set 2[12] Input Selection')
field(name='SEL13', register=r, offset=8, width=5, access='read-write',
      doc='Set 2[13] Input Selection')
field(name='SEL14', register=r, offset=16, width=5, access='read-write',
      doc='Set 2[14] Input Selection')
field(name='SEL15', register=r, offset=24, width=5, access='read-write',
      doc='Set 2[15] Input Selection')

r = register('MSCSET3CON3', width=32, block=gtm_intf, offset=0x0000023c,
             access='read-only', reset=0x00000000,
             doc='MSC Set 3 Control 3 Register')
field(name='SEL12', register=r, offset=0, width=5, access='read-write',
      doc='Set 3[12] Input Selection')
field(name='SEL13', register=r, offset=8, width=5, access='read-write',
      doc='Set 3[13] Input Selection')
field(name='SEL14', register=r, offset=16, width=5, access='read-write',
      doc='Set 3[14] Input Selection')
field(name='SEL15', register=r, offset=24, width=5, access='read-write',
      doc='Set 3[15] Input Selection')

r = register('MSC0INLCON', width=32, block=gtm_intf, offset=0x00000290,
             access='read-only', reset=0x00000000,
             doc='MSC0 Input Low Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq Low 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq Low 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq Low 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq Low 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq Low 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq Low 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq Low 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq Low 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq Low 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq Low 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq Low 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq Low 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq Low 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq Low 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq Low 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq Low 15 Output Selection')

r = register('MSC1INLCON', width=32, block=gtm_intf, offset=0x0000029c,
             access='read-only', reset=0x00000000,
             doc='MSC1 Input Low Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq Low 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq Low 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq Low 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq Low 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq Low 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq Low 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq Low 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq Low 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq Low 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq Low 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq Low 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq Low 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq Low 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq Low 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq Low 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq Low 15 Output Selection')

r = register('MSC0INHCON', width=32, block=gtm_intf, offset=0x00000294,
             access='read-only', reset=0x00000000,
             doc='MSC0 Input High Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq High 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq High 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq High 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq High 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq High 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq High 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq High 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq High 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq High 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq High 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq High 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq High 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq High 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq High 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq High 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq High 15 Output Selection')

r = register('MSC1INHCON', width=32, block=gtm_intf, offset=0x000002a0,
             access='read-only', reset=0x00000000,
             doc='MSC1 Input High Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq High 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq High 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq High 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq High 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq High 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq High 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq High 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq High 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq High 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq High 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq High 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq High 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq High 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq High 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq High 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq High 15 Output Selection')

r = register('MSC0INLEXTCON', width=32, block=gtm_intf, offset=0x00000298,
             access='read-only', reset=0x00000000,
             doc='MSC0 Input Low Extended Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq LowExtended 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq LowExtended 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq LowExtended 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq LowExtended 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq LowExtended 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq LowExtended 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq LowExtended 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq LowExtended 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq LowExtended 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq LowExtended 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq LowExtended 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq LowExtended 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq LowExtended 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq LowExtended 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq LowExtended 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq LowExtended 15 Output Selection')

r = register('MSC1INLEXTCON', width=32, block=gtm_intf, offset=0x000002a4,
             access='read-only', reset=0x00000000,
             doc='MSC1 Input Low Extended Control Register')
field(name='SEL0', register=r, offset=0, width=2, access='read-write',
      doc='GTM MSCq LowExtended 0 Output Selection')
field(name='SEL1', register=r, offset=2, width=2, access='read-write',
      doc='GTM MSCq LowExtended 1 Output Selection')
field(name='SEL2', register=r, offset=4, width=2, access='read-write',
      doc='GTM MSCq LowExtended 2 Output Selection')
field(name='SEL3', register=r, offset=6, width=2, access='read-write',
      doc='GTM MSCq LowExtended 3 Output Selection')
field(name='SEL4', register=r, offset=8, width=2, access='read-write',
      doc='GTM MSCq LowExtended 4 Output Selection')
field(name='SEL5', register=r, offset=10, width=2, access='read-write',
      doc='GTM MSCq LowExtended 5 Output Selection')
field(name='SEL6', register=r, offset=12, width=2, access='read-write',
      doc='GTM MSCq LowExtended 6 Output Selection')
field(name='SEL7', register=r, offset=14, width=2, access='read-write',
      doc='GTM MSCq LowExtended 7 Output Selection')
field(name='SEL8', register=r, offset=16, width=2, access='read-write',
      doc='GTM MSCq LowExtended 8 Output Selection')
field(name='SEL9', register=r, offset=18, width=2, access='read-write',
      doc='GTM MSCq LowExtended 9 Output Selection')
field(name='SEL10', register=r, offset=20, width=2, access='read-write',
      doc='GTM MSCq LowExtended 10 Output Selection')
field(name='SEL11', register=r, offset=22, width=2, access='read-write',
      doc='GTM MSCq LowExtended 11 Output Selection')
field(name='SEL12', register=r, offset=24, width=2, access='read-write',
      doc='GTM MSCq LowExtended 12 Output Selection')
field(name='SEL13', register=r, offset=26, width=2, access='read-write',
      doc='GTM MSCq LowExtended 13 Output Selection')
field(name='SEL14', register=r, offset=28, width=2, access='read-write',
      doc='GTM MSCq LowExtended 14 Output Selection')
field(name='SEL15', register=r, offset=30, width=2, access='read-write',
      doc='GTM MSCq LowExtended 15 Output Selection')

r = register('PSI5OUTSEL', width=32, block=gtm_intf, offset=0x000002cc,
             access='read-only', reset=0x00000000,
             doc='PSI5 Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to PSI50 connection')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to PSI51 connection')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to PSI52 connection')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to PSI53 connection')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to PSI54 connection')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to PSI55 connection')

r = register('PSI5SOUTSEL', width=32, block=gtm_intf, offset=0x000002d0,
             access='read-only', reset=0x00000000,
             doc='PSI5-S Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 0')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 4')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 1')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 5')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 2')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 6')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 3')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to PSI5-S connection 7')

r = register('LCDCDCOUTSEL', width=32, block=gtm_intf, offset=0x000002d4,
             access='read-only', reset=0x00000000,
             doc='LCDCDC Output Select Register')
field(name='SEL', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to LCDCDC connection')

r = register('DTMAUXINSEL', width=32, block=gtm_intf, offset=0x000002d8,
             access='read-only', reset=0x00000000,
             doc='DTM_AUX Input Selection Register')
field(name='ASEL0', register=r, offset=0, width=2, access='read-write',
      doc='CDTM0_DTM4_AUX Input Selection (ATOMx_CH0...3)')
field(name='ASEL1', register=r, offset=2, width=2, access='read-write',
      doc='CDTM1_DTM4_AUX Input Selection (ATOMx_CH0...3)')
field(name='ASEL2', register=r, offset=4, width=2, access='read-write',
      doc='CDTM2_DTM4_AUX Input Selection (ATOMx_CH0...3)')
field(name='ASEL3', register=r, offset=6, width=2, access='read-write',
      doc='CDTM3_DTM4_AUX Input Selection (ATOMx_CH0...3)')
field(name='ASEL4', register=r, offset=8, width=2, access='read-write',
      doc='CDTM4_DTM4_AUX Input Selection (ATOMx_CH0...3)')
field(name='TSEL0', register=r, offset=16, width=2, access='read-write',
      doc='CDTM0_DTM0_AUX Input Selection (TOMx_CH0...3)')
field(name='TSEL1', register=r, offset=18, width=2, access='read-write',
      doc='CDTM1_DTM0_AUX Input Selection (TOMx_CH0...3)')
field(name='TSEL2', register=r, offset=20, width=2, access='read-write',
      doc='CDTM2_DTM0_AUX Input Selection (TOMx_CH0...3)')

r = register('CANOUTSEL0', width=32, block=gtm_intf, offset=0x000002dc,
             access='read-only', reset=0x00000000,
             doc='CAN0/CAN1 Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 0')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 1')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 2')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 3')
field(name='SEL4', register=r, offset=16, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 4')
field(name='SEL5', register=r, offset=20, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 5')
field(name='SEL6', register=r, offset=24, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 6')
field(name='SEL7', register=r, offset=28, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 7')

r = register('CANOUTSEL1', width=32, block=gtm_intf, offset=0x000002e0,
             access='read-only', reset=0x00000000,
             doc='CAN2 Output Select Register')
field(name='SEL0', register=r, offset=0, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 0')
field(name='SEL1', register=r, offset=4, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 1')
field(name='SEL2', register=r, offset=8, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 2')
field(name='SEL3', register=r, offset=12, width=4, access='read-write',
      doc='Output Selection for GTM to CAN connection 3')
