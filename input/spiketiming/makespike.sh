#! /bin/bash
a=0
while [ $a -ne 1000 ]
do
    echo "${a}"
    ipython mkSpikeTrains.py
    a=`expr $a + 1`
done
