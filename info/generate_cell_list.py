
#! /usr/bin/python
# coding: UTF-8

###########################################
# FILE NAME : generate_rn_list.py
# 2015.05.07
# Heewon Park
###########################################

###########################################
# File information
# This program generate cells list
#
#
NSWC     = 3

NPN   = 5
NLN   = 35
NCELL = NPN + NLN

LISTFILENAME = "./network_info_%dcells.dat"%(NCELL)

PN    = [None for _ in range(NPN)]
PN[0] = dict(cellid = 2, swcid = 0, swcpath = "./swc/050622_4_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "./info/syn/200syn.dat") 
LN    = [None for _ in range(NLN)]
LN[0] = dict(cellid = 3, swcid = 0, swcpath = "./swc/040823_5_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "./info/syn/300syn.dat") 
LN[1] = dict(cellid = 3, swcid = 1, swcpath = "./swc/040823_5_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "./info/syn/300syn.dat")

def write_header(f):
    f.write("# gid, cellid, swcid, cloneid, SWC file path, position&rotation file,
    Synapse information file\n")
    f.write("$ CELLS %d\n"%(NUM_RN))

def write_line(f, cell, gid, cloneid):
    f.write("%d %d %d %d %s %s %s\n"%(gid, cell['cellid'],cell['swcid'],gid,cell['swcpath'],cell['ppath'],cell['synpath']))

def main():
    F = open(LISTFILENAME,'w')
    write_header(F)
    for i in range(NPN):
        
