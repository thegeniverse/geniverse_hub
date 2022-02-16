import setuptools

with open(
        "README.md",
        "r",
        encoding="utf-8",
) as fh:
    long_description = fh.read()

setuptools.setup(
    name="geniverse_hub",
    version="0.0.6",
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
)