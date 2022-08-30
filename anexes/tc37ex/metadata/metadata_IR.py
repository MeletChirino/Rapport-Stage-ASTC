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

vlab.properties(name="IfxIr3Wrapper", kind="leaf")
intTargetSocket = vlab.bus("ir3_intf", kind="target", width=32)

# INT registers
r = register('ID', width=32, block=intTargetSocket, offset=0x0008,
             access='read-only', reset=0x00B9C000,
             doc='Module Identification Register')
field(name='MOD_REV', register=r, offset=0, width=8, access='read-only',
      doc='Module Revision Number')
field(name='MOD_TYPE', register=r, offset=8, width=8, access='read-only',
      doc='Module Type')
field(name='MOD_NUMBER', register=r, offset=16, width=16, access='read-only',
      doc='Module Number Value')

r = register('SRB0', width=32, block=intTargetSocket, offset=0x0010,
             access='read-only', reset=0x00000000,
             doc='Service Request Broadcast Register 0')
field(name='TRIG0', register=r, offset=0, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 0')
field(name='TRIG1', register=r, offset=1, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 1')
field(name='TRIG2', register=r, offset=2, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 2')
field(name='TRIG3', register=r, offset=3, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 3')
field(name='TRIG4', register=r, offset=4, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 4')
field(name='TRIG5', register=r, offset=5, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 5')
field(name='TRIG6', register=r, offset=6, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 6')
field(name='TRIG7', register=r, offset=7, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 7')

r = register('SRB1', width=32, block=intTargetSocket, offset=0x0014,
             access='read-only', reset=0x00000000,
             doc='Service Request Broadcast Register 1')
field(name='TRIG0', register=r, offset=0, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 0')
field(name='TRIG1', register=r, offset=1, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 1')
field(name='TRIG2', register=r, offset=2, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 2')
field(name='TRIG3', register=r, offset=3, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 3')
field(name='TRIG4', register=r, offset=4, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 4')
field(name='TRIG5', register=r, offset=5, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 5')
field(name='TRIG6', register=r, offset=6, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 6')
field(name='TRIG7', register=r, offset=7, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 7')

r = register('SRB2', width=32, block=intTargetSocket, offset=0x0018,
             access='read-only', reset=0x00000000,
             doc='Service Request Broadcast Register 2')
field(name='TRIG0', register=r, offset=0, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 0')
field(name='TRIG1', register=r, offset=1, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 1')
field(name='TRIG2', register=r, offset=2, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 2')
field(name='TRIG3', register=r, offset=3, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 3')
field(name='TRIG4', register=r, offset=4, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 4')
field(name='TRIG5', register=r, offset=5, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 5')
field(name='TRIG6', register=r, offset=6, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 6')
field(name='TRIG7', register=r, offset=7, width=1, access='write-only',
      doc='General Purpose Service Request Trigger 7')

r = register('OOBS', width=32, block=intTargetSocket, offset=0x0080,
             access='read-only', reset=0x00000000,
             doc='OTGM OTGB0/1 Status')
field(name='OTGB0', register=r, offset=0, width=16, access='read-only',
      doc='Status of OTGB0')
field(name='OTGB1', register=r, offset=16, width=16, access='read-only',
      doc='Status of OTGB1')

r = register('OSSIC', width=32, block=intTargetSocket, offset=0x0084,
             access='read-only', reset=0x00000000,
             doc='OTGM SSI Control')
field(name='TGS', register=r, offset=0, width=2, access='read-write',
      doc='Trigger Set for OTGB0/1')
field(name='TGB', register=r, offset=2, width=1, access='read-write',
      doc='OTGB0/1 Bus Select')

r = register('OIXTS', width=32, block=intTargetSocket, offset=0x0088,
             access='read-only', reset=0x00000000,
             doc='OTGM IRQ MUX Trigger Set Select')
field(name='TGS', register=r, offset=0, width=2, access='read-write',
      doc='Trigger Set Select for OTGB0/1 Overlay')
field(name='OBS', register=r, offset=8, width=2, access='read-write',
      doc='Overlay Byte Select')

r = register('OIXMS', width=32, block=intTargetSocket, offset=0x008c,
             access='read-only', reset=0x00000000,
             doc='OTGM IRQ MUX Missed IRQ Select')
field(name='MIRQ', register=r, offset=0, width=10, access='read-write',
      doc='SRN Index for Missed Interrupt Trigger')

r = register('OIXS0', width=32, block=intTargetSocket, offset=0x0090,
             access='read-only', reset=0x00000000,
             doc='OTGM IRQ MUX Select 0')
field(name='IRQ0', register=r, offset=0, width=10, access='read-write',
      doc='SRN Index for Interrupt Trigger 0')
field(name='IRQ1', register=r, offset=16, width=10, access='read-write',
      doc='SRN Index for Interrupt Trigger 1')

r = register('OIXS1', width=32, block=intTargetSocket, offset=0x0094,
             access='read-only', reset=0x00000000,
             doc='OTGM IRQ MUX Select 1')
field(name='IRQ2', register=r, offset=0, width=10, access='read-write',
      doc='SRN Index for Interrupt Trigger 2')
field(name='IRQ3', register=r, offset=16, width=10, access='read-write',
      doc='SRN Index for Interrupt Trigger 3')

r = register('OIT', width=32, block=intTargetSocket, offset=0x00a0,
             access='read-only', reset=0x00000000,
             doc='OTGM IRQ Trace')
field(name='TOS0', register=r, offset=0, width=3, access='read-write',
      doc='Type of Service for Observation on OTGB0')
field(name='OE0', register=r, offset=7, width=1, access='read-write',
      doc='Output Enable for OTGB0')
field(name='TOS1', register=r, offset=8, width=3, access='read-write',
      doc='Type of Service for Observation on OTGB1')
field(name='OE1', register=r, offset=15, width=1, access='read-write',
      doc='Output Enable for OTGB1')

r = register('OMISP', width=32, block=intTargetSocket, offset=0x00a4,
             access='read-only', reset=0x00000000,
             doc='OTGM MCDS I/F Sensitivity Posedge')
field(name='OTGB0', register=r, offset=0, width=16, access='read-write',
      doc='Bitwise Posedge Sensitivity for OTGB0')
field(name='OTGB1', register=r, offset=16, width=16, access='read-write',
      doc='Bitwise Posedge Sensitivity for OTGB1')

r = register('OMISN', width=32, block=intTargetSocket, offset=0x00a8,
             access='read-only', reset=0x00000000,
             doc='OTGM MCDS I/F Sensitivity Negedge')
field(name='OTGB0', register=r, offset=0, width=16, access='read-write',
      doc='Bitwise Negedge Sensitivity for OTGB0')
field(name='OTGB1', register=r, offset=16, width=16, access='read-write',
      doc='Bitwise Negedge Sensitivity for OTGB1')

r = register('ACCEN_CONFIG0', width=32, block=intTargetSocket, offset=0x00f0,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering all INT_ECRx and all SRCy[15:0], Register 0')
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

r = register('ACCEN_CONFIG1', width=32, block=intTargetSocket, offset=0x00f4,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering all INT_ECRx and all SRCy[15:0], Register 1')

r = register('ACCEN_SRB00', width=32, block=intTargetSocket, offset=0x0100,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering SRB0, Register 0')
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

r = register('ACCEN_SRB10', width=32, block=intTargetSocket, offset=0x0108,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering SRB1, Register 0')
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

r = register('ACCEN_SRB20', width=32, block=intTargetSocket, offset=0x0110,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering SRB2, Register 0')
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

r = register('ACCEN_SRB01', width=32, block=intTargetSocket, offset=0x0104,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering SRB0, Register 1')

r = register('ACCEN_SRB11', width=32, block=intTargetSocket, offset=0x010c,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering SRB1, Register 1')

r = register('ACCEN_SRB21', width=32, block=intTargetSocket, offset=0x0114,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering SRB2, Register 1')

r = register('ACCEN_SRC_TOS00', width=32, block=intTargetSocket, offset=0x0180,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU0, Register 0')
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

r = register('ACCEN_SRC_TOS10', width=32, block=intTargetSocket, offset=0x0188,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU1, Register 0')
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

r = register('ACCEN_SRC_TOS20', width=32, block=intTargetSocket, offset=0x0190,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU2, Register 0')
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

r = register('ACCEN_SRC_TOS30', width=32, block=intTargetSocket, offset=0x0198,
             access='read-only', reset=0xFFFFFFFF,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU3, Register 0')
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

r = register('ACCEN_SRC_TOS01', width=32, block=intTargetSocket, offset=0x0184,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU0, Register 1')

r = register('ACCEN_SRC_TOS11', width=32, block=intTargetSocket, offset=0x018c,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU1, Register 1')

r = register('ACCEN_SRC_TOS21', width=32, block=intTargetSocket, offset=0x0194,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU2, Register 1')

r = register('ACCEN_SRC_TOS31', width=32, block=intTargetSocket, offset=0x019c,
             access='read-only', reset=0x00000000,
             doc='Access Enable covering all SRCx[31:16] mapped to ICU3, Register 1')

r = register('LWSR0', width=32, block=intTargetSocket, offset=0x0200,
             access='read-only', reset=0x00000000,
             doc='Latest Winning Service Request Register 0, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Latest Winner Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Latest Winner ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Latest Winner Index Number')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='LWSR Register Status')

r = register('LWSR1', width=32, block=intTargetSocket, offset=0x0210,
             access='read-only', reset=0x00000000,
             doc='Latest Winning Service Request Register 1, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Latest Winner Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Latest Winner ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Latest Winner Index Number')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='LWSR Register Status')

r = register('LWSR2', width=32, block=intTargetSocket, offset=0x0220,
             access='read-only', reset=0x00000000,
             doc='Latest Winning Service Request Register 2, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Latest Winner Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Latest Winner ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Latest Winner Index Number')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='LWSR Register Status')

r = register('LWSR3', width=32, block=intTargetSocket, offset=0x0230,
             access='read-only', reset=0x00000000,
             doc='Latest Winning Service Request Register 3, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Latest Winner Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Latest Winner ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Latest Winner Index Number')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='LWSR Register Status')

r = register('LASR0', width=32, block=intTargetSocket, offset=0x0204,
             access='read-only', reset=0x00000000,
             doc='Last Acknowledged Service Request Register 0, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Last Acknowledged Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Last Acknowledged Interrupt ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Last Acknowledged Interrupt SRN ID')

r = register('LASR1', width=32, block=intTargetSocket, offset=0x0214,
             access='read-only', reset=0x00000000,
             doc='Last Acknowledged Service Request Register 1, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Last Acknowledged Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Last Acknowledged Interrupt ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Last Acknowledged Interrupt SRN ID')

r = register('LASR2', width=32, block=intTargetSocket, offset=0x0224,
             access='read-only', reset=0x00000000,
             doc='Last Acknowledged Service Request Register 2, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Last Acknowledged Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Last Acknowledged Interrupt ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Last Acknowledged Interrupt SRN ID')

r = register('LASR3', width=32, block=intTargetSocket, offset=0x0234,
             access='read-only', reset=0x00000000,
             doc='Last Acknowledged Service Request Register 3, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-only',
      doc='Last Acknowledged Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-only',
      doc='Last Acknowledged Interrupt ECC')
field(name='ID', register=r, offset=16, width=10, access='read-only',
      doc='Last Acknowledged Interrupt SRN ID')

r = register('ECR0', width=32, block=intTargetSocket, offset=0x0208,
             access='read-only', reset=0x00000000,
             doc='Error Capture Register 0, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-write',
      doc='Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-write',
      doc='Service Request ECC')
field(name='ID', register=r, offset=16, width=10, access='read-write',
      doc='Service Request Node ID')
field(name='EOVCLR', register=r, offset=28, width=1, access='write-only',
      doc='Error Overflow Bit')
field(name='STATCLR', register=r, offset=29, width=1, access='write-only',
      doc='Error Status Bit')
field(name='EOV', register=r, offset=30, width=1, access='read-only',
      doc='Error Overflow Bit')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='Error Status Bit')

r = register('ECR1', width=32, block=intTargetSocket, offset=0x0218,
             access='read-only', reset=0x00000000,
             doc='Error Capture Register 1, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-write',
      doc='Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-write',
      doc='Service Request ECC')
field(name='ID', register=r, offset=16, width=10, access='read-write',
      doc='Service Request Node ID')
field(name='EOVCLR', register=r, offset=28, width=1, access='write-only',
      doc='Error Overflow Bit')
field(name='STATCLR', register=r, offset=29, width=1, access='write-only',
      doc='Error Status Bit')
field(name='EOV', register=r, offset=30, width=1, access='read-only',
      doc='Error Overflow Bit')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='Error Status Bit')

r = register('ECR2', width=32, block=intTargetSocket, offset=0x0228,
             access='read-only', reset=0x00000000,
             doc='Error Capture Register 2, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-write',
      doc='Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-write',
      doc='Service Request ECC')
field(name='ID', register=r, offset=16, width=10, access='read-write',
      doc='Service Request Node ID')
field(name='EOVCLR', register=r, offset=28, width=1, access='write-only',
      doc='Error Overflow Bit')
field(name='STATCLR', register=r, offset=29, width=1, access='write-only',
      doc='Error Status Bit')
field(name='EOV', register=r, offset=30, width=1, access='read-only',
      doc='Error Overflow Bit')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='Error Status Bit')

r = register('ECR3', width=32, block=intTargetSocket, offset=0x0238,
             access='read-only', reset=0x00000000,
             doc='Error Capture Register 3, related to ICUx')
field(name='PN', register=r, offset=0, width=8, access='read-write',
      doc='Service Request Priority Number')
field(name='ECC', register=r, offset=10, width=5, access='read-write',
      doc='Service Request ECC')
field(name='ID', register=r, offset=16, width=10, access='read-write',
      doc='Service Request Node ID')
field(name='EOVCLR', register=r, offset=28, width=1, access='write-only',
      doc='Error Overflow Bit')
field(name='STATCLR', register=r, offset=29, width=1, access='write-only',
      doc='Error Status Bit')
field(name='EOV', register=r, offset=30, width=1, access='read-only',
      doc='Error Overflow Bit')
field(name='STAT', register=r, offset=31, width=1, access='read-only',
      doc='Error Status Bit')

# SRC registers
def src_fields(r):
    vlab.field(name="SRPN", register=r, offset = 0, width = 8 ,access = "read-write")
    vlab.field(name="SRE", register=r, offset = 10, width = 1 ,access = "read-write")
    vlab.field(name="TOS", register=r, offset = 11, width = 3 ,access = "read-write")
    vlab.field(name="ECC", register=r, offset = 16, width = 5 ,access = "read-write")
    vlab.field(name="SRR", register=r, offset = 24, width = 1 ,access = "read-only")
    vlab.field(name="CLRR", register=r, offset = 25, width = 1 ,access = "write-only")
    vlab.field(name="SETR", register=r, offset = 26, width = 1 ,access = "write-only")
    vlab.field(name="IOV", register=r, offset = 27, width = 1 ,access = "read-only")
    vlab.field(name="IOVCLR", register=r, offset = 28, width = 1 ,access = "write-only")
    vlab.field(name="SWS", register=r, offset = 29, width = 1 ,access = "read-only")
    vlab.field(name="SWSCLR", register=r, offset = 30, width = 1 ,access = "write-only")

r = vlab.register('CPU0SB', width=32, block=intTargetSocket, offset=0x00001000, reset=0x00000000, doc='CPU0 Software Breakpoint Service Request')
src_fields(r)
r = vlab.register('CPU1SB', width=32, block=intTargetSocket, offset=0x00001004, reset=0x00000000, doc='CPU1 Software Breakpoint Service Request')
src_fields(r)
r = vlab.register('CPU2SB', width=32, block=intTargetSocket, offset=0x00001008, reset=0x00000000, doc='CPU2 Software Breakpoint Service Request')
src_fields(r)
r = vlab.register('BCUSPB', width=32, block=intTargetSocket, offset=0x00001020, reset=0x00000000, doc='SBCU Service Request [SPB Bus Control Unit)')
src_fields(r)
r = vlab.register('XBAR0', width=32, block=intTargetSocket, offset=0x00001030, reset=0x00000000, doc='SRI Domain 0 Service Request')
src_fields(r)
r = vlab.register('CERBERUS0', width=32, block=intTargetSocket, offset=0x00001040, reset=0x00000000, doc='Cerberus Service Request 0')
src_fields(r)
r = vlab.register('CERBERUS1', width=32, block=intTargetSocket, offset=0x00001044, reset=0x00000000, doc='Cerberus Service Request 1')
src_fields(r)
r = vlab.register('ASCLIN0TX', width=32, block=intTargetSocket, offset=0x00001050, reset=0x00000000, doc='ASCLIN0 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN1TX', width=32, block=intTargetSocket, offset=0x0000105C, reset=0x00000000, doc='ASCLIN1 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN2TX', width=32, block=intTargetSocket, offset=0x00001068, reset=0x00000000, doc='ASCLIN2 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN3TX', width=32, block=intTargetSocket, offset=0x00001074, reset=0x00000000, doc='ASCLIN3 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN4TX', width=32, block=intTargetSocket, offset=0x00001080, reset=0x00000000, doc='ASCLIN4 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN5TX', width=32, block=intTargetSocket, offset=0x0000108C, reset=0x00000000, doc='ASCLIN5 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN6TX', width=32, block=intTargetSocket, offset=0x00001098, reset=0x00000000, doc='ASCLIN6 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN7TX', width=32, block=intTargetSocket, offset=0x000010A4, reset=0x00000000, doc='ASCLIN7 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN8TX', width=32, block=intTargetSocket, offset=0x000010B0, reset=0x00000000, doc='ASCLIN8 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN9TX', width=32, block=intTargetSocket, offset=0x000010BC, reset=0x00000000, doc='ASCLIN9 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN10TX', width=32, block=intTargetSocket, offset=0x000010C8, reset=0x00000000, doc='ASCLIN10 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN11TX', width=32, block=intTargetSocket, offset=0x000010D4, reset=0x00000000, doc='ASCLIN11 Transmit Service Request')
src_fields(r)
r = vlab.register('ASCLIN0RX', width=32, block=intTargetSocket, offset=0x00001054, reset=0x00000000, doc='ASCLIN0 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN1RX', width=32, block=intTargetSocket, offset=0x00001060, reset=0x00000000, doc='ASCLIN1 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN2RX', width=32, block=intTargetSocket, offset=0x0000106C, reset=0x00000000, doc='ASCLIN2 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN3RX', width=32, block=intTargetSocket, offset=0x00001078, reset=0x00000000, doc='ASCLIN3 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN4RX', width=32, block=intTargetSocket, offset=0x00001084, reset=0x00000000, doc='ASCLIN4 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN5RX', width=32, block=intTargetSocket, offset=0x00001090, reset=0x00000000, doc='ASCLIN5 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN6RX', width=32, block=intTargetSocket, offset=0x0000109C, reset=0x00000000, doc='ASCLIN6 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN7RX', width=32, block=intTargetSocket, offset=0x000010A8, reset=0x00000000, doc='ASCLIN7 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN8RX', width=32, block=intTargetSocket, offset=0x000010B4, reset=0x00000000, doc='ASCLIN8 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN9RX', width=32, block=intTargetSocket, offset=0x000010C0, reset=0x00000000, doc='ASCLIN9 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN10RX', width=32, block=intTargetSocket, offset=0x000010CC, reset=0x00000000, doc='ASCLIN10 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN11RX', width=32, block=intTargetSocket, offset=0x000010D8, reset=0x00000000, doc='ASCLIN11 Receive Service Request')
src_fields(r)
r = vlab.register('ASCLIN0ERR', width=32, block=intTargetSocket, offset=0x00001058, reset=0x00000000, doc='ASCLIN0 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN1ERR', width=32, block=intTargetSocket, offset=0x00001064, reset=0x00000000, doc='ASCLIN1 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN2ERR', width=32, block=intTargetSocket, offset=0x00001070, reset=0x00000000, doc='ASCLIN2 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN3ERR', width=32, block=intTargetSocket, offset=0x0000107C, reset=0x00000000, doc='ASCLIN3 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN4ERR', width=32, block=intTargetSocket, offset=0x00001088, reset=0x00000000, doc='ASCLIN4 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN5ERR', width=32, block=intTargetSocket, offset=0x00001094, reset=0x00000000, doc='ASCLIN5 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN6ERR', width=32, block=intTargetSocket, offset=0x000010A0, reset=0x00000000, doc='ASCLIN6 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN7ERR', width=32, block=intTargetSocket, offset=0x000010AC, reset=0x00000000, doc='ASCLIN7 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN8ERR', width=32, block=intTargetSocket, offset=0x000010B8, reset=0x00000000, doc='ASCLIN8 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN9ERR', width=32, block=intTargetSocket, offset=0x000010C4, reset=0x00000000, doc='ASCLIN9 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN10ERR', width=32, block=intTargetSocket, offset=0x000010D0, reset=0x00000000, doc='ASCLIN10 Error Service Request')
src_fields(r)
r = vlab.register('ASCLIN11ERR', width=32, block=intTargetSocket, offset=0x000010DC, reset=0x00000000, doc='ASCLIN11 Error Service Request')
src_fields(r)
r = vlab.register('MTUDONE', width=32, block=intTargetSocket, offset=0x000010EC, reset=0x00000000, doc='MTU Done Service Request')
src_fields(r)
r = vlab.register('QSPI0TX', width=32, block=intTargetSocket, offset=0x000010F0, reset=0x00000000, doc='QSPI0 Transmit Service Request')
src_fields(r)
r = vlab.register('QSPI1TX', width=32, block=intTargetSocket, offset=0x00001104, reset=0x00000000, doc='QSPI1 Transmit Service Request')
src_fields(r)
r = vlab.register('QSPI2TX', width=32, block=intTargetSocket, offset=0x00001118, reset=0x00000000, doc='QSPI2 Transmit Service Request')
src_fields(r)
r = vlab.register('QSPI3TX', width=32, block=intTargetSocket, offset=0x0000112C, reset=0x00000000, doc='QSPI3 Transmit Service Request')
src_fields(r)
r = vlab.register('QSPI4TX', width=32, block=intTargetSocket, offset=0x00001140, reset=0x00000000, doc='QSPI4 Transmit Service Request')
src_fields(r)
r = vlab.register('QSPI0RX', width=32, block=intTargetSocket, offset=0x000010F4, reset=0x00000000, doc='QSPI0 Receive Service Request')
src_fields(r)
r = vlab.register('QSPI1RX', width=32, block=intTargetSocket, offset=0x00001108, reset=0x00000000, doc='QSPI1 Receive Service Request')
src_fields(r)
r = vlab.register('QSPI2RX', width=32, block=intTargetSocket, offset=0x0000111C, reset=0x00000000, doc='QSPI2 Receive Service Request')
src_fields(r)
r = vlab.register('QSPI3RX', width=32, block=intTargetSocket, offset=0x00001130, reset=0x00000000, doc='QSPI3 Receive Service Request')
src_fields(r)
r = vlab.register('QSPI4RX', width=32, block=intTargetSocket, offset=0x00001144, reset=0x00000000, doc='QSPI4 Receive Service Request')
src_fields(r)
r = vlab.register('QSPI0ERR', width=32, block=intTargetSocket, offset=0x000010F8, reset=0x00000000, doc='QSPI0 Error Service Request')
src_fields(r)
r = vlab.register('QSPI1ERR', width=32, block=intTargetSocket, offset=0x0000110C, reset=0x00000000, doc='QSPI1 Error Service Request')
src_fields(r)
r = vlab.register('QSPI2ERR', width=32, block=intTargetSocket, offset=0x00001120, reset=0x00000000, doc='QSPI2 Error Service Request')
src_fields(r)
r = vlab.register('QSPI3ERR', width=32, block=intTargetSocket, offset=0x00001134, reset=0x00000000, doc='QSPI3 Error Service Request')
src_fields(r)
r = vlab.register('QSPI4ERR', width=32, block=intTargetSocket, offset=0x00001148, reset=0x00000000, doc='QSPI4 Error Service Request')
src_fields(r)
r = vlab.register('QSPI0PT', width=32, block=intTargetSocket, offset=0x000010FC, reset=0x00000000, doc='QSPI0 Phase Transition Service Request')
src_fields(r)
r = vlab.register('QSPI1PT', width=32, block=intTargetSocket, offset=0x00001110, reset=0x00000000, doc='QSPI1 Phase Transition Service Request')
src_fields(r)
r = vlab.register('QSPI2PT', width=32, block=intTargetSocket, offset=0x00001124, reset=0x00000000, doc='QSPI2 Phase Transition Service Request')
src_fields(r)
r = vlab.register('QSPI3PT', width=32, block=intTargetSocket, offset=0x00001138, reset=0x00000000, doc='QSPI3 Phase Transition Service Request')
src_fields(r)
r = vlab.register('QSPI4PT', width=32, block=intTargetSocket, offset=0x0000114C, reset=0x00000000, doc='QSPI4 Phase Transition Service Request')
src_fields(r)
r = vlab.register('QSPI0U', width=32, block=intTargetSocket, offset=0x00001100, reset=0x00000000, doc='QSPI0 User Defined Service Request')
src_fields(r)
r = vlab.register('QSPI1U', width=32, block=intTargetSocket, offset=0x00001114, reset=0x00000000, doc='QSPI1 User Defined Service Request')
src_fields(r)
r = vlab.register('QSPI2U', width=32, block=intTargetSocket, offset=0x00001128, reset=0x00000000, doc='QSPI2 User Defined Service Request')
src_fields(r)
r = vlab.register('QSPI3U', width=32, block=intTargetSocket, offset=0x0000113C, reset=0x00000000, doc='QSPI3 User Defined Service Request')
src_fields(r)
r = vlab.register('QSPI4U', width=32, block=intTargetSocket, offset=0x00001150, reset=0x00000000, doc='QSPI4 User Defined Service Request')
src_fields(r)
r = vlab.register('HSCT0', width=32, block=intTargetSocket, offset=0x00001180, reset=0x00000000, doc='HSCT0 Service Request')
src_fields(r)
r = vlab.register('HSSL0COK0', width=32, block=intTargetSocket, offset=0x00001190, reset=0x00000000, doc='HSSL0 Channel 0 OK Service Request')
src_fields(r)
r = vlab.register('HSSL0COK1', width=32, block=intTargetSocket, offset=0x000011A0, reset=0x00000000, doc='HSSL0 Channel 1 OK Service Request')
src_fields(r)
r = vlab.register('HSSL0COK2', width=32, block=intTargetSocket, offset=0x000011B0, reset=0x00000000, doc='HSSL0 Channel 2 OK Service Request')
src_fields(r)
r = vlab.register('HSSL0COK3', width=32, block=intTargetSocket, offset=0x000011C0, reset=0x00000000, doc='HSSL0 Channel 3 OK Service Request')
src_fields(r)
r = vlab.register('HSSL0RDI0', width=32, block=intTargetSocket, offset=0x00001194, reset=0x00000000, doc='HSSL0 Channel 0 Read Data Service Request')
src_fields(r)
r = vlab.register('HSSL0RDI1', width=32, block=intTargetSocket, offset=0x000011A4, reset=0x00000000, doc='HSSL0 Channel 1 Read Data Service Request')
src_fields(r)
r = vlab.register('HSSL0RDI2', width=32, block=intTargetSocket, offset=0x000011B4, reset=0x00000000, doc='HSSL0 Channel 2 Read Data Service Request')
src_fields(r)
r = vlab.register('HSSL0RDI3', width=32, block=intTargetSocket, offset=0x000011C4, reset=0x00000000, doc='HSSL0 Channel 3 Read Data Service Request')
src_fields(r)
r = vlab.register('HSSL0ERR0', width=32, block=intTargetSocket, offset=0x00001198, reset=0x00000000, doc='HSSL0 Channel 0 Error Service Request')
src_fields(r)
r = vlab.register('HSSL0ERR1', width=32, block=intTargetSocket, offset=0x000011A8, reset=0x00000000, doc='HSSL0 Channel 1 Error Service Request')
src_fields(r)
r = vlab.register('HSSL0ERR2', width=32, block=intTargetSocket, offset=0x000011B8, reset=0x00000000, doc='HSSL0 Channel 2 Error Service Request')
src_fields(r)
r = vlab.register('HSSL0ERR3', width=32, block=intTargetSocket, offset=0x000011C8, reset=0x00000000, doc='HSSL0 Channel 3 Error Service Request')
src_fields(r)
r = vlab.register('HSSL0TRG0', width=32, block=intTargetSocket, offset=0x0000119C, reset=0x00000000, doc='HSSL0 Channel 0 Trigger Interrupt Service Request')
src_fields(r)
r = vlab.register('HSSL0TRG1', width=32, block=intTargetSocket, offset=0x000011AC, reset=0x00000000, doc='HSSL0 Channel 1 Trigger Interrupt Service Request')
src_fields(r)
r = vlab.register('HSSL0TRG2', width=32, block=intTargetSocket, offset=0x000011BC, reset=0x00000000, doc='HSSL0 Channel 2 Trigger Interrupt Service Request')
src_fields(r)
r = vlab.register('HSSL0TRG3', width=32, block=intTargetSocket, offset=0x000011CC, reset=0x00000000, doc='HSSL0 Channel 3 Trigger Interrupt Service Request')
src_fields(r)
r = vlab.register('HSSL0EXI', width=32, block=intTargetSocket, offset=0x000011D0, reset=0x00000000, doc='HSSL0 Exception Service Request')
src_fields(r)
r = vlab.register('I2C0DTR', width=32, block=intTargetSocket, offset=0x00001220, reset=0x00000000, doc='I2C0 Data Transfer Request')
src_fields(r)
r = vlab.register('I2C0ERR', width=32, block=intTargetSocket, offset=0x00001224, reset=0x00000000, doc='I2C0 Error Service Request')
src_fields(r)
r = vlab.register('I2C0P', width=32, block=intTargetSocket, offset=0x00001228, reset=0x00000000, doc='I2C0 Protocol Service Request')
src_fields(r)
r = vlab.register('SENT0', width=32, block=intTargetSocket, offset=0x00001240, reset=0x00000000, doc='SENT TRIG0 Service Request')
src_fields(r)
r = vlab.register('SENT1', width=32, block=intTargetSocket, offset=0x00001244, reset=0x00000000, doc='SENT TRIG1 Service Request')
src_fields(r)
r = vlab.register('SENT2', width=32, block=intTargetSocket, offset=0x00001248, reset=0x00000000, doc='SENT TRIG2 Service Request')
src_fields(r)
r = vlab.register('SENT3', width=32, block=intTargetSocket, offset=0x0000124C, reset=0x00000000, doc='SENT TRIG3 Service Request')
src_fields(r)
r = vlab.register('SENT4', width=32, block=intTargetSocket, offset=0x00001250, reset=0x00000000, doc='SENT TRIG4 Service Request')
src_fields(r)
r = vlab.register('SENT5', width=32, block=intTargetSocket, offset=0x00001254, reset=0x00000000, doc='SENT TRIG5 Service Request')
src_fields(r)
r = vlab.register('SENT6', width=32, block=intTargetSocket, offset=0x00001258, reset=0x00000000, doc='SENT TRIG6 Service Request')
src_fields(r)
r = vlab.register('SENT7', width=32, block=intTargetSocket, offset=0x0000125C, reset=0x00000000, doc='SENT TRIG7 Service Request')
src_fields(r)
r = vlab.register('SENT8', width=32, block=intTargetSocket, offset=0x00001260, reset=0x00000000, doc='SENT TRIG8 Service Request')
src_fields(r)
r = vlab.register('SENT9', width=32, block=intTargetSocket, offset=0x00001264, reset=0x00000000, doc='SENT TRIG9 Service Request')
src_fields(r)
r = vlab.register('MSC0SR0', width=32, block=intTargetSocket, offset=0x00001270, reset=0x00000000, doc='MSC0 Service Request 0')
src_fields(r)
r = vlab.register('MSC0SR1', width=32, block=intTargetSocket, offset=0x00001274, reset=0x00000000, doc='MSC0 Service Request 1')
src_fields(r)
r = vlab.register('MSC0SR2', width=32, block=intTargetSocket, offset=0x00001278, reset=0x00000000, doc='MSC0 Service Request 2')
src_fields(r)
r = vlab.register('MSC0SR3', width=32, block=intTargetSocket, offset=0x0000127C, reset=0x00000000, doc='MSC0 Service Request 3')
src_fields(r)
r = vlab.register('MSC0SR4', width=32, block=intTargetSocket, offset=0x00001280, reset=0x00000000, doc='MSC0 Service Request 4')
src_fields(r)
r = vlab.register('MSC1SR0', width=32, block=intTargetSocket, offset=0x00001284, reset=0x00000000, doc='MSC1 Service Request 0')
src_fields(r)
r = vlab.register('MSC1SR1', width=32, block=intTargetSocket, offset=0x00001288, reset=0x00000000, doc='MSC1 Service Request 1')
src_fields(r)
r = vlab.register('MSC1SR2', width=32, block=intTargetSocket, offset=0x0000128C, reset=0x00000000, doc='MSC1 Service Request 2')
src_fields(r)
r = vlab.register('MSC1SR3', width=32, block=intTargetSocket, offset=0x00001290, reset=0x00000000, doc='MSC1 Service Request 3')
src_fields(r)
r = vlab.register('MSC1SR4', width=32, block=intTargetSocket, offset=0x00001294, reset=0x00000000, doc='MSC1 Service Request 4')
src_fields(r)
r = vlab.register('CCU60SR0', width=32, block=intTargetSocket, offset=0x000012C0, reset=0x00000000, doc='CCU0 Service Request 0')
src_fields(r)
r = vlab.register('CCU60SR1', width=32, block=intTargetSocket, offset=0x000012C4, reset=0x00000000, doc='CCU0 Service Request 1')
src_fields(r)
r = vlab.register('CCU60SR2', width=32, block=intTargetSocket, offset=0x000012C8, reset=0x00000000, doc='CCU0 Service Request 2')
src_fields(r)
r = vlab.register('CCU60SR3', width=32, block=intTargetSocket, offset=0x000012CC, reset=0x00000000, doc='CCU0 Service Request 3')
src_fields(r)
r = vlab.register('CCU61SR0', width=32, block=intTargetSocket, offset=0x000012D0, reset=0x00000000, doc='CCU1 Service Request 0')
src_fields(r)
r = vlab.register('CCU61SR1', width=32, block=intTargetSocket, offset=0x000012D4, reset=0x00000000, doc='CCU1 Service Request 1')
src_fields(r)
r = vlab.register('CCU61SR2', width=32, block=intTargetSocket, offset=0x000012D8, reset=0x00000000, doc='CCU1 Service Request 2')
src_fields(r)
r = vlab.register('CCU61SR3', width=32, block=intTargetSocket, offset=0x000012DC, reset=0x00000000, doc='CCU1 Service Request 3')
src_fields(r)
r = vlab.register('GPT120CIRQ', width=32, block=intTargetSocket, offset=0x000012E0, reset=0x00000000, doc='GPT120 CAPREL Service Request')
src_fields(r)
r = vlab.register('GPT120T2', width=32, block=intTargetSocket, offset=0x000012E4, reset=0x00000000, doc='GPT120 Timer 2 Service Request')
src_fields(r)
r = vlab.register('GPT120T3', width=32, block=intTargetSocket, offset=0x000012E8, reset=0x00000000, doc='GPT120 Timer 3 Service Request')
src_fields(r)
r = vlab.register('GPT120T4', width=32, block=intTargetSocket, offset=0x000012EC, reset=0x00000000, doc='GPT120 Timer 4 Service Request')
src_fields(r)
r = vlab.register('GPT120T5', width=32, block=intTargetSocket, offset=0x000012F0, reset=0x00000000, doc='GPT120 Timer 5 Service Request')
src_fields(r)
r = vlab.register('GPT120T6', width=32, block=intTargetSocket, offset=0x000012F4, reset=0x00000000, doc='GPT120 Timer 6 Service Request')
src_fields(r)
r = vlab.register('STM0SR0', width=32, block=intTargetSocket, offset=0x00001300, reset=0x00000000, doc='System Timer 0 Service Request 0')
src_fields(r)
r = vlab.register('STM0SR1', width=32, block=intTargetSocket, offset=0x00001304, reset=0x00000000, doc='System Timer 0 Service Request 1')
src_fields(r)
r = vlab.register('STM1SR0', width=32, block=intTargetSocket, offset=0x00001308, reset=0x00000000, doc='System Timer 1 Service Request 0')
src_fields(r)
r = vlab.register('STM1SR1', width=32, block=intTargetSocket, offset=0x0000130C, reset=0x00000000, doc='System Timer 1 Service Request 1')
src_fields(r)
r = vlab.register('STM2SR0', width=32, block=intTargetSocket, offset=0x00001310, reset=0x00000000, doc='System Timer 2 Service Request 0')
src_fields(r)
r = vlab.register('STM2SR1', width=32, block=intTargetSocket, offset=0x00001314, reset=0x00000000, doc='System Timer 2 Service Request 1')
src_fields(r)
r = vlab.register('FCE0', width=32, block=intTargetSocket, offset=0x00001330, reset=0x00000000, doc='FCE0 Error Service Request')
src_fields(r)
r = vlab.register('DMAERR0', width=32, block=intTargetSocket, offset=0x00001340, reset=0x00000000, doc='DMA Error Service Request 0')
src_fields(r)
r = vlab.register('DMAERR1', width=32, block=intTargetSocket, offset=0x00001344, reset=0x00000000, doc='DMA Error Service Request 1')
src_fields(r)
r = vlab.register('DMAERR2', width=32, block=intTargetSocket, offset=0x00001348, reset=0x00000000, doc='DMA Error Service Request 2')
src_fields(r)
r = vlab.register('DMAERR3', width=32, block=intTargetSocket, offset=0x0000134C, reset=0x00000000, doc='DMA Error Service Request 3')
src_fields(r)
r = vlab.register('DMACH0', width=32, block=intTargetSocket, offset=0x00001370, reset=0x00000000, doc='DMA Channel 0 Service Request')
src_fields(r)
r = vlab.register('DMACH1', width=32, block=intTargetSocket, offset=0x00001374, reset=0x00000000, doc='DMA Channel 1 Service Request')
src_fields(r)
r = vlab.register('DMACH2', width=32, block=intTargetSocket, offset=0x00001378, reset=0x00000000, doc='DMA Channel 2 Service Request')
src_fields(r)
r = vlab.register('DMACH3', width=32, block=intTargetSocket, offset=0x0000137C, reset=0x00000000, doc='DMA Channel 3 Service Request')
src_fields(r)
r = vlab.register('DMACH4', width=32, block=intTargetSocket, offset=0x00001380, reset=0x00000000, doc='DMA Channel 4 Service Request')
src_fields(r)
r = vlab.register('DMACH5', width=32, block=intTargetSocket, offset=0x00001384, reset=0x00000000, doc='DMA Channel 5 Service Request')
src_fields(r)
r = vlab.register('DMACH6', width=32, block=intTargetSocket, offset=0x00001388, reset=0x00000000, doc='DMA Channel 6 Service Request')
src_fields(r)
r = vlab.register('DMACH7', width=32, block=intTargetSocket, offset=0x0000138C, reset=0x00000000, doc='DMA Channel 7 Service Request')
src_fields(r)
r = vlab.register('DMACH8', width=32, block=intTargetSocket, offset=0x00001390, reset=0x00000000, doc='DMA Channel 8 Service Request')
src_fields(r)
r = vlab.register('DMACH9', width=32, block=intTargetSocket, offset=0x00001394, reset=0x00000000, doc='DMA Channel 9 Service Request')
src_fields(r)
r = vlab.register('DMACH10', width=32, block=intTargetSocket, offset=0x00001398, reset=0x00000000, doc='DMA Channel 10 Service Request')
src_fields(r)
r = vlab.register('DMACH11', width=32, block=intTargetSocket, offset=0x0000139C, reset=0x00000000, doc='DMA Channel 11 Service Request')
src_fields(r)
r = vlab.register('DMACH12', width=32, block=intTargetSocket, offset=0x000013A0, reset=0x00000000, doc='DMA Channel 12 Service Request')
src_fields(r)
r = vlab.register('DMACH13', width=32, block=intTargetSocket, offset=0x000013A4, reset=0x00000000, doc='DMA Channel 13 Service Request')
src_fields(r)
r = vlab.register('DMACH14', width=32, block=intTargetSocket, offset=0x000013A8, reset=0x00000000, doc='DMA Channel 14 Service Request')
src_fields(r)
r = vlab.register('DMACH15', width=32, block=intTargetSocket, offset=0x000013AC, reset=0x00000000, doc='DMA Channel 15 Service Request')
src_fields(r)
r = vlab.register('DMACH16', width=32, block=intTargetSocket, offset=0x000013B0, reset=0x00000000, doc='DMA Channel 16 Service Request')
src_fields(r)
r = vlab.register('DMACH17', width=32, block=intTargetSocket, offset=0x000013B4, reset=0x00000000, doc='DMA Channel 17 Service Request')
src_fields(r)
r = vlab.register('DMACH18', width=32, block=intTargetSocket, offset=0x000013B8, reset=0x00000000, doc='DMA Channel 18 Service Request')
src_fields(r)
r = vlab.register('DMACH19', width=32, block=intTargetSocket, offset=0x000013BC, reset=0x00000000, doc='DMA Channel 19 Service Request')
src_fields(r)
r = vlab.register('DMACH20', width=32, block=intTargetSocket, offset=0x000013C0, reset=0x00000000, doc='DMA Channel 20 Service Request')
src_fields(r)
r = vlab.register('DMACH21', width=32, block=intTargetSocket, offset=0x000013C4, reset=0x00000000, doc='DMA Channel 21 Service Request')
src_fields(r)
r = vlab.register('DMACH22', width=32, block=intTargetSocket, offset=0x000013C8, reset=0x00000000, doc='DMA Channel 22 Service Request')
src_fields(r)
r = vlab.register('DMACH23', width=32, block=intTargetSocket, offset=0x000013CC, reset=0x00000000, doc='DMA Channel 23 Service Request')
src_fields(r)
r = vlab.register('DMACH24', width=32, block=intTargetSocket, offset=0x000013D0, reset=0x00000000, doc='DMA Channel 24 Service Request')
src_fields(r)
r = vlab.register('DMACH25', width=32, block=intTargetSocket, offset=0x000013D4, reset=0x00000000, doc='DMA Channel 25 Service Request')
src_fields(r)
r = vlab.register('DMACH26', width=32, block=intTargetSocket, offset=0x000013D8, reset=0x00000000, doc='DMA Channel 26 Service Request')
src_fields(r)
r = vlab.register('DMACH27', width=32, block=intTargetSocket, offset=0x000013DC, reset=0x00000000, doc='DMA Channel 27 Service Request')
src_fields(r)
r = vlab.register('DMACH28', width=32, block=intTargetSocket, offset=0x000013E0, reset=0x00000000, doc='DMA Channel 28 Service Request')
src_fields(r)
r = vlab.register('DMACH29', width=32, block=intTargetSocket, offset=0x000013E4, reset=0x00000000, doc='DMA Channel 29 Service Request')
src_fields(r)
r = vlab.register('DMACH30', width=32, block=intTargetSocket, offset=0x000013E8, reset=0x00000000, doc='DMA Channel 30 Service Request')
src_fields(r)
r = vlab.register('DMACH31', width=32, block=intTargetSocket, offset=0x000013EC, reset=0x00000000, doc='DMA Channel 31 Service Request')
src_fields(r)
r = vlab.register('DMACH32', width=32, block=intTargetSocket, offset=0x000013F0, reset=0x00000000, doc='DMA Channel 32 Service Request')
src_fields(r)
r = vlab.register('DMACH33', width=32, block=intTargetSocket, offset=0x000013F4, reset=0x00000000, doc='DMA Channel 33 Service Request')
src_fields(r)
r = vlab.register('DMACH34', width=32, block=intTargetSocket, offset=0x000013F8, reset=0x00000000, doc='DMA Channel 34 Service Request')
src_fields(r)
r = vlab.register('DMACH35', width=32, block=intTargetSocket, offset=0x000013FC, reset=0x00000000, doc='DMA Channel 35 Service Request')
src_fields(r)
r = vlab.register('DMACH36', width=32, block=intTargetSocket, offset=0x00001400, reset=0x00000000, doc='DMA Channel 36 Service Request')
src_fields(r)
r = vlab.register('DMACH37', width=32, block=intTargetSocket, offset=0x00001404, reset=0x00000000, doc='DMA Channel 37 Service Request')
src_fields(r)
r = vlab.register('DMACH38', width=32, block=intTargetSocket, offset=0x00001408, reset=0x00000000, doc='DMA Channel 38 Service Request')
src_fields(r)
r = vlab.register('DMACH39', width=32, block=intTargetSocket, offset=0x0000140C, reset=0x00000000, doc='DMA Channel 39 Service Request')
src_fields(r)
r = vlab.register('DMACH40', width=32, block=intTargetSocket, offset=0x00001410, reset=0x00000000, doc='DMA Channel 40 Service Request')
src_fields(r)
r = vlab.register('DMACH41', width=32, block=intTargetSocket, offset=0x00001414, reset=0x00000000, doc='DMA Channel 41 Service Request')
src_fields(r)
r = vlab.register('DMACH42', width=32, block=intTargetSocket, offset=0x00001418, reset=0x00000000, doc='DMA Channel 42 Service Request')
src_fields(r)
r = vlab.register('DMACH43', width=32, block=intTargetSocket, offset=0x0000141C, reset=0x00000000, doc='DMA Channel 43 Service Request')
src_fields(r)
r = vlab.register('DMACH44', width=32, block=intTargetSocket, offset=0x00001420, reset=0x00000000, doc='DMA Channel 44 Service Request')
src_fields(r)
r = vlab.register('DMACH45', width=32, block=intTargetSocket, offset=0x00001424, reset=0x00000000, doc='DMA Channel 45 Service Request')
src_fields(r)
r = vlab.register('DMACH46', width=32, block=intTargetSocket, offset=0x00001428, reset=0x00000000, doc='DMA Channel 46 Service Request')
src_fields(r)
r = vlab.register('DMACH47', width=32, block=intTargetSocket, offset=0x0000142C, reset=0x00000000, doc='DMA Channel 47 Service Request')
src_fields(r)
r = vlab.register('DMACH48', width=32, block=intTargetSocket, offset=0x00001430, reset=0x00000000, doc='DMA Channel 48 Service Request')
src_fields(r)
r = vlab.register('DMACH49', width=32, block=intTargetSocket, offset=0x00001434, reset=0x00000000, doc='DMA Channel 49 Service Request')
src_fields(r)
r = vlab.register('DMACH50', width=32, block=intTargetSocket, offset=0x00001438, reset=0x00000000, doc='DMA Channel 50 Service Request')
src_fields(r)
r = vlab.register('DMACH51', width=32, block=intTargetSocket, offset=0x0000143C, reset=0x00000000, doc='DMA Channel 51 Service Request')
src_fields(r)
r = vlab.register('DMACH52', width=32, block=intTargetSocket, offset=0x00001440, reset=0x00000000, doc='DMA Channel 52 Service Request')
src_fields(r)
r = vlab.register('DMACH53', width=32, block=intTargetSocket, offset=0x00001444, reset=0x00000000, doc='DMA Channel 53 Service Request')
src_fields(r)
r = vlab.register('DMACH54', width=32, block=intTargetSocket, offset=0x00001448, reset=0x00000000, doc='DMA Channel 54 Service Request')
src_fields(r)
r = vlab.register('DMACH55', width=32, block=intTargetSocket, offset=0x0000144C, reset=0x00000000, doc='DMA Channel 55 Service Request')
src_fields(r)
r = vlab.register('DMACH56', width=32, block=intTargetSocket, offset=0x00001450, reset=0x00000000, doc='DMA Channel 56 Service Request')
src_fields(r)
r = vlab.register('DMACH57', width=32, block=intTargetSocket, offset=0x00001454, reset=0x00000000, doc='DMA Channel 57 Service Request')
src_fields(r)
r = vlab.register('DMACH58', width=32, block=intTargetSocket, offset=0x00001458, reset=0x00000000, doc='DMA Channel 58 Service Request')
src_fields(r)
r = vlab.register('DMACH59', width=32, block=intTargetSocket, offset=0x0000145C, reset=0x00000000, doc='DMA Channel 59 Service Request')
src_fields(r)
r = vlab.register('DMACH60', width=32, block=intTargetSocket, offset=0x00001460, reset=0x00000000, doc='DMA Channel 60 Service Request')
src_fields(r)
r = vlab.register('DMACH61', width=32, block=intTargetSocket, offset=0x00001464, reset=0x00000000, doc='DMA Channel 61 Service Request')
src_fields(r)
r = vlab.register('DMACH62', width=32, block=intTargetSocket, offset=0x00001468, reset=0x00000000, doc='DMA Channel 62 Service Request')
src_fields(r)
r = vlab.register('DMACH63', width=32, block=intTargetSocket, offset=0x0000146C, reset=0x00000000, doc='DMA Channel 63 Service Request')
src_fields(r)
r = vlab.register('DMACH64', width=32, block=intTargetSocket, offset=0x00001470, reset=0x00000000, doc='DMA Channel 64 Service Request')
src_fields(r)
r = vlab.register('DMACH65', width=32, block=intTargetSocket, offset=0x00001474, reset=0x00000000, doc='DMA Channel 65 Service Request')
src_fields(r)
r = vlab.register('DMACH66', width=32, block=intTargetSocket, offset=0x00001478, reset=0x00000000, doc='DMA Channel 66 Service Request')
src_fields(r)
r = vlab.register('DMACH67', width=32, block=intTargetSocket, offset=0x0000147C, reset=0x00000000, doc='DMA Channel 67 Service Request')
src_fields(r)
r = vlab.register('DMACH68', width=32, block=intTargetSocket, offset=0x00001480, reset=0x00000000, doc='DMA Channel 68 Service Request')
src_fields(r)
r = vlab.register('DMACH69', width=32, block=intTargetSocket, offset=0x00001484, reset=0x00000000, doc='DMA Channel 69 Service Request')
src_fields(r)
r = vlab.register('DMACH70', width=32, block=intTargetSocket, offset=0x00001488, reset=0x00000000, doc='DMA Channel 70 Service Request')
src_fields(r)
r = vlab.register('DMACH71', width=32, block=intTargetSocket, offset=0x0000148C, reset=0x00000000, doc='DMA Channel 71 Service Request')
src_fields(r)
r = vlab.register('DMACH72', width=32, block=intTargetSocket, offset=0x00001490, reset=0x00000000, doc='DMA Channel 72 Service Request')
src_fields(r)
r = vlab.register('DMACH73', width=32, block=intTargetSocket, offset=0x00001494, reset=0x00000000, doc='DMA Channel 73 Service Request')
src_fields(r)
r = vlab.register('DMACH74', width=32, block=intTargetSocket, offset=0x00001498, reset=0x00000000, doc='DMA Channel 74 Service Request')
src_fields(r)
r = vlab.register('DMACH75', width=32, block=intTargetSocket, offset=0x0000149C, reset=0x00000000, doc='DMA Channel 75 Service Request')
src_fields(r)
r = vlab.register('DMACH76', width=32, block=intTargetSocket, offset=0x000014A0, reset=0x00000000, doc='DMA Channel 76 Service Request')
src_fields(r)
r = vlab.register('DMACH77', width=32, block=intTargetSocket, offset=0x000014A4, reset=0x00000000, doc='DMA Channel 77 Service Request')
src_fields(r)
r = vlab.register('DMACH78', width=32, block=intTargetSocket, offset=0x000014A8, reset=0x00000000, doc='DMA Channel 78 Service Request')
src_fields(r)
r = vlab.register('DMACH79', width=32, block=intTargetSocket, offset=0x000014AC, reset=0x00000000, doc='DMA Channel 79 Service Request')
src_fields(r)
r = vlab.register('DMACH80', width=32, block=intTargetSocket, offset=0x000014B0, reset=0x00000000, doc='DMA Channel 80 Service Request')
src_fields(r)
r = vlab.register('DMACH81', width=32, block=intTargetSocket, offset=0x000014B4, reset=0x00000000, doc='DMA Channel 81 Service Request')
src_fields(r)
r = vlab.register('DMACH82', width=32, block=intTargetSocket, offset=0x000014B8, reset=0x00000000, doc='DMA Channel 82 Service Request')
src_fields(r)
r = vlab.register('DMACH83', width=32, block=intTargetSocket, offset=0x000014BC, reset=0x00000000, doc='DMA Channel 83 Service Request')
src_fields(r)
r = vlab.register('DMACH84', width=32, block=intTargetSocket, offset=0x000014C0, reset=0x00000000, doc='DMA Channel 84 Service Request')
src_fields(r)
r = vlab.register('DMACH85', width=32, block=intTargetSocket, offset=0x000014C4, reset=0x00000000, doc='DMA Channel 85 Service Request')
src_fields(r)
r = vlab.register('DMACH86', width=32, block=intTargetSocket, offset=0x000014C8, reset=0x00000000, doc='DMA Channel 86 Service Request')
src_fields(r)
r = vlab.register('DMACH87', width=32, block=intTargetSocket, offset=0x000014CC, reset=0x00000000, doc='DMA Channel 87 Service Request')
src_fields(r)
r = vlab.register('DMACH88', width=32, block=intTargetSocket, offset=0x000014D0, reset=0x00000000, doc='DMA Channel 88 Service Request')
src_fields(r)
r = vlab.register('DMACH89', width=32, block=intTargetSocket, offset=0x000014D4, reset=0x00000000, doc='DMA Channel 89 Service Request')
src_fields(r)
r = vlab.register('DMACH90', width=32, block=intTargetSocket, offset=0x000014D8, reset=0x00000000, doc='DMA Channel 90 Service Request')
src_fields(r)
r = vlab.register('DMACH91', width=32, block=intTargetSocket, offset=0x000014DC, reset=0x00000000, doc='DMA Channel 91 Service Request')
src_fields(r)
r = vlab.register('DMACH92', width=32, block=intTargetSocket, offset=0x000014E0, reset=0x00000000, doc='DMA Channel 92 Service Request')
src_fields(r)
r = vlab.register('DMACH93', width=32, block=intTargetSocket, offset=0x000014E4, reset=0x00000000, doc='DMA Channel 93 Service Request')
src_fields(r)
r = vlab.register('DMACH94', width=32, block=intTargetSocket, offset=0x000014E8, reset=0x00000000, doc='DMA Channel 94 Service Request')
src_fields(r)
r = vlab.register('DMACH95', width=32, block=intTargetSocket, offset=0x000014EC, reset=0x00000000, doc='DMA Channel 95 Service Request')
src_fields(r)
r = vlab.register('DMACH96', width=32, block=intTargetSocket, offset=0x000014F0, reset=0x00000000, doc='DMA Channel 96 Service Request')
src_fields(r)
r = vlab.register('DMACH97', width=32, block=intTargetSocket, offset=0x000014F4, reset=0x00000000, doc='DMA Channel 97 Service Request')
src_fields(r)
r = vlab.register('DMACH98', width=32, block=intTargetSocket, offset=0x000014F8, reset=0x00000000, doc='DMA Channel 98 Service Request')
src_fields(r)
r = vlab.register('DMACH99', width=32, block=intTargetSocket, offset=0x000014FC, reset=0x00000000, doc='DMA Channel 99 Service Request')
src_fields(r)
r = vlab.register('DMACH100', width=32, block=intTargetSocket, offset=0x00001500, reset=0x00000000, doc='DMA Channel 100 Service Request')
src_fields(r)
r = vlab.register('DMACH101', width=32, block=intTargetSocket, offset=0x00001504, reset=0x00000000, doc='DMA Channel 101 Service Request')
src_fields(r)
r = vlab.register('DMACH102', width=32, block=intTargetSocket, offset=0x00001508, reset=0x00000000, doc='DMA Channel 102 Service Request')
src_fields(r)
r = vlab.register('DMACH103', width=32, block=intTargetSocket, offset=0x0000150C, reset=0x00000000, doc='DMA Channel 103 Service Request')
src_fields(r)
r = vlab.register('DMACH104', width=32, block=intTargetSocket, offset=0x00001510, reset=0x00000000, doc='DMA Channel 104 Service Request')
src_fields(r)
r = vlab.register('DMACH105', width=32, block=intTargetSocket, offset=0x00001514, reset=0x00000000, doc='DMA Channel 105 Service Request')
src_fields(r)
r = vlab.register('DMACH106', width=32, block=intTargetSocket, offset=0x00001518, reset=0x00000000, doc='DMA Channel 106 Service Request')
src_fields(r)
r = vlab.register('DMACH107', width=32, block=intTargetSocket, offset=0x0000151C, reset=0x00000000, doc='DMA Channel 107 Service Request')
src_fields(r)
r = vlab.register('DMACH108', width=32, block=intTargetSocket, offset=0x00001520, reset=0x00000000, doc='DMA Channel 108 Service Request')
src_fields(r)
r = vlab.register('DMACH109', width=32, block=intTargetSocket, offset=0x00001524, reset=0x00000000, doc='DMA Channel 109 Service Request')
src_fields(r)
r = vlab.register('DMACH110', width=32, block=intTargetSocket, offset=0x00001528, reset=0x00000000, doc='DMA Channel 110 Service Request')
src_fields(r)
r = vlab.register('DMACH111', width=32, block=intTargetSocket, offset=0x0000152C, reset=0x00000000, doc='DMA Channel 111 Service Request')
src_fields(r)
r = vlab.register('DMACH112', width=32, block=intTargetSocket, offset=0x00001530, reset=0x00000000, doc='DMA Channel 112 Service Request')
src_fields(r)
r = vlab.register('DMACH113', width=32, block=intTargetSocket, offset=0x00001534, reset=0x00000000, doc='DMA Channel 113 Service Request')
src_fields(r)
r = vlab.register('DMACH114', width=32, block=intTargetSocket, offset=0x00001538, reset=0x00000000, doc='DMA Channel 114 Service Request')
src_fields(r)
r = vlab.register('DMACH115', width=32, block=intTargetSocket, offset=0x0000153C, reset=0x00000000, doc='DMA Channel 115 Service Request')
src_fields(r)
r = vlab.register('DMACH116', width=32, block=intTargetSocket, offset=0x00001540, reset=0x00000000, doc='DMA Channel 116 Service Request')
src_fields(r)
r = vlab.register('DMACH117', width=32, block=intTargetSocket, offset=0x00001544, reset=0x00000000, doc='DMA Channel 117 Service Request')
src_fields(r)
r = vlab.register('DMACH118', width=32, block=intTargetSocket, offset=0x00001548, reset=0x00000000, doc='DMA Channel 118 Service Request')
src_fields(r)
r = vlab.register('DMACH119', width=32, block=intTargetSocket, offset=0x0000154C, reset=0x00000000, doc='DMA Channel 119 Service Request')
src_fields(r)
r = vlab.register('DMACH120', width=32, block=intTargetSocket, offset=0x00001550, reset=0x00000000, doc='DMA Channel 120 Service Request')
src_fields(r)
r = vlab.register('DMACH121', width=32, block=intTargetSocket, offset=0x00001554, reset=0x00000000, doc='DMA Channel 121 Service Request')
src_fields(r)
r = vlab.register('DMACH122', width=32, block=intTargetSocket, offset=0x00001558, reset=0x00000000, doc='DMA Channel 122 Service Request')
src_fields(r)
r = vlab.register('DMACH123', width=32, block=intTargetSocket, offset=0x0000155C, reset=0x00000000, doc='DMA Channel 123 Service Request')
src_fields(r)
r = vlab.register('DMACH124', width=32, block=intTargetSocket, offset=0x00001560, reset=0x00000000, doc='DMA Channel 124 Service Request')
src_fields(r)
r = vlab.register('DMACH125', width=32, block=intTargetSocket, offset=0x00001564, reset=0x00000000, doc='DMA Channel 125 Service Request')
src_fields(r)
r = vlab.register('DMACH126', width=32, block=intTargetSocket, offset=0x00001568, reset=0x00000000, doc='DMA Channel 126 Service Request')
src_fields(r)
r = vlab.register('DMACH127', width=32, block=intTargetSocket, offset=0x0000156C, reset=0x00000000, doc='DMA Channel 127 Service Request')
src_fields(r)
r = vlab.register('GETH0', width=32, block=intTargetSocket, offset=0x00001580, reset=0x00000000, doc='GETH Service Request 0')
src_fields(r)
r = vlab.register('GETH1', width=32, block=intTargetSocket, offset=0x00001584, reset=0x00000000, doc='GETH Service Request 1')
src_fields(r)
r = vlab.register('GETH2', width=32, block=intTargetSocket, offset=0x00001588, reset=0x00000000, doc='GETH Service Request 2')
src_fields(r)
r = vlab.register('GETH3', width=32, block=intTargetSocket, offset=0x0000158C, reset=0x00000000, doc='GETH Service Request 3')
src_fields(r)
r = vlab.register('GETH4', width=32, block=intTargetSocket, offset=0x00001590, reset=0x00000000, doc='GETH Service Request 4')
src_fields(r)
r = vlab.register('GETH5', width=32, block=intTargetSocket, offset=0x00001594, reset=0x00000000, doc='GETH Service Request 5')
src_fields(r)
r = vlab.register('GETH6', width=32, block=intTargetSocket, offset=0x00001598, reset=0x00000000, doc='GETH Service Request 6')
src_fields(r)
r = vlab.register('GETH7', width=32, block=intTargetSocket, offset=0x0000159C, reset=0x00000000, doc='GETH Service Request 7')
src_fields(r)
r = vlab.register('GETH8', width=32, block=intTargetSocket, offset=0x000015A0, reset=0x00000000, doc='GETH Service Request 8')
src_fields(r)
r = vlab.register('GETH9', width=32, block=intTargetSocket, offset=0x000015A4, reset=0x00000000, doc='GETH Service Request 9')
src_fields(r)
r = vlab.register('CAN0INT0', width=32, block=intTargetSocket, offset=0x000015B0, reset=0x00000000, doc='CAN0 Service Request 0')
src_fields(r)
r = vlab.register('CAN0INT1', width=32, block=intTargetSocket, offset=0x000015B4, reset=0x00000000, doc='CAN0 Service Request 1')
src_fields(r)
r = vlab.register('CAN0INT2', width=32, block=intTargetSocket, offset=0x000015B8, reset=0x00000000, doc='CAN0 Service Request 2')
src_fields(r)
r = vlab.register('CAN0INT3', width=32, block=intTargetSocket, offset=0x000015BC, reset=0x00000000, doc='CAN0 Service Request 3')
src_fields(r)
r = vlab.register('CAN0INT4', width=32, block=intTargetSocket, offset=0x000015C0, reset=0x00000000, doc='CAN0 Service Request 4')
src_fields(r)
r = vlab.register('CAN0INT5', width=32, block=intTargetSocket, offset=0x000015C4, reset=0x00000000, doc='CAN0 Service Request 5')
src_fields(r)
r = vlab.register('CAN0INT6', width=32, block=intTargetSocket, offset=0x000015C8, reset=0x00000000, doc='CAN0 Service Request 6')
src_fields(r)
r = vlab.register('CAN0INT7', width=32, block=intTargetSocket, offset=0x000015CC, reset=0x00000000, doc='CAN0 Service Request 7')
src_fields(r)
r = vlab.register('CAN0INT8', width=32, block=intTargetSocket, offset=0x000015D0, reset=0x00000000, doc='CAN0 Service Request 8')
src_fields(r)
r = vlab.register('CAN0INT9', width=32, block=intTargetSocket, offset=0x000015D4, reset=0x00000000, doc='CAN0 Service Request 9')
src_fields(r)
r = vlab.register('CAN0INT10', width=32, block=intTargetSocket, offset=0x000015D8, reset=0x00000000, doc='CAN0 Service Request 10')
src_fields(r)
r = vlab.register('CAN0INT11', width=32, block=intTargetSocket, offset=0x000015DC, reset=0x00000000, doc='CAN0 Service Request 11')
src_fields(r)
r = vlab.register('CAN0INT12', width=32, block=intTargetSocket, offset=0x000015E0, reset=0x00000000, doc='CAN0 Service Request 12')
src_fields(r)
r = vlab.register('CAN0INT13', width=32, block=intTargetSocket, offset=0x000015E4, reset=0x00000000, doc='CAN0 Service Request 13')
src_fields(r)
r = vlab.register('CAN0INT14', width=32, block=intTargetSocket, offset=0x000015E8, reset=0x00000000, doc='CAN0 Service Request 14')
src_fields(r)
r = vlab.register('CAN0INT15', width=32, block=intTargetSocket, offset=0x000015EC, reset=0x00000000, doc='CAN0 Service Request 15')
src_fields(r)
r = vlab.register('CAN1INT0', width=32, block=intTargetSocket, offset=0x000015F0, reset=0x00000000, doc='CAN1 Service Request 0')
src_fields(r)
r = vlab.register('CAN1INT1', width=32, block=intTargetSocket, offset=0x000015F4, reset=0x00000000, doc='CAN1 Service Request 1')
src_fields(r)
r = vlab.register('CAN1INT2', width=32, block=intTargetSocket, offset=0x000015F8, reset=0x00000000, doc='CAN1 Service Request 2')
src_fields(r)
r = vlab.register('CAN1INT3', width=32, block=intTargetSocket, offset=0x000015FC, reset=0x00000000, doc='CAN1 Service Request 3')
src_fields(r)
r = vlab.register('CAN1INT4', width=32, block=intTargetSocket, offset=0x00001600, reset=0x00000000, doc='CAN1 Service Request 4')
src_fields(r)
r = vlab.register('CAN1INT5', width=32, block=intTargetSocket, offset=0x00001604, reset=0x00000000, doc='CAN1 Service Request 5')
src_fields(r)
r = vlab.register('CAN1INT6', width=32, block=intTargetSocket, offset=0x00001608, reset=0x00000000, doc='CAN1 Service Request 6')
src_fields(r)
r = vlab.register('CAN1INT7', width=32, block=intTargetSocket, offset=0x0000160C, reset=0x00000000, doc='CAN1 Service Request 7')
src_fields(r)
r = vlab.register('CAN1INT8', width=32, block=intTargetSocket, offset=0x00001610, reset=0x00000000, doc='CAN1 Service Request 8')
src_fields(r)
r = vlab.register('CAN1INT9', width=32, block=intTargetSocket, offset=0x00001614, reset=0x00000000, doc='CAN1 Service Request 9')
src_fields(r)
r = vlab.register('CAN1INT10', width=32, block=intTargetSocket, offset=0x00001618, reset=0x00000000, doc='CAN1 Service Request 10')
src_fields(r)
r = vlab.register('CAN1INT11', width=32, block=intTargetSocket, offset=0x0000161C, reset=0x00000000, doc='CAN1 Service Request 11')
src_fields(r)
r = vlab.register('CAN1INT12', width=32, block=intTargetSocket, offset=0x00001620, reset=0x00000000, doc='CAN1 Service Request 12')
src_fields(r)
r = vlab.register('CAN1INT13', width=32, block=intTargetSocket, offset=0x00001624, reset=0x00000000, doc='CAN1 Service Request 13')
src_fields(r)
r = vlab.register('CAN1INT14', width=32, block=intTargetSocket, offset=0x00001628, reset=0x00000000, doc='CAN1 Service Request 14')
src_fields(r)
r = vlab.register('CAN1INT15', width=32, block=intTargetSocket, offset=0x0000162C, reset=0x00000000, doc='CAN1 Service Request 15')
src_fields(r)
r = vlab.register('VADCG0SR0', width=32, block=intTargetSocket, offset=0x00001670, reset=0x00000000, doc='EVADC Group 0 Service Request 0')
src_fields(r)
r = vlab.register('VADCG0SR1', width=32, block=intTargetSocket, offset=0x00001674, reset=0x00000000, doc='EVADC Group 0 Service Request 1')
src_fields(r)
r = vlab.register('VADCG0SR2', width=32, block=intTargetSocket, offset=0x00001678, reset=0x00000000, doc='EVADC Group 0 Service Request 2')
src_fields(r)
r = vlab.register('VADCG0SR3', width=32, block=intTargetSocket, offset=0x0000167C, reset=0x00000000, doc='EVADC Group 0 Service Request 3')
src_fields(r)
r = vlab.register('VADCG1SR0', width=32, block=intTargetSocket, offset=0x00001680, reset=0x00000000, doc='EVADC Group 1 Service Request 0')
src_fields(r)
r = vlab.register('VADCG1SR1', width=32, block=intTargetSocket, offset=0x00001684, reset=0x00000000, doc='EVADC Group 1 Service Request 1')
src_fields(r)
r = vlab.register('VADCG1SR2', width=32, block=intTargetSocket, offset=0x00001688, reset=0x00000000, doc='EVADC Group 1 Service Request 2')
src_fields(r)
r = vlab.register('VADCG1SR3', width=32, block=intTargetSocket, offset=0x0000168C, reset=0x00000000, doc='EVADC Group 1 Service Request 3')
src_fields(r)
r = vlab.register('VADCG2SR0', width=32, block=intTargetSocket, offset=0x00001690, reset=0x00000000, doc='EVADC Group 2 Service Request 0')
src_fields(r)
r = vlab.register('VADCG2SR1', width=32, block=intTargetSocket, offset=0x00001694, reset=0x00000000, doc='EVADC Group 2 Service Request 1')
src_fields(r)
r = vlab.register('VADCG2SR2', width=32, block=intTargetSocket, offset=0x00001698, reset=0x00000000, doc='EVADC Group 2 Service Request 2')
src_fields(r)
r = vlab.register('VADCG2SR3', width=32, block=intTargetSocket, offset=0x0000169C, reset=0x00000000, doc='EVADC Group 2 Service Request 3')
src_fields(r)
r = vlab.register('VADCG3SR0', width=32, block=intTargetSocket, offset=0x000016A0, reset=0x00000000, doc='EVADC Group 3 Service Request 0')
src_fields(r)
r = vlab.register('VADCG3SR1', width=32, block=intTargetSocket, offset=0x000016A4, reset=0x00000000, doc='EVADC Group 3 Service Request 1')
src_fields(r)
r = vlab.register('VADCG3SR2', width=32, block=intTargetSocket, offset=0x000016A8, reset=0x00000000, doc='EVADC Group 3 Service Request 2')
src_fields(r)
r = vlab.register('VADCG3SR3', width=32, block=intTargetSocket, offset=0x000016AC, reset=0x00000000, doc='EVADC Group 3 Service Request 3')
src_fields(r)
r = vlab.register('VADCG8SR0', width=32, block=intTargetSocket, offset=0x000016F0, reset=0x00000000, doc='EVADC Group 8 Service Request 0')
src_fields(r)
r = vlab.register('VADCG8SR1', width=32, block=intTargetSocket, offset=0x000016F4, reset=0x00000000, doc='EVADC Group 8 Service Request 1')
src_fields(r)
r = vlab.register('VADCG8SR2', width=32, block=intTargetSocket, offset=0x000016F8, reset=0x00000000, doc='EVADC Group 8 Service Request 2')
src_fields(r)
r = vlab.register('VADCG8SR3', width=32, block=intTargetSocket, offset=0x000016FC, reset=0x00000000, doc='EVADC Group 8 Service Request 3')
src_fields(r)
r = vlab.register('VADCG9SR0', width=32, block=intTargetSocket, offset=0x00001700, reset=0x00000000, doc='EVADC Group 9 Service Request 0')
src_fields(r)
r = vlab.register('VADCG9SR1', width=32, block=intTargetSocket, offset=0x00001704, reset=0x00000000, doc='EVADC Group 9 Service Request 1')
src_fields(r)
r = vlab.register('VADCG9SR2', width=32, block=intTargetSocket, offset=0x00001708, reset=0x00000000, doc='EVADC Group 9 Service Request 2')
src_fields(r)
r = vlab.register('VADCG9SR3', width=32, block=intTargetSocket, offset=0x0000170C, reset=0x00000000, doc='EVADC Group 9 Service Request 3')
src_fields(r)
r = vlab.register('VADCG10SR0', width=32, block=intTargetSocket, offset=0x00001710, reset=0x00000000, doc='EVADC Group 10 Service Request 0')
src_fields(r)
r = vlab.register('VADCG10SR1', width=32, block=intTargetSocket, offset=0x00001714, reset=0x00000000, doc='EVADC Group 10 Service Request 1')
src_fields(r)
r = vlab.register('VADCG10SR2', width=32, block=intTargetSocket, offset=0x00001718, reset=0x00000000, doc='EVADC Group 10 Service Request 2')
src_fields(r)
r = vlab.register('VADCG10SR3', width=32, block=intTargetSocket, offset=0x0000171C, reset=0x00000000, doc='EVADC Group 10 Service Request 3')
src_fields(r)
r = vlab.register('VADCG11SR0', width=32, block=intTargetSocket, offset=0x00001720, reset=0x00000000, doc='EVADC Group 11 Service Request 0')
src_fields(r)
r = vlab.register('VADCG11SR1', width=32, block=intTargetSocket, offset=0x00001724, reset=0x00000000, doc='EVADC Group 11 Service Request 1')
src_fields(r)
r = vlab.register('VADCG11SR2', width=32, block=intTargetSocket, offset=0x00001728, reset=0x00000000, doc='EVADC Group 11 Service Request 2')
src_fields(r)
r = vlab.register('VADCG11SR3', width=32, block=intTargetSocket, offset=0x0000172C, reset=0x00000000, doc='EVADC Group 11 Service Request 3')
src_fields(r)
r = vlab.register('VADCFC0SR0', width=32, block=intTargetSocket, offset=0x00001730, reset=0x00000000, doc='EVADC Fast Compare 0 Service Request SR0')
src_fields(r)
r = vlab.register('VADCFC1SR0', width=32, block=intTargetSocket, offset=0x00001734, reset=0x00000000, doc='EVADC Fast Compare 1 Service Request SR0')
src_fields(r)
r = vlab.register('VADCFC2SR0', width=32, block=intTargetSocket, offset=0x00001738, reset=0x00000000, doc='EVADC Fast Compare 2 Service Request SR0')
src_fields(r)
r = vlab.register('VADCFC3SR0', width=32, block=intTargetSocket, offset=0x0000173C, reset=0x00000000, doc='EVADC Fast Compare 3 Service Request SR0')
src_fields(r)
r = vlab.register('VADCCG0SR0', width=32, block=intTargetSocket, offset=0x00001750, reset=0x00000000, doc='EVADC Common Group 0 Service Request 0')
src_fields(r)
r = vlab.register('VADCCG0SR1', width=32, block=intTargetSocket, offset=0x00001754, reset=0x00000000, doc='EVADC Common Group 0 Service Request 1')
src_fields(r)
r = vlab.register('VADCCG0SR2', width=32, block=intTargetSocket, offset=0x00001758, reset=0x00000000, doc='EVADC Common Group 0 Service Request 2')
src_fields(r)
r = vlab.register('VADCCG0SR3', width=32, block=intTargetSocket, offset=0x0000175C, reset=0x00000000, doc='EVADC Common Group 0 Service Request 3')
src_fields(r)
r = vlab.register('VADCCG1SR0', width=32, block=intTargetSocket, offset=0x00001760, reset=0x00000000, doc='EVADC Common Group 1 Service Request 0')
src_fields(r)
r = vlab.register('VADCCG1SR1', width=32, block=intTargetSocket, offset=0x00001764, reset=0x00000000, doc='EVADC Common Group 1 Service Request 1')
src_fields(r)
r = vlab.register('VADCCG1SR2', width=32, block=intTargetSocket, offset=0x00001768, reset=0x00000000, doc='EVADC Common Group 1 Service Request 2')
src_fields(r)
r = vlab.register('VADCCG1SR3', width=32, block=intTargetSocket, offset=0x0000176C, reset=0x00000000, doc='EVADC Common Group 1 Service Request 3')
src_fields(r)
r = vlab.register('DSADCSRM0', width=32, block=intTargetSocket, offset=0x00001770, reset=0x00000000, doc='DSADC SRM0 Service Request')
src_fields(r)
r = vlab.register('DSADCSRM1', width=32, block=intTargetSocket, offset=0x00001778, reset=0x00000000, doc='DSADC SRM1 Service Request')
src_fields(r)
r = vlab.register('DSADCSRM2', width=32, block=intTargetSocket, offset=0x00001780, reset=0x00000000, doc='DSADC SRM2 Service Request')
src_fields(r)
r = vlab.register('DSADCSRM3', width=32, block=intTargetSocket, offset=0x00001788, reset=0x00000000, doc='DSADC SRM3 Service Request')
src_fields(r)
r = vlab.register('DSADCSRM4', width=32, block=intTargetSocket, offset=0x00001790, reset=0x00000000, doc='DSADC SRM4 Service Request')
src_fields(r)
r = vlab.register('DSADCSRM5', width=32, block=intTargetSocket, offset=0x00001798, reset=0x00000000, doc='DSADC SRM5 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA0', width=32, block=intTargetSocket, offset=0x00001774, reset=0x00000000, doc='DSADC SRA0 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA1', width=32, block=intTargetSocket, offset=0x0000177C, reset=0x00000000, doc='DSADC SRA1 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA2', width=32, block=intTargetSocket, offset=0x00001784, reset=0x00000000, doc='DSADC SRA2 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA3', width=32, block=intTargetSocket, offset=0x0000178C, reset=0x00000000, doc='DSADC SRA3 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA4', width=32, block=intTargetSocket, offset=0x00001794, reset=0x00000000, doc='DSADC SRA4 Service Request')
src_fields(r)
r = vlab.register('DSADCSRA5', width=32, block=intTargetSocket, offset=0x0000179C, reset=0x00000000, doc='DSADC SRA5 Service Request')
src_fields(r)
r = vlab.register('ERAY0INT0', width=32, block=intTargetSocket, offset=0x00001800, reset=0x00000000, doc='E-RAY 0 Service Request 0')
src_fields(r)
r = vlab.register('ERAY0INT1', width=32, block=intTargetSocket, offset=0x00001804, reset=0x00000000, doc='E-RAY 0 Service Request 1')
src_fields(r)
r = vlab.register('ERAY0TINT0', width=32, block=intTargetSocket, offset=0x00001808, reset=0x00000000, doc='E-RAY 0 Timer Interrupt 0 Service Request')
src_fields(r)
r = vlab.register('ERAY0TINT1', width=32, block=intTargetSocket, offset=0x0000180C, reset=0x00000000, doc='E-RAY 0 Timer Interrupt 1 Service Request')
src_fields(r)
r = vlab.register('ERAY0NDAT0', width=32, block=intTargetSocket, offset=0x00001810, reset=0x00000000, doc='E-RAY 0 New Data 0 Service Request')
src_fields(r)
r = vlab.register('ERAY0NDAT1', width=32, block=intTargetSocket, offset=0x00001814, reset=0x00000000, doc='E-RAY 0 New Data 1 Service Request')
src_fields(r)
r = vlab.register('ERAY0MBSC0', width=32, block=intTargetSocket, offset=0x00001818, reset=0x00000000, doc='E-RAY 0 Message Buffer Status Changed 0 Service Request')
src_fields(r)
r = vlab.register('ERAY0MBSC1', width=32, block=intTargetSocket, offset=0x0000181C, reset=0x00000000, doc='E-RAY 0 Message Buffer Status Changed 1 Service Request')
src_fields(r)
r = vlab.register('ERAY0OBUSY', width=32, block=intTargetSocket, offset=0x00001820, reset=0x00000000, doc='E-RAY 0 Output Buffer Busy')
src_fields(r)
r = vlab.register('ERAY0IBUSY', width=32, block=intTargetSocket, offset=0x00001824, reset=0x00000000, doc='E-RAY 0 Input Buffer Busy')
src_fields(r)
r = vlab.register('DMUHOST', width=32, block=intTargetSocket, offset=0x00001860, reset=0x00000000, doc='DMU Host Service Request')
src_fields(r)
r = vlab.register('DMUFSI', width=32, block=intTargetSocket, offset=0x00001864, reset=0x00000000, doc='DMU FSI Service Request')
src_fields(r)
r = vlab.register('HSM0', width=32, block=intTargetSocket, offset=0x00001870, reset=0x00000000, doc='HSM Service Request 0')
src_fields(r)
r = vlab.register('HSM1', width=32, block=intTargetSocket, offset=0x00001874, reset=0x00000000, doc='HSM Service Request 1')
src_fields(r)
r = vlab.register('SCUERU0', width=32, block=intTargetSocket, offset=0x00001880, reset=0x00000000, doc='SCU ERU Service Request 0')
src_fields(r)
r = vlab.register('SCUERU1', width=32, block=intTargetSocket, offset=0x00001884, reset=0x00000000, doc='SCU ERU Service Request 1')
src_fields(r)
r = vlab.register('SCUERU2', width=32, block=intTargetSocket, offset=0x00001888, reset=0x00000000, doc='SCU ERU Service Request 2')
src_fields(r)
r = vlab.register('SCUERU3', width=32, block=intTargetSocket, offset=0x0000188C, reset=0x00000000, doc='SCU ERU Service Request 3')
src_fields(r)
r = vlab.register('PMSDTS', width=32, block=intTargetSocket, offset=0x000018AC, reset=0x00000000, doc='PMS DTS Service Request')
src_fields(r)
r = vlab.register('PMS0', width=32, block=intTargetSocket, offset=0x000018B0, reset=0x00000000, doc='Power Management System Service Request 0')
src_fields(r)
r = vlab.register('PMS1', width=32, block=intTargetSocket, offset=0x000018B4, reset=0x00000000, doc='Power Management System Service Request 1')
src_fields(r)
r = vlab.register('PMS2', width=32, block=intTargetSocket, offset=0x000018B8, reset=0x00000000, doc='Power Management System Service Request 2')
src_fields(r)
r = vlab.register('PMS3', width=32, block=intTargetSocket, offset=0x000018BC, reset=0x00000000, doc='Power Management System Service Request 3')
src_fields(r)
r = vlab.register('SCR', width=32, block=intTargetSocket, offset=0x000018C0, reset=0x00000000, doc='Stand By Controller Service Request')
src_fields(r)
r = vlab.register('SMU0', width=32, block=intTargetSocket, offset=0x000018D0, reset=0x00000000, doc='SMU Service Request 0')
src_fields(r)
r = vlab.register('SMU1', width=32, block=intTargetSocket, offset=0x000018D4, reset=0x00000000, doc='SMU Service Request 1')
src_fields(r)
r = vlab.register('SMU2', width=32, block=intTargetSocket, offset=0x000018D8, reset=0x00000000, doc='SMU Service Request 2')
src_fields(r)
r = vlab.register('PSI50', width=32, block=intTargetSocket, offset=0x000018E0, reset=0x00000000, doc='PSI5 Service Request 0')
src_fields(r)
r = vlab.register('PSI51', width=32, block=intTargetSocket, offset=0x000018E4, reset=0x00000000, doc='PSI5 Service Request 1')
src_fields(r)
r = vlab.register('PSI52', width=32, block=intTargetSocket, offset=0x000018E8, reset=0x00000000, doc='PSI5 Service Request 2')
src_fields(r)
r = vlab.register('PSI53', width=32, block=intTargetSocket, offset=0x000018EC, reset=0x00000000, doc='PSI5 Service Request 3')
src_fields(r)
r = vlab.register('PSI54', width=32, block=intTargetSocket, offset=0x000018F0, reset=0x00000000, doc='PSI5 Service Request 4')
src_fields(r)
r = vlab.register('PSI55', width=32, block=intTargetSocket, offset=0x000018F4, reset=0x00000000, doc='PSI5 Service Request 5')
src_fields(r)
r = vlab.register('PSI56', width=32, block=intTargetSocket, offset=0x000018F8, reset=0x00000000, doc='PSI5 Service Request 6')
src_fields(r)
r = vlab.register('PSI57', width=32, block=intTargetSocket, offset=0x000018FC, reset=0x00000000, doc='PSI5 Service Request 7')
src_fields(r)
r = vlab.register('DAM0LI0', width=32, block=intTargetSocket, offset=0x00001910, reset=0x00000000, doc='DAM0 Limit 0 Service Request')
src_fields(r)
r = vlab.register('DAM0RI0', width=32, block=intTargetSocket, offset=0x00001914, reset=0x00000000, doc='DAM0 Ready 0 Service Reques')
src_fields(r)
r = vlab.register('DAM0LI1', width=32, block=intTargetSocket, offset=0x00001918, reset=0x00000000, doc='DAM0 Limit 1 Service Request')
src_fields(r)
r = vlab.register('DAM0RI1', width=32, block=intTargetSocket, offset=0x0000191C, reset=0x00000000, doc='DAM0 Ready 1 Service Request')
src_fields(r)
r = vlab.register('DAM0DR', width=32, block=intTargetSocket, offset=0x00001920, reset=0x00000000, doc='DAM0 DMA Ready Service Request')
src_fields(r)
r = vlab.register('DAM0ERR', width=32, block=intTargetSocket, offset=0x00001924, reset=0x00000000, doc='DAM0 Error Service Request')
src_fields(r)
r = vlab.register('PSI5S0', width=32, block=intTargetSocket, offset=0x00001950, reset=0x00000000, doc='PSI5-S Service Request 0')
src_fields(r)
r = vlab.register('PSI5S1', width=32, block=intTargetSocket, offset=0x00001954, reset=0x00000000, doc='PSI5-S Service Request 1')
src_fields(r)
r = vlab.register('PSI5S2', width=32, block=intTargetSocket, offset=0x00001958, reset=0x00000000, doc='PSI5-S Service Request 2')
src_fields(r)
r = vlab.register('PSI5S3', width=32, block=intTargetSocket, offset=0x0000195C, reset=0x00000000, doc='PSI5-S Service Request 3')
src_fields(r)
r = vlab.register('PSI5S4', width=32, block=intTargetSocket, offset=0x00001960, reset=0x00000000, doc='PSI5-S Service Request 4')
src_fields(r)
r = vlab.register('PSI5S5', width=32, block=intTargetSocket, offset=0x00001964, reset=0x00000000, doc='PSI5-S Service Request 5')
src_fields(r)
r = vlab.register('PSI5S6', width=32, block=intTargetSocket, offset=0x00001968, reset=0x00000000, doc='PSI5-S Service Request 6')
src_fields(r)
r = vlab.register('PSI5S7', width=32, block=intTargetSocket, offset=0x0000196C, reset=0x00000000, doc='PSI5-S Service Request 7')
src_fields(r)
r = vlab.register('GPSR00', width=32, block=intTargetSocket, offset=0x00001990, reset=0x00000000, doc='General Purpose Group 0 Service Request 0')
src_fields(r)
r = vlab.register('GPSR01', width=32, block=intTargetSocket, offset=0x00001994, reset=0x00000000, doc='General Purpose Group 0 Service Request 1')
src_fields(r)
r = vlab.register('GPSR02', width=32, block=intTargetSocket, offset=0x00001998, reset=0x00000000, doc='General Purpose Group 0 Service Request 2')
src_fields(r)
r = vlab.register('GPSR03', width=32, block=intTargetSocket, offset=0x0000199C, reset=0x00000000, doc='General Purpose Group 0 Service Request 3')
src_fields(r)
r = vlab.register('GPSR04', width=32, block=intTargetSocket, offset=0x000019A0, reset=0x00000000, doc='General Purpose Group 0 Service Request 4')
src_fields(r)
r = vlab.register('GPSR05', width=32, block=intTargetSocket, offset=0x000019A4, reset=0x00000000, doc='General Purpose Group 0 Service Request 5')
src_fields(r)
r = vlab.register('GPSR06', width=32, block=intTargetSocket, offset=0x000019A8, reset=0x00000000, doc='General Purpose Group 0 Service Request 6')
src_fields(r)
r = vlab.register('GPSR07', width=32, block=intTargetSocket, offset=0x000019AC, reset=0x00000000, doc='General Purpose Group 0 Service Request 7')
src_fields(r)
r = vlab.register('GPSR10', width=32, block=intTargetSocket, offset=0x000019B0, reset=0x00000000, doc='General Purpose Group 1 Service Request 0')
src_fields(r)
r = vlab.register('GPSR11', width=32, block=intTargetSocket, offset=0x000019B4, reset=0x00000000, doc='General Purpose Group 1 Service Request 1')
src_fields(r)
r = vlab.register('GPSR12', width=32, block=intTargetSocket, offset=0x000019B8, reset=0x00000000, doc='General Purpose Group 1 Service Request 2')
src_fields(r)
r = vlab.register('GPSR13', width=32, block=intTargetSocket, offset=0x000019BC, reset=0x00000000, doc='General Purpose Group 1 Service Request 3')
src_fields(r)
r = vlab.register('GPSR14', width=32, block=intTargetSocket, offset=0x000019C0, reset=0x00000000, doc='General Purpose Group 1 Service Request 4')
src_fields(r)
r = vlab.register('GPSR15', width=32, block=intTargetSocket, offset=0x000019C4, reset=0x00000000, doc='General Purpose Group 1 Service Request 5')
src_fields(r)
r = vlab.register('GPSR16', width=32, block=intTargetSocket, offset=0x000019C8, reset=0x00000000, doc='General Purpose Group 1 Service Request 6')
src_fields(r)
r = vlab.register('GPSR17', width=32, block=intTargetSocket, offset=0x000019CC, reset=0x00000000, doc='General Purpose Group 1 Service Request 7')
src_fields(r)
r = vlab.register('GPSR20', width=32, block=intTargetSocket, offset=0x000019D0, reset=0x00000000, doc='General Purpose Group 2 Service Request 0')
src_fields(r)
r = vlab.register('GPSR21', width=32, block=intTargetSocket, offset=0x000019D4, reset=0x00000000, doc='General Purpose Group 2 Service Request 1')
src_fields(r)
r = vlab.register('GPSR22', width=32, block=intTargetSocket, offset=0x000019D8, reset=0x00000000, doc='General Purpose Group 2 Service Request 2')
src_fields(r)
r = vlab.register('GPSR23', width=32, block=intTargetSocket, offset=0x000019DC, reset=0x00000000, doc='General Purpose Group 2 Service Request 3')
src_fields(r)
r = vlab.register('GPSR24', width=32, block=intTargetSocket, offset=0x000019E0, reset=0x00000000, doc='General Purpose Group 2 Service Request 4')
src_fields(r)
r = vlab.register('GPSR25', width=32, block=intTargetSocket, offset=0x000019E4, reset=0x00000000, doc='General Purpose Group 2 Service Request 5')
src_fields(r)
r = vlab.register('GPSR26', width=32, block=intTargetSocket, offset=0x000019E8, reset=0x00000000, doc='General Purpose Group 2 Service Request 6')
src_fields(r)
r = vlab.register('GPSR27', width=32, block=intTargetSocket, offset=0x000019EC, reset=0x00000000, doc='General Purpose Group 2 Service Request 7')
src_fields(r)
r = vlab.register('GTMAEIIRQ', width=32, block=intTargetSocket, offset=0x00001A70, reset=0x00000000, doc='AEI Shared Service Request')
src_fields(r)
r = vlab.register('GTMARUIRQ0', width=32, block=intTargetSocket, offset=0x00001A74, reset=0x00000000, doc='ARU Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMARUIRQ1', width=32, block=intTargetSocket, offset=0x00001A78, reset=0x00000000, doc='ARU Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMARUIRQ2', width=32, block=intTargetSocket, offset=0x00001A7C, reset=0x00000000, doc='ARU Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMBRCIRQ', width=32, block=intTargetSocket, offset=0x00001A80, reset=0x00000000, doc='BRC Shared Service Request')
src_fields(r)
r = vlab.register('GTMCMPIRQ', width=32, block=intTargetSocket, offset=0x00001A84, reset=0x00000000, doc='CMP Shared Service Request')
src_fields(r)
r = vlab.register('GTMSPE0IRQ', width=32, block=intTargetSocket, offset=0x00001A88, reset=0x00000000, doc='SPE0 Shared Service Request')
src_fields(r)
r = vlab.register('GTMSPE1IRQ', width=32, block=intTargetSocket, offset=0x00001A8C, reset=0x00000000, doc='SPE1 Shared Service Request')
src_fields(r)
r = vlab.register('GTMPSM00', width=32, block=intTargetSocket, offset=0x00001AA0, reset=0x00000000, doc='PSM0 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMPSM01', width=32, block=intTargetSocket, offset=0x00001AA4, reset=0x00000000, doc='PSM0 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMPSM02', width=32, block=intTargetSocket, offset=0x00001AA8, reset=0x00000000, doc='PSM0 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMPSM03', width=32, block=intTargetSocket, offset=0x00001AAC, reset=0x00000000, doc='PSM0 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMPSM04', width=32, block=intTargetSocket, offset=0x00001AB0, reset=0x00000000, doc='PSM0 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMPSM05', width=32, block=intTargetSocket, offset=0x00001AB4, reset=0x00000000, doc='PSM0 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMPSM06', width=32, block=intTargetSocket, offset=0x00001AB8, reset=0x00000000, doc='PSM0 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMPSM07', width=32, block=intTargetSocket, offset=0x00001ABC, reset=0x00000000, doc='PSM0 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMDPLL0', width=32, block=intTargetSocket, offset=0x00001B00, reset=0x00000000, doc='DPLL Service Request 0')
src_fields(r)
r = vlab.register('GTMDPLL1', width=32, block=intTargetSocket, offset=0x00001B04, reset=0x00000000, doc='DPLL Service Request 1')
src_fields(r)
r = vlab.register('GTMDPLL2', width=32, block=intTargetSocket, offset=0x00001B08, reset=0x00000000, doc='DPLL Service Request 2')
src_fields(r)
r = vlab.register('GTMDPLL3', width=32, block=intTargetSocket, offset=0x00001B0C, reset=0x00000000, doc='DPLL Service Request 3')
src_fields(r)
r = vlab.register('GTMDPLL4', width=32, block=intTargetSocket, offset=0x00001B10, reset=0x00000000, doc='DPLL Service Request 4')
src_fields(r)
r = vlab.register('GTMDPLL5', width=32, block=intTargetSocket, offset=0x00001B14, reset=0x00000000, doc='DPLL Service Request 5')
src_fields(r)
r = vlab.register('GTMDPLL6', width=32, block=intTargetSocket, offset=0x00001B18, reset=0x00000000, doc='DPLL Service Request 6')
src_fields(r)
r = vlab.register('GTMDPLL7', width=32, block=intTargetSocket, offset=0x00001B1C, reset=0x00000000, doc='DPLL Service Request 7')
src_fields(r)
r = vlab.register('GTMDPLL8', width=32, block=intTargetSocket, offset=0x00001B20, reset=0x00000000, doc='DPLL Service Request 8')
src_fields(r)
r = vlab.register('GTMDPLL9', width=32, block=intTargetSocket, offset=0x00001B24, reset=0x00000000, doc='DPLL Service Request 9')
src_fields(r)
r = vlab.register('GTMDPLL10', width=32, block=intTargetSocket, offset=0x00001B28, reset=0x00000000, doc='DPLL Service Request 10')
src_fields(r)
r = vlab.register('GTMDPLL11', width=32, block=intTargetSocket, offset=0x00001B2C, reset=0x00000000, doc='DPLL Service Request 11')
src_fields(r)
r = vlab.register('GTMDPLL12', width=32, block=intTargetSocket, offset=0x00001B30, reset=0x00000000, doc='DPLL Service Request 12')
src_fields(r)
r = vlab.register('GTMDPLL13', width=32, block=intTargetSocket, offset=0x00001B34, reset=0x00000000, doc='DPLL Service Request 13')
src_fields(r)
r = vlab.register('GTMDPLL14', width=32, block=intTargetSocket, offset=0x00001B38, reset=0x00000000, doc='DPLL Service Request 14')
src_fields(r)
r = vlab.register('GTMDPLL15', width=32, block=intTargetSocket, offset=0x00001B3C, reset=0x00000000, doc='DPLL Service Request 15')
src_fields(r)
r = vlab.register('GTMDPLL16', width=32, block=intTargetSocket, offset=0x00001B40, reset=0x00000000, doc='DPLL Service Request 16')
src_fields(r)
r = vlab.register('GTMDPLL17', width=32, block=intTargetSocket, offset=0x00001B44, reset=0x00000000, doc='DPLL Service Request 17')
src_fields(r)
r = vlab.register('GTMDPLL18', width=32, block=intTargetSocket, offset=0x00001B48, reset=0x00000000, doc='DPLL Service Request 18')
src_fields(r)
r = vlab.register('GTMDPLL19', width=32, block=intTargetSocket, offset=0x00001B4C, reset=0x00000000, doc='DPLL Service Request 19')
src_fields(r)
r = vlab.register('GTMDPLL20', width=32, block=intTargetSocket, offset=0x00001B50, reset=0x00000000, doc='DPLL Service Request 20')
src_fields(r)
r = vlab.register('GTMDPLL21', width=32, block=intTargetSocket, offset=0x00001B54, reset=0x00000000, doc='DPLL Service Request 21')
src_fields(r)
r = vlab.register('GTMDPLL22', width=32, block=intTargetSocket, offset=0x00001B58, reset=0x00000000, doc='DPLL Service Request 22')
src_fields(r)
r = vlab.register('GTMDPLL23', width=32, block=intTargetSocket, offset=0x00001B5C, reset=0x00000000, doc='DPLL Service Request 23')
src_fields(r)
r = vlab.register('GTMDPLL24', width=32, block=intTargetSocket, offset=0x00001B60, reset=0x00000000, doc='DPLL Service Request 24')
src_fields(r)
r = vlab.register('GTMDPLL25', width=32, block=intTargetSocket, offset=0x00001B64, reset=0x00000000, doc='DPLL Service Request 25')
src_fields(r)
r = vlab.register('GTMDPLL26', width=32, block=intTargetSocket, offset=0x00001B68, reset=0x00000000, doc='DPLL Service Request 26')
src_fields(r)
r = vlab.register('GTMERR', width=32, block=intTargetSocket, offset=0x00001B70, reset=0x00000000, doc='Error Service Request')
src_fields(r)
r = vlab.register('GTMTIM00', width=32, block=intTargetSocket, offset=0x00001B90, reset=0x00000000, doc='TIM0 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM01', width=32, block=intTargetSocket, offset=0x00001B94, reset=0x00000000, doc='TIM0 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM02', width=32, block=intTargetSocket, offset=0x00001B98, reset=0x00000000, doc='TIM0 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM03', width=32, block=intTargetSocket, offset=0x00001B9C, reset=0x00000000, doc='TIM0 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM04', width=32, block=intTargetSocket, offset=0x00001BA0, reset=0x00000000, doc='TIM0 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM05', width=32, block=intTargetSocket, offset=0x00001BA4, reset=0x00000000, doc='TIM0 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM06', width=32, block=intTargetSocket, offset=0x00001BA8, reset=0x00000000, doc='TIM0 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM07', width=32, block=intTargetSocket, offset=0x00001BAC, reset=0x00000000, doc='TIM0 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTIM10', width=32, block=intTargetSocket, offset=0x00001BB0, reset=0x00000000, doc='TIM1 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM11', width=32, block=intTargetSocket, offset=0x00001BB4, reset=0x00000000, doc='TIM1 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM12', width=32, block=intTargetSocket, offset=0x00001BB8, reset=0x00000000, doc='TIM1 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM13', width=32, block=intTargetSocket, offset=0x00001BBC, reset=0x00000000, doc='TIM1 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM14', width=32, block=intTargetSocket, offset=0x00001BC0, reset=0x00000000, doc='TIM1 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM15', width=32, block=intTargetSocket, offset=0x00001BC4, reset=0x00000000, doc='TIM1 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM16', width=32, block=intTargetSocket, offset=0x00001BC8, reset=0x00000000, doc='TIM1 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM17', width=32, block=intTargetSocket, offset=0x00001BCC, reset=0x00000000, doc='TIM1 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTIM20', width=32, block=intTargetSocket, offset=0x00001BD0, reset=0x00000000, doc='TIM2 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM21', width=32, block=intTargetSocket, offset=0x00001BD4, reset=0x00000000, doc='TIM2 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM22', width=32, block=intTargetSocket, offset=0x00001BD8, reset=0x00000000, doc='TIM2 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM23', width=32, block=intTargetSocket, offset=0x00001BDC, reset=0x00000000, doc='TIM2 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM24', width=32, block=intTargetSocket, offset=0x00001BE0, reset=0x00000000, doc='TIM2 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM25', width=32, block=intTargetSocket, offset=0x00001BE4, reset=0x00000000, doc='TIM2 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM26', width=32, block=intTargetSocket, offset=0x00001BE8, reset=0x00000000, doc='TIM2 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM27', width=32, block=intTargetSocket, offset=0x00001BEC, reset=0x00000000, doc='TIM2 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTIM30', width=32, block=intTargetSocket, offset=0x00001BF0, reset=0x00000000, doc='TIM3 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM31', width=32, block=intTargetSocket, offset=0x00001BF4, reset=0x00000000, doc='TIM3 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM32', width=32, block=intTargetSocket, offset=0x00001BF8, reset=0x00000000, doc='TIM3 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM33', width=32, block=intTargetSocket, offset=0x00001BFC, reset=0x00000000, doc='TIM3 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM34', width=32, block=intTargetSocket, offset=0x00001C00, reset=0x00000000, doc='TIM3 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM35', width=32, block=intTargetSocket, offset=0x00001C04, reset=0x00000000, doc='TIM3 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM36', width=32, block=intTargetSocket, offset=0x00001C08, reset=0x00000000, doc='TIM3 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM37', width=32, block=intTargetSocket, offset=0x00001C0C, reset=0x00000000, doc='TIM3 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTIM40', width=32, block=intTargetSocket, offset=0x00001C10, reset=0x00000000, doc='TIM4 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM41', width=32, block=intTargetSocket, offset=0x00001C14, reset=0x00000000, doc='TIM4 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM42', width=32, block=intTargetSocket, offset=0x00001C18, reset=0x00000000, doc='TIM4 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM43', width=32, block=intTargetSocket, offset=0x00001C1C, reset=0x00000000, doc='TIM4 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM44', width=32, block=intTargetSocket, offset=0x00001C20, reset=0x00000000, doc='TIM4 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM45', width=32, block=intTargetSocket, offset=0x00001C24, reset=0x00000000, doc='TIM4 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM46', width=32, block=intTargetSocket, offset=0x00001C28, reset=0x00000000, doc='TIM4 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM47', width=32, block=intTargetSocket, offset=0x00001C2C, reset=0x00000000, doc='TIM4 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTIM50', width=32, block=intTargetSocket, offset=0x00001C30, reset=0x00000000, doc='TIM5 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTIM51', width=32, block=intTargetSocket, offset=0x00001C34, reset=0x00000000, doc='TIM5 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTIM52', width=32, block=intTargetSocket, offset=0x00001C38, reset=0x00000000, doc='TIM5 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTIM53', width=32, block=intTargetSocket, offset=0x00001C3C, reset=0x00000000, doc='TIM5 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTIM54', width=32, block=intTargetSocket, offset=0x00001C40, reset=0x00000000, doc='TIM5 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTIM55', width=32, block=intTargetSocket, offset=0x00001C44, reset=0x00000000, doc='TIM5 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTIM56', width=32, block=intTargetSocket, offset=0x00001C48, reset=0x00000000, doc='TIM5 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTIM57', width=32, block=intTargetSocket, offset=0x00001C4C, reset=0x00000000, doc='TIM5 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMMCS00', width=32, block=intTargetSocket, offset=0x00001CB0, reset=0x00000000, doc='MCS0 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMMCS01', width=32, block=intTargetSocket, offset=0x00001CB4, reset=0x00000000, doc='MCS0 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMMCS02', width=32, block=intTargetSocket, offset=0x00001CB8, reset=0x00000000, doc='MCS0 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMMCS03', width=32, block=intTargetSocket, offset=0x00001CBC, reset=0x00000000, doc='MCS0 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCS04', width=32, block=intTargetSocket, offset=0x00001CC0, reset=0x00000000, doc='MCS0 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMMCS05', width=32, block=intTargetSocket, offset=0x00001CC4, reset=0x00000000, doc='MCS0 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMMCS06', width=32, block=intTargetSocket, offset=0x00001CC8, reset=0x00000000, doc='MCS0 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMMCS07', width=32, block=intTargetSocket, offset=0x00001CCC, reset=0x00000000, doc='MCS0 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMMCS10', width=32, block=intTargetSocket, offset=0x00001CD0, reset=0x00000000, doc='MCS1 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMMCS11', width=32, block=intTargetSocket, offset=0x00001CD4, reset=0x00000000, doc='MCS1 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMMCS12', width=32, block=intTargetSocket, offset=0x00001CD8, reset=0x00000000, doc='MCS1 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMMCS13', width=32, block=intTargetSocket, offset=0x00001CDC, reset=0x00000000, doc='MCS1 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCS14', width=32, block=intTargetSocket, offset=0x00001CE0, reset=0x00000000, doc='MCS1 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMMCS15', width=32, block=intTargetSocket, offset=0x00001CE4, reset=0x00000000, doc='MCS1 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMMCS16', width=32, block=intTargetSocket, offset=0x00001CE8, reset=0x00000000, doc='MCS1 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMMCS17', width=32, block=intTargetSocket, offset=0x00001CEC, reset=0x00000000, doc='MCS1 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMMCS20', width=32, block=intTargetSocket, offset=0x00001CF0, reset=0x00000000, doc='MCS2 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMMCS21', width=32, block=intTargetSocket, offset=0x00001CF4, reset=0x00000000, doc='MCS2 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMMCS22', width=32, block=intTargetSocket, offset=0x00001CF8, reset=0x00000000, doc='MCS2 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMMCS23', width=32, block=intTargetSocket, offset=0x00001CFC, reset=0x00000000, doc='MCS2 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCS24', width=32, block=intTargetSocket, offset=0x00001D00, reset=0x00000000, doc='MCS2 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMMCS25', width=32, block=intTargetSocket, offset=0x00001D04, reset=0x00000000, doc='MCS2 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMMCS26', width=32, block=intTargetSocket, offset=0x00001D08, reset=0x00000000, doc='MCS2 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMMCS27', width=32, block=intTargetSocket, offset=0x00001D0C, reset=0x00000000, doc='MCS2 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMMCS30', width=32, block=intTargetSocket, offset=0x00001D10, reset=0x00000000, doc='MCS3 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMMCS31', width=32, block=intTargetSocket, offset=0x00001D14, reset=0x00000000, doc='MCS3 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMMCS32', width=32, block=intTargetSocket, offset=0x00001D18, reset=0x00000000, doc='MCS3 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMMCS33', width=32, block=intTargetSocket, offset=0x00001D1C, reset=0x00000000, doc='MCS3 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCS34', width=32, block=intTargetSocket, offset=0x00001D20, reset=0x00000000, doc='MCS3 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMMCS35', width=32, block=intTargetSocket, offset=0x00001D24, reset=0x00000000, doc='MCS3 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMMCS36', width=32, block=intTargetSocket, offset=0x00001D28, reset=0x00000000, doc='MCS3 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMMCS37', width=32, block=intTargetSocket, offset=0x00001D2C, reset=0x00000000, doc='MCS3 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMMCS40', width=32, block=intTargetSocket, offset=0x00001D30, reset=0x00000000, doc='MCS4 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMMCS41', width=32, block=intTargetSocket, offset=0x00001D34, reset=0x00000000, doc='MCS4 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMMCS42', width=32, block=intTargetSocket, offset=0x00001D38, reset=0x00000000, doc='MCS4 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMMCS43', width=32, block=intTargetSocket, offset=0x00001D3C, reset=0x00000000, doc='MCS4 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCS44', width=32, block=intTargetSocket, offset=0x00001D40, reset=0x00000000, doc='MCS4 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMMCS45', width=32, block=intTargetSocket, offset=0x00001D44, reset=0x00000000, doc='MCS4 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMMCS46', width=32, block=intTargetSocket, offset=0x00001D48, reset=0x00000000, doc='MCS4 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMMCS47', width=32, block=intTargetSocket, offset=0x00001D4C, reset=0x00000000, doc='MCS4 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTOM00', width=32, block=intTargetSocket, offset=0x00001E10, reset=0x00000000, doc='TOM0 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTOM01', width=32, block=intTargetSocket, offset=0x00001E14, reset=0x00000000, doc='TOM0 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTOM02', width=32, block=intTargetSocket, offset=0x00001E18, reset=0x00000000, doc='TOM0 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTOM03', width=32, block=intTargetSocket, offset=0x00001E1C, reset=0x00000000, doc='TOM0 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTOM04', width=32, block=intTargetSocket, offset=0x00001E20, reset=0x00000000, doc='TOM0 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTOM05', width=32, block=intTargetSocket, offset=0x00001E24, reset=0x00000000, doc='TOM0 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTOM06', width=32, block=intTargetSocket, offset=0x00001E28, reset=0x00000000, doc='TOM0 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTOM07', width=32, block=intTargetSocket, offset=0x00001E2C, reset=0x00000000, doc='TOM0 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTOM10', width=32, block=intTargetSocket, offset=0x00001E30, reset=0x00000000, doc='TOM1 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTOM11', width=32, block=intTargetSocket, offset=0x00001E34, reset=0x00000000, doc='TOM1 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTOM12', width=32, block=intTargetSocket, offset=0x00001E38, reset=0x00000000, doc='TOM1 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTOM13', width=32, block=intTargetSocket, offset=0x00001E3C, reset=0x00000000, doc='TOM1 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTOM14', width=32, block=intTargetSocket, offset=0x00001E40, reset=0x00000000, doc='TOM1 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTOM15', width=32, block=intTargetSocket, offset=0x00001E44, reset=0x00000000, doc='TOM1 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTOM16', width=32, block=intTargetSocket, offset=0x00001E48, reset=0x00000000, doc='TOM1 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTOM17', width=32, block=intTargetSocket, offset=0x00001E4C, reset=0x00000000, doc='TOM1 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMTOM20', width=32, block=intTargetSocket, offset=0x00001E50, reset=0x00000000, doc='TOM2 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMTOM21', width=32, block=intTargetSocket, offset=0x00001E54, reset=0x00000000, doc='TOM2 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMTOM22', width=32, block=intTargetSocket, offset=0x00001E58, reset=0x00000000, doc='TOM2 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMTOM23', width=32, block=intTargetSocket, offset=0x00001E5C, reset=0x00000000, doc='TOM2 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMTOM24', width=32, block=intTargetSocket, offset=0x00001E60, reset=0x00000000, doc='TOM2 Shared Service Request 4')
src_fields(r)
r = vlab.register('GTMTOM25', width=32, block=intTargetSocket, offset=0x00001E64, reset=0x00000000, doc='TOM2 Shared Service Request 5')
src_fields(r)
r = vlab.register('GTMTOM26', width=32, block=intTargetSocket, offset=0x00001E68, reset=0x00000000, doc='TOM2 Shared Service Request 6')
src_fields(r)
r = vlab.register('GTMTOM27', width=32, block=intTargetSocket, offset=0x00001E6C, reset=0x00000000, doc='TOM2 Shared Service Request 7')
src_fields(r)
r = vlab.register('GTMATOM00', width=32, block=intTargetSocket, offset=0x00001EF0, reset=0x00000000, doc='ATOM0 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM01', width=32, block=intTargetSocket, offset=0x00001EF4, reset=0x00000000, doc='ATOM0 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM02', width=32, block=intTargetSocket, offset=0x00001EF8, reset=0x00000000, doc='ATOM0 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM03', width=32, block=intTargetSocket, offset=0x00001EFC, reset=0x00000000, doc='ATOM0 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMATOM10', width=32, block=intTargetSocket, offset=0x00001F00, reset=0x00000000, doc='ATOM1 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM11', width=32, block=intTargetSocket, offset=0x00001F04, reset=0x00000000, doc='ATOM1 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM12', width=32, block=intTargetSocket, offset=0x00001F08, reset=0x00000000, doc='ATOM1 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM13', width=32, block=intTargetSocket, offset=0x00001F0C, reset=0x00000000, doc='ATOM1 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMATOM20', width=32, block=intTargetSocket, offset=0x00001F10, reset=0x00000000, doc='ATOM2 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM21', width=32, block=intTargetSocket, offset=0x00001F14, reset=0x00000000, doc='ATOM2 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM22', width=32, block=intTargetSocket, offset=0x00001F18, reset=0x00000000, doc='ATOM2 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM23', width=32, block=intTargetSocket, offset=0x00001F1C, reset=0x00000000, doc='ATOM2 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMATOM30', width=32, block=intTargetSocket, offset=0x00001F20, reset=0x00000000, doc='ATOM3 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM31', width=32, block=intTargetSocket, offset=0x00001F24, reset=0x00000000, doc='ATOM3 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM32', width=32, block=intTargetSocket, offset=0x00001F28, reset=0x00000000, doc='ATOM3 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM33', width=32, block=intTargetSocket, offset=0x00001F2C, reset=0x00000000, doc='ATOM3 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMATOM40', width=32, block=intTargetSocket, offset=0x00001F30, reset=0x00000000, doc='ATOM4 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM41', width=32, block=intTargetSocket, offset=0x00001F34, reset=0x00000000, doc='ATOM4 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM42', width=32, block=intTargetSocket, offset=0x00001F38, reset=0x00000000, doc='ATOM4 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM43', width=32, block=intTargetSocket, offset=0x00001F3C, reset=0x00000000, doc='ATOM4 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMATOM50', width=32, block=intTargetSocket, offset=0x00001F40, reset=0x00000000, doc='ATOM5 Shared Service Request 0')
src_fields(r)
r = vlab.register('GTMATOM51', width=32, block=intTargetSocket, offset=0x00001F44, reset=0x00000000, doc='ATOM5 Shared Service Request 1')
src_fields(r)
r = vlab.register('GTMATOM52', width=32, block=intTargetSocket, offset=0x00001F48, reset=0x00000000, doc='ATOM5 Shared Service Request 2')
src_fields(r)
r = vlab.register('GTMATOM53', width=32, block=intTargetSocket, offset=0x00001F4C, reset=0x00000000, doc='ATOM5 Shared Service Request 3')
src_fields(r)
r = vlab.register('GTMMCSW0', width=32, block=intTargetSocket, offset=0x00001FD0, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 0')
src_fields(r)
r = vlab.register('GTMMCSW1', width=32, block=intTargetSocket, offset=0x00001FD4, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 1')
src_fields(r)
r = vlab.register('GTMMCSW2', width=32, block=intTargetSocket, offset=0x00001FD8, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 2')
src_fields(r)
r = vlab.register('GTMMCSW3', width=32, block=intTargetSocket, offset=0x00001FDC, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 3')
src_fields(r)
r = vlab.register('GTMMCSW4', width=32, block=intTargetSocket, offset=0x00001FE0, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 4')
src_fields(r)
r = vlab.register('GTMMCSW5', width=32, block=intTargetSocket, offset=0x00001FE4, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 5')
src_fields(r)
r = vlab.register('GTMMCSW6', width=32, block=intTargetSocket, offset=0x00001FE8, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 6')
src_fields(r)
r = vlab.register('GTMMCSW7', width=32, block=intTargetSocket, offset=0x00001FEC, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 7')
src_fields(r)
r = vlab.register('GTMMCSW8', width=32, block=intTargetSocket, offset=0x00001FF0, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 8')
src_fields(r)
r = vlab.register('GTMMCSW9', width=32, block=intTargetSocket, offset=0x00001FF4, reset=0x00000000, doc='GTM Multi Channel Sequencer Service Request 9')
src_fields(r)
