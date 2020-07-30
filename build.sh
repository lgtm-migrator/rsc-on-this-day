#!/bin/bash

# Script to build sdist and bdist_wheel for rsc-on-this-day

# Create venv and activate
python3 -m venv ./build-venv
source ./build-venv/bin/activate

# Install dependencies
pip3 install setuptools pip wheel --upgrade
pip3 install -r requirements.txt
pip3 install -r doc-source/requirements.txt

# Make manpage
./make_manpage.sh

# Run python setup
python3 setup.py sdist bdist_wheel

# deactivate venv and delete
deactivate
rm -rf ./build-venv
