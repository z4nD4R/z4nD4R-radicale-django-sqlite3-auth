#!/usr/bin/env python3
# from distutils.core import setup
# setup(name="radicale_django_auth", packages=["radicale_django_auth"])

import setuptools



with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="radicale-django-sqlite3-auth", # Replace with your own username
    version="0.0.1",
    author="z4nD4R",
    author_email="ms@zndr.tech",
    description="Django sqlite3 authentication backend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/z4nD4R",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
