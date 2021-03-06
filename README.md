# `geniverse_hub` 🪐
Use and contribute to the Geniverse HUB 🪐 with the following instructions.

# Setup
First install the `geniverse_hub` python package with the following command:

```bash 
pip install geniverse-hub
```

This will provide you with the required scripts to download and utilize the models available in the hub.

All the models are extracted from github repositories. Hence, one requirement for this library to work is to have _Git_ installed and working in your machine. All the available models are referenced in this [config file](./geniverse_hub/hub_config.json) with its owner, name and ditribution (i.e., the branch to be used within the github repo).

In order to install the required dependencies for a required module, add the name of the module within squared brackets after the install command as follows:

# Usage
There are some common functionalities for downloading and loading models in the hub. The following is an example on how to use `VQGAN`:

```python
from geniverse_hub import hub_utils
taming_utils = hub_utils.load_from_hub(module_name="taming", )
model = taming_utils.load_model()
```

You can utilize any of the models in the hub's [config file](./geniverse_hub/hub_config.json) by changing the value of `module_name` for the corresponding model that you intend to load.

The result will be equivelant to a python package where you will have access to functionalities of the specific module that you loaded such as loading a model. In order to find the functionalities for each of the models, access their respective documentation in `https://github.com/<owner>/<name>/tree/<dist>` where `owner`, `name` and `dist` can be found in the hub's [config file](./geniverse_hub/hub_config.json).

# Contribute
In order to contribute to the Geniverse Hub 🪐 you just need to create a github repository following some simple guidelines and reference it within our [config file](./geniverse_hub/hub_config.json).

## Contribution Guidelines
In order for your model to be accessible from the hub, you must provide with a `requirements.txt` file where all the python dependencies are stated. The repository should contain a python package with the same name os the repository. This package should contain a `modeling_utils.py` script where the functionalities for your model are available. The result from `geniverse_hub.hub_utils.load_module(<your-module's-name>)` will be the set of functions and classes that you implement there.

You can find an example of this coding structure in our `taming` implementation in `https://github.com/thegeniverse/taming/tree/master`. Here, we have a python package with the same name as the repo (`taming`) with all the required code for this module to work. There, we can also find the `modeling_utils.py`. Inside this file there are all the functionalities that we give access for anyone using our model from the hub. For example, we can find the function `load_model()` that can be used to load a VQGAN model. 

### Add Requirements
Your requirement file should be named `requirements.txt` and should be placed on the root folder of your repositroy.

### Create Python Module
Your python module should be created from a folder with the same name as your github repository. If your repository name is `taming` the name of this folder should be `taming` too. Assuming that you are using a new version of Python it is not required to add a `__init__.py` within this folder in order for Python to understand that is a module, but we encourage you to do so to make it more explicit (it is also very convenient to manage what gets imported when your module is invoked).


### Add Modeling Utils
Within the Python module just created there should be a file names `modeling_utils.py`. This file will provide anyone that wants to use your code with easy-to-use functionalities and/or classes to load the model that you provide.

### Create a Local PyPi Package
The final step is to add a `setup.py` in the root folder of your project in order for it to be imported by `geniverse_hub` 🪐. This file need not to be useful to be uploaded to the __Python Package Index__ and it can be as simple as the following template:

```python
import setuptools

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements_list = req_file.read().strip().split("\n")

setuptools.setup(
    name="<module-name>",
    packages=["<module-name>"],
    install_requires=requirements_list,
)
```

Where `<module-name>` of course references the name of your module and github repo (that, as we mentioned before, it shoule be the same).

**WARNING!!!** Make sure that the name of your module is unique so python do not get confused when it loads it!

The structure of your project should look something like this:

```
- <module-name>
    + <module-name>
        - `__init__.py` (optional)
        - `modeling_utils.py`
    + `setup.py`
```