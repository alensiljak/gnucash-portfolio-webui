#!/usr/bin/env python3
"""Setup"""
from setuptools import setup, find_packages
from distutils.core import setup
from codecs import open
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gnucash-portfolio-webui",
    #packages=["gnucash_portfolio_webui"],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    version="1.3.4",
    description="Web UI for GnuCash Portfolio",
    author="Alen Siljak",
    author_email="alen.siljak@gmx.com",
    url="https://github.com/MisterY/gnucash-portfolio-webui",
    # download_url = "http://chardet.feedparser.org/download/python3-chardet-1.0.1.tgz",
    keywords=["gnucash", "finance", "portfolio", "webui"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    install_requires=[
        'flask',
        'flask_assets',
        'gnucash-portfolio'
    ],
    entry_points={
        'console_scripts': [
            'gpweb=gnucash_portfolio_webui.app:run_server',
        ],
    },
    include_package_data=True
)
