# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:44:23 2016

@author: david
"""

import pandas as pd
import numpy as np

df = pd.read_csv('StateEU28NAICS4.txt', sep='\t')
df.PARTNER.unique()
df.STATE.unique()

#Count Null Values
df.insull().sum()



StateIndexDF = df.groupby([df.STATE, df.NAICS]).Y_2015
print(StateIndexDF.sum())
print(StateIndexDF.Y_2015.sum())