import os
import sys
import importlib
import pkgutil
import subprocess
import requests

import git

from geniverse_hub.hub_config import HUB_CONFIG_DICT, HUB_MODULE_DIR


def load_from_hub(module_name: str, ):
    if module_name in os.listdir(HUB_MODULE_DIR):
        print(f"Found cache from {module_name}...")

    else:
        print(f"Loading {module_name}...")

        module_list = HUB_CONFIG_DICT["modules"]
        module_config = next(
            filter(
                lambda config: config["name"] == module_name,
                module_list,
            ))

        module_owner = module_config["owner"]
        module_dist = module_config["dist"]

        try:
            requirements_url = ("https://raw.githubusercontent.com/"
                                f"{module_owner}/"
                                f"{module_name}/"
                                f"{module_dist}/"
                                "requirements.txt")

            required_packages = requests.get(
                requirements_url).text.strip().split("\n")

            subprocess.call(['pip', 'install', '-U', *required_packages])

        except:
            print(f"WARNING! {module_name} with no requirements.", )

        module_git_url = f"https://github.com/{module_owner}/{module_name}"

        git.Repo.clone_from(
            module_git_url,
            os.path.join(HUB_MODULE_DIR, module_name),
            branc=module_dist,
        )

    file_path_list = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), module_name),
    ]

    sys.path += file_path_list

    for loader, module_name, is_pkg in pkgutil.walk_packages(file_path_list):
        print("MODULE NAME", module_name)
        submodule = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = submodule

    hub_module = importlib.import_module(f"geniverse_hub.{module_name}", )

    hub_module_utils = hub_module.modeling_utils

    return hub_module_utils
