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
HOC_NAME="./dose-response-SingleCore.hoc"

NRNOPT=\
" -c STOPTIME=2500"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"\
" -c NCELL=1"\
" -c NRN=1"\
" -c CELL_bATYPE=1"\
" -c WEIGHT_RNtoPN=0.50"\
" -c WEIGHT_RNtoLN=0.02"\
" -c PN_NACH_GMAX=0.3"\
" -c RND_SEED=0"

MPIEXEC="mpiexec -n 1"
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $NRNOPT
echo $EXEC
time $EXEC |tee $OUT

python ../src/drawGraph.py $RECORD_DIR
#python ../src/drawISF.py $SPIKE_DIR
python ../src/spike_analyze.py $SPIKE_DIR
#python ../src/whole_in_one_spike.py $SPIKE_DIR
python ./draw_DoseCurve.py $SPIKE_DIR
#python ./draw_FreqCurve.py $SPIKE_DIR
