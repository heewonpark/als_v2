
#! /bin/sh

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
mpiexec -np 4 nrniv -mpi main.hoc
