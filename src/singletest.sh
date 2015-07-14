#! /bin/bash

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./singletest.hoc"
EXEC="${NRNIV} ${HOC_NAME}"
echo $EXEC
time $EXEC |tee $OUT
