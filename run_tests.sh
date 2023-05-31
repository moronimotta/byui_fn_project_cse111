#!/bin/bash

cd src
python -m unittest discover -s . -p "*.py"

