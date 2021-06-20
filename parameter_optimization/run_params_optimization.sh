#!/bin/csh

#SBATCH --wckey xfq22001
#SBATCH -N 1
#SBATCH -n 36
#SBATCH -J ADF_
#SBATCH -e job.err
#SBATCH -o job.out
#SBATCH -q normal
#SBATCH -t 00:30:00

module purge
module load ADFModelingSuite/2020.102-pc64-linux-intelmpi-bin
setenv I_MPI_FABRICS shm:ofa # Network fabric provided by the Open Fabrics Alliance (OFA)
setenv I_MPI_FALLBACK no # No fallback to ethernet

setenv NSCM $SLURM_NTASKS

./geometry_optimization.py