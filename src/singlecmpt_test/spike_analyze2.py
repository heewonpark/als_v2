#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing graph of peak ISF and spike counts
#2015.04.01

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
    pcid = 0
    cellid = 0
    filename = ''

case = []
cellides = []

case1 = []
cellides1 = []

if len(sys.argv) is 2:
    if(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                if('BALPN' in fname)&('peakISF.csv' in fname):
                    print fname
                    p = re.compile(r'(\d+)spikerecord_BALPN(\d+)_peakISF.csv')
                    a = p.search(fname)
                    pcid, cellid = a.groups()
                    print pcid, cellid
                    pcid = int(pcid)
                    cellid = int(cellid)
                    d = Data()
                    d.pcid = pcid
                    d.cellid = cellid
                    d.filename= full_dir
                    case.append(d)
                    if(cellid in cellides)==False:
                        cellides.append(cellid)
                        #print cellid
                elif('BALPN' in fname)&('spikecounts.csv' in fname):
                    print fname
                    p1 = re.compile(r'(\d+)spikerecord_BALPN(\d+)_spikecounts.csv')
                    a1 = p1.search(fname)
                    pcid1, cellid1 = a1.groups()
                    print pcid1, cellid1
                    pcid1 = int(pcid1)
                    cellid1 = int(cellid1)
                    d1 = Data()
                    d1.pcid = pcid1
                    d1.cellid = cellid1
                    d1.filename= full_dir
                    case1.append(d1)
                    if(cellid1 in cellides1)==False:
                        cellides1.append(cellid1)
                        #print cellid1

                    
def drawPeakISFAllinOne():
    for i in range(len(cellides)):
        print "i ", i
        rowdata=[[] for _ in range(8)]
        istim1 =[0 for _ in range(8)]
        istim2 =[0 for _ in range(8)]
        for c in case:
            if(c.cellid == cellides[i]):
                print c.filename,c.cellid,c.pcid
                f = open(c.filename,'rb')
                reader = csv.reader(f)
                """
                istim1 = reader[0][0]
                istim2 = reader[0][1]
                for row in range(1,len(reader)):
                    rowdata[c.pcid][row]=reader[row][1]
                
                """
                
                row = reader.next()
                istim1[c.pcid] = row[0]
                istim2[c.pcid] = row[1]
                print "istim",istim1,istim2
                for row in reader:
                    #print "print ",row[1]
                    rowdata[c.pcid].append(float(row[1]))
                    
                f.close()
        
        fig = plt.figure(figsize=(10,5.0))
        x = [j for j in range(len(rowdata[c.pcid]))]
        #plt.plot(x[1:20],rowdata[0][1:20],color='r')
        #plt.plot(x[1:20],rowdata[1][1:20],color='b')
        #plt.plot(x[1:20],rowdata[2][1:20],color='g')
        
        plt.plot(x[1:31],rowdata[0][1:31],color='r',label = '1000ng')
        plt.plot(x[1:31],rowdata[1][1:31],color='b',label = '100ng')
        plt.plot(x[1:31],rowdata[2][1:31],color='g',label = '10ng')

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
        imgFilename = "%speakISFAllinOne%d.png"%(sys.argv[1],cellides[i])
        plt.savefig(imgFilename)
        plt.close()

                    
def drawSpikeCountAllinOne():
    for i in range(len(cellides1)):
        print "i ", i
        rowdata=[[] for _ in range(8)]
        istim1 =[0 for _ in range(8)]
        istim2 =[0 for _ in range(8)]
        for c in case1:
            if(c.cellid == cellides1[i]):
                print c.filename,c.cellid,c.pcid
                f = open(c.filename,'rb')
                reader = csv.reader(f)
                """
                istim1 = reader[0][0]
                istim2 = reader[0][1]
                for row in range(1,len(reader)):
                    rowdata[c.pcid][row]=reader[row][1]
                
                """
                
                row = reader.next()
                istim1[c.pcid] = row[0]
                istim2[c.pcid] = row[1]
                print "istim",istim1,istim2
                for row in reader:
                    #print "print ",row[1]
                    rowdata[c.pcid].append(float(row[1]))
                    
                f.close()
        
        fig = plt.figure()
        x = [j for j in range(len(rowdata[c.pcid]))]
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
                plt.plot(x[1:31],rowdata[k][1:31],color =clist[k])
                sssssssss = 0
        plt.ylabel("Spike counts[spikes]")
        plt.xlabel("stimulus pulse number")
        #plt.legend(loc=0)
        imgFilename = "%sspikecountsAllinOne%d.png"%(sys.argv[1],cellides1[i])
        plt.savefig(imgFilename)
        plt.close()

drawPeakISFAllinOne()
drawSpikeCountAllinOne()
