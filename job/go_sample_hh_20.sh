#!/bin/bash -x
#
#PJM --rsc-list "rscgrp=small"
#PJM --rsc-list "node=2"
#PJM --mpi "shape=1"
#PJM --mpi "proc=8"
#PJM --rsc-list "elapse=00:10:00"

#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

#PJM --stgin "rank=* ../bin/estimation_main %r:./"
#PJM --stgin "rank=* ../src/*.par %r:./"
#PJM --stgin "rank=* ../../data/targetdata/sample_hh/* %r:./"
#PJM --stgin "rank=0 ../hoc/* %r:../"
#PJM --stgin "rank=0 /home/hp120263/k01480/neuron_kplus/specials/sparc64/special %r:../"
#--PJM --stgin "rank=0 /home/e16003/neuron_kplus/specials/sparc64/special %r:../"
#PJM --stgin "rank=0 ../../data/targetdata/sample_hh/* %r:../"
#PJM --stgin "rank=0 ../../data/swc/*.swc %r:../"

#--PJM --stgout "rank=0 %r:../*.dat ./"
#PJM --stgout "rank=0 %r:./*.dat ../../data/estimation_results/sample_hh/%j/"

#PJM -s
#--PJM -m "e"
#

. /work/system/Env_base
export FLIB_CNTL_BARRIER_ERR=FALSE
#export OMP_NUM_THREADS=16

EXECFILE="./estimation_main"
GENE_NUM="8"
MU="-1" # -1 defaults (1/2 of GENE_NUM)
MAXITER="10"
MAXEVAL="-1"
NUM_NRN_PROC="8"
HOCFILE="./spikegen_hh_k.hoc"
#NRNIV="./nrniv"
NRNIV="./special"
NRNOPT="{}"
SETTINGFILE_SUFFIX=20
WEIGHT_FIT=1
INITFILE="./cmaes_initials.par"

#MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"
MPIEXEC="mpiexec"

# PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
# PROF="fipp -C -Ihwm,call -d ./prof -i10 -Srange"
PROF=""

time ${PROF} ${MPIEXEC} ${EXECFILE} ${GENE_NUM} ${MAXITER} ${MAXEVAL} ${SETTINGFILE_SUFFIX} ${NUM_NRN_PROC} ${HOCFILE} ${NRNIV} ${NRNOPT} ${WEIGHT_FIT} ${MU} ${INITFILE}
# time ./special ./multi_hh.py -nobanner -nogui -python
# time ./special ./multi_hh.hoc -nobanner -nogui
# cd ..
# time ${NRNIV} ${HOCFILE} -nobanner -nogui

