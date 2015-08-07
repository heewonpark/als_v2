#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
oecho "TIME : ${Time}"
RESULT_DIR="../single-result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
SPIKE_DIR="${RESULT_DIR}${Time}/spike"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
mkdir -p ${SPIKE_DIR}

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./main.hoc"

NRNOPT=\
" -c STOPTIME=12010"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c GABAB_ON=1"\
" -c GABAA_ON=1"\
" -c NSYNAPSE=100"\
" -c NPN=50"\
" -c NLN=350"\
" -c NRN=2000"\
" -c WEIGHT_RNtoPN=0.10"\
" -c WEIGHT_RNtoLN=0.02"\
" -c GABAA_LTOP=9.0"\
" -c GABAA_LTOL=1.0"\
" -c GABAB_LTOP=20.0"\
" -c GABAB_LTOL=1.5"

MPIEXEC="mpiexec -n 8"

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
python ../src/drawISF.py $SPIKE_DIR
