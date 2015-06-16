
#! /bin/sh

mpiexec -np 8 ../../specials/x86_64/special -mpi parallel_gaba_test.hoc
#../../specials/x86_64/special parallel_gaba_test.hoc
#mpiexec -np 2 python parallel_gap_sample.py
