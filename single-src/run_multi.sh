#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../single-result/"
RECORD_DIR10="${RESULT_DIR}${Time}/record/10/"
RECORD_DIR100="${RESULT_DIR}${Time}/record/100/"
RECORD_DIR1000="${RESULT_DIR}${Time}/record/1000/"
SPIKE_DIR10="${RESULT_DIR}${Time}/spike/10/"
SPIKE_DIR100="${RESULT_DIR}${Time}/spike/100/"
SPIKE_DIR1000="${RESULT_DIR}${Time}/spike/1000/"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR10}
mkdir -p ${RECORD_DIR100}
mkdir -p ${RECORD_DIR1000}
mkdir -p ${SPIKE_DIR10}
mkdir -p ${SPIKE_DIR100}
mkdir -p ${SPIKE_DIR1000}

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./main-multi-dose.hoc"


NRNOPT=\
" -c STOPTIME=3000"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c GABAB_ON=1"\
" -c GABAA_ON=1"\
" -c PTOL_ON=1"\
" -c NSYNAPSE=350"\
" -c NPN=10"\
" -c NLN=70"\
" -c NRN=0"\
" -c GABAA_LTOP=18.0"\
" -c GABAA_LTOL=0.0"\
" -c GABAB_LTOP=22.0"\
" -c GABAB_LTOL=0.7"\
" -c PN_NACH_GMAX=0.38"\
" -c LN_NACH_GMAX=0.10"\
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

python ../src/drawGraph.py $RECORD_DIR10
python ../src/drawGraph.py $RECORD_DIR100
python ../src/drawGraph.py $RECORD_DIR1000
##python ../src/drawISF.py $SPIKE_DIR
python ../src/spike_analyze.py $SPIKE_DIR10
python ../src/spike_analyze.py $SPIKE_DIR100
python ../src/spike_analyze.py $SPIKE_DIR1000
python ../src/whole_in_one_spike.py $SPIKE_DIR10
python ../src/whole_in_one_spike.py $SPIKE_DIR100
python ../src/whole_in_one_spike.py $SPIKE_DIR1000
