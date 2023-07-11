#!/bin/sh
#SBATCH --job-name train-lol-palette            # this is a parameter to help you sort your job when listing it
#SBATCH --ntasks 1                    # number of tasks in your job. One by default
#SBATCH --cpus-per-task 1             # number of cpus for each task. One by default
#SBATCH --mem-per-cpu 10000
#SBATCH --partition shared-gpu         # the partition to use. By default debug-cpu
#SBATCH --time 00:10:00                  # maximum run time.
#SBATCH --gpus ampere:1
##SBATCH --gres VramPerGpu:20G

 
module load GCC/10.3.0 OpenMPI/4.1.1 SciPy-bundle/2021.05 PyTorch/1.11.0-CUDA-11.3.1 torchvision/0.12.0-PyTorch-1.11.0-CUDA-11.3.1               # load a specific software using module, for example Python
 
source .env/bin/activate
echo SLURM allocated GPUs: $CUDA_VISIBLE_DEVICES
python -m palette train --debug -c lol.json -gpu $CUDA_VISIBLE_DEVICES
deactivate