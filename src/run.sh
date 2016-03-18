#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
SPIKE_DIR="${RESULT_DIR}${Time}/spike"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
mkdir -p ${SPIKE_DIR}

NRNIV="../specials/x86_64/special -mpi"
#HOC_NAME="./main_antenna.hoc"
HOC_NAME="./main.hoc"
#HOC_NAME="./ln_test.hoc"
#HOC_NAME="./main_test.hoc"
#HOC_NAME="./loadbalance_test.hoc"

NRNOPT=\
" -c STOPTIME=40"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c WEIGHT_200=0.05"\
" -c WEIGHT_300=0.004"\
" -c WEIGHT_301=0.008"\
" -c GABAA_GMAX_LTOL=5.0"\
" -c GABAB_GMAX_LTOL=5.0"\
" -c GABAA_GMAX_LTOP=0.2"\
" -c GABAB_GMAX_LTOP=0.0065"\       
" -c GABAB_ON=1"\
" -c GABAA_ON=1"

MPIEXEC="mpiexec -n 4"
#MPIEXEC="mpiexec -n 5"
#MPIEXEC="mpiexec -n 1"
#MPIEXEC=""

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
#mpiexec -np 8 ./mod/x86_64/special -mpi main.hoc
echo $EXEC
time $EXEC |tee $OUT

python drawGraph.py $RECORD_DIR
python drawISF.py $SPIKE_DIR
