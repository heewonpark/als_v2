#! /usr/bin/python
# coding: UTF-8

# 2015.11.19

#----------------------------------------------------
#This Program is for drawing graph of Dose-response curve
#
#
#
#
#
#
#----------------------------------------------------

import numpy as np
import sys
import os.path

class Spike_Data:
    def __init__(self):
        self.interval = -1
        self.delay    = -1
        self.size     = -1
        self.tstop    = -1
        self.istim1   = -1
        self.istim2   = -1
        self.data     = None
        self.header   = ""
        self.t_list   = []
        self.if_list  = []
        self.peakFreq = -100
        self.avgFreq  = 0

    def Read(self, filename):
        _file_ = open(filename, 'r')
        for line in _file_:
            if line[0]=="$":
                self.header += line
            else :
                record = line.rstrip('\n')
                try :
                    self.t_list.append(float(record))
                except ValueError:
                    pass
        _file_.close()

    def show_header(self):
        print self.header
    def show_t_list(self):
        for record in self.t_list:
            print record

    def calc_peakFreq(self):
        peak = -100
        for ifreq in self.if_list:
            if(ifreq>peak):
                peak=ifreq
        self.peakFreq = peak

    # Calculate instantaneous frequency
    def calc_iFreq(self):
        for i in range(len(self.t_list)-1):
            ifreq = 1000.0/(self.t_list[i+1]-self.t_list[i])
            #print ifreq
            self.if_list.append(ifreq)
        self.calc_peakFreq()

    # Calculate average frequency between offset of stimulation and after 100ms of offset
    def calc_avgFreq(self):
        cnt = 0
        for record in self.t_list:
            if(record<100):
                cnt+=1
        self.avgFreq = float(cnt)/(100.0/1000.0)
