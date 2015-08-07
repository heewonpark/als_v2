
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
import csv

from synapse_list_format import SYNLIST
###########################################
# DEFAULT SETTING
NSWC  = 3
NPN   = 5
NLN   = 35
###########################################

NPN = 1
NLN = 2

NCELL = NPN + NLN

#LISTFILENAME = "./info/network_info_%dcells.dat"%(NCELL)
NAME = "cells_newsynapse"
#NAME = "PN"
LISTFILENAME = "./network_info_%d%s.dat"%(NCELL,NAME)
SYNPATH_DIR  = "../synapse_info/%d%s/"%(NCELL,NAME)
SYNPATH_DIR2  = "../input/synapse_info/%d%s/"%(NCELL,NAME)
SYNLIST_DIR  = "../input/synapse_list/"
SYNLIST_DIR_W  = "../input/synapse_list/%d%s/"%(NCELL,NAME)
SYNLIST_DIR_M  = "../synapse_list/%d%s/"%(NCELL,NAME)

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

    def getGid(self):
        return self.gid

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
#PN_default[0].setBase(cellid = 2, swcid = 0, swcpath = "../input/swc/050622_4_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/050622_4_sn_SynapseList.dat")
PN_default[0].setBase(cellid = 2, swcid = 0, swcpath = "../input/swc/050622_4_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN0804/050622_4_sn_SynapseList.dat")

LN_default    = [None for _ in range(NLNSWC)]
#LN_default[0] = CELL()
#LN_default[0].setBase(cellid = 3, swcid = 0, swcpath = "../input/swc/040823_5_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/040823_5_sn_SynapseList.dat") 
#LN_default[1] = CELL()
#LN_default[1].setBase(cellid = 3, swcid = 1, swcpath = "../input/swc/050205_7_sn_bestrigid0106_mkRegion.swc", ppath = "none", synpath = "none",fromRN = "../input/synapse_list/fromRN/050205_7_sn_SynapseList.dat")
LN_default[0] = CELL()
LN_default[0].setBase(cellid = 3, swcid = 2, swcpath = "../input/swc/040823_5_sn_bestrigid0106_mkRegion_reduction.swc", ppath = "none", synpath = "none",fromRN ="../input/synapse_list/fromRN0804/040823_5_sn_reduction_SynapseList.dat")
LN_default[1] = CELL()
LN_default[1].setBase(cellid = 3, swcid = 3, swcpath = "../input/swc/050205_7_sn_bestrigid0106_mkRegion_reduction.swc", ppath = "none", synpath = "none",fromRN ="../input/synapse_list/fromRN0804/050205_7_sn_reduction_SynapseList.dat")

PN = [CELL() for _ in range(NPN)]
LN = [CELL() for _ in range(NLN)]


s200_300 = SYNLIST()
s200_300.set_nconnections(10)
s200_300_precmpts = [1164, 1173, 1180, 1160, 1164, 1169, 1168, 1155, 1152, 1161 ]
s200_300_pstcmpts = [20072,14649,14519,15068,20092,16526,14097,19017,17076,19171]
s200_300.set_precmpts(s200_300_precmpts)
s200_300.set_pstcmpts(s200_300_pstcmpts)

s300_200 = SYNLIST()
s300_200.set_nconnections(10)
s300_200_precmpts = [2739, 2730, 2366, 2363, 2055, 2050, 1809, 1801, 1590, 1579 ]
s300_200_pstcmpts = [110,  107,  104,  101,  98,   97,   94,   114,  109,  102  ]
s300_200.set_precmpts(s300_200_precmpts)
s300_200.set_pstcmpts(s300_200_pstcmpts)

s301_200 = SYNLIST()
s301_200.set_nconnections(10)
s301_200_precmpts = [3572, 4958, 5487, 1846, 6691, 7140, 3610, 3524, 2733, 4517 ]
s301_200_pstcmpts = [101,  102,  94,   98,   125,  119,  114,  108,  103,  93   ]
s301_200.set_precmpts(s301_200_precmpts)
s301_200.set_pstcmpts(s301_200_pstcmpts)

s300_301 = SYNLIST()
s300_301.set_nconnections(10)
s300_301_precmpts = [21015,14644, 8240,15191, 8804,21375, 8239,15706,15171,21088]
s300_301_pstcmpts = [11079,10877,11534,11093,11257,10351,11580,11879,11949,11038]
s300_301.set_precmpts(s300_301_precmpts)
s300_301.set_pstcmpts(s300_301_pstcmpts)

s301_300 = SYNLIST()
s301_300.set_nconnections(10)
s301_300_precmpts = [10351,10877,11083,10380,11422,11681,10351,11083,11219,11093]
s301_300_pstcmpts = [21374,15191, 8242,21309, 8239, 9486,21436, 8804,21088,15070]
s301_300.set_precmpts(s301_300_precmpts)
s301_300.set_pstcmpts(s301_300_pstcmpts)

def write_header(f):
    f.write("# gid, cellid, swcid, cloneid, SWC file path, position&rotation file, Synapse information file\n")
    f.write("$ CELLS %d\n"%(NCELL))

def mkCellList():
    F = open(LISTFILENAME,'w')
    write_header(F)
    #gid = 0

    F.write("$ PN %d\n"%(NPN))
    j = 0
    print "PN"
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
    print "LN"
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

def write_line_syn2(f,precell, postcell, filetype, gidbase):
    pre_gid  = precell.getGid()
    post_gid = postcell.getGid()
    synfilename  = "%d_%d_%s.txt"%(pre_gid,post_gid,filetype)
    synfile_path = SYNLIST_DIR_W + synfilename
    f.write("%d %d %s\n"%(pre_gid,post_gid,synfile_path))

    if(precell.nid == 300) & (postcell.nid == 200):
        synlist = s300_200
    elif(precell.nid == 301) & (postcell.nid == 200):
        synlist = s301_200
    elif(precell.nid == 300) & (postcell.nid == 301):
        synlist = s300_301
    elif(precell.nid == 301) & (postcell.nid == 300):
        synlist = s301_300
    elif(precell.nid == 302) & (postcell.nid == 303):
        synlist = SYNLIST()
        synlist.read_synlist_format(302,303,"../synapse_list/302_303_template.csv")
    elif(precell.nid == 303) & (postcell.nid == 302):
        synlist = SYNLIST()
        synlist.read_synlist_format(303,302,"../synapse_list/303_302_template.csv")
    elif(precell.nid == 302) & (postcell.nid == 200):
        synlist = SYNLIST()
        synlist.read_synlist_format(302,200,"../synapse_list/302_200_manual.csv")
    elif(precell.nid == 303) & (postcell.nid == 200):
        synlist = SYNLIST()
        synlist.read_synlist_format(303,200,"../synapse_list/303_200_manual.csv")
    
    synfile_path_m = SYNLIST_DIR_M + synfilename
    if not os.path.exists(SYNLIST_DIR_M):
        os.makedirs(SYNLIST_DIR_M)
        print "MAKE DIR(%s)\n"%(SYNLIST_DIR_M)

    gids = [gidbase + i for i in range(synlist.nconnections)]
    synlist.set_pregid(pre_gid)
    synlist.set_pstgid(post_gid)
    synlist.set_gids(gids)
    synlist.write_synlist(synfile_path_m)

def writeSynData(cell,gidbase):
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
                write_line_syn2(F,cell,PN[i],"manual",gidbase)
        gidbase += 10    
        for i in range(NLN):
            if(cell.swcid != LN[i].swcid):
                write_line_syn2(F,cell,LN[i],"randomize",gidbase)
        gidbase += 10
    F.close()
    return gidbase

def mkSynData():
    if not os.path.exists(SYNPATH_DIR):
        os.makedirs(SYNPATH_DIR)
        print "MAKE DIR(%s)\n"%(SYNPATH_DIR)

    GID_BASE = 2000000
    
    for i in range(NPN):
        PN[i].setSynpath_write()
        PN[i].setSynpath_make()
        writeSynData(PN[i],0)
    for i in range(NLN):
        LN[i].setSynpath_write()
        LN[i].setSynpath_make()
        GID_BASE = writeSynData(LN[i],GID_BASE)
        

def main():
    mkCellList()
    mkSynData()

main()
