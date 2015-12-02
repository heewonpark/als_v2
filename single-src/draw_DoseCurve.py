#! /usr/bin/python
# coding: UTF-8

# 2015.11.19

#----------------------------------------------------
#This Program is for drawing graph of Dose-response curve
#
#
#
#
#
#
#----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import re

from spike_data import Spike_Data

data = []
pattern = re.compile(r'Spikerecord_PN_Dose(?P<dose>\d+)_(?P<id>\d+).dat')
pattern2 = re.compile(r'Spikerecord_LN_Dose(?P<dose>\d+)_(?P<id>\d+).dat')

if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        sd = Spike_Data()
        sd.Read(sys.argv[1])
        sd.calc_iFreq()
        sd.calc_avgFreq()
        print sd.peakFreq, sd.avgFreq
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.dat'):
                    #print "!!!!!",ext
                    if '_PN_' in full_dir:
                        print full_dir                    
                        result = pattern.search(fname)
                        dose=result.group('dose')
                        sd = Spike_Data()
                        sd.Read(full_dir)
                        sd.calc_iFreq()
                        sd.calc_avgFreq()
                        print sd.peakFreq, sd.avgFreq
                        data.append([int(dose), sd.peakFreq, sd.avgFreq])
                        sd = None
                    elif '_LN##_' in full_dir:
                        print full_dir                    
                        result = pattern2.search(fname)
                        freq=result.group('dose')
                        sd = Spike_Data()
                        sd.Read(full_dir)
                        sd.calc_iFreq()
                        sd.calc_avgFreq()
                        print sd.peakFreq, sd.avgFreq
                        data.append([int(freq), sd.peakFreq, sd.avgFreq])
                        sd = None

    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"

print data
data = np.array(data)
print len(data)

for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        #print data[i][0], data[j][0]
        temp = np.copy(data[i])
        #print temp
        if(data[i][0] > data[j][0]):
            data[i] = data[j]
            #print temp
            data[j] = temp
            #print temp, data[i], data[j]
print data
print data.T
transpose_data = data.T
wfilename="%s/DoseCurve.csv"%(target_dir)
fh = open(wfilename,"wb")
writer = csv.writer(fh)
for d in data:
    writer.writerow(d)

fig1 = plt.figure()
plt.plot(transpose_data[0],transpose_data[1])
plt.xlim(1,100000)
plt.ylim(0,350)
plt.xscale('log')
plt.title('Peak Frequency')
fig1name="%s/DoseCurve_peak.png"%(target_dir)

fig1.savefig(fig1name)

fig2 = plt.figure()
plt.plot(transpose_data[0],transpose_data[2])
plt.xlim(1,100000)
plt.ylim(0,350)
plt.xscale('log')
plt.title('Average Frequency')

fig2name="%s/DoseCurve_avgFreq.png"%(target_dir)
fig2.savefig(fig2name)

plt.show()


