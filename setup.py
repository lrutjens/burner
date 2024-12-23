from burner.version import __version__
from setuptools import setup, find_packages

setup(
    name="burner",
    version=__version__,
    description="Subtitle generation with Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rkulyassa/burner/",
    license="MIT",
    author="Ryan Kulyassa",
    author_email="rkulyassa@gmail.com",
    packages=find_packages(),
    install_requires=["numpy>=1.14.5"],
)
