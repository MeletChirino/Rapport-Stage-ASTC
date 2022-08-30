def identifier():
    return "aurix"

def name():
    return "Aurix Virtual Platform"

def platform_modules():
    import sys
    
    modules = []        
    if 'vc100' in sys.executable:   
        modules.append(("aurix.tc27xb.sim",                 ["TC27xB", "Load simulator"]))
        modules.append(("aurix_scripts.tc27xb_self_test",   ["TC27xB", "Run self test"]))
        modules.append(("aurix.tc27x.sim",                  ["TC27xC", "Load simulator"]))
        modules.append(("aurix_scripts.tc27x_self_test",    ["TC27xC", "Run self test"]))
        modules.append(("aurix.tc29x.sim",                  ["TC29x", "Load simulator"]))
        modules.append(("aurix_scripts.tc29x_self_test",    ["TC29x", "Run self test"]))
        
    modules.append(("aurix.tc39x.sim",                  ["TC39xA", "Load simulator"]))
    modules.append(("aurix_scripts.tc39x_self_test",    ["TC39xA", "Run self test"]))
    modules.append(("aurix.tc39xb.sim",                 ["TC39xB", "Load simulator"]))
    modules.append(("aurix_scripts.tc39xb_self_test",   ["TC39xB", "Run self test"]))
    modules.append(("aurix.tc38x.sim",                  ["TC38x", "Load simulator"]))
    modules.append(("aurix_scripts.tc38x_self_test",    ["TC38x", "Run self test"]))
    modules.append(("aurix.tc3ex.sim",                  ["TC3Ex", "Load simulator"]))
    modules.append(("aurix_scripts.tc3ex_self_test",    ["TC3Ex", "Run self test"]))
    modules.append(("aurix.tc36x.sim",                  ["TC36x", "Load simulator"]))
    modules.append(("aurix.tc37x.sim",                  ["TC37x", "Load simulator"]))
    modules.append(("aurix.tc37xext.sim",               ["TC37xEXT", "Load simulator"]))
    modules.append(("aurix_scripts.tc37xext_self_test", ["TC37xEXT", "Run self test"]))
    modules.append(("aurix.tc33x.sim",                  ["TC33x", "Load simulator"]))
    
    return modules