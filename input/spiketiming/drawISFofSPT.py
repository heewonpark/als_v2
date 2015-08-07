#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing graph of ISF
#
#-------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import matplotlib
matplotlib.rc('xtick',labelsize = 15)
matplotlib.rc('ytick',labelsize = 15)


interval = -1
delay = -1
size = -1
tstop = -1
# spt : spike timing
def readSpikeRecordFile(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()

    spt = [] #spike timing
    for i in range(len(data)-1):
        if(data[i][0]!='$'):
            time = data[i].rstrip('\n')
            #print time
            #spt.append(float(time))
            try :
                spt.append(float(time))
            except ValueError:
                pass

    #print spt
    datafile.close()
    return spt
  
def drawISF(filename):
    spt = readSpikeRecordFile(filename)
    freqs = []
    times = []
    freq = 0
    #print spt
    for i in range(len(spt)):
        if(i>0):
            freq = 1/(spt[i]-spt[i-1])
            time = (spt[i]+spt[i-1])/2
            #print time, freq
            freqs.append(freq)
            times.append(time)
    plt.plot(times,freqs)
    plt.xlabel("Spike timing[ms]",fontsize=15)
    plt.ylim(0,300)
    plt.ylabel("ISF[Hz]",fontsize=15)
    tmp = filename.rsplit('.',1)
    imgFilename = "%s_ISF.png"%tmp[0]
    plt.savefig(imgFilename)
    plt.close()

"""
s = readSpikeRecordFile("./spikerecord/spikerecord_BALPN0.dat")
Pulses = reconstruct_data(s)
drawSpikeCounts(Pulses)
drawPeakISF(Pulses)
"""

if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        s = readSpikeRecordFile(sys.argv[1])
        Pulses = reconstruct_data(s)
        drawSpikeCounts(Pulses,sys.argv[1],1)
        drawPeakISF(Pulses,sys.argv[1],1)
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.dat'):
                    print full_dir                    
                    #s = readSpikeRecordFile(full_dir)
                    drawISF(full_dir)
                    
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"


