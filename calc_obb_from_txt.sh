#!/bin/bash
conan install -g virtualenv -if /tmp/myenv reader/0.1@ar/stable
source /tmp/myenv/activate.sh
calc_obb_from_txt --input "$1"
source /tmp/myenv/deactivate.sh
