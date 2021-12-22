import os
import importlib

from geniverse_hub.hub_config import HUB_CONFIG_DICT, HUB_MODULE_DIR


def load_from_hub(module_name: str, ):
    try:
        print(f"Loading {module_name}...")
        hub_module_utils = importlib.import_module(
            f"{module_name}.modeling_utils")

        return hub_module_utils

    except:
        module_config = [
            config_dict for config_dict in HUB_CONFIG_DICT["modules"]
            if config_dict["name"] == module_name
        ][0]

        module_owner = module_config["owner"]
        module_name = module_config["name"]
        module_dist = module_config["dist"]

        print(f"Initiating {module_name} from {module_owner}")

        requirement_name = f"https://github.com/{module_owner}/{module_name}/archive/{module_dist}.zip"
        print(f"Whoops! You do not have {module_name} installed")
        print("Run the following command to install it:")
        print(f"\x1b[6;30;47mpip install {requirement_name}")

        return None
