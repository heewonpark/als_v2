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
import scipy as sp
import matplotlib.pyplot as plt
from SpikeFuncs import *

def double_exp(x, alpha1, beta, gamma1, alpha2, gamma2):
    result = alpha1 * sp.exp(-(x-beta)/gamma1)  +  alpha2 * sp.exp(-(x-beta)/gamma2)
    return result

def Michaelis_Menten(c,parameter):
    K = parameter[0]
    Tau_max = parameter[1]
    n = parameter[2]
    r = Tau_max/(1+np.power(K/c,n))
    return r

def Calculate_Alpha1(c,parameter):
    factor=parameter[3]
    return factor * Michaelis_Menten(c,parameter[0:3])
def Calculate_Alpha2(c,parameter):
    factor=parameter[4]
    return factor * Michaelis_Menten(c,parameter[0:3])

read_para = open("saveParameter.dat",'r')
para_dat = read_para.readlines()
read_para.close()

C = 0.0

de_para = [0 for _ in range(5)]
de_para = para_dat[0].split('\t')
de_para.remove('\n')
for i in range(5):
    de_para[i] = float(de_para[i])
    #print de_para
    
cf1_para = [0 for _ in range(3)]
cf1_para = para_dat[1].split('\t')
cf1_para.remove('\n')
for i in range(3):
    cf1_para[i] = float(cf1_para[i])
    #print cf1_para
            
cf2_para = [0 for _ in range(5)]
cf2_para = para_dat[2].split('\t')
cf2_para.remove('\n')
for i in range(5):
    cf2_para[i] = float(cf2_para[i])
    #print cf2_para

#spt : spike timing
def load_spt_data(nfiles,nstims,dose):
    
    for i in range(nfiles):
        #DIR = "./%ddose_%dstims/"%(dose,nstims)
        DIR = "./%ddose_%dstims_poisson/"%(dose,nstims)
        #DIR = "./%ddose_%dstims_test/"%(dose,nstims)
        #DIR = "./%ddose_%dstims_filtering_adaptation2/"%(dose,nstims)
        #DIR = "./%ddose_%dstims_filtering/"%(dose,nstims)
        #DIR = "./1000dose_30stims_2000dose_30stims_filtering/"
        fn = "%sspt%03d.dat"%(DIR,i)
        #fn = "./1stim/spiketiming%d.dat"%(i)
        spt = np.loadtxt(fn,float)
        #print i
        try:
            if(i==0):
                spts = spt[:-1]
            else:
                spts = np.append(spts,spt[:-1])
        except TypeError:
            print "No spikes", spt
        #print"LOAD FILE : %s"%(fn)
        #print spt
        #print spts
    return spts

INTERVAL = 1.2 # 1.2s
BIN      = 0.05 # 0.1s
print INTERVAL, BIN

def PSTH(nfiles,nstims,dose):
    global INTERVAL, BIN
    print INTERVAL, BIN

    print "NUM OF FILES: %d\nNUM OF STIMS: %d\nDOSE: %d"%(nfiles,nstims,dose)
    parameter = np.loadtxt("Michaelis-Menten_Parameter_PSTH.txt",float)
    print"[PARAMETERSFOR MICHAELIS-MENTEN]\nk = %f, Tau_max = %f, n = %f, factor1 = %.10f, factor2 = %.10f"%(parameter[0],parameter[1],parameter[2],parameter[3],parameter[4])
    print parameter
    print"\n[PARAMETERS FOR DOUBLE EXPONENTIAL]\nALPHA1 = %f, BETA = %f, GAMMA1 = %f, ALPHA2 = %f, GAMMA2= %f"%(de_para[0],de_para[1],de_para[2],de_para[3],de_para[4])
    print de_para
    de_para[0]= Calculate_Alpha1(dose,parameter)
    de_para[3]= Calculate_Alpha2(dose,parameter)
    de_para[1]-=6
    print "ALPHA1 = %f, ALPHA2 = %f\n"%(de_para[0],de_para[3])

    if(nstims!=1):
        steps = int(nstims*INTERVAL/BIN)
    elif(nstims==1):
        steps = int(8.0/BIN)
        INTERVAL = 8.0
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
            #print "OVER",s
            continue
        #print "%f %d %f"%(s,int((s-6.0)/BIN),float(1/BIN/nfiles))
        step_freq[int((s-6.0)/BIN)]+=float(1/BIN/nfiles)

    X = np.linspace(0,8,100)
    fig = plt.figure(figsize=(10,8),dpi=400)
    #plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 20 #フォントサイズを設定
    #plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
    #plt.rcParams['xtics.major.size'] = 10 #x軸目盛りの長さ
    #plt.rcParams['xtics.major.width'] = 1.5 #x軸目盛りの太さ
    plt.plot(X,double_exp(X,*de_para),'r-',linewidth=3.0,label=r'$F(c,t)$')
    plt.bar(step_time,step_freq,width=BIN,color='#3b3b3b',label='PSTH')
    plt.xlabel('Time[s]',fontsize=25)
    plt.ylabel('Frequency[Hz]',fontsize=25)
    plt.title('PSTH')
    plt.legend(fontsize=20)
    save_fn = "%ddose_%dstims_PSTH_forthesis2.png"%(dose,nstims)
    plt.savefig(save_fn)
    plt.show()

#PSTH(1000,1,100)

def PSTH_poisson(nfiles,nstims,dose):
    global INTERVAL, BIN
    print INTERVAL, BIN

    if(nstims!=1):
        steps = int(nstims*INTERVAL/BIN)
    elif(nstims==1):
        steps = int(8.0/BIN)
        INTERVAL = 8.0
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
        if((s)>INTERVAL*nstims):
            #print "OVER",s
            continue
        #print "%f %d %f"%(s,int((s-6.0)/BIN),float(1/BIN/nfiles))
        step_freq[int((s)/BIN)]+=float(1/BIN/nfiles)

    X = np.linspace(0,8,100)
    fig = plt.figure(figsize=(10,8),dpi=400)
    #plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 20 #フォントサイズを設定
    #plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
    #plt.rcParams['xtics.major.size'] = 10 #x軸目盛りの長さ
    #plt.rcParams['xtics.major.width'] = 1.5 #x軸目盛りの太さ
    time=np.arange(0,5000,1)
    print time
    tau = getTau(dose)
    freq = [frequency(t,dose,tau) for t in time]
    time = time/1000.0
    print time
    plt.plot(time, freq)
    plt.bar(step_time,step_freq,width=BIN,color='#3b3b3b',label='PSTH')
    plt.xlabel('Time[s]',fontsize=25)
    plt.ylabel('Frequency[Hz]',fontsize=25)
    plt.title('PSTH')
    plt.legend(fontsize=20)
    save_fn = "%ddose_%dstims_PSTH_poisson.png"%(dose,nstims)
    plt.savefig(save_fn)
    plt.show()

PSTH_poisson(1000,1,10)
