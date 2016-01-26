#! /usr/bin/python
# coding: UTF-8

###############################
#2016.01.24
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def Michaelis_Menten(c):
    #K = parameter[0]
    #Tau_max = parameter[1]
    #n = parameter[2]
    K = 3135.20
    Tau_max = 60
    n = 1
    r = Tau_max/(1+np.power(K/c,n))
    return r

def exp_single(x,alpha,beta,gamma):
    c = 1.5
    #beta = 250
    return alpha * sp.exp(-(x-beta)/gamma)+c

def getTau(dose):
    if(dose<=2000):
        tau = [-23.623,80.746]
    elif(dose>2000)&(dose<=5000):
        tau_rise = (-71.682-(-23.623))*(dose-2000)/3000 - 23.623
        tau_fall = (125.36-80.746)*(dose-2000)/3000 + 80.746
        tau = [tau_rise,tau_fall]
    elif(dose==10000):
        tau_rise = -50.481
        tau_fall = 175.01
        tau = [tau_rise,tau_fall]
    print dose,tau
    return tau

def frequency(t, dose, tau):
    peak_freq = Michaelis_Menten(dose)
    peak_time = 250 # ms 
    if(t<=peak_time):
        tau_rise = tau[0]
        freq = exp_single(t, peak_freq,peak_time,tau_rise)
    elif(t>peak_time):
        tau_fall = tau[1]
        freq = exp_single(t, peak_freq,peak_time,tau_fall)
    return freq

def mean_frequency_response_curve():
    time=np.arange(0,1000,1)

    f10 = [frequency(t,10,getTau(10)) for t in time]
    f100 = [frequency(t,100,getTau(100)) for t in time]
    f1000 = [frequency(t,1000,getTau(1000)) for t in time]
    f2000 = [frequency(t,2000,getTau(2000)) for t in time]
    f5000 = [frequency(t,5000,getTau(5000)) for t in time]
    f10000 = [frequency(t,10000,getTau(10000)) for t in time]

    #fig1 = plt.figure()
    fig1 = plt.figure(figsize=(4,3),dpi=250)
    fig1.subplots_adjust(bottom=0.2)
    ax = fig1.add_subplot(111)

    #plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 10 #フォントサイズを設定
    #plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
    #plt.rcParams['xtics.major.size'] = 10 #x軸目盛りの長さ
    #plt.rcParams['xtics.major.width'] = 1.5 #x軸目盛りの太さ
    plt.plot(time,f10,label="10ng")
    plt.plot(time,f100,label="100ng")
    plt.plot(time,f1000,label="1000ng")
    plt.plot(time,f2000,label="2000ng")
    plt.plot(time,f5000,label="5000ng")
    plt.plot(time,f10000,label="10000ng")
    #plt.legend()
    plt.legend(frameon=False)
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [ms]")
    #plt.savefig("mean-frequency-response.png")
    plt.savefig("mean-frequency-response_small.png")
    plt.show()

#mean_frequency_response_curve()
def uniform():
    return np.random.rand()

def frange(start,stop,step):
    array = [start+step*i for i in range(int((stop-start)/step))]
    return array

def poisson_model(_FILE_NAME_,dose):
    dt = 0.025
    T=frange(0, 5000, dt)
    T = np.array(T)

    Vorn=[]
    isf =[]
    T_isf=[]
    t_tmp=False
    t_isf =0.0
    
    psth   = []
    t_psth = []
    nspike=[]
    spt = []
    flg = 0
    tau = getTau(dose)
    for t in T:
        if(uniform()<=frequency(t,dose,tau)*dt/1000.0):
            nspike.append(t)
            spt.append(t/1000.0)
    np.savetxt(_FILE_NAME_,spt,footer="%d"%len(spt),fmt='%f',comments='')

def poisson_model_multi(_FILE_NAME_,dose,nstim):
    dt = 0.025
    T_max = 1200
    T=frange(0, T_max, dt)
    T = np.array(T)

    Vorn=[]
    isf =[]
    T_isf=[]
    t_tmp=False
    t_isf =0.0
    
    psth   = []
    t_psth = []
    nspike=[]
    spt = []
    flg = 0
    tau = getTau(dose)
    for n in range(nstim):
        for t in T:
            if(uniform()<=frequency(t,dose,tau)*dt/1000.0):
                tt = t + n*T_max
                nspike.append(tt)
                spt.append(tt/1000.0)
    np.savetxt(_FILE_NAME_,spt,footer="%d"%len(spt),fmt='%f',comments='')
#poisson_model()

