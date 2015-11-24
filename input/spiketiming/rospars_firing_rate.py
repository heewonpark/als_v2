#! /usr/bin/python
# coding: UTF-8

# 2015.11.19

#----------------------------------------------------
#This Program is for testing rospars et al. 2014(Plos Computational Biology)
#
#
#----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def firing_rate(C, F_M, C_half):
    n= -0.27
    n= np.power(10,n)
    result = F_M/(1+np.exp(-np.log(10*n*(C-C_half))))
    print C, result
    return result

def firing_rate1(M, F_M, M_half):
    n = -0.27
    n = np.power(10,n)
    result = F_M/(1+np.power(M_half/M,n))
    return result

c_array = [float(i/100.0) for i in range(-200, 400)]
c_array = np.array(c_array)
print c_array
m_array = [float(i/100.0) for i in range(1, 5000000)]
f_m = 162.0
c_half = 1.15
fig1 = plt.figure()
#plt.plot(c_array, firing_rate(c_array, f_m, c_half))
m_half = np.power(10, c_half)

print 0.1, firing_rate1(0.1, f_m, m_half)
print 1, firing_rate1(1, f_m, m_half)
print 10, firing_rate1(10, f_m, m_half)

#plt.plot(m_array, firing_rate1(m_array, f_m, m_half))
#plt.xscale('log')
#plt.ylim(0,250)
#plt.savefig('rospars_firing_rate.png')
#plt.show()

