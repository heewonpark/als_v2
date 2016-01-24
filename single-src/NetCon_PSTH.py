#! /usr/bin/python
# coding: UTF-8                                                                                      

####################################################
# FILE NAME : 
# AUTHOR : HEEWON PARK
# 2015.12.23
#
####################################################

####################################################
# MODIFIED HISTORY
#
#
#

import numpy as np
import matplotlib.pyplot as plt
import sys
import os.path

print "::::: NetCon_PSTH.py :::::"
BIN      = 10.0 # ms

def PSTH(_FILENAME_):
    global BIN
    netcon  = np.loadtxt(_FILENAME_,skiprows=1)
    maximum = netcon.max()
    steps   = int(np.ceil(maximum/BIN))
    print "Maximum : %f, Steps : %d"%(maximum,steps)
    print netcon.shape
    step_freq = [0.0 for i in range(steps+1)]
    step_time = [i*BIN for i in range(steps+1)]

    if(len(netcon.shape)==1):
        column = 1
        for n in netcon:
            if(n!=0.0):
                step_freq[int(n/BIN)]+=float(1000/BIN/column)
    else:
        column = netcon.shape[1]
        for net in netcon:
            for n in net:
                if(n!=0.0):
                    step_freq[int(n/BIN)]+=float(1000/BIN/column)

    #print step_freq, step_time
    fig = plt.figure()
    plt.bar(step_time,step_freq,width=BIN)
    plt.xlabel('Time[s]')
    plt.ylabel('Frequency[Hz]')
    plt.title('PSTH')
    plt.xlim(0,500)
    plt.ylim(0,120)
    _TMP_ = _FILENAME_.rsplit('.',1)
    _SAVE_FIG_="%s_PSTH.png"%_TMP_[0]
    plt.title(_SAVE_FIG_)
    plt.savefig(_SAVE_FIG_)

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
                if(('NetCon' in full_dir)&('.txt' in full_dir)):
                    print full_dir                    
                    #butterworth(full_dir,'all')
                    PSTH(full_dir)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"

