#!/bin/bash
echo "Setting up directory structure"
mkdir -p data
mkdir -p data/searches
mkdir -p models
echo "Creating virtual environemnt with venv"
python3 -m venv venv
source venv/bin/activate
echo "Installing dependencies"
pip install -r requirements.txt