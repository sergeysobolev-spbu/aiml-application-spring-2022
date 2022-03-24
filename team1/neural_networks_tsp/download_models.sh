#!/bin/bash
mkdir ./logs
cd ./logs
pip3 install gdown
gdown https://drive.google.com/uc?id=1qmk1_5a8XT_hrOV_i3uHM9tMVnZBFEAF
tar -xvf old-tsp-models.tar.gz
mv tsp-models/tsp* .
