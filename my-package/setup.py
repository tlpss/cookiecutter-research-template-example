import setuptools
from setuptools import find_packages

setuptools.setup(
    name="my-package",
    version="0.0.1",
    author="Thomas Lips",
    author_email="todo@gmail.com",
    description="TODO",
    install_requires=[
        "numpy",
    ],
    packages=find_packages(),
)
