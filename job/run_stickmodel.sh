#!/bin/bash -x
#PJM --rsc-list "node=1"
#PJM --rsc-list "elapse=00:05:00"
#PJM --rsc-list "rscgrp=small"
#PJM --mpi "proc=2"
#PJM -s

# staging
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

# CHANGE TO YOUR OWN DIR
#PJM --stgin-basedir /home/hp120263/k01793/code/al_V2/

#PJM --stgin "rank=* ./src/singlecmpt_test/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus/stgin/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus/specials/sparc64/special %r:./"

#PJM --stgout "rank=* %r:./*.txt /data/hp120263/park/record/%j/"

# SET UP ENVIRONMENT OF LANGUAGE 
. /work/system/Env_base

#--#export OMP_NUM_THREADS=8

NRNIV="./special -mpi"
#HOC_NAME="./main.hoc"
HOC_NAME="./parallel_gaba_test.hoc"
#NRNOPT=""
NRNOPT=\
" -c STOPTIME=5"\
" -c IS_SUPERCOMPUTER=1"

#LPG="lpgparm -t 4MB -s 4MB -d 4MB -h 4MB -p 4MB"
MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"

#PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
#PROF="fipp -C -Ihwm,call -d ./prof"
PROF=""

echo "${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
time ${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync


