from vlab import *
import vlab
from aurix.tc37xext.defines import *
from aurix.stub_utils import create_stub_factory
import model_stubs

properties(
    name="emem",
    kind="hierarchical",
    extensions = {"copyright": "ASTC", "creation_year": 2022})

router_component = component('tlm_router_32', module='vlab.components')
router = instantiate(router_component, 'EMEM_ROUTER', args=[vlab.NAME, 3, 6], visibility="hidden")

for i in range(3):
    name = "EMEM{}".format(i)
    ram_name = name + "_RAM"
    emem_ram = instantiate(component("tlm_memory_32", module="vlab.components"), ram_name, args=[vlab.NAME, SRI_MEMORY_MAP[ram_name][1], 0, False], doc="{} memory model".format(ram_name))

    connect((router, "initiator_socket", i*2), (emem_ram, 'target_socket'))
    router.obj.add_address_mapping(i*2, SRI_MEMORY_MAP[ram_name][0], SRI_MEMORY_MAP[ram_name][1], SRI_MEMORY_MAP[ram_name][0])
    ram_cached_name = ram_name + "_CACHED"
    router.obj.add_address_mapping(i*2, SRI_MEMORY_MAP[ram_cached_name][0], SRI_MEMORY_MAP[ram_cached_name][1], SRI_MEMORY_MAP[ram_cached_name][0])

    # Helper to create stub models from a description
    stub_initiator = create_stub_factory(model_stubs)

    ##### EMEM SFR ######
    stub_initiator((router, "initiator_socket", i *2 +1), "EMEM", name, None)
    router.obj.add_address_mapping(i *2 +1, SRI_MEMORY_MAP[name][0], SRI_MEMORY_MAP[name][1], SRI_MEMORY_MAP[name][0])

    vlab.expose((router, "target_socket", i), "{}_SLAVE".format(name))