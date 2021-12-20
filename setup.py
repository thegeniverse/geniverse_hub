import setuptools
import requests

from geniverse_hub.hub_config import HUB_CONFIG_DICT

extra_deps = {}
for module_config in HUB_CONFIG_DICT["modules"]:
    module_owner = module_config["owner"]
    module_name = module_config["name"]
    module_dist = module_config["dist"]

    print(f"Initiating {module_name} from {module_owner}")

    requirements_url = ("https://raw.githubusercontent.com/"
                        f"{module_owner}/"
                        f"{module_name}/"
                        f"{module_dist}/"
                        "requirements.txt")

    try:
        extra_deps[module_name] = requests.get(
            requirements_url).text.strip().split("\n")
    except:
        print(f"WARNING! {module_name} with no requirements.", )
        print(f"There was an error retreiving {requirements_url}.")
        continue

print(extra_deps)

with open(
        "README.md",
        "r",
        encoding="utf-8",
) as fh:
    long_description = fh.read()

setuptools.setup(
    name="geniverse_hub",
    version="0.0.0",
    author="Javi and Vicc",
    author_email="vipermu97@gmail.com",
    description="Library for downloading and loading generative AI models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thegeniverse/geniverse_hub",
    project_urls={
        "Docs": "https://github.com/thegeniverse/geniverse_hub/docs",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "gitpython==3.1.24",
    ],
)