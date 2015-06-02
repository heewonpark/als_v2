# coding: utf-8

######################################################################################
# 2015.05.14 Heewon Park
# 
######################################################################################


######################################################################################
# MODIFIED HISTORY
# 
#
#
#

from neuron import h
import os

h.load_file("CellSwc.hoc")
h.load_file("nrngui.hoc")
h.load_file("stdlib.hoc")

cell = h.CellSwc("./swc/070224_SN-23-R.swc")


#sh = h.PlotShape(1)
#sh.scale(0,0)
#sh.size(-140,140,-140,140)
#sh.exec_menu("Shape Plot")

h.tstop = 1
#h.dt    = TIMESTEP

h.run()
print h.psection()

