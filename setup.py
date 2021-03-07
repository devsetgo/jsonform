# -*- coding: utf-8 -*-
"""Setup script for realpython-reader"""

import os.path

from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="json_form",
    version="0.0.1",
    description="Pydantic generated JSON Schema Forms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/devsetgo/json_form",
    project_urls={
        "Documentation": "https://github.com/devsetgo/jsonform",
        "Source": "https://github.com/devsetgo/jsonform",
    },
    author="Mike Ryan",
    author_email="mikeryan56@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="Common file, folder, and regex functions",
    python_requires=">=3.8",
    packages=["json_form"],
    include_package_data=True,
    install_requires=["pydantic==1.8"],
)
