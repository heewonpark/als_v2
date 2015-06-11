#! /bin/bash

Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
BASE_DIR="../result/"
RECORD_DIR="${BASE_DIR}${Time}/record"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
