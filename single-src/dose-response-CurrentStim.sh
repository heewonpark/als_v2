#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../single-result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
SPIKE_DIR="${RESULT_DIR}${Time}/spike"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
mkdir -p ${SPIKE_DIR}

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./dose-response-CurrentStim.hoc"

NRNOPT=\
" -c STOPTIME=500"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c NCELL=500"

MPIEXEC="mpiexec -n 8"
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $NRNOPT
echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
python ./drawDoseResponse.py $SPIKE_DIR
