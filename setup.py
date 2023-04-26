import pandasflow
from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme = readme_file.read()



setup(
    name="pandasflow",
    version=pandasflow.__version__,
    author="Priboy313",
    author_email="Priboy313@yandex.ru",
    description="A set of custom python modules for friendly workflow on pandas",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Priboy313/pandasflow",
    packages=find_packages(),
    install_requires=pandasflow.requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)