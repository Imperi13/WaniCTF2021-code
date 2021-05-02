import angr

project = angr.Project("./licence",auto_load_libs=False)

addr_main = project.loader.main_bin.get_symbol('main').addr

print(addr_main)
