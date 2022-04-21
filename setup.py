# from distutils.core import setup
from setuptools import find_packages, setup
import pathlib

setup(
    # Application name:
    name="wDRMetrics",
    
    # Version number (initial):
    version="0.0.4",
    
    # Application author details:
    author="Zhang",
    author_email="oo@zju.edu.cn",
    
    # Packages
    packages=["wDRMetrics"],
    
    package_dir={'wDRMetrics.templates': 'wDRMetrics/templates', 'wDRMetrics.static': 'wDRMetrics/static'},

    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/wDRMetrics/",
    
    #
    license="LICENSE.txt",
    description="A GUI wrapper for pyDRMetrics. Rewritten using Flask.",
    
    long_description_content_type='text/markdown',
    long_description= open('README.md').read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "pyDRMetrics",
    ],
)

# To Build and Publish (for developer only), 
# Run: python setup.py sdist bdist_wheel; twine upload dist/*