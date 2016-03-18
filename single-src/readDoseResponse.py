#! /usr/bin/python
# coding: UTF-8


import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv

f1 = open(".csv",'r')
f2 = open(".csv",'r')

data1 = csv.reader(f1)
data2 = csv.reader(f2)

for d in data1:
    d1x.append(d[0])
    d1f.append(d[1])

for d in data2:
    d2x.append(d[0])
    d2f.append(d[1])

fig = plt.figure(figsize=(10,8),dpi=400)
fig.subplots_adjust(bottom=0.2)
ax1 = fig.add_subplot(111)

#plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams['font.size'] = 20 #フォントサイズを設定
#plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
#plt.rcParams['xtics.major.size'] = 10 #x軸目盛りの長さ                                         
#plt.rcParams['xtics.major.width'] = 1.5 #x軸目盛りの太さ     

#ax2.plot(X1,Z,'r',label='Dose')
#ax2.set_xscale('log')
#ax2.set_xlim(0.1,10000)
#ax2.set_xlabel("Dose[ng]")
#ax1.plot(istims,peakISF,"b.",label='Istim',linewidth=2.0)
ax1.plot(d1x,d1f,"b",label='Tunned',linewidth=2.0)
ax1.plot(d2x,d2f,"r",label='Not tunned',linewidth=2.0)
#ax1.set_xlim(100,1000000)
ax1.set_xlim(0.1,1000)
ax1.set_ylim(0,350)
ax1.set_xscale('log')
ax1.set_xlabel("Imax [nA]")
ax1.set_ylabel("Peak ISF [Hz]")
#ax1.set_legend()
#ax2.set_legend()
_SAVE_FIG_ = "%s/DoseResponseCurve.png"%target_dir
#plt.title(_SAVE_FIG_)
plt.savefig(_SAVE_FIG_)
plt.show()
