#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing graph of peak ISF and spike counts
#2015.04.01

# Single Antennal lobe simulationのデータ解析で使えるように改良中

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import re

clist = [[] for _ in range(8)]
clist[0] = 'b'
clist[1] = 'g'
clist[2] = 'r'
clist[3] = 'c'
clist[4] = 'm'
clist[5] = 'y'
clist[6] = 'k'
clist[7] = '#77ff77'

class Data():
    gid=-1    
    filename = ''

case0 = []
gides0=[]

case1 = []
gides1 = []

if len(sys.argv) is 2:
    if(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                if('PN' in fname)&('peakISF.csv' in fname):
                    print fname
                    p = re.compile(r'Spikerecord_PN(\d+)_peakISF.csv')
                    print p
                    a = p.search(fname)
                    print a
                    gid = a.groups()
                    print gid
                    gid = int(gid[0])
                    d = Data()
                    d.gid = gid
                    d.filename= full_dir
                    case0.append(d)
                    if(gid in gides0)==False:
                        gides0.append(gid)
                        #print cellid
                elif('PN' in fname)&('spikecounts.csv' in fname):
                    print fname
                    p1 = re.compile(r'Spikerecord_PN(\d+)_spikecounts.csv')
                    a1 = p1.search(fname)
                    gid1 = a1.groups()
                    
                    gid1 = int(gid1[0])
                   
                    d1 = Data()
                    d1.gid = gid1
                    d1.filename= full_dir
                    case1.append(d1)
                    if(gid1 in gides1)==False:
                        gides1.append(gid1)
                        #print cellid1

                    
def drawPeakISFAllinOne():
    wholedata = [[] for _ in range(len(gides0))]
    istim1 =[0 for _ in range(len(gides0))]
    istim2 =[0 for _ in range(len(gides0))]

    for i in range(len(gides0)):
        print "i ", i
        rowdata=[[] for _ in range(len(gides0))]
        for c in case0:
            if(c.gid == gides0[i]):
                print c.filename,c.gid
                f = open(c.filename,'rb')
                reader = csv.reader(f)
                """
                istim1 = reader[0][0]
                istim2 = reader[0][1]
                for row in range(1,len(reader)):
                    rowdata[c.pcid][row]=reader[row][1]
                
                """
                
                row = reader.next()
                istim1[c.gid] = row[0]
                istim2[c.gid] = row[1]
                #print "istim",istim1,istim2
                for row in reader:
                    #print "print ",row[1]
                    #rowdata[c.gid].append(float(row[1]))
                    rowdata[0].append(float(row[1]))
                    wholedata[c.gid].append(float(row[1]))
                f.close()
        
        fig = plt.figure(figsize=(10,5.0))
        x = [j for j in range(len(rowdata[0]))]
        #plt.plot(x[1:20],rowdata[0][1:20],color='r')
        #plt.plot(x[1:20],rowdata[1][1:20],color='b')
        #plt.plot(x[1:20],rowdata[2][1:20],color='g')
        #print x
        print rowdata[0]
        plt.plot(x[1:],rowdata[0][1:],color='r')

        #for k in range(0,len(rowdata)):
            #if(len(rowdata[k])!=0):
                #Label = "I1=%d, I2=%d"%(int(istim1[k]),int(istim2[k]))
                #plt.plot(x[21:-1],rowdata[k][21:-1],label = Label)
                #Label = "P(LN-PN):%.1f"%((k+1)*0.2)
                #Label = "Gmax:%.1f"%((k+1)*0.5)
                #plt.plot(x[1: 20],rowdata[k][1: 20],color =clist[k],label = Label)
                #plt.plot(x[21:-1],rowdata[k][21:-1],color =clist[k])
                #plt.plot(x[1:31],rowdata[k][1:31],color =clist[k])

        #plt.plot(x[1:20],rowdata[0][1:20])
        #for k in range(1,len(rowdata)):
            #if(len(rowdata[k])!=0):
                #Label = "I1=%d, I2=%d"%(int(istim1[k]),int(istim2[k]))
                #plt.plot(x[21:-1],rowdata[k][21:-1],label = Label)
                #plt.plot(x[21:-1],rowdata[k][21:-1])
                #sdw= 0
        plt.ylabel("peak ISF[Hz]")
        plt.xlabel("stimulus pulse number")

        plt.legend(loc=0)
        imgFilename = "%speakISFAllinOne%d.png"%(sys.argv[1],gides0[i])
        plt.savefig(imgFilename)
        plt.close()
    
    fig2 = plt.figure(figsize=(10,5.0))
    print wholedata[0]
    print len(wholedata[0])
    avg = [0 for i in range(len(wholedata[0]))]
    for i in range(len(wholedata)):
        for j in range(len(wholedata[i])):
            avg[j] +=wholedata[i][j]
    for i in range(len(avg)):
        avg[i] = avg[i]/len(gides0)
    print "AVG"
    print avg
    #wholedata = wholedata/len(gides0)
    print "WHOLE"
    print wholedata
    x_whole = [j for j in range(len(wholedata[0]))]    

    csv_fn = "%sAvg_peakISF.csv"%(sys.argv[1])
    csv_f  = open(csv_fn,'wb')
    writer = csv.writer(csv_f)
    for i in range(len(avg)-1):
        writer.writerow([x_whole[i+1],avg[i+1]])

    plt.plot(x_whole[1:],avg[1:],color='b')
    for wd in wholedata:
        plt.plot(x_whole[1:],wd[1:],color='r')
    plt.ylabel("peak ISF[Hz]")
    plt.xlabel("stimulus pulse number")
    plt.title("AVERAGE OF PEAK ISF")
    avgFilename = "%sAvg_peakISF.png"%(sys.argv[1])
    plt.savefig(avgFilename)                    

def drawSpikeCountAllinOne():
    wholedata = [[] for _ in range(len(gides0))]
    istim1 =[0 for _ in range(len(gides0))]
    istim2 =[0 for _ in range(len(gides0))]
    for i in range(len(gides1)):
        print "i ", i
        rowdata=[[] for _ in range(8)]
        for c in case1:
            if(c.gid == gides1[i]):
                print c.filename,c.gid
                f = open(c.filename,'rb')
                reader = csv.reader(f)
                """
                istim1 = reader[0][0]
                istim2 = reader[0][1]
                for row in range(1,len(reader)):
                    rowdata[c.pcid][row]=reader[row][1]
                
                """
                
                row = reader.next()
                istim1[c.gid] = row[0]
                istim2[c.gid] = row[1]
                #print "istim",istim1,istim2
                for row in reader:
                    #print "print ",row[1]
                    #rowdata[c.gid].append(float(row[1]))
                    rowdata[0].append(float(row[1]))
                    wholedata[c.gid].append(float(row[1]))
                f.close()
        print rowdata[0]
        fig = plt.figure()
        x = [j for j in range(len(rowdata[0]))]
        #plt.plot(x[1:20],rowdata[0][1:20])
        #plt.plot(x[1:20],rowdata[0][1:20],color='r')
        #plt.plot(x[1:20],rowdata[1][1:20],color='b')
        #plt.plot(x[1:20],rowdata[2][1:20],color='g')
        
        #plt.plot(x[21:-1],rowdata[0][21:-1],color='r',label = 'delay = 0')
        #plt.plot(x[21:-1],rowdata[1][21:-1],color='b',label = 'delay = 100')
        #plt.plot(x[21:-1],rowdata[2][21:-1],color='g',label = 'delay = 200')

        #plt.plot(x[1:-1],rowdata[0][1:-1])

        for k in range(0,len(rowdata)):
            if(len(rowdata[k])!=0):
                #Label = "I1=%d, I2=%d"%(int(istim1[k]),int(istim2[k]))
                #plt.plot(x[21:-1],rowdata[k][21:-1],label = Label)
                #Label = "Gmax:%.1f"%(k*0.1)
                #Label = "Gmax:%.1f"%((k+1)*0.5)
                #Label = "P(LN-PN):%.1f"%((k+1)*0.2)
                #plt.plot(x[1: 20],rowdata[k][1: 20],color =clist[k])
                #plt.plot(x[21:-1],rowdata[k][21:-1],color =clist[k])
                plt.plot(x[1:],rowdata[k][1:],color =clist[k])
                sssssssss = 0
        plt.ylabel("Spike counts[spikes]")
        plt.xlabel("stimulus pulse number")
        #plt.legend(loc=0)
        imgFilename = "%sspikecountsAllinOne%d.png"%(sys.argv[1],gides1[i])
        plt.savefig(imgFilename)
        plt.close()
    fig3 = plt.figure(figsize=(10,5.0))
    avg = [0 for i in range(len(wholedata[0]))]
    for i in range(len(wholedata)):
        for j in range(len(wholedata[i])):
            avg[j] +=wholedata[i][j]
    print "AAAAAAAAAAAAA"
    print avg
    for i in range(len(avg)):
        avg[i] = avg[i]/len(gides0)
    print "AAAAAAAAAAAAA"
    print avg

    #wholedata = wholedata/len(gides0)
    print "WHOLE"
    print wholedata
    print "XXXXX"
    x_whole = [j for j in range(len(wholedata[0]))]
    print x_whole
    csv_fn = "%sAvg_spikecounts.csv"%(sys.argv[1])
    csv_f  = open(csv_fn,'wb')
    writer = csv.writer(csv_f)
    for i in range(len(avg)-1):
        writer.writerow([x_whole[i+1],avg[i+1]])


    plt.plot(x_whole[1:],avg[1:],color='b')
    for wd in wholedata:
        plt.plot(x_whole[1:],wd[1:],color='r')
    plt.ylabel("Spike Counts[AP/stim]")
    plt.xlabel("stimulus pulse number")
    plt.title("AVERAGE OF SPIKECOUNT")
    avgFilename = "%sAvg_spikecounts.png"%(sys.argv[1])
    plt.savefig(avgFilename)                    


drawPeakISFAllinOne()
drawSpikeCountAllinOne()
