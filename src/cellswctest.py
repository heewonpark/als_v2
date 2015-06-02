from neuron import h
import neuron as nrn
import os.path
import numpy as np
import csv
import operator
import random

import swc
nrn.load_mechanisms("./mod")
h.load_file("CellSwc_Ver2.hoc")

h.CellSwc("./swc/050622_4_sn_bestrigid0106_mkRegion.swc")
