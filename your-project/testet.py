#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:07:32 2020

@author: goncalopinto
"""
import json
import pandas as pd

with open("testedata.json","r") as file:
    teste=json.load(file)
    
with open("testedatacold.json","r") as file:
    testecold=json.load(file)
    
print(pd.DataFrame(teste))


