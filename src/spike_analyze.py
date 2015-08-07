#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing graph of peak ISF and spike counts
#
# How to use this program
# $ipython drawGraph.py filenames
# $ipython drawGraph.py directory
# comment added 2015.03.30
#-------------------------------------------------

#2015.03.31
#CSVファイル作成機能追加

#2015.05.17 X range chaned [1:-1]
#2015.05.17 fontsize is changed

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import matplotlib
matplotlib.rc('xtick',labelsize = 15)
matplotlib.rc('ytick',labelsize = 15)


interval = -1
delay = -1
size = -1
tstop = -1
def readSpikeRecordFile(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()
    global interval, delay, size, tstop,istim1,istim2
    interval = int(data[0].split(":")[1])
    delay = float(data[1].split(":")[1])
    size = int(data[2].split(":")[1])
    tstop = int(data[3].split(":")[1])
    istim1 = int(data[4].split(":")[1])
    #istim2 = int(data[5].split(":")[1])
    istim2 = float(data[5].split(":")[1])
    #interval = 1200
    print "Interval : %d, Delay : %f, number of data : %d, tstop : %d"%(interval, delay, size, tstop)
    spt = [] #spike timing
    for i in range(len(data)):
        if(data[i][0]!='$'):
            time = data[i].rstrip('\n')
            #print time
            #spt.append(float(time))
            try :
                spt.append(float(time))
            except ValueError:
                pass
    #print spt
    return spt

def reconstruct_data(spt):
    num = int(math.ceil(float(tstop)/float(interval)))
    #print num, float(tstop)/float(interval)
    #print "Interval : %d, Delay : %f, number of data : %d, tstop : %d"%(interval, delay, size, tstop)
    pulses = [[] for i in range(num+1)]
    cnt = 0
    #print "len(spt) ",len(spt)
    for i in range(0,num+1):
        j=0
        if(cnt>=len(spt)):
            #print "break"
            break
        #print "cnt ", cnt
        #print "spt[cnt]",spt[cnt]
        #print delay+float(interval*i)
        
        while(spt[cnt]<(delay+float(interval*i))):
            pulses[i].append(spt[cnt])
            cnt +=1
            if(cnt>=len(spt)):
                #print "break"
                break
            j+=1

    cnt2 = 0
    for j in range(len(pulses)):
        #print pulses[j]
        cnt2 += len(pulses[j])
    #Error check
    #print cnt2
    if(size != cnt2):
        print "Reconstruct_data ERROR"
        return 

    return pulses
   
def drawSpikeCounts(pulses,filename,show):
    fig = plt.figure()
    i = [ j for j in range(len(pulses))]
    #print "i",i, len(pulses[1])
    length = [ len(pulses[j]) for j in range(len(pulses))]
    #print length
    tmp = filename.rsplit('.',1)
    csvfilename = "%s_spikecounts.csv"%tmp[0]
    f = open(csvfilename,'wb')
    writer = csv.writer(f)
    writer.writerow([istim1,istim2])
    for k in range(len(i)):
        writer.writerow([i[k],length[k]])

    f.close()
    plt.plot(i[1:-1],length[1:-1])
    plt.xlabel("stimulus pulse number",fontsize=15)
    plt.ylabel("Spike Counts[spikes]",fontsize=15)
    plt.ylim(0,50)
    tmp = filename.rsplit('.',1)
    imgFilename = "%s_spikecounts.png"%tmp[0]
    plt.savefig(imgFilename)
    if(show == True):
        plt.show()
    plt.close()
    

def drawPeakISF(pulses,filename,show):
    fig = plt.figure()
    peakISF = [None for i in range(len(pulses))]
    x = [i for i in range(len(pulses))]
    for i in range(len(pulses)):
        if(len(pulses[i])==0):
           peakISF[i]=0
        
        maximum = 0
        for j in range(len(pulses[i])-1):
           ISF = 1000/(pulses[i][j+1]-pulses[i][j])
           if(ISF>maximum):
               maximum = ISF
        peakISF[i] = maximum

    tmp = filename.rsplit('.',1)
    csvfilename = "%s_peakISF.csv"%tmp[0]
    f = open(csvfilename,'wb')
    writer = csv.writer(f)
    writer.writerow([istim1,istim2])
    print len(x)
    for i in range(len(x)):
        writer.writerow([x[i],peakISF[i]])
    f.close()
   
    plt.plot(x[1:-1], peakISF[1:-1])
    plt.ylabel("peak ISF[Hz]",fontsize=15)
    plt.xlabel("stimulus pulse number",fontsize=15)
    plt.ylim(0,300)
    imgFilename = "%s_PeakISF.png"%tmp[0]
    plt.savefig(imgFilename)
    if(show == True):
        plt.show()
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
                    s = readSpikeRecordFile(full_dir)
                    Pulses = reconstruct_data(s)
                    drawSpikeCounts(Pulses,full_dir,0)
                    drawPeakISF(Pulses,full_dir,0)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"


