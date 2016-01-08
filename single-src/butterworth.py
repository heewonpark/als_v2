#! /usr/bin/python
# coding: utf-8

#-------------------------------------------------
#This Program is for drawing graph with voltage record
#
# How to use this program
# $ipython butterworth.py filenames
# $ipython butterworht.py directory
#-------------------------------------------------

# 2015.12.15
# Yuqiao Guの論文に乗っているButterworth filterの実装

import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import sys
import os.path

# https://ccrma.stanford.edu/~jos/fp/Butterworth_Lowpass_Filter_Example.html
# http://oceanpython.org/2013/03/11/signal-filtering-butterworth-filter/
# http://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units
# http://org-technology.com/posts/low-pass-filter.html

def butterworth(_FILENAME_,option='low'):
    dt = 0.025 / 1000.0
    fs  = 1/dt
    nyq = 0.5*fs
    #lowcut = 5
    lowcut = 40
    low = lowcut / nyq
    cutoff = 2*lowcut/fs

    y = np.loadtxt(_FILENAME_)
    t_s = np.linspace(1,y.size, y.size)*dt -dt # Second
    t_ms = t_s*1000 # Milliseconds[ms]
    _TMP_     = _FILENAME_.rsplit('.',1)
    
    if((option=='low')|(option=='all')):
        b_low, a_low = signal.butter(4,cutoff,btype='lowpass')
        y_low = signal.lfilter(b_low,a_low,y)
        print y_low.size
        minimum = np.amin(y_low[:int(500/dt/1000)])
        pos     = np.where(minimum==y_low)
        print minimum, pos
        print y_low[pos]
        print t_ms[pos]
        fig1 = plt.figure()
        plt.plot(t_ms,y,"b")
        plt.plot(t_ms,y_low,"r",linewidth=2, label="butter-low")
        #plt.plot(t,y_low+y_high,"y",linewidth=2, label="butter-high")
        plt.text(t_ms[pos]-5,minimum-3,"%.3f"%minimum,fontsize=15)
        plt.xlim(0,500)
        plt.legend(loc="upper right")
        plt.xlabel("Time[s]")
        plt.ylabel("Amplitude")

        _SAVEDAT_ = "%s_lowpass.dat"%_TMP_[0]
        np.savetxt(_SAVEDAT_,y_low,fmt="%.5f")

        _SAVEFIG_ = "%s_lowpass.png"%_TMP_[0]    
        plt.title(_SAVEFIG_)
        plt.savefig(_SAVEFIG_)

    if((option=='high')|(option=='all')):
        b_high, a_high = signal.butter(4,cutoff,btype='highpass')
        y_high = signal.lfilter(b_high,a_high,y)
        
        fig2 = plt.figure()
        plt.plot(t_ms,y_high,"g",linewidth=2, label="butter-high")
        plt.xlim(0,500)
        plt.legend(loc="upper right")
        plt.xlabel("Time[s]")
        plt.ylabel("Amplitude")

        _SAVEDAT_ = "%s_highpass.dat"%_TMP_[0]
        np.savetxt(_SAVEDAT_,y_high,fmt="%.5f")

        _SAVEFIG_ = "%s_highpass.png"%_TMP_[0]
        plt.title(_SAVEFIG_)
        plt.savefig(_SAVEFIG_)


if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        #drawGraph(sys.argv[1],1)
        print "Input argument was Filename, Do Nothing"
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if '_Sum.dat' in full_dir:
                    print full_dir                    
                    #butterworth(full_dir,'all')
                    butterworth(full_dir,'low')
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"
