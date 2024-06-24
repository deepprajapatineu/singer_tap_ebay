#!/usr/bin/env python
from setuptools import setup

setup(
    name="singer_tap_eBay",
    version="0.1.0",
    description="Singer.io tap for extracting data from eBay's General Ledger API",
    author="Deep Prajapati",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["singer_tap_eBay"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        'google-auth',
        'google-api-python-client'
    ],
    entry_points="""
    [console_scripts]
    singer_tap_eBay=singer_tap_eBay:main
    """,
    packages=["singer_tap_eBay"],
    package_data = {
        "schemas": ["singer_tap_eBay/schemas/*.json"]
    },
    include_package_data=True,
)
