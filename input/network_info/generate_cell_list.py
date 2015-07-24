
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

import copy
import random
import os

###########################################
# DEFAULT SETTING
NSWC  = 3
NPN   = 5
NLN   = 35
###########################################

#NPN = 8
#NLN = 0

NCELL = NPN + NLN

#LISTFILENAME = "./info/network_info_%dcells.dat"%(NCELL)
LISTFILENAME = "./network_info_%dcells.dat"%(NCELL)
SYNPATH_DIR  = "../synapse_info/%dcells/"%(NCELL)
SYNPATH_DIR2  = "../input/synapse_info/%dcells/"%(NCELL)
SYNLIST_DIR  = "../input/synapse_list/"
NPNSWC = 1
NLNSWC = 2

class CELL:
    def __init__(self):
        self.gid     = -1
        self.cellid  = -1
        self.swcid   = -1
        self.cloneid = -1
        self.swcpath = "none"
        self.ppath   = "none"
        self.synpath = "none"
        self.fromRN  = "none"
        self.max_clone = 0
        self.synpath_dir_w = "none"
        self.synpath_dir_m = "none"
        self.synapth_fn  = "none"

    def setBase(self,cellid,swcid,swcpath, ppath, synpath,fromRN):
        self.cellid  = cellid
        self.swcid   = swcid
        self.swcpath = swcpath
        self.ppath   = ppath
        self.synpath = synpath
        self.fromRN  = fromRN

    def setGid(self,gid):
        self.gid     = gid

    def setCloneid(self,cloneid):
        self.cloneid = cloneid

    def calcGid(self):
        self.gid = self.cellid * 100000 + self.swcid * 1000 + self.cloneid

    def setNid(self):
        self.nid = self.cellid * 100 + self.swcid

    def writeline(self,f):
        f.write("%d %d %d %d %s %s %s\n"%(self.gid, self.cellid,self.swcid,self.cloneid,self.swcpath,self.ppath,self.synpath_w))

    def setSynpath_write(self):
        self.synpath_dir_w = SYNPATH_DIR2
        self.synpath_fn  = "%dsyn.dat"%(self.gid)
        self.synpath_w = self.synpath_dir_w+self.synpath_fn

    def setSynpath_make(self):
        self.synpath_dir_m = SYNPATH_DIR
        self.synpath_fn  = "%dsyn.dat"%(self.gid)
        self.synpath_m = self.synpath_dir_m+self.synpath_fn

    def writeFromRN(self,f):
        f.write("%s\n"%(self.fromRN))
    
    def getCellid(self):
        return self.cellid

    
PN_default    = [None for _ in range(NPNSWC)]
PN_default[0] = CELL()
PN_default[0].setBase(cellid = 2, swcid = 0, swcpath = "../input/swc/050622_4_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/050622_4_sn_SynapseList.dat")
LN_default    = [None for _ in range(NLNSWC)]
LN_default[0] = CELL()
LN_default[0].setBase(cellid = 3, swcid = 0, swcpath = "../input/swc/040823_5_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/040823_5_sn_SynapseList.dat") 
LN_default[1] = CELL()
LN_default[1].setBase(cellid = 3, swcid = 1, swcpath = "../input/swc/050205_7_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/050205_7_sn_SynapseList.dat")

PN = [CELL() for _ in range(NPN)]
LN = [CELL() for _ in range(NLN)]

def write_header(f):
    f.write("# gid, cellid, swcid, cloneid, SWC file path, position&rotation file, Synapse information file\n")
    f.write("$ CELLS %d\n"%(NCELL))

def mkCellList():
    F = open(LISTFILENAME,'w')
    write_header(F)
    #gid = 0

    F.write("$ PN %d\n"%(NPN))
    j = 0
    for k in range(NPN):
        PN_default[j].max_clone += 1
        print PN_default[j].max_clone
        j+=1
        if(j==NPNSWC):
            j=0
    cnt = 0
    for j in range(NPNSWC):
        for k in range(PN_default[j].max_clone):
            PN[cnt] = copy.copy(PN_default[j])
            #PN[cnt].setGid(gid)
            PN[cnt].setCloneid(k)
            PN[cnt].calcGid()
            PN[cnt].setNid()
            PN[cnt].setSynpath_write()
            PN[cnt].writeline(F)
            #gid +=1
            cnt +=1

    F.write("$ LN %d\n"%(NLN))
    j=0
    for k in range(NLN):
        LN_default[j].max_clone += 1
        print LN_default[j].max_clone
        j+=1
        if(j==NLNSWC):
            j=0
    cnt = 0
    for j in range(NLNSWC):
        for k in range(LN_default[j].max_clone):
            LN[cnt] = copy.copy(LN_default[j])
            #LN[cnt].setGid(gid)
            LN[cnt].setCloneid(k)
            LN[cnt].calcGid()
            LN[cnt].setNid()
            LN[cnt].setSynpath_write()
            LN[cnt].writeline(F)
            #gid +=1
            cnt +=1


def write_header_syn(f):
    f.write("# This file shows the file path of synapse\n")

def write_line_syn(f,precell, postcell, filetype):
    pre_nid  = precell.nid
    post_nid = postcell.nid
    synfilename  = "%d_%d_%s.txt"%(pre_nid,post_nid,filetype)
    synfile_path = SYNLIST_DIR + synfilename
    f.write("%d %d %s\n"%(precell.gid, postcell.gid, synfile_path))

def writeSynData(cell):
    F = open(cell.synpath_m,'w')
    print cell.synpath_m
    write_header_syn(F)
    F.write("$ fromRN\n")
    cell.writeFromRN(F)
    LNtoPN = [0 for i in range(NPN)]
    LtoP = 0
    LtoL = 0
    if(cell.getCellid() == 3):
        F.write("$ CtoC\n")
        for i in range(NPN):
            if(random.random()<=1.0):
                LNtoPN[i] = 1
                LtoP += 1
        for i in range(NLN):
            if(cell.swcid != LN[i].swcid):
                LtoL += 1
        F.write("%d\n"%(LtoP + LtoL))
        for i in range(NPN):
            if(LNtoPN[i]==1):
                write_line_syn(F,cell,PN[i],"manual")
            
        for i in range(NLN):
            if(cell.swcid != LN[i].swcid):
                write_line_syn(F,cell,LN[i],"randomize")
    F.close()

def mkSynData():
    if not os.path.exists(SYNPATH_DIR):
        os.makedirs(SYNPATH_DIR)
        print "MAKE DIR(%s)\n"%(SYNPATH_DIR)
    for i in range(NPN):
        PN[i].setSynpath_write()
        PN[i].setSynpath_make()
        writeSynData(PN[i])
    for i in range(NLN):
        LN[i].setSynpath_write()
        LN[i].setSynpath_make()
        writeSynData(LN[i])

def main():
    mkCellList()
    mkSynData()

main()
