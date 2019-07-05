import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blockstreamesplora",
    version="0.0.1",
    author="Dumitru Valeriu Voicu",
    author_email="valinsky@protonmail.com",
    description="Python API wrapper for Blockstream Esplora",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valinsky/blockstreamesplora",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
