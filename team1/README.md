# Travelling Salesman Problem neural networks

based on https://github.com/chaitjo/graph-convnet-tsp

adapted for AWS Sagemaker studio lab

clone this directory somewhere and run following commands from terminal:

    cd neural_networks_tsp
    conda create -y -n gcn-tsp-env python=3.6.7
    conda activate gcn-tsp-env
    conda install -y pytorch=0.4.1 cuda90 -c pytorch
    pip3 install numpy==1.15.4 scipy==1.1.0 matplotlib==3.0.2 seaborn==0.9.0 pandas==0.24.2 networkx==2.2 scikit-learn==0.20.2 tensorflow-gpu==1.12.0 tensorboard==1.12.0 Cython
    pip3 install tensorboardx==1.5 fastprogress==0.1.18
    pip3 install jupyterlab
    git clone https://github.com/jvkersch/pyconcorde
    cd pyconcorde
    pip install -e .
    cd ..
    ./download_models.sh
    
then run ``tsp_100.ipynb`` notebook with ``gsp-tpv-env`` kernel
