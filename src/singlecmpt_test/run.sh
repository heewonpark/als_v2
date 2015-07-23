#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="./result/"
RECORD_DIR="${RESULT_DIR}${Time}/"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}

NRNOPT=\
" -c STOPTIME=500"\
" -c IS_SUPERCOMPUTER=0"\
" -c START_TIME=${Time}"

#HOC_NAME="gaba_orn_test.hoc"
#HOC_NAME="netcon_gaba_test.hoc"
#HOC_NAME="couple_gaba.hoc"
HOC_NAME="Type2LN.hoc"
#EXEC="mpiexec -np 6 ../../specials/x86_64/special -mpi"
#EXEC="../../specials/x86_64/special -mpi"
EXEC="../../specials/x86_64/special"

echo "${EXEC} ${NRNOPT} ${HOC_NAME}"
time ${EXEC} ${NRNOPT} ${HOC_NAME}|tee ${OUT}

python ../drawGraph.py ${RECORD_DIR}
