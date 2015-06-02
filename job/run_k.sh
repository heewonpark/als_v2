#!/bin/bash -x
#PJM --rsc-list "node=8"
#PJM --rsc-list "elapse=00:10:00"
#PJM --rsc-list "rscgrp=small"
#PJM --mpi "proc=64"
#PJM -s

# staging
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

# CHANGE TO YOUR OWN DIR
#PJM --stgin-basedir /home/hp120263/k01793/

#--PJM --stgout "rank=* %r:./prof/* /data/hp120263/k01793/result/prof/%j/"

#--PJM --stgin "rank=* ./stgin/* %r:./"
#PJM --stgin "rank=* $KPLUS/sparc64/special %r:./"
#PJM --stgin "rank=* ./hoc/* %r:./"


. /work/system/Env_base

#export OMP_NUM_THREADS=8

NRNIV="$KPLUS/specials/sparc64/special -mpi"
HOC_NAME="../main.hoc"
#NRNOPT=""

LPG="lpgparm -t 4MB -s 4MB -d 4MB -h 4MB -p 4MB"
MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"

#PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
#PROF="fipp -C -Ihwm,call -d ./prof"
PROF=""

echo "${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
time ${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync


