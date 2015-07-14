#! /bin/bash

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./runtime_LN.hoc"
EXEC="${NRNIV} ${HOC_NAME}"
echo $EXEC
time $EXEC |tee $OUT
