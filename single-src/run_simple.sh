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
HOC_NAME="./main-test.hoc"


NRNOPT=\
" -c STOPTIME=6000"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c GABAB_ON=1"\
" -c GABAA_ON=1"\
" -c PTOL_ON=1"\
" -c NSYNAPSE=100"\
" -c NPN=1"\
" -c NLN=1"\
" -c NRN=100"\
" -c GABAA_LTOP=0.0"\
" -c GABAA_LTOL=0.0"\
" -c GABAB_LTOP=0.0"\
" -c GABAB_LTOL=0.0"\
" -c PN_NACH_GMAX=0.38"\
" -c LN_NACH_GMAX=0.10"\
" -c WEIGHT_RNtoPN=0.040"\
" -c WEIGHT_RNtoLN=0.018"\
" -c PtoL_NACH_GMAX=0.1"\
" -c DOSE=1000"\
" -c NSTIM=30"\
" -c PROB_LTOP=0.5"\
" -c PROB_LTOL=1.0"\
" -c PROB_PTOL=0.5"\
" -c RND_SEED=0"\
" -c JOBID=0"\
" -c RNtoLN_Latency=150"\
" -c VOLTAGERECORD=1"\
" -c CURRENTRECORD=0"


MPIEXEC="mpiexec -n 8"
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
#python ../src/drawISF.py $SPIKE_DIR
python ../src/spike_analyze.py $SPIKE_DIR
python ../src/whole_in_one_spike.py $SPIKE_DIR
