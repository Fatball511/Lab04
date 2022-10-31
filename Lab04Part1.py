#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:53:42 2022

@author: keithcheng
"""


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sy

Com = pd.read_csv("censusCrimeClean.csv")

[corr_value1,p_value1]=(sy.pearsonr(Com["medIncome"],Com["ViolentCrimesPerPop"]))

print("correlation value of Pearson is ",corr_value1)
print("p value of Pearson is ",p_value1)

[corr_value2,p_value2]=(sy.spearmanr(Com["medIncome"],Com["ViolentCrimesPerPop"]))

print("correlation value of Spearson is ",corr_value2)
print("p value of Spearson is ",p_value2)

plt.scatter(Com["medIncome"], Com["ViolentCrimesPerPop"])


