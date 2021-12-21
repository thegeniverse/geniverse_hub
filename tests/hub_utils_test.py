from geniverse_hub import hub_utils

try:
    model_name = "taming"
    model = hub_utils.load_from_hub(model_name)
    print("OK!")
except Exception as e:
    print("ERROR!")
    print(e)

from taming.modeling_utils import load_vqgan

try:
    vqgan_model = load_vqgan()
    print("OK!")
except:
    print("FAILED")