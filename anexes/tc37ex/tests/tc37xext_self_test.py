import vlab
import os.path


self_test_path = os.path.join(vlab.get_properties()["toolboxes"]["aurix"]["path"], "examples","tc37xext","system_test")

vlab.load("aurix.tc37xext.sim",args=["--image="+os.path.join(self_test_path, "Test_Tricore.elf")] + __args__)

# Run the simulation.
vlab.run(60, "ms", blocking=True)

vlab.exit()