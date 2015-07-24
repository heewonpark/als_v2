#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./main.hoc"
#HOC_NAME="./loadbalance_test.hoc"

NRNOPT=\
" -c STOPTIME=200"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c WEIGHT_200=0.05"\
" -c WEIGHT_300=0.05"\
" -c WEIGHT_301=0.008"\
" -c GMAX_LTOL=5.0"\
" -c GMAX_LTOP=0.6"\
" -c GABAB_ON=0"\
" -c GABAA_ON=1"

#MPIEXEC="mpiexec -n 4"
MPIEXEC="mpiexec -n 8"
#MPIEXEC=""

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
#mpiexec -np 8 ./mod/x86_64/special -mpi main.hoc
echo $EXEC
time $EXEC |tee $OUT

python drawGraph.py $RECORD_DIR
