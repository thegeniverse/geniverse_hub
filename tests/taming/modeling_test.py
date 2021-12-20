from geniverse_hub.taming.modeling_utils import load_vqgan

try:
    vqgan_model = load_vqgan()
    print("OK!")
except:
    print("FAILED")