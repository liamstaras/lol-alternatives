#!/bin/sh
#SBATCH --job-name train-lol-palette            # this is a parameter to help you sort your job when listing it
#SBATCH --ntasks 1                    # number of tasks in your job. One by default
#SBATCH --cpus-per-task 1             # number of cpus for each task. One by default
#SBATCH --mem-per-cpu 10000
##SBATCH --partition shared-gpu         # the partition to use. By default debug-cpu
#SBATCH --partition private-dpt-gpu
#SBATCH --time 01:00:00                  # maximum run time.
#SBATCH --gpus ampere:1
##SBATCH --gres VramPerGpu:40G

source ./requirements/modules.sh
source .env/bin/activate
echo SLURM allocated GPUs: $CUDA_VISIBLE_DEVICES
python -m palette train --debug -c configurations/palette/lol.json -gpu $CUDA_VISIBLE_DEVICES
deactivate