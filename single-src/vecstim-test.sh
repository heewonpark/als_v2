#! /bin/bash

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./vecstim-test.hoc"

#MPIEXEC="mpiexec -n 8"
MPIEXEC=""
EXEC="${MPIEXEC} ${NRNIV} ${HOC_NAME}"

echo $EXEC
$EXEC

python ../src/drawGraph.py "./"
