#! /usr/bin/python
# coding: UTF-8

import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy import stats

def readCSV(filename):
    f = open(filename, 'rb')
    reader = csv.reader(f)
    data = [[] for i in range(len(reader))]
    for row in reader:
        for i in range(len(row)):
            data[i].append(row[i])
    print data


