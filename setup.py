"""py-motmetrics - Metrics for multiple object tracker (MOT) benchmarking.

Christoph Heindl, 2017
https://github.com/cheind/py-motmetrics
"""
import io
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Get the directory where setup.py is located
here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "requirements.txt")) as f:
    required = f.read().splitlines()

with io.open(os.path.join(here, "Readme.md"), encoding="utf-8") as f:
    long_description = f.read()

# Handle version number with optional .dev postfix when building a develop branch
# on AppVeyor.
VERSION = io.open(os.path.join(here, "motmetrics/__init__.py")).readlines()[-1].split()[-1].strip('"')
BUILD_NUMBER = os.environ.get("APPVEYOR_BUILD_NUMBER", None)
BRANCH_NAME = os.environ.get("APPVEYOR_REPO_BRANCH", "develop")
if BUILD_NUMBER is not None and BRANCH_NAME != "master":
    VERSION = "{}.dev{}".format(VERSION, BUILD_NUMBER)

setup(
    name="motmetrics",
    version=VERSION,
    description="Metrics for multiple object tracker benchmarking.",
    author="Christoph Heindl, Jack Valmadre",
    url="https://github.com/cheind/py-motmetrics",
    license="MIT",
    install_requires=required,
    packages=["motmetrics", "motmetrics.tests", "motmetrics.apps"],
    include_package_data=True,
    keywords="tracker MOT evaluation metrics compare",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
