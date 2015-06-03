#!/bin/bash -x
#PJM --rsc-list "node=2"
#PJM --rsc-list "elapse=00:05:00"
#PJM --rsc-list "rscgrp=small"
#--PJM --rsc-list "rscgrp=debug"
#PJM --mpi "proc=16"
#PJM -s

# staging
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

# CHANGE TO YOUR OWN DIR
#PJM --stgin-basedir /home/hp120263/k01793/code/al_V2/

#PJM --stgin "rank=* ./input/* %r:../input/"
#PJM --stgin "rank=* ./input/network_info/* %r:../input/network_info/"
#PJM --stgin "rank=* ./input/spiketiming/* %r:../input/spiketiming/"
#PJM --stgin "rank=* ./input/swc/* %r:../input/swc/"
#PJM --stgin "rank=* ./input/swc/rn0514/* %r:../input/swc/rn0514/"
#PJM --stgin "rank=* ./input/synapse_info/* %r:../input/synapse_info/"
#PJM --stgin "rank=* ./input/synapse_info/syn/* %r:../input/synapse_info/syn/"
#PJM --stgin "rank=* ./input/synapse_list/* %r:../input/synapse_list/"
#PJM --stgin "rank=* ./input/synapse_list/fromRN/* %r:../input/synapse_list/fromRN/"

#PJM --stgin "rank=* ./src/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus/stgin/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus/specials/sparc64/special %r:./"

#PJM --stgout "rank=* %r:./*.txt /data/hp120263/park/record/%j/"
#PJM --stgout "rank=* %r:./record/* /data/hp120263/park/result/%j/"
#PJM --stgout "rank=* %r:./result/record/* /data/hp120263/park/result/record/%j/"

# SET UP ENVIRONMENT OF LANGUAGE 
. /work/system/Env_base

#export OMP_NUM_THREADS=8

NRNIV="./special -mpi"
HOC_NAME="./main.hoc"
#NRNOPT=""
NRNOPT=\
" -c STOPTIME=300"\
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


