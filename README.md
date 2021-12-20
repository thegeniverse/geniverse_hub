# `geniverse_hub` 🪐
Use and contribute to the Geniverse HUB 🪐 with the following instructions.

# Setup
First install the `geniverse_hub` python package with the following command:

```bash 
pip install geniverse_hub
```

This will provide you with the required scripts to download and utilize the models available in the hub.

All the models are extracted from github repositories. Hence, one requirement for this library to work is to have _Git_ installed and working in your machine. All the available models are referenced in this [config file](./geniverse_hub/hub_config.json) with its owner, name and ditribution (i.e., the branch to be used within the github repo).

# Usage
There are some common functionalities for downloading and loading models in the hub. The following is an example on how to use `VQGAN`:

```python
from geniverse_hub import hub_utils
model = hub_utils.load_from_hub(module_name="taming", )
```

You can utilize any of the models in the hub's [config file](./geniverse_hub/hub_config.json) by changing the value of `module_name` for the corresponding model that you intend to load.

The result will be a `HubModel` instance that will allow you to utilize the loaded model. In order to find the functionalities for each of the models, access their respective documentation in [WIP].

# Contribute
In order to contribute to the Geniverse Hub 🪐 you just need to create a github repository following some simple guidelines and reference it within our [config file](./geniverse_hub/hub_config.json).

## Implementation requirements
In order for your model to be accessible from the hub, you must provide with a `requirements.txt` file where all the python dependencies are stated and a `modeling_utils.py` script where the functionalities for your model are available.

