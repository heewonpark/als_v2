#!/bin/bash -x
#
#PJM --rsc-list "rscgrp=small"
#PJM --rsc-list "node=33"
#PJM --mpi "shape=1"
#PJM --mpi "proc=8"
#PJM --rsc-list "elapse=02:00:00"

#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

#PJM --stgin-basedir /home/hp120263/k01793/code/al_V2/
#PJM --stgin "rank=* /home/hp120263/k01793/github/estimator_park/estimation/bin/estimation_main %r:./"
#PJM --stgin "rank=* /home/hp120263/k01793/github/estimator_park/estimation/src/*.par %r:./"
#PJM --stgin "rank=* ./input/estimation_data/* %r:./"
#PJM --stgin "rank=0 ./single-src/* %r:../"
#PJM --stgin "rank=0 ./src/* %r:../"

#PJM --stgin "rank=* ./input/spiketiming/5000dose_1stims_filtering/* %r:../input/spiketiming/5000dose_1stims_filtering/"
#PJM --stgin "rank=* ./input/spiketiming/1000dose_1stims_filtering/* %r:../input/spiketiming/1000dose_1stims_filtering/"
#PJM --stgin "rank=* ./input/spiketiming/1000dose_1stims_filtering/* %r:../input/spiketiming/1000dose_1stims_filtering_adaptation/"
#PJM --stgin "rank=* ./input/spiketiming/100dose_1stims_filtering/* %r:../input/spiketiming/100dose_1stims_filtering/"
#PJM --stgin "rank=* ./input/spiketiming/10dose_1stims_filtering/* %r:../input/spiketiming/10dose_1stims_filtering/"

#PJM --stgin "rank=0 /home/hp120263/k01793/github/neuron_kplus72/specials/sparc64/special %r:../"
#--PJM --stgin "rank=0 /home/e16003/neuron_kplus/specials/sparc64/special %r:../"
#PJM --stgin "rank=0 ./input/estimation_data/* %r:../"
#PJM --stgin "rank=* /home/hp120263/k01793/github/neuron_kplus72/stgin/* %r:../"

#PJM --stgout "rank=* %r:./*.dat /data/hp120263/park/estimation/dose_MsPN/%j/"

#PJM -s

. /work/system/Env_base
export FLIB_CNTL_BARRIER_ERR=FALSE
#export OMP_NUM_THREADS=16

EXECFILE="./estimation_main"
GENE_NUM="256"
MU="-1" # -1 defaults (1/2 of GENE_NUM)
MAXITER="50"
MAXEVAL="-1"
NUM_NRN_PROC="256"
HOCFILE="./dose-response-estimator4_5s.hoc"
#NRNIV="./nrniv"
NRNIV="./special"
NRNOPT="{}"
SETTINGFILE_SUFFIX=10
WEIGHT_FIT=1
INITFILE="./cmaes_initials.par"

#MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"
MPIEXEC="mpiexec"

# PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
# PROF="fipp -C -Ihwm,call -d ./prof -i10 -Srange"
PROF=""

time ${PROF} ${MPIEXEC} ${EXECFILE} ${GENE_NUM} ${MAXITER} ${MAXEVAL} ${SETTINGFILE_SUFFIX} ${NUM_NRN_PROC} ${HOCFILE} ${NRNIV} ${NRNOPT} ${WEIGHT_FIT} ${MU} ${INITFILE}