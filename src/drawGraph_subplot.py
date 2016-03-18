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
from matplotlib import pylab
import sys
import os.path
import numpy as np

#plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.linewidth'] = 2.0
#plt.rcParams['xtics.major.size'] = 10
#plt.rcParams['xtics.major.width'] = 1.5

#fig = plt.figure()
fig = plt.figure(figsize=(6,6),dpi=250)
count = 1
def drawGraph(filename, show):
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

    flg = pylab.figure()
    for j in range(1,nColumns):
        pylab.plot(vec[0], vec[j])
    #pylab.ylim(-100, 80)

    pylab.xlabel("time[ms]")
    #pylab.ylabel("current[nA]")
    pylab.ylabel("membrain potential[mV]")
    tmp = filename.rsplit('.',1)
    imgFilename = "%s.png"%tmp[0]
    #print imgFilename, tmp
    pylab.savefig(imgFilename)
    if(show==True):
        pylab.show()
    pylab.close()
    
    #plt.subplot(3,1,count)
    plt.subplot(4,1,count)
    #plt.axis('off')
    for j in range(1,nColumns):
        plt.plot(np.array(vec[0])-150, vec[j],'b',linewidth=2.0)
    #plt.xlabel("time[ms]")
    plt.xlim(-100,900)
    #plt.xticks(np.arange(50,1150,200),np.arange(-100,1100,100))
    plt.xticks(np.arange(0,1000,200))
    if(count==1):
        plt.yticks(np.arange(-100,100,50))
        plt.tick_params(labelbottom='off')
        ax1 = fig.add_axes((0, 0.2, 1, 0.8))
        ax1.plot(vec[0],vec[1])
    if(count==2):
        plt.yticks(np.arange(0,20,5))
        plt.ylim(-1,10.0)
        plt.tick_params(labelbottom='off')
    if(count==3):
        plt.yticks(np.arange(0,0.15,0.05))
        plt.ylim(-0.01,0.10)
        plt.tick_params(labelbottom='off')
    if(count==4):
        plt.yticks(np.arange(-10,1,5))
        plt.ylim(-10,1)
        #plt.ylabel("membrain potential[mV]")
        #plt.plot([50,150],[-0.05,-0.05],'k',linewidth=4.0)
        

"""
drawGraph("../single-result/1018204713/record/Iclamp_LN1.txt",0)
count+=1
drawGraph("../single-result/1018204713/record/Iclamp_PN0.txt",0)
count+=1
drawGraph("../single-result/1018205741/record/Iclamp_PN0.txt",0)

plt.savefig("../single-result/graph.png")
plt.show()
"""
drawGraph("../single-result/0206214135/record/Voltage_LN_0.txt",0)
count+=1
drawGraph("../single-result/0206214135/record/GABAa_PN_1.txt",0)
count+=1
drawGraph("../single-result/0206212307/record/GABAb_PN_1.txt",0)
count+=1
drawGraph("../single-result/0206215752/record/Exp2Syn_LN_1.txt",0)

plt.savefig("../single-result/ipsc.png")
plt.show()
plt.close()
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
       
        
