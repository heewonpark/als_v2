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
" -c STOPTIME=72000"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c GABAB_ON=1"\
" -c GABAA_ON=1"\
" -c PTOL_ON=1"\
" -c NSYNAPSE=100"\
" -c NPN=5"\
" -c NLN=35"\
" -c NRN=200"\
" -c WEIGHT_RNtoPN=0.15"\
" -c WEIGHT_RNtoLN=0.020"\
" -c GABAA_LTOP=1.5"\
" -c GABAA_LTOL=0.1"\
" -c GABAB_LTOP=20.0"\
" -c GABAB_LTOL=0.03"\
" -c DOSE=100"\
" -c NSTIM=30"\
" -c PROB_LTOP=0.5"\
" -c PROB_LTOL=1.0"\
" -c PROB_PTOL=0.5"\
" -c WEIGHT_PTOL=0.12"\
" -c RND_SEED=1"


MPIEXEC="mpiexec -n 8"
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
#python ../src/drawISF.py $SPIKE_DIR
python ../src/spike_analyze.py $SPIKE_DIR
python ../src/whole_in_one_spike.py $SPIKE_DIR
