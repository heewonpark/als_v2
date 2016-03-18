#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing dose-response curve
#2015.04.01

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import re

import pickle

class Data():
    pcid = 0
    cellid = 0
    filename = ''

istims = []
spts = []
def readSpikeRecordFile(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()
    global interval, delay, size, tstop,istim1,istim2
    interval = int(data[0].split(":")[1])
    delay = float(data[1].split(":")[1])
    size = int(data[2].split(":")[1])
    tstop = int(data[3].split(":")[1])
    istim1 = float(data[4].split(":")[1])
    istim2 = float(data[5].split(":")[1])

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
    istims.append(istim1)
    spts.append(spt)
    return spt

peakISF = []
def drawDoseResponse():
    for spt in spts:
        maximum = 0
        for i in range(len(spt)-1):
            ISF = 1000/(spt[i+1]-spt[i])
            if(ISF>maximum):
                maximum = ISF
        peakISF.append(maximum)

    #fig = plt.figure()
    fig = plt.figure(figsize=(10,8),dpi=400)
    fig.subplots_adjust(bottom=0.2)
    ax1 = fig.add_subplot(111)
    #ax2 = ax1.twiny()
    # From fujiwara 2014
    X = [1,10,100,1000,5000]
    Y = [25,75,175,260,270]
    
    Z = []
    X1 = []
    for y in Y:
        #y = y * 170/270
        y = y
        Z.append(y)
        print y
    for x in X:
        #x = x * 100
        X1.append(x)
        print x
        
    #plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 20 #フォントサイズを設定
    #plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
    #plt.rcParams['xtics.major.size'] = 10 #x軸目盛りの長さ                                         
    #plt.rcParams['xtics.major.width'] = 1.5 #x軸目盛りの太さ     

    #ax2.plot(X1,Z,'r',label='Dose')
    #ax2.set_xscale('log')
    #ax2.set_xlim(0.1,10000)
    #ax2.set_xlabel("Dose[ng]")
    ax1.plot(istims,peakISF,"b.",label='Istim',linewidth=2.0)
    #ax1.set_xlim(100,1000000)
    ax1.set_xlim(0.1,1000)
    ax1.set_ylim(0,350)
    ax1.set_xscale('log')
    ax1.set_xlabel("Imax [nA]")
    ax1.set_ylabel("Peak ISF [Hz]")
    #ax1.set_legend()
    #ax2.set_legend()
    _SAVE_FIG_ = "%s/DoseResponseCurve.png"%target_dir
    #plt.title(_SAVE_FIG_)
    plt.savefig(_SAVE_FIG_)
    plt.show()

case = []
cellides = []
if len(sys.argv) is 2:
    if(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.dat'):
                    print full_dir                    
                    readSpikeRecordFile(full_dir)
        drawDoseResponse()


#f1 = open('istims.pkl','wb')
#pickle.dump(istims,f1)
#f1.close()

#f2 = open('peakISF.pkl','wb')
#pickle.dump(peakISF,f2)
#f2.close()
_SAVE_CSV_ = "%s/DoseResponse.csv"%target_dir
f = open(_SAVE_CSV_,'w')
for i in range(len(istims)):
    f.write("%f,%f\n"%(istims[i],peakISF[i]))
f.close()
