# python-gpu-tutorial

This tutorial demonstrate how to run numba through Jupyter python node book on a GPU on the Sherlock cluster at Stanford.

salloc -N 1 -n 2 --time=8:00:00 --gres=gpu:1 -p gpu -C GPU_SKU:P40
salloc -N 1 -n 2 --gres=gpu:2 -p gpu –time=8:00:00
squeue -u zyzhang
ssh -XY sh-112-05
cd $PI_HOME/zyzhang/usertests/tutorial/nvlab/2018/gtc2018-numba/

ml load py-jupyter/1.0.0_py36
ml load py-numba/0.35.0_py36
ml load cuda/8.0.61
ml load py-scipystack/1.0_py36

export NUMBAPRO_LIBDEVICE=/share/software/user/open/cuda/8.0.61/nvvm/libdevice/
export NUMBAPRO_NVVM=/share/software/user/open/cuda/8.0.61/nvvm/lib64/libnvvm.so

C_PORT=$(( (UID*RANDOM)%55500 + 9000 ))
R_HOST=$(hostname -s)
R_PORT=$(( C_PORT + RANDOM%1000 ))

echo $C_PORT
42312

echo $R_HOST
sh-112-05

echo $R_PORT
43022

Start the jupyter note book on a (gpu) compute node allocated previously. The name of the compute node is given by R_HOST. The notebook will communicate through port $R_PORT on the compute node. 
unbuffer jupyter-notebook --no-browser --log-level=0 --ip=${R_HOST} --port=${R_PORT} | unbuffer -p sed "s/${R_HOST}:${R_PORT}/localhost:${C_PORT}/g"

Copy/paste this URL into your browser when you connect for the first time,
to login with a token:
    http://localhost:42312/?token=686ea6763625257e08bc241b7a6710a01fffabd822d3c737

Now, set up a tunnel between the $C_PORT on the local Linux or Windows machine and the  $R_PORT on the remote compute node  $R_HOST. The tunnel is set up through the log in node on Sherlock 2:
ssh -XY -L 42312:sh-112-05:43022 zyzhang@login.sherlock.stanford.edu

On the local machine  http://localhost:42312 will diplay the notebook started on the remote compute node through a browser.  
