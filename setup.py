# import json
import setuptools
# import urllib.request

# hub_config_url = "https://raw.githubusercontent.com/thegeniverse/geniverse_hub/main/geniverse_hub/hub_config.json"
# res = urllib.request.urlopen(hub_config_url).read()
# HUB_CONFIG_DICT = json.loads(res)

# extra_deps = {}
# extra_deps["all"] = []
# for module_config in HUB_CONFIG_DICT["modules"]:
#     module_owner = module_config["owner"]
#     module_name = module_config["name"]
#     module_dist = module_config["dist"]

#     print(f"Initiating {module_name} from {module_owner}")

#     try:
#         requirement_name = f"{module_name} @ https://github.com/{module_owner}/{module_name}/archive/{module_dist}.zip"
#         extra_deps[module_name] = [requirement_name]
#         extra_deps["all"].append(requirement_name)

#     except:
#         print(f"WARNING! {module_name} not found.", )
#         continue

# print(extra_deps)

with open(
        "README.md",
        "r",
        encoding="utf-8",
) as fh:
    long_description = fh.read()

setuptools.setup(
    name="geniverse_hub",
    version="0.0.4",
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
    install_requires=[],
    # extras_require=extra_deps,
)