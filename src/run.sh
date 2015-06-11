#! /bin/bash

NRNIV="../specials/x86_64/special -mpi"
HOC_NAME="./main.hoc"

NRNOPT=\
" -c STOPTIME=100"\
" -c IS_SUPERCOMPUTER=0"

MPIEXEC="mpiexec -n 4"
#MPIEXEC=""

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
#mpiexec -np 8 ./mod/x86_64/special -mpi main.hoc
echo $EXEC
time $EXEC
