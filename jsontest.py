# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:27:54 2016

@author: david
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./StateExportsN3.txt', sep='\t')

df2 = df[df.STATE <= 'California']



def fdrec(df):
    drec = dict()
    ncols = df.values.shape[1]
    for line in df.values:
        d = drec
        for j, col in enumerate(line[:-1]):
            if not col in d.keys():
                if j != ncols-2:
                    d[col] = {}
                    d = d[col]
                else:
                    d[col] = line[-1]
            else:
                if j != ncols-2:
                    d = d[col]
    return drec




test = fdrec(df)
import json
test2 = json.dumps(test)
#f = open('outputfile.json', 'w')
#f.write(test2)

