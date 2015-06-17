#! /usr/bin/python
# coding: UTF-8

###########################################
# FILE NAME : generate_rn_list.py
# 2015.05.07
# Heewon Park
###########################################

###########################################
# File information
# This program generate rn list
#
#

#NUM_RN = 2000
#NUM_RN = 500
NUM_RN = 20000
LISTFILENAME = "./network_info_%drns.dat"%(NUM_RN)
SWCFILEPATH_DIR = "../input/swc/rn0514/"
SWCFILENAME = "orn"
NUM_SWCFILES = 100
CELLID = 1 # cellid for rn is 1 (pn = 2, ln = 3)
POSITIONFILEPATH = "none"
SYNAPSEINFOPATH = "none"
def write_header(f):
    f.write("# cellid, swcid, cloneid, SWC file path, position&rotation file, Synapse information file\n")
    f.write("$ RN %d\n"%(NUM_RN))

def write_line(f, cid, sid, clid, spath, ppath, synpath):
    f.write("%d %d %d %s %s %s\n"%(cid, sid, clid, spath, ppath, synpath))

def main():
    F = open(LISTFILENAME,'w')
    write_header(F)
    counter = 0
    cloneid = [0 for _ in range(NUM_SWCFILES)]
    for i in range(NUM_RN):
        SWCFILEPATH = SWCFILEPATH_DIR + SWCFILENAME + "%04d.swc"%(counter)
        swcid = counter
        write_line(F, CELLID, swcid, cloneid[swcid], SWCFILEPATH, POSITIONFILEPATH, SYNAPSEINFOPATH) 
        counter = counter + 1
        cloneid[swcid] = cloneid[swcid]+1
        if(counter == NUM_SWCFILES):
            counter = 0
    #print SWCFILEPATH
main()
