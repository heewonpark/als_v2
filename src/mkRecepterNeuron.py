#! /usr/bin/python
# coding: UTF-8

###########################################
# FILE NAME : mkRecepterNeuron.py
# 2015.04.27
# Heewon Park
###########################################

###########################################
# MODIFIED HISTORY
# 2015.05.14 radious and diameter of axon changed
# ncmt = 120
#
#

import datetime
import locale
import os
import math
import random

directory = "../input/swc/rn_6axon"
NUM_RN_SWC = 100
source = "DESIGNED BY PARK"
scale_x = 1.0
scale_y = 1.0
scale_z = 1.0

NUM_BRANCH = 6
x_origin = 0.0
y_origin = 0.0
z_origin = 0.0
#radius = 2500 # for Length of antenna
radius = 500
theta = math.pi / 500.0 /2

r_axon = 2
n0 = 1
t_axon = 2
p0 = -1

t_dend = 3
length_dend = 100
r_dend = 10

def write_header(f):
    d = datetime.datetime.today()
    
    f.write("#ORIGINAL_SOURCE %s\n"%(source))
    f.write("#CREATURE \n")
    f.write("#REGION \n")
    f.write("#FIELD/LAYER \n")
    f.write("#TYPE \n")
    f.write("#CONTRIBUTOR \n")
    f.write("#REFERENCE \n")
    f.write("#RAW \n")
    f.write("#EXTRAS \n")
    f.write("#SOMA_AREA \n")
    f.write("#SHINKAGE_CORRECTION 1.000000 1.000000 1.000000\n")
    f.write("#VERSION_NUMBER \n")
    f.write("#VERSION_DATE %s-%s-%s\n"%(d.year, d.month, d.day))
    f.write("#SCALE %.1f %.1f %.1f\n"%(scale_x, scale_y, scale_z))

# ncmp : number of compartment
def calcCoordinate(ncmt):
    x = [0.0 for _ in range(ncmt)]
    y = [0.0 for _ in range(ncmt)]
    z = [0.0 for _ in range(ncmt)]

    xrev = [0.0 for _ in range(ncmt)]
    yrev = [0.0 for _ in range(ncmt)]
    zrev= [0.0 for _ in range(ncmt)]

    i = 0
    while i<ncmt:
        if(i==0):
            x[i]=x_origin
            y[i]=y_origin
        else:
            x[i] = x[i-1] + radius*theta*math.sin(i*theta)
            y[i] = y[i-1] + radius*theta*math.cos(i*theta)
        #print x[i], y[i]
        i +=1

    i=0
    while i<ncmt:
        xrev[i] = x[ncmt-1-i]
        yrev[i] = y[ncmt-1-i]
        i +=1
    xyz = []
    xyz.append(xrev)
    xyz.append(yrev)
    xyz.append(zrev)
    return xyz
        
# n sample number
# t type
# x,y,z  position
# r radius of compartment
# p parent sample
def writeAxon(f,ncmt):
    xyz = []
    xyz = calcCoordinate(ncmt)
    #print xyz[0]
    #print xyz[1]
    #print xyz[2]
    f.write("%d %d %f %f %f %f %d\n"%(n0, t_axon, xyz[0][0], xyz[1][0], xyz[2][0], r_axon, p0))
    for i in range(1,ncmt):
        f.write("%d %d %f %f %f %f %d\n"%(i+1, t_axon, xyz[0][i], xyz[1][i], xyz[2][i], r_axon, i))

def writeDendrite(f,ncmt):
    beta = math.pi/3
    alpha = math.pi*2 / NUM_BRANCH
    for i in range(NUM_BRANCH):
        xd = length_dend * math.sin(alpha*i) * math.cos(beta)
        yd = -length_dend * math.cos(beta)
        zd = length_dend * math.cos(alpha*i) * math.cos(beta)
        f.write("%d %d %f %f %f %f %d\n"%(ncmt+i+1, t_dend, xd, yd, zd, r_dend, ncmt))

def write_swcfile(counter):
    if not os.path.exists(directory):
        os.mkdir(directory)
    filename = "orn%04d.swc"%(counter)
    path = os.path.join(directory,filename)
    f = open(path,'w')
    write_header(f)
    #random.seed()
    
    #ncmt = int(random.uniform(100,500))
    ncmt = 120
    writeAxon(f,ncmt)
    writeDendrite(f,ncmt)

for i in range(0,NUM_RN_SWC):
    write_swcfile(i)
