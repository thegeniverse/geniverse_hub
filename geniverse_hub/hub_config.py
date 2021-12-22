import os
import urllib.request
import json

HUB_MODULE_DIR = os.path.dirname(__file__)

HUB_CONFIG_PATH = os.path.join(HUB_MODULE_DIR, "./hub_config.json")

hub_config_url = "https://raw.githubusercontent.com/thegeniverse/geniverse_hub/main/geniverse_hub/hub_config.json"
res = urllib.request.urlopen(hub_config_url).read()
HUB_CONFIG_DICT = json.loads(res)
