
#! /usr/bin/python
# coding: UTF-8

###########################################
# FILE NAME : gen_SynapseList.py
# 2015.07.17
# Heewon Park
###########################################

###########################################
# File information
# This program generate cells list
#
#

import random
import os

for i in range(4):
    FILENAME = "200_200_temp_for_prof%d.txt"%(i)
    f = open(FILENAME, 'w')
    f.write("$ PRE_CEL 200\n")
    f.write("$ POST_CELL 200\n")
    nconnect = 10
    f.write("$ NCONNECTIONS %d\n"%(nconnect))
    for j in range(nconnect):
        a=random.randint(0,1212)
        b=random.randint(0,1212)
        f.write("%d %d\n"%(a,b))
        
