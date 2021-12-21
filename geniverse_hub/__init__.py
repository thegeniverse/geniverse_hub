import os
import sys

from geniverse_hub.hub_utils import HUB_CONFIG_DICT

module_name_list = [conf["name"] for conf in HUB_CONFIG_DICT["modules"]]
for module_name in module_name_list:
    module_path = f"./geniverse_hub/{module_name}"

    if os.path.exists(module_path):
        print(f"{module_name} module found and added to path!")
        sys.path.append(module_path)
