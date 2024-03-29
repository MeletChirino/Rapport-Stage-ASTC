#------------------------------------------------------------------------------
# Copyright (C) Australian Semiconductor Technology Company. 2015.
# All Rights Reserved.
#
# This is unpublished proprietary source code of the Australian Semiconductor
# Technology Company (ASTC). The copyright notice does not evidence any
# actual or intended publication of such source code.
#------------------------------------------------------------------------------

import vlab
vlab.properties(name="IfxEmem", kind="leaf")
ememTargetSocket = vlab.bus("ememTargetSocket", kind="target", width=32)
vlab.register('CLC', width=32, block=ememTargetSocket, offset=0x0000)
vlab.field(name="DISR", register="CLC", offset = 0, width = 1 ,access = "read-write")
vlab.field(name="DISS", register="CLC", offset = 1, width = 1 ,access = "read-only")
vlab.register('ID', width=32, block=ememTargetSocket, offset=0x0008)
vlab.field(name="MOD_REV", register="ID", offset = 0, width = 8 ,access = "read-only")
vlab.field(name="MOD_TYPE", register="ID", offset = 8, width = 8 ,access = "read-only")
vlab.field(name="MOD_NUM", register="ID", offset = 16, width = 16 ,access = "read-only")
vlab.register('TILECONFIG', width=32, block=ememTargetSocket, offset=0x0020)
vlab.field(name="TCM0", register="TILECONFIG", offset = 0, width = 2 ,access = "write-only")
vlab.field(name="TCM1", register="TILECONFIG", offset = 2, width = 2 ,access = "write-only")
vlab.field(name="TCM2", register="TILECONFIG", offset = 4, width = 2 ,access = "write-only")
vlab.field(name="TCM3", register="TILECONFIG", offset = 6, width = 2 ,access = "write-only")
vlab.field(name="TCM4", register="TILECONFIG", offset = 8, width = 2 ,access = "write-only")
vlab.field(name="TCM5", register="TILECONFIG", offset = 10, width = 2 ,access = "write-only")
vlab.field(name="TCM6", register="TILECONFIG", offset = 12, width = 2 ,access = "write-only")
vlab.field(name="TCM7", register="TILECONFIG", offset = 14, width = 2 ,access = "write-only")
vlab.field(name="XCM0", register="TILECONFIG", offset = 16, width = 2 ,access = "write-only")
vlab.field(name="XCM1", register="TILECONFIG", offset = 18, width = 2 ,access = "write-only")
vlab.field(name="XCM2", register="TILECONFIG", offset = 20, width = 2 ,access = "write-only")
vlab.field(name="XCM3", register="TILECONFIG", offset = 22, width = 2 ,access = "write-only")
vlab.field(name="XCM4", register="TILECONFIG", offset = 24, width = 2 ,access = "write-only")
vlab.field(name="XCM5", register="TILECONFIG", offset = 26, width = 2 ,access = "write-only")
vlab.field(name="XCM6", register="TILECONFIG", offset = 28, width = 2 ,access = "write-only")
vlab.field(name="XCM7", register="TILECONFIG", offset = 30, width = 2 ,access = "write-only")
vlab.register('TILECC', width=32, block=ememTargetSocket, offset=0x0024)
vlab.field(name="TCM0", register="TILECC", offset = 0, width = 1 ,access = "read-write")
vlab.field(name="TCM1", register="TILECC", offset = 1, width = 1 ,access = "read-write")
vlab.field(name="TCM2", register="TILECC", offset = 2, width = 1 ,access = "read-write")
vlab.field(name="TCM3", register="TILECC", offset = 3, width = 1 ,access = "read-write")
vlab.field(name="TCM4", register="TILECC", offset = 4, width = 1 ,access = "read-write")
vlab.field(name="TCM5", register="TILECC", offset = 5, width = 1 ,access = "read-write")
vlab.field(name="TCM6", register="TILECC", offset = 6, width = 1 ,access = "read-write")
vlab.field(name="TCM7", register="TILECC", offset = 7, width = 1 ,access = "read-write")
vlab.field(name="XCM0", register="TILECC", offset = 8, width = 1 ,access = "read-write")
vlab.field(name="XCM1", register="TILECC", offset = 9, width = 1 ,access = "read-write")
vlab.field(name="XCM2", register="TILECC", offset = 10, width = 1 ,access = "read-write")
vlab.field(name="XCM3", register="TILECC", offset = 11, width = 1 ,access = "read-write")
vlab.field(name="XCM4", register="TILECC", offset = 12, width = 1 ,access = "read-write")
vlab.field(name="XCM5", register="TILECC", offset = 13, width = 1 ,access = "read-write")
vlab.field(name="XCM6", register="TILECC", offset = 14, width = 1 ,access = "read-write")
vlab.field(name="XCM7", register="TILECC", offset = 15, width = 1 ,access = "read-write")
vlab.field(name="XCM8", register="TILECC", offset = 16, width = 1 ,access = "read-write")
vlab.field(name="XCM9", register="TILECC", offset = 17, width = 1 ,access = "read-write")
vlab.field(name="XCM10", register="TILECC", offset = 18, width = 1 ,access = "read-write")
vlab.field(name="XCM11", register="TILECC", offset = 19, width = 1 ,access = "read-write")
vlab.field(name="XCM12", register="TILECC", offset = 20, width = 1 ,access = "read-write")
vlab.field(name="XCM13", register="TILECC", offset = 21, width = 1 ,access = "read-write")
vlab.field(name="XCM14", register="TILECC", offset = 22, width = 1 ,access = "read-write")
vlab.field(name="XCM15", register="TILECC", offset = 23, width = 1 ,access = "read-write")
vlab.register('TILECT', width=32, block=ememTargetSocket, offset=0x0028)
vlab.field(name="TCM0", register="TILECT", offset = 0, width = 1 ,access = "read-write")
vlab.field(name="TCM1", register="TILECT", offset = 1, width = 1 ,access = "read-write")
vlab.field(name="TCM2", register="TILECT", offset = 2, width = 1 ,access = "read-write")
vlab.field(name="TCM3", register="TILECT", offset = 3, width = 1 ,access = "read-write")
vlab.field(name="TCM4", register="TILECT", offset = 4, width = 1 ,access = "read-write")
vlab.field(name="TCM5", register="TILECT", offset = 5, width = 1 ,access = "read-write")
vlab.field(name="TCM6", register="TILECT", offset = 6, width = 1 ,access = "read-write")
vlab.field(name="TCM7", register="TILECT", offset = 7, width = 1 ,access = "read-write")
vlab.field(name="XTM0", register="TILECT", offset = 16, width = 1 ,access = "read-write")
vlab.field(name="XTM1", register="TILECT", offset = 17, width = 1 ,access = "read-write")
vlab.register('TILESTATE', width=32, block=ememTargetSocket, offset=0x002c)
vlab.field(name="TCM0", register="TILESTATE", offset = 0, width = 2 ,access = "read-only")
vlab.field(name="TCM1", register="TILESTATE", offset = 2, width = 2 ,access = "read-only")
vlab.field(name="TCM2", register="TILESTATE", offset = 4, width = 2 ,access = "read-only")
vlab.field(name="TCM3", register="TILESTATE", offset = 6, width = 2 ,access = "read-only")
vlab.field(name="TCM4", register="TILESTATE", offset = 8, width = 2 ,access = "read-only")
vlab.field(name="TCM5", register="TILESTATE", offset = 10, width = 2 ,access = "read-only")
vlab.field(name="TCM6", register="TILESTATE", offset = 12, width = 2 ,access = "read-only")
vlab.field(name="TCM7", register="TILESTATE", offset = 14, width = 2 ,access = "read-only")
vlab.field(name="XCM0", register="TILESTATE", offset = 16, width = 2 ,access = "read-only")
vlab.field(name="XCM1", register="TILESTATE", offset = 18, width = 2 ,access = "read-only")
vlab.field(name="XCM2", register="TILESTATE", offset = 20, width = 2 ,access = "read-only")
vlab.field(name="XCM3", register="TILESTATE", offset = 22, width = 2 ,access = "read-only")
vlab.field(name="XCM4", register="TILESTATE", offset = 24, width = 2 ,access = "read-only")
vlab.field(name="XCM5", register="TILESTATE", offset = 26, width = 2 ,access = "read-only")
vlab.field(name="XCM6", register="TILESTATE", offset = 28, width = 2 ,access = "read-only")
vlab.field(name="XCM7", register="TILESTATE", offset = 30, width = 2 ,access = "read-only")
vlab.register('SBRCTR', width=32, block=ememTargetSocket, offset=0x0034)
vlab.field(name="STBLOCK", register="SBRCTR", offset = 0, width = 1 ,access = "read-only")
vlab.field(name="STBULK", register="SBRCTR", offset = 1, width = 3 ,access = "write-only")
vlab.field(name="STBSLK", register="SBRCTR", offset = 4, width = 4 ,access = "write-only")
vlab.field(name="STBPON", register="SBRCTR", offset = 16, width = 1 ,access = "read-only")
vlab.register('ACCEN1', width=32, block=ememTargetSocket, offset=0x00f8)
vlab.register('ACCEN0', width=32, block=ememTargetSocket, offset=0x00fc)
vlab.field(name="EN0", register="ACCEN0", offset = 0, width = 1 ,access = "read-write")
vlab.field(name="EN1", register="ACCEN0", offset = 1, width = 1 ,access = "read-write")
vlab.field(name="EN2", register="ACCEN0", offset = 2, width = 1 ,access = "read-write")
vlab.field(name="EN3", register="ACCEN0", offset = 3, width = 1 ,access = "read-write")
vlab.field(name="EN4", register="ACCEN0", offset = 4, width = 1 ,access = "read-write")
vlab.field(name="EN5", register="ACCEN0", offset = 5, width = 1 ,access = "read-write")
vlab.field(name="EN6", register="ACCEN0", offset = 6, width = 1 ,access = "read-write")
vlab.field(name="EN7", register="ACCEN0", offset = 7, width = 1 ,access = "read-write")
vlab.field(name="EN8", register="ACCEN0", offset = 8, width = 1 ,access = "read-write")
vlab.field(name="EN9", register="ACCEN0", offset = 9, width = 1 ,access = "read-write")
vlab.field(name="EN10", register="ACCEN0", offset = 10, width = 1 ,access = "read-write")
vlab.field(name="EN11", register="ACCEN0", offset = 11, width = 1 ,access = "read-write")
vlab.field(name="EN12", register="ACCEN0", offset = 12, width = 1 ,access = "read-write")
vlab.field(name="EN13", register="ACCEN0", offset = 13, width = 1 ,access = "read-write")
vlab.field(name="EN14", register="ACCEN0", offset = 14, width = 1 ,access = "read-write")
vlab.field(name="EN15", register="ACCEN0", offset = 15, width = 1 ,access = "read-write")
vlab.field(name="EN16", register="ACCEN0", offset = 16, width = 1 ,access = "read-write")
vlab.field(name="EN17", register="ACCEN0", offset = 17, width = 1 ,access = "read-write")
vlab.field(name="EN18", register="ACCEN0", offset = 18, width = 1 ,access = "read-write")
vlab.field(name="EN19", register="ACCEN0", offset = 19, width = 1 ,access = "read-write")
vlab.field(name="EN20", register="ACCEN0", offset = 20, width = 1 ,access = "read-write")
vlab.field(name="EN21", register="ACCEN0", offset = 21, width = 1 ,access = "read-write")
vlab.field(name="EN22", register="ACCEN0", offset = 22, width = 1 ,access = "read-write")
vlab.field(name="EN23", register="ACCEN0", offset = 23, width = 1 ,access = "read-write")
vlab.field(name="EN24", register="ACCEN0", offset = 24, width = 1 ,access = "read-write")
vlab.field(name="EN25", register="ACCEN0", offset = 25, width = 1 ,access = "read-write")
vlab.field(name="EN26", register="ACCEN0", offset = 26, width = 1 ,access = "read-write")
vlab.field(name="EN27", register="ACCEN0", offset = 27, width = 1 ,access = "read-write")
vlab.field(name="EN28", register="ACCEN0", offset = 28, width = 1 ,access = "read-write")
vlab.field(name="EN29", register="ACCEN0", offset = 29, width = 1 ,access = "read-write")
vlab.field(name="EN30", register="ACCEN0", offset = 30, width = 1 ,access = "read-write")
vlab.field(name="EN31", register="ACCEN0", offset = 31, width = 1 ,access = "read-write")
