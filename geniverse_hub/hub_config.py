import json
import os

HUB_MODULE_DIR = os.path.dirname(__file__)

HUB_CONFIG_PATH = os.path.join(HUB_MODULE_DIR, "./hub_config.json")
HUB_CONFIG_DICT = {}

with open(HUB_CONFIG_PATH, "rb") as hub_config_file:
    HUB_CONFIG_DICT = json.load(hub_config_file)