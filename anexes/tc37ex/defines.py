# Copyright (C) Australian Semiconductor Technology Company (ASTC). 2011-2012.
# All Rights Reserved.
#
# This is unpublished proprietary source code of the Australian Semiconductor
# Technology Company (ASTC).  The copyright notice does not evidence any actual
# or intended publication of such source code.
# -----------------------------------------------------------------------------
# Information taken from 
# https://www.infineon.com/dgdl/Infineon-AURIX_TC37xEXT-UserManual-v02_00-EN.pdf?fileId=5546d4627506bb32017527203f913b3d

# oscillator clock (period in NS)
XTAL_CLOCK_FREQUENCY = 50

# Memory types
MEMTYPE_CPU0LOCAL    = 0 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPU1LOCAL    = 1 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPU2LOCAL    = 2 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPU3LOCAL    = 3 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPU4LOCAL    = 4 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPU5LOCAL    = 5 #CPULOCAL means that the memory is managed internally to the CPU model
MEMTYPE_CPUDUPLICATE = 6 #CPUDUPLICATE means that the memory is duplicated on all the CPU models
MEMTYPE_RAM          = 7
MEMTYPE_REGISTER     = 8
MEMTYPE_FLASH = 9
OTHER= 10

MEMORY_SIZE_256MB= 0x10000000
MEMORY_SIZE_192MB= 0x0D000000
MEMORY_SIZE_128MB= 0x08000000
MEMORY_SIZE_112MB= 0x07000000
MEMORY_SIZE_96MB = 0x06000000
MEMORY_SIZE_64MB = 0x04000000
MEMORY_SIZE_16MB = 0x1000000
MEMORY_SIZE_12MB = 0x0C00000
MEMORY_SIZE_10MB = 0x0A00000
MEMORY_SIZE_3MB = 0x0300000
MEMORY_SIZE_2MB = 0x0200000
MEMORY_SIZE_1MB = 0x0100000
MEMORY_SIZE_640KB = 0x100000
MEMORY_SIZE_512KB = 0x80000
MEMORY_SIZE_256KB = 0x40000
MEMORY_SIZE_240KB = 0x3C000
MEMORY_SIZE_128KB = 0x20000
MEMORY_SIZE_96KB = 0x18000
MEMORY_SIZE_64KB = 0x10000
MEMORY_SIZE_32KB = 0x8000
MEMORY_SIZE_24KB = 0x6000
MEMORY_SIZE_16KB  = 0x4000
MEMORY_SIZE_12KB  = 0x3000
MEMORY_SIZE_8KB  = 0x2000
MEMORY_SIZE_5KB  = 0x1400
MEMORY_SIZE_4KB  = 0x1000
MEMORY_SIZE_2KB  = 0x800
MEMORY_SIZE_1KB  = 0x400
MEMORY_SIZE_512B  = 0x200
MEMORY_SIZE_256B  = 0x100

CORE_LOCAL_MEMORY_MAP = {
    # local CPU memories connected to core router
    'PSPR'                  : (0xC0000000, MEMORY_SIZE_64KB, MEMTYPE_RAM),
    'DSPR0'                 : (0xD0000000, MEMORY_SIZE_240KB, MEMTYPE_RAM),
    'DSPR1'                 : (0xD0000000, MEMORY_SIZE_240KB, MEMTYPE_RAM),
    'DSPR2'                 : (0xD0000000, MEMORY_SIZE_96KB, MEMTYPE_RAM),
    'PCACHE'                : (0xC0010000, MEMORY_SIZE_32KB, MEMTYPE_RAM),
    'DCACHE'                : (0xD0018000, MEMORY_SIZE_16KB, MEMTYPE_RAM),

    # PFLASH : Program Flash (Non Volatile Memory)
    #          Compared to AURIX, the PFlash memory is distributed between the processors to provide high performance access to a local
    #          PFlash bank. (LPB)
    'PFLASH0'               : (0xA0000000, MEMORY_SIZE_3MB, MEMTYPE_FLASH),
    'PFLASH1'               : (0xA0300000, MEMORY_SIZE_3MB, MEMTYPE_FLASH),
    'PFLASH0_CACHED'        : (0x80000000, MEMORY_SIZE_3MB, MEMTYPE_FLASH),
    'PFLASH1_CACHED'        : (0x80300000, MEMORY_SIZE_3MB, MEMTYPE_FLASH),
    
    # DLMU : Direct-connected Local Memory Unit or Distributed Local Memory Unit
    #        The DLMU is a contiguous portion of the global LMU SRAM. The DLMU provides fast, deterministic data access
    #        to a segment of the global LMU, ideally for use by the local CPU for global data.
    'DLMU0'        : (0xB0000000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),
    'DLMU1'        : (0xB0010000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),
    'DLMU2'        : (0xB0020000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),
    'DLMU0_CACHED' : (0x90000000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),
    'DLMU1_CACHED' : (0x90010000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),
    'DLMU2_CACHED' : (0x90020000, MEMORY_SIZE_64KB,  MEMTYPE_RAM),


    'SPB'               : (0xF0000000, 0x07FFFFFF, OTHER),
    'SRI_SEG1_7_CPU2'   : (0x50000000, 0x0FFFFFFF, MEMTYPE_CPU2LOCAL),
    'SRI_SEG1_7_CPU1'   : (0x60000000, 0x0FFFFFFF, MEMTYPE_CPU1LOCAL),
    'SRI_SEG1_7_CPU0'   : (0x70000000, 0x0FFFFFFF, MEMTYPE_CPU0LOCAL),
    'SRI_SEG1_7'        : (0x10000000, 0x70000000, OTHER),
    'SRI_SEG8'          : (0x81000000, 0x0EFFFFFF, OTHER),
    'SRI_SEG9_0'        : (0x90040000, 0x00100000, OTHER),
    'SRI_SEG9_1'        : (0x90400000, 0x0FC00000, OTHER),
    'SRI_SEGA'          : (0xA1000000, 0x0EFFFFFF, OTHER),
    'SRI_SEGB_0'        : (0xB0040000, 0x00100000, OTHER),
    'SRI_SEGB_1'        : (0xB0400000, 0x0FC00000, OTHER),
    'SRI_SEGF'          : (0xF8000000, 0x08000000, OTHER),


    # Special Function Registers (SFRs) and Core Special Function Registers (CSFRs).
    'CPU_0_SFR_CSFR'        : (0xF8800000, 2*MEMORY_SIZE_64KB, MEMTYPE_CPU0LOCAL),
    'CPU_1_SFR_CSFR'        : (0xF8820000, 2*MEMORY_SIZE_64KB, MEMTYPE_CPU1LOCAL),
    'CPU_2_SFR_CSFR'        : (0xF8840000, 2*MEMORY_SIZE_64KB, MEMTYPE_CPU2LOCAL),
    # SFRs
    'CPU_0_SFR'             : (0xF8800000, MEMORY_SIZE_64KB, MEMTYPE_CPU0LOCAL),
    'CPU_1_SFR'             : (0xF8820000, MEMORY_SIZE_64KB, MEMTYPE_CPU1LOCAL),
    'CPU_2_SFR'             : (0xF8840000, MEMORY_SIZE_64KB, MEMTYPE_CPU2LOCAL),
    # CSFRs
    'CPU_0_CSFR'            : (0xF8810000, MEMORY_SIZE_64KB, MEMTYPE_CPU0LOCAL),
    'CPU_1_CSFR'            : (0xF8830000, MEMORY_SIZE_64KB, MEMTYPE_CPU1LOCAL),
    'CPU_2_CSFR'            : (0xF8850000, MEMORY_SIZE_64KB, MEMTYPE_CPU2LOCAL),
}

# This is the Shared Resource Interconnect memory map for the Aurix platform
# This is a dictionary that maps the memory region name to a tuple with 2 or 3
# elements: (starting address, size, memory type if applicable, model name if applicable)
SRI_MEMORY_MAP = {

    # PFI : Program Flash Interface
    'PFI0'        : (0xA8080000, MEMORY_SIZE_512KB, MEMTYPE_RAM),
    'PFI1'        : (0xA8380000, MEMORY_SIZE_512KB, MEMTYPE_RAM),

    # EC : Erase counter
    'EC0'         : (0xA8000000, MEMORY_SIZE_16KB, MEMTYPE_RAM),
    'EC1'         : (0xA8300000, MEMORY_SIZE_16KB, MEMTYPE_RAM),

    # DFLASH : Data Flash (Non Volatile Memory)
    #          Utilized by user and security applications to store data.
    'DFLASH0'      : (0xAF000000, MEMORY_SIZE_256KB, MEMTYPE_FLASH),
    'DFLASH0_UCB'  : (0xAF400000, MEMORY_SIZE_24KB,  MEMTYPE_FLASH),
    'DFLASH0_CFS'  : (0xAF800000, MEMORY_SIZE_64KB,  MEMTYPE_FLASH),
    'DFLASH1_CACHE': (0xAFC00000, MEMORY_SIZE_128KB, MEMTYPE_FLASH),
    'DFLASH1'      : (0xFFC00000, MEMORY_SIZE_128KB, MEMTYPE_FLASH),

    #OLDA: Online Data Acquisition
    'OLDA_CACHED'  : (0x8FE00000, MEMORY_SIZE_512KB, MEMTYPE_RAM),
    'OLDA'         : (0xAFE00000, MEMORY_SIZE_512KB, MEMTYPE_RAM),

    #BROM
    'BROM_CACHED'  : (0x8FFF0000, MEMORY_SIZE_64KB, MEMTYPE_RAM),
    'BROM'         : (0xAFFF0000, MEMORY_SIZE_64KB, MEMTYPE_RAM),

    # LMU : Local Memory Unit
    #       The Local Memory Unit is an SRI peripheral providing access to volatile memory resources. Its primary purpose
    #       is to provide 256 KiB of local memory for general purpose usage.
    'LMU0RAM'           : (0xB0040000, MEMORY_SIZE_128KB, MEMTYPE_RAM),
    'LMU0RAM_CACHED'    : (0x90040000, MEMORY_SIZE_128KB, MEMTYPE_RAM),
    'LMU0'              : (0xF8100000, MEMORY_SIZE_64KB,  MEMTYPE_REGISTER, "LMU"),

    # DAM : Default Application Memory
    #       The Default Application Memory is an SRI peripheral providing access to volatile memory resources. Its primary
    #       purpose is to provide 64 kBytes or 32 kBytes of local memory for general purpose usage.
    'DAM0RAM'          : (0xB0400000, MEMORY_SIZE_64KB, MEMTYPE_RAM),
    'DAM0RAM_CACHED'   : (0x90400000, MEMORY_SIZE_64KB, MEMTYPE_RAM),
    'DAM0'             : (0xF8500000, MEMORY_SIZE_32KB, MEMTYPE_REGISTER, "DAM"),

    # Other registers
    'XBAR_DOM0'    : (0xF8700000, MEMORY_SIZE_64KB,   MEMTYPE_REGISTER, "XBAR"),
    'FSI_RAM'      : (0xF8020000, MEMORY_SIZE_32KB, MEMTYPE_RAM),
    'FSI_REG'      : (0xF8030000, MEMORY_SIZE_256B, MEMTYPE_RAM),
    'PMU_REG'      : (0xF8038000, MEMORY_SIZE_32KB,   MEMTYPE_REGISTER, "PMU_REG"),
    'DMU_REG'      : (0xF8040000, MEMORY_SIZE_256KB,  MEMTYPE_REGISTER, "DMU_REG"),

    #sri slave interface
    'AMU00'           : (0xF8508000, MEMORY_SIZE_256B,  MEMTYPE_RAM),
    'AMU01'           : (0xF8508100, MEMORY_SIZE_256B,  MEMTYPE_RAM),
    'ADMA0'           : (0xF8508400, MEMORY_SIZE_256B,  MEMTYPE_RAM),
    
    'DOM2'             : (0xFB7000000, MEMORY_SIZE_64KB),
    
    #EMEM_RAM
    'EMEM0_RAM'        : (0xB9000000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM1_RAM'        : (0xB9100000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM2_RAM'        : (0xB9200000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM0_RAM_CACHED' : (0x99000000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM1_RAM_CACHED' : (0x99100000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM2_RAM_CACHED' : (0x99200000, MEMORY_SIZE_1MB, MEMTYPE_RAM),
    'EMEM0'            : (0xFB000000, MEMORY_SIZE_64KB,   MEMTYPE_REGISTER, "EMEM"),
    'EMEM1'            : (0xFB010000, MEMORY_SIZE_64KB,   MEMTYPE_REGISTER, "EMEM"),
    'EMEM2'            : (0xFB020000, MEMORY_SIZE_64KB,   MEMTYPE_REGISTER, "EMEM"),
    #EMEM CONTROL REGISTER
    'EMEM_CONTROL'     : (0xFA006000, MEMORY_SIZE_256B,   MEMTYPE_REGISTER, "EMEM_CONTROL"), #should be on the BBB
    
    'XTM_CACHED'       : (0xB9400000, MEMORY_SIZE_512KB, MEMTYPE_RAM),
    'XTM'              : (0xFA000000, MEMORY_SIZE_24KB, MEMTYPE_RAM),
}


# This is the System Peripheral Bus memory map for the Aurix platform
# This is a dictionary that maps the memory region name to a tuple with 2 or 3
# elements: (starting address, size, register model if available)
SPB_MEMORY_MAP = {

    'FCE0'          : (0xF0000000, MEMORY_SIZE_512B),
    'CBS'           : (0xF0000400, MEMORY_SIZE_512B),

    'ASCLIN_0_1'       : (0xF0000600, MEMORY_SIZE_512B, "ASCLIN"),
    'ASCLIN_2_3'       : (0xF0000800, MEMORY_SIZE_512B, "ASCLIN"),
    'ASCLIN_4_5'       : (0xF0000A00, MEMORY_SIZE_512B, "ASCLIN"),
    'ASCLIN_6_7'       : (0xF0000C00, MEMORY_SIZE_512B, "ASCLIN"),
    'ASCLIN_8_9'       : (0xF0000E00, MEMORY_SIZE_512B, "ASCLIN"),

    'STM0'          : (0xF0001000, MEMORY_SIZE_256B),
    'STM1'          : (0xF0001100, MEMORY_SIZE_256B),
    'STM2'          : (0xF0001200, MEMORY_SIZE_256B),

    'GPT120'        : (0xF0001800, MEMORY_SIZE_256B),

    'QSPI0'         : (0xF0001C00, MEMORY_SIZE_256B),
    'QSPI1'         : (0xF0001D00, MEMORY_SIZE_256B),
    'QSPI2'         : (0xF0001E00, MEMORY_SIZE_256B),
    'QSPI3'         : (0xF0001F00, MEMORY_SIZE_256B),
    'QSPI4'         : (0xF0002000, MEMORY_SIZE_256B),

    'MSC0'          : (0xF0002600, MEMORY_SIZE_256B),
    'MSC1'          : (0xF0002700, MEMORY_SIZE_256B),

    'CCU60'         : (0xF0002A00, MEMORY_SIZE_256B),
    'CCU61'         : (0xF0002B00, MEMORY_SIZE_256B),

    'SENT'          : (0xF0003000, 11*MEMORY_SIZE_256B),
    'PSI5'          : (0xF0005000, 11*MEMORY_SIZE_256B),
    'PSI5S'         : (0xF0007000, MEMORY_SIZE_4KB),
    'DMA'           : (0xF0010000, MEMORY_SIZE_16KB),

    'ERAY0'         : (0xF001C000, MEMORY_SIZE_4KB, "ERAY"),
    'GETH_SNPS'     : (0xF001D000, MEMORY_SIZE_8KB),# Doc says 8.2Kbytes = 0x60FF
    'GETH'          : (0xF001F000, MEMORY_SIZE_4KB),
    # --- ADD ---
    'GETH1_SNPS'    : (0xF0019000, MEMORY_SIZE_8KB),# Doc says 8.2Kbytes = 0x60FF
    'GETH1'         : (0xF001B000, MEMORY_SIZE_4KB),
    
    'EVADC'         : (0xF0020000, MEMORY_SIZE_16KB),
    'EDSADC'        : (0xF0024000, MEMORY_SIZE_4KB, "EDSADC"),
    'CONVCTRL'      : (0xF0025000, MEMORY_SIZE_256B),
    'SBCU'          : (0xF0030000, MEMORY_SIZE_256B),
    'IOM0'          : (0xF0035000, MEMORY_SIZE_512B),
    
    'SCU'           : (0xF0036000, MEMORY_SIZE_1KB),
    'SMU'           : (0xF0036800, MEMORY_SIZE_2KB),
    'IR'            : (0xF0037000, MEMORY_SIZE_12KB),

    'P00'           : (0xF003A000, MEMORY_SIZE_256B),
    'P01'           : (0xF003A100, MEMORY_SIZE_256B),
    'P02'           : (0xF003A200, MEMORY_SIZE_256B),
    'P10'           : (0xF003AA00, MEMORY_SIZE_256B),
    'P11'           : (0xF003AB00, MEMORY_SIZE_256B),
    'P12'           : (0xF003AC00, MEMORY_SIZE_256B),
    'P13'           : (0xF003AD00, MEMORY_SIZE_256B),
    'P14'           : (0xF003AE00, MEMORY_SIZE_256B),
    'P15'           : (0xF003AF00, MEMORY_SIZE_256B),
    'P20'           : (0xF003B400, MEMORY_SIZE_256B),
    'P21'           : (0xF003B500, MEMORY_SIZE_256B),
    'P22'           : (0xF003B600, MEMORY_SIZE_256B),
    'P23'           : (0xF003B700, MEMORY_SIZE_256B),
    'P32'           : (0xF003C000, MEMORY_SIZE_256B),
    'P33'           : (0xF003C100, MEMORY_SIZE_256B),
    'P34'           : (0xF003C200, MEMORY_SIZE_256B),
    'P40'           : (0xF003C800, MEMORY_SIZE_256B),

    'HSM'           : (0xF0040000, MEMORY_SIZE_128KB),
    'MTU'           : (0xF0060000, MEMORY_SIZE_256B, "MTU"),
    'HSSL0'         : (0xF0080000, MEMORY_SIZE_1KB),
    'HSCT0'         : (0xF0090000, MEMORY_SIZE_64KB),
    'I2C0'          : (0xF00C0000, MEMORY_SIZE_64KB),
    'I2C0_SCR'      : (0xF00D0000, MEMORY_SIZE_256B),

    'GTM_part1'     : (0xF0100000, 0x9FD00),
    'GTM_part2'     : (0xF01A0000, 0x60000),
    'GTMWRAPPER'    : (0xF019FD00, 0x300),

    # according to documentation the size of those is 36Kb each
    'MCMCAN0'       : (0xF0200000, MEMORY_SIZE_64KB),
    'MCMCAN1'       : (0xF0210000, MEMORY_SIZE_64KB),
    'MCMCAN2'       : (0xF0220000, MEMORY_SIZE_64KB),

    #''' --- ADD ---
    #'SDMMC0'        : (0XF02B0000, MEMORY_SIZE_4KB),
    #'''

    'SCR_XRAM'      : (0xF0240000, MEMORY_SIZE_8KB),
    'PMS'           : (0xF0248000, MEMORY_SIZE_512B, "PMS"),

    'ASCLIN_10_11'  : (0xF02C0A00, MEMORY_SIZE_512B, "ASCLIN"),

    'CONSOLE'       : (0xF7500000, MEMORY_SIZE_1KB) # Steal Tricore reserved memory to run console module
}


# Mapping of DSPR regions for each core.
#  core id: [global address, local address, size]
CORE_DSPR_MAPPING = {
    0: [0x70000000, 0xD0000000, MEMORY_SIZE_240KB],
    1: [0x60000000, 0xD0000000, MEMORY_SIZE_240KB],
    2: [0x50000000, 0xD0000000, MEMORY_SIZE_96KB],
}

CORE_PSPR_MAPPING = {
    0: [0x70100000, 0xC0000000, MEMORY_SIZE_64KB],
    1: [0x60100000, 0xC0000000, MEMORY_SIZE_64KB],
    2: [0x50100000, 0xC0000000, MEMORY_SIZE_64KB],
}

##############################################################
# PLATFORM IMPLEMENTATION
# Ref: p.49 of AURIXTC3XX_ts_part1_V2.5.1.pdf
##############################################################

NUM_CORES = 3
NUM_STM = 3

# Analog Inputs
# p.680 of TC37X_ts_appx_V2.5.1.pdf
# The max groupd ID is FC3 which mapped as the 16th group. 
NUMBER_OF_EVADC_GROUPS  = 16
NUM_PRIMARY_GROUP = 4
NUM_PRIMARY_GROUP_CHANNEL = 8
NUM_SECONDARY_GROUP = 4
NUM_SECONDARY_GROUP_CHANNEL = 16
NUM_FAST_GROUP = 4
NUM_FAST_GROUP_CHANNEL = 1
# TODO: EDSADC is not instantiated
NUMBER_OF_EDSADC_GROUPS = 0
# Table 261, p.683 of TC37X_ts_appx_V2.5.1.pdf find the maximum AN, starting from AN0
NUMBER_OF_AN_PINS = 48
# Table 261, p.683  of TC37X_ts_appx_V2.5.1.pdf, counting the pXX.Y ports
NUMBER_OF_AI_PORTS = 28 # Ports with analog input support, pXX.Y AI

# core_num + 1 x dma + 1 x gtm_mcs
spb_num_masters = 5
spb_num_slaves = 191

# p.26 of https://www.infineon.com/dgdl/Infineon-AURIX_TC37xEXT-UserManual-v02_00-EN.pdf?fileId=5546d4627506bb32017527203f913b3d,
# SCI = 16
sri_num_slaves = 17 + 6
sri_dom2_num_slaves = 5
# p.27 of https://www.infineon.com/dgdl/Infineon-AURIX_TC37xEXT-UserManual-v02_00-EN.pdf?fileId=5546d4627506bb32017527203f913b3d, 
# MCI = 0..12
sri_num_masters = 13 + 6
sri_dom2_num_masters = 5
# p.27 of TC36x_appx_um_v1.4.pdf
SRI_CPU_MCI = [(0, 2), (1, 3), (2, 4)] # (CORE ID, MCI)
SRI_CPU_SCI = [(0, 3, 4), (1, 5, 6), (2, None, 8)] # (CORE ID, XBAR CPUP interface for PFLASH, XBAR CPUS interface for LMU)
# p.125 of  TC36x_appx_um_v1.4.pdf
STM_SCU_ERU = [(0, 'scuEruChannelIn1_i', 3), (1, 'scuEruChannelIn3_i', 3), (2, 'scuEruChannelIn5_i', 3)]

# GTM
# p.378 of TC37X_ts_appx_V2.5.1.pdf
NUM_SPE = 2
NUM_MCS = 5
NUM_MCS_CHANNEL = 8
NUM_TIM = 6
NUM_TIM_CHANNEL = 8
NUM_TOM = 3
NUM_TOM_CHANNEL = 16
NUM_ATOM = 6
NUM_ATOM_CHANNEL = 8

# p.740 of TC37X_ts_appx_V2.5.1.pdf
NUM_QSPI = 5

# p.764 of TC37X_ts_appx_V2.5.1.pdf
NUM_MSC = 2

# p.771 of TC37X_ts_appx_V2.5.1.pdf
NUM_MCMCAN = 3
# number of node per MCMCAN
NUM_MCAN = 4

# p.708 of TC37X_ts_appx_V2.5.1.pdf
# page 35 of TC39x_A_v1_2_4_Platform_User_Manual_v1_2_4.pdf
# 2 kernls per ASCLIN model, so that 12 / 2 = 6 instances of ASCLINs are needed
NUM_ASCLIN = 6

analog_ref_gnd = {
    'ALL': 2,
    1: [],
    2: ['EVADC_G0', 'EVADC_G1', 'EVADC_G2', 'EVADC_G3', 'EVADC_G8', 'EVADC_G9', 'EVADC_G10', 'EVADC_G11', 'EVADC_G12', 'EVADC_G13', 'EVADC_G14', 'EVADC_G15'],
}

# NUM EMEM_RAM slaves
NUM_EMEM = 3