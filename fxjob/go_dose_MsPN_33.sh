#!/bin/bash -x
#
#PJM --rsc-list "rscgrp=fx-middle"
#PJM --rsc-list "node=9"
#PJM --mpi "shape=1"
#PJM --mpi "proc=32"
#PJM --rsc-list "elapse=12:00:00"

#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

#PJM -s

. /work/system/Env_base
export FLIB_CNTL_BARRIER_ERR=FALSE
#export OMP_NUM_THREADS=16

EXECFILE="/home/usr7/z48927t/github/estimator_park/estimation/bin/estimation_main"
GENE_NUM="256"
MU="-1" # -1 defaults (1/2 of GENE_NUM)
MAXITER="200"
MAXEVAL="-1"
NUM_NRN_PROC="256"
HOCFILE="./dose-response-estimator.hoc"
#NRNIV="./nrniv"
#NRNIV="./special"
NRNIV="/home/usr7/z48927t/github/neuron_kplus72/specials/sparc64/special"
NRNOPT="{}"
SETTINGFILE_SUFFIX=10
WEIGHT_FIT=1
INITFILE="/home/usr7/z48927t/github/estimator_park/estimation/src/cmaes_initials.par"
#INITFILE="./cmaes_initials.par"

#MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"
MPIEXEC="mpiexec"

# PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
# PROF="fipp -C -Ihwm,call -d ./prof -i10 -Srange"
PROF=""

time ${PROF} ${MPIEXEC} ${EXECFILE} ${GENE_NUM} ${MAXITER} ${MAXEVAL} ${SETTINGFILE_SUFFIX} ${NUM_NRN_PROC} ${HOCFILE} ${NRNIV} ${NRNOPT} ${WEIGHT_FIT} ${MU} ${INITFILE}