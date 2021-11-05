from distutils.core import setup
from setuptools import find_packages

setup(
    name="surveyextractor",
    packages=find_packages(),
    version="0.0.1",
    license="LGPL",
    description="Python library for reading and writing survey results for EASE project.",
    author="Pelle Rosenbeck Gøeg",
    url="https://github.com/TRG-BUILD",
    keywords=["survey", "extraction"]
)