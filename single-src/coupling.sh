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
HOC_NAME="./coupling.hoc"

NRNOPT=\
" -c START_TIME=${Time}"

#MPIEXEC="mpiexec -n 8"
MPIEXEC=""
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $NRNOPT
echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
#python ./butterworth.py $RECORD_DIR
#python ./NetCon_PSTH.py $SPIKE_DIR
##python ../src/drawISF.py $SPIKE_DIR
#python ../src/spike_analyze.py $SPIKE_DIR
##python ../src/whole_in_one_spike.py $SPIKE_DIR
#python ./draw_DoseCurve.py $SPIKE_DIR
#python ./draw_FreqCurve.py $SPIKE_DIR
