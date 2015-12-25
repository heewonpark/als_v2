#! /usr/bin/python
# coding: UTF-8

# 2015.12.15

#----------------------------------------------------
#
#
#----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path

DATA = []
DOSE = []
LATENCY=[]
if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.txt'):
                    #print "!!!!!",ext
                    if 'Latencies' in full_dir:
                        print full_dir                    
                        dose,latency = np.loadtxt(full_dir,skiprows=1,unpack=True)
                        #DOSE=DOSE+dose
                        DOSE.extend(dose)
                        #LATENCY.append(latency)
                        #LATENCY=LATENCY+latency
                        LATENCY.extend(latency)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"

DOSE = np.array(DOSE)
LATENCY = np.array(LATENCY)
DATA.append(DOSE)
DATA.append(LATENCY)
#print DATA
DATA = np.array(DATA)
DATAT = DATA.T
#print DATA.T

for i in range(len(DATAT)-1):
    for j in range(i+1,len(DATAT)):
        temp = np.copy(DATAT[i])
        if(DATAT[i][0]>DATAT[j][0]):
            DATAT[i] = DATAT[j]
            DATAT[j] = temp

DATAT=np.array(DATAT)
#print DATAT
divid=[[] for i in range(10)]
NRN = 100
for i in range(len(DATAT)):
    #print i
    divid[int(i/NRN)].append(DATAT[i])

divid = np.array(divid)
#print divid

average = []
for div in divid:
    div_ = np.array(div)
    div_ = div_.T
    x    = div_[0][0]
    avg  = np.average(div_[1])
    average.append([x,avg])

#print average
average = np.array(average)
average = average.T
#print DOSE
#print LATENCY
fig = plt.figure()
plt.plot(DOSE,LATENCY,".")
plt.plot(average[0],average[1],"-")
plt.xlim(0,5)
plt.ylim(0.0,0.3)
FIG_NAME = "%s/Latency.png"%(target_dir)
plt.savefig(FIG_NAME)
#plt.show()
