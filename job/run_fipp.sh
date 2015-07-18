#!/bin/bash -x
#PJM --rsc-list "node=1"
#PJM --rsc-list "elapse=24:00:00"
#PJM --rsc-list "rscgrp=small"
#PJM --mpi "proc=1"
#PJM -s

# staging
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

# CHANGE TO YOUR OWN DIR
#PJM --stgin-basedir /home/hp120263/k01793/code/al_V2/

#PJM --stgin "rank=* ./input/* %r:../input/"
#PJM --stgin "rank=* ./input/network_info/* %r:../input/network_info/"
#PJM --stgin "rank=* ./input/spiketiming/* %r:../input/spiketiming/"
#--#PJM --stgin "rank=* ./input/spiketiming/40stim/* %r:../input/spiketiming/40stim/"
#PJM --stgin "rank=* ./input/swc/* %r:../input/swc/"
#PJM --stgin "rank=* ./input/swc/rn0514/* %r:../input/swc/rn0514/"
#PJM --stgin "rank=* ./input/synapse_info/* %r:../input/synapse_info/"
#PJM --stgin "rank=* ./input/synapse_info/40cells/* %r:../input/synapse_info/40cells/"
#PJM --stgin "rank=* ./input/synapse_info/8cells/* %r:../input/synapse_info/8cells/"
#PJM --stgin "rank=* ./input/synapse_list/* %r:../input/synapse_list/"
#PJM --stgin "rank=* ./input/synapse_list/fromRN/* %r:../input/synapse_list/fromRN/"

#PJM --stgin "rank=* ./src/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus_devel/stgin/* %r:./"
#PJM --stgin "rank=* ../../github/neuron_kplus_devel/specials/sparc64/special %r:./"

#PJM --stgout "rank=* %r:./*.txt /data/hp120263/park/al_V2/%j/record/"
#PJM --stgout "rank=* %r:./*.dat /data/hp120263/park/al_V2/%j/spike/"
#PJM --stgout "rank=* %r:./*.hoc /data/hp120263/park/al_V2/%j/src/"
#PJM --stgout "rank=* %r:./pd/* /data/hp120263/park/al_V2/%j/pd/"

# SET UP ENVIRONMENT OF LANGUAGE 
. /work/system/Env_base

#--#export OMP_NUM_THREADS=8

NRNIV="./special -mpi"
#HOC_NAME="./main.hoc"
HOC_NAME="./loadbalance_test.hoc"
#NRNOPT=""
NRNOPT=\
" -c STOPTIME=20"\
" -c IS_SUPERCOMPUTER=1"\
" -c INTERVAL=1200"\
" -c WEIGHT_200=0.350"\
" -c WEIGHT_300=0.008"\
" -c WEIGHT_301=0.002"\
" -c GMAX_LTOL=5.0"\
" -c GMAX_LTOP=0.07"

LPG="lpgparm -t 4MB -s 4MB -d 4MB -h 4MB -p 4MB"
MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"

#PROF="fapp -C -d ./pd -L1 -Hevent=Statistics"
#PROF="fapp -C -d ./pd -Ihwm -Hevent=Performance"
#PROF="fapp -C -d ./pd -Ihwm -Hevent=Statistics"
PROF="fipp -C -Srange -Ihwm,call -d ./pd"
#PROF=""

echo "${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
time ${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync