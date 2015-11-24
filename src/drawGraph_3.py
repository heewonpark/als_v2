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

fig = plt.figure()
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

    plt.subplot(3,1,count)
    for j in range(1,nColumns):
        plt.plot(vec[0], vec[j])
    plt.xlabel("time[ms]")
    if(count==2):
        plt.ylabel("membrain potential[mV]")

drawGraph("../single-result/1018204713/record/Iclamp_LN1.txt",0)
count+=1
drawGraph("../single-result/1018204713/record/Iclamp_PN0.txt",0)
count+=1
drawGraph("../single-result/1018205741/record/Iclamp_PN0.txt",0)

plt.savefig("../single-result/graph.png")
plt.show()
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
       
        
