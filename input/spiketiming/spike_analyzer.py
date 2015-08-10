#! /usr/bin/python
# coding: UTF-8                                                                                      

####################################################
# FILE NAME : spike_analyzer.py
# AUTHOR : HEEWON PARK
# 2015.08.04
# 生成されたスパイクタイミングが正しいのか検証するためのコード
####################################################

####################################################
# MODIFIED HISTORY
#
#
#

import numpy as np
import matplotlib.pyplot as plt

#spt : spike timing
def load_spt_data(nfiles,nstims,dose):
    
    for i in range(nfiles):
        #DIR = "./%ddose_%dstims/"%(dose,nstims)
        #DIR = "./%ddose_%dstims_test/"%(dose,nstims)
        #DIR = "./%ddose_%dstims_filtering/"%(dose,nstims)
        DIR = "./1000dose_30stims_2000dose_30stims_filtering/"
        fn = "%sspt%03d.dat"%(DIR,i)
        #fn = "./1stim/spiketiming%d.dat"%(i)
        spt = np.loadtxt(fn,float)
        if(i==0):
            spts = spt[:-1]
        else:
            spts = np.append(spts,spt[:-1])
        print"LOAD FILE : %s"%(fn)
        #print spt
        #print spts
    return spts

INTERVAL = 1.2 # 1.2s
BIN      = 0.1 # 0.1s

def PSTH(nfiles,nstims,dose):
    if(nstims!=1):
        steps = int(nstims*INTERVAL/BIN)
        
    elif(nstims==1):
        steps = int(8.0/BIN)
        print "steps1",steps
    else:
        print "***ERROR IN PSTH***"
        return

    print steps
    step_freq = [0 for i in range(steps+1)]
    step_time = [0 for i in range(steps+1)]
    for i in range(steps+1):
        step_time[i] = i*BIN
    spts = load_spt_data(nfiles,nstims,dose)
    for s in spts:
        # スパイクが6.0ｓから始まるので6を引く
        if((s-6.0)>INTERVAL*nstims):
            print "OVER",s
            continue
        #print "%f %d %f"%(s,int((s-6.0)/BIN),float(1/BIN/nfiles))
        step_freq[int((s-6.0)/BIN)]+=float(1/BIN/nfiles)

    fig = plt.figure()
    plt.bar(step_time,step_freq,width=0.1)
    plt.xlabel('Time[s]')
    plt.ylabel('Frequency[Hz]')
    plt.title('PSTH')
    save_fn = "%ddose_%dstims_PSTH.png"%(dose,nstims)
    plt.savefig(save_fn)
    plt.show()

PSTH(1000,60,10)
