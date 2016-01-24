#! /usr/bin/python
#-------------------------------------------------
#This Program is for drawing graph with voltage record
#
# How to use this program
# $ipython drawGraph.py filenames
# $ipython drawGraph.py directory
# comment added 2015.03.30
#-------------------------------------------------


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import pylab
import sys
import os.path
import numpy as np

def Reader(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()
    nDatas, nColumns = data[0].split(' ')
    nDatas = int(nDatas)
    nColumns = int(nColumns)
    print nDatas, nColumns
    vec = [[0 for i in range(nDatas)] for j in range(nColumns)]

    dummy = []
    for i in range(0,nDatas):
        #print i
        #print data[i].split('\t')
        dummy = data[i+1].split('\t')
        for j in range(nColumns):
            #print j, dummy[j]
            try:
                vec[j][i]=float(dummy[j])
            except ValueError:
                print dummy[j]
            except IndexError:
                print j,"  ", i
    return vec

def Draw():
    #dir_ = "../single-result/0117224752/record/"
    dir_ = "../single-result/0117213403/record/"
    #dir_ = "../single-result/0117225303/record/"
    iclamp = Reader("%sStimVec_default0.txt"%dir_)
    volt   = Reader("%sVoltage_default0.txt"%dir_)
    fig = plt.figure()
    plt.rcParams['font.size']=15
    gs1 = gridspec.GridSpec(3, 3)
    #gs1.update(left=0.05, right=0.48, wspace=0.05)
    ax1 = plt.subplot(gs1[:-1, :])
    ax1.plot(volt[0],volt[1],'k')
    ax1.set_ylabel('Membrain Potential[mV]')
    ax1.set_ylim(-100,80)
    ax2 = plt.subplot(gs1[-1, :])
    ax2.plot(iclamp[0],iclamp[1],'k')
    ax2.set_ylim(-10,20)
    ax2.set_xlabel('Times[ms]')
    ax2.set_ylabel('Current[nA]')
    #    plt.plot(iclamp[0],iclamp[1])
    plt.savefig("./Single_HH_RN.png")
    plt.show()

Draw()


def drawGraph(filename, show):
    datafile = open(filename,'r')
    data = datafile.readlines()
    nDatas, nColumns = data[0].split(' ')
    nDatas = int(nDatas)
    nColumns = int(nColumns)
    print nDatas, nColumns
    vec = [[0 for i in range(nDatas)] for j in range(nColumns)]
    svec = [0 for i in range(nDatas)]

    dummy = []
    for i in range(0,nDatas):
        #print i
        #print data[i].split('\t')
        dummy = data[i+1].split('\t')
        for j in range(nColumns):
            #print j, dummy[j]
            try:
                vec[j][i]=float(dummy[j])
            except ValueError:
                print dummy[j]
            except IndexError:
                print j,"  ", i

    tmp = filename.rsplit('.',1)
    imgFilename = "%s.png"%tmp[0]

    flg = pylab.figure()
    if 'Synaptic' in filename:
        for i in range(nDatas):
            for j in range(1,nColumns):
                svec[i] += vec[j][i]
        pylab.plot(vec[0], svec)
        pylab.ylabel("Current[nA]")        
        _SAVETXT_NAME_ = "%s_Sum.dat"%(tmp[0])
        np.savetxt(_SAVETXT_NAME_, svec, fmt="%.5f")
    else:
        pylab.ylabel("membrain potential[mV]")

    for j in range(1,nColumns):
        pylab.plot(vec[0], vec[j])
    #pylab.ylim(-100, 80)
    #pylab.xlim(0,500)
    pylab.xlabel("time[ms]")
    #pylab.ylabel("current[nA]")
    
    #print imgFilename, tmp
    pylab.title(imgFilename)
    pylab.savefig(imgFilename)
    if(show==True):
        pylab.show()
    pylab.close()
"""
if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        drawGraph(sys.argv[1],1)
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.txt'):
                    print full_dir                    
                    drawGraph(full_dir,0)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"
"""
"""
elif len(sys.argv) is 2:
    Filename = sys.argv[1]
    drawGraph(Filename)
elif len(sys.argv) is 3:
    target_dir = os.path.normpath(sys.argv[2])
    if((sys.argv[1] = '-r')&os.path.exists(target_dir):
"""    
