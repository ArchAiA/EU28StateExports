# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:05:17 2016

@author: david
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./StateExportsN3.txt', sep='\t')
df = df.drop([222479, 222480]) #Dropping Null Rows






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
f = open('outputfile.json', 'w')
f.write(test2)





























#ATTEMPT 01

#dfState = df.groupby([df.STATE, df.PARTNER, df.NAICS])


#Print Each State's Exports to Each EU28 Country by NAICS 3 Code for 2015
#print(dfState.Y_2015.sum())


#df[df.STATE=='Wyoming']
#df[df.STATE=='Wyoming'].Y_2015
#
#
#
#df2 = pd.read_csv('StatesToEU28NAICS3SOOJSL.txt', sep='\t')
#df2State = df2.groupby([df2.STATE, df2.PARTNER, df2.NAICS, df2.YEAR])
#
#test = df2.to_json()
#f = open('workfile.json', 'w')
#f.write(test)

#ATTEMPT 01
