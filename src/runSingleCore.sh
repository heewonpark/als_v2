
#! /bin/sh

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
./mod/x86_64/special -mpi main.hoc
