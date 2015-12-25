import numpy as np
import matplotlib.pyplot as plt
import os

def favg_S(t,parameter):
    t_sti = 0.0
    fsp = 1.5
    q = 0.9

    if(parameter==0.1):
        fpe = 16.0
        
        T_lat = 250.0
        T_d2pe = 150.0
        
        tau_rise = 180.0
        tau_fall1 = 130.0
        tau_fall2 = 20.0*1000
    elif(parameter==1):
        fpe = 35.0
        
        T_lat = 250.0
        T_d2pe = 115.0
        
        tau_rise = 128.6
        tau_fall1 = 170.0
        tau_fall2 = 10.0*1000
    elif(parameter==10):
        fpe = 154.0
        
        T_lat = 150.0
        T_d2pe = 115.0
        
        tau_rise = 155.0
        tau_fall1 = 115.0
        tau_fall2 = 5.0*1000

    if(t<=t_sti+T_lat):
        f = fsp
        #print "1",f
    elif ((t_sti+T_lat)<=t) and (t<=(t_sti+T_lat+T_d2pe)):
        exp_rise = np.exp(-(t-t_sti-T_lat)/tau_rise)
        f = fsp + (fpe-fsp)*(1-exp_rise)
        #print "2",f,(1-np.exp(-(t-t_sti-T_lat)/tau_rise))
    else:
        exp_rise = np.exp(-T_d2pe/tau_rise)
        exp_fall1 = np.exp(-(t-(t_sti+T_lat+T_d2pe))/tau_fall1)
        exp_fall2 = np.exp(-(t-(t_sti+T_lat+T_d2pe))/tau_fall2)
        f = fsp + (fpe-fsp)*(1-exp_rise)*(q*exp_fall1+(1-q)*exp_fall2)
        #print "3",f
    return f

def favg_L(t,parameter):
    t_sti = 0.0
    fsp = 1.5
    q = 0.72

    if(parameter==1):
        fpe = 130.0
        fpl = 30.0

        T_lat = 170.0
        T_d2pe = 110.0
        T_pl = 870.0

        tau_rise = 140.0
        tau_fall1 = 70.0
        tau_fall2 = 0.3*1000
        tau_fall3 = 11.791*1000

    elif(parameter==2):
        fpe = 125.0
        fpl = 30.0

        T_lat = 140.0
        T_d2pe = 160.0
        T_pl = 330.0

        tau_rise = 150.0
        tau_fall1 = 40.0
        tau_fall2 = 0.2*1000
        tau_fall3 = 10.5*1000
    
    if(t<=t_sti+T_lat):
        f = fsp
        #elif ((t_sti+T_lat)<=t) and (t<=t_pe):
    elif ((t_sti+T_lat)<=t) and (t<=t_sti+T_lat+T_d2pe):
        exp_rise =np.exp(-(t-t_sti-T_lat)/tau_rise)
        f = fsp + (fpe-fsp)*(1-exp_rise)
    elif ((t_sti+T_lat+T_d2pe)<=t) and (t<=(t_sti+T_lat+T_d2pe+T_pl)):
        exp_rise =np.exp(-T_d2pe/tau_rise)
        exp_fall1=np.exp(-(t-(t_sti+T_lat+T_d2pe))/tau_fall1)
        f = fpl + (fsp+(fpe-fsp)*(1-exp_rise)-fpl)*exp_fall1
        #print "2",f,np.exp(-(t-(t_sti+T_lat+T_d2pe))/tau_fall1)
    else:
        exp_fall2=np.exp(-(t-(t_sti+T_lat+T_d2pe+T_pl))/tau_fall2)
        exp_fall3=np.exp(-(t-(t_sti+T_lat+T_d2pe+T_pl))/tau_fall3)
        f = fsp+(fpl-fsp)*(q*exp_fall2+(1-q)*exp_fall3)
        #print "3",f,exp_fall2,exp_fall3

    return f

def mean_frequency_response_curve():
    t=[i/10.0 for i in range(-20000,100000)]
    t = np.array(t)
    #print t
    fs1=[favg_S(i,0.1) for i in t]
    fs2=[favg_S(i,1) for i in t]
    fs3=[favg_S(i,10) for i in t]

    fl1=[favg_L(i,1) for i in t]
    fl2=[favg_L(i,2) for i in t]
    #print fs
    
    fig1 = plt.figure()
    plt.plot(t,fs1,".")
    plt.plot(t,fs2,".")
    plt.plot(t,fs3,".")
    plt.savefig("ChangeDose_Period_Fixed.png")

    fig2 = plt.figure()
    plt.plot(t,fl1,".")
    plt.plot(t,fl2,".")
    plt.savefig("ChangePeriod.png")

    plt.show()

def uniform():
    return np.random.rand()

def frange(start,stop,step):
    array = [start+step*i for i in range(int((stop-start)/step))]
    return array

def poisson_model():
    dt = 0.025
    #T=[i/10.0 for i in range(-20000,100000)]
    T=frange(0, 10000, dt)
    T = np.array(T)
    Vorn=[]
    isf =[]
    T_isf=[]
    t_tmp=False
    t_isf =0.0
    
    psth   = []
    t_psth = []
    nspike=[]
    flg = 0
    for t in T:
        #print t
        if(abs(t)%50)==0:
            #print t
            if(flg!=0):
                psth.append(len(nspike)*20)
                nspike=[]
            t_psth.append(t)
            flg+=1

        if(uniform()<=favg_S(t,1)*dt/1000):
            Vorn.append(50)
            #print"%f\t%f\t%f"%(t,t_tmp,t-t_tmp)
            nspike.append(t)
            if(t_tmp==False):
                t_tmp = t
            elif(t-t_tmp)!=dt:
                t_isf = (t+t_tmp)/2
                f = 1000/(t-t_tmp)
                isf.append(f)
                T_isf.append(t_isf)
                t_tmp = t
        else:
            Vorn.append(-62)
            
    #print isf
    #print T_isf
    #print t_psth
    #print psth
    
    fig1 = plt.figure()
    plt.plot(T,Vorn)
    plt.savefig("membrane_potential.png")
    
    fig2 = plt.figure()
    plt.plot(T_isf,isf)
    plt.savefig("Instantaneous_frequency.png")
    fig3 = plt.figure()
    plt.bar(t_psth[:-1],psth,width=50)
    plt.savefig("psth.png")
    plt.show()

def poisson_model(_FILE_NAME_,dose):
    dt = 0.025
    #T=[i/10.0 for i in range(-20000,100000)]
    T=frange(0, 10000, dt)
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
    for t in T:
        #print t
        if(abs(t)%50)==0:
            #print t
            if(flg!=0):
                psth.append(len(nspike)*20)
                nspike=[]
            t_psth.append(t)
            flg+=1

        if(uniform()<=favg_S(t,dose)*dt/1000):
            Vorn.append(50)
            #print"%f\t%f\t%f"%(t,t_tmp,t-t_tmp)
            nspike.append(t)
            spt.append(t/1000.0)
            if(t_tmp==False):
                t_tmp = t
            elif(t-t_tmp)!=dt:
                t_isf = (t+t_tmp)/2
                f = 1000/(t-t_tmp)
                isf.append(f)
                T_isf.append(t_isf)
                t_tmp = t
        else:
            Vorn.append(-62)
    np.savetxt(_FILE_NAME_,spt,footer="%d"%len(spt),fmt='%f',comments='')

#poisson_model()

def main():
    dose = 10
    #_SAVE_DIR_ = "./%fdose_1stims_yuqiao/"%(dose)
    _SAVE_DIR_ = "./%ddose_1stims_yuqiao/"%(dose)
    if not os.path.exists(_SAVE_DIR_):
        os.makedirs(_SAVE_DIR_)
    for i in range(1000):
        _SAVE_NAME_="%sspt%03d.dat"%(_SAVE_DIR_,i)
        print _SAVE_NAME_
        poisson_model(_SAVE_NAME_,dose)

main()
