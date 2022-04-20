# from distutils.core import setup
from setuptools import find_packages, setup
import pathlib

setup(
    # Application name:
    name="wDRMetrics",
    
    # Version number (initial):
    version="0.0.1",
    
    # Application author details:
    author="Zhang",
    author_email="oo@zju.edu.cn",
    
    # Packages
    packages=["wDRMetrics"],
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/wDRMetrics/",
    
    #
    license="LICENSE.txt",
    description="A GUI wrapper for pyDRMetrics. Rewritten using Flask.",
    
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    
    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)

# To Build and Publish (for developer only), 
# Run: python setup.py sdist bdist_wheel; twine upload dist/*