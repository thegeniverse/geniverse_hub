import pkgutil

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    print("LOADING MODULE NAME", module_name)
    __all__.append(module_name)
    submodule = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = submodule