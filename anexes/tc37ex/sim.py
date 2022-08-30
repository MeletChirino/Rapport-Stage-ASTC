# ----------------------------------------------------------------------------#
# Copyright (C) Australian Semiconductor Technology Company (ASTC). 2013.
# All Rights Reserved.
#
# This is unpublished proprietary source code of the Australian Semiconductor
# Technology Company (ASTC).  The copyright notice does not evidence any actual
# or intended publication of such source code.
# ----------------------------------------------------------------------------#

import vlab
import aurix.common
import sysc

__version__ = '1.0.0'

# Determine the loaded module's toolbox library name.
library = __name__.rsplit('.', 1)[0]
variant = __name__.split(".")[1]

print("\nAURIX Virtual Platform Toolbox ({0}) {1}\n".format(
    variant.upper(), __version__))

vlab.properties(name=variant, extensions={"sc_writer_policy": "unchecked"})

aurix.common.enable_common_options()

args = vlab.parse_args()
args["variant"] = variant

# SCU model has an issue, it creates a systemC event in the past. It causes oscar to indefinitely displays :
# "Error: (E544) simulation time value overflow, simulation aborted"
# To avoid this flood of prints we disable this error message.
sysc.sc_report_handler().set_actions("simulation time value overflow", sysc.SC_DO_NOTHING)

platform = vlab.instantiate(vlab.component(description="aurix.tc37x.description"), #TC37xEXT makes use of TC37x description
                            name=variant, args=args)

if args["testbench"] != "":
    vlab.load(args["testbench"], args=__args__)

vlab.stub(platform)

aurix.common.handle_common_options(args)

# Run the simulation for the specified amount of time (if more than 0)
if args["run"] > 0:
    vlab.run(args["run"], time_unit="s", blocking=True)

