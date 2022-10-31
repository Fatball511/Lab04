#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:26:59 2022

@author: keithcheng
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sy
from math import sqrt
H = pd.read_csv("heart.csv")

H["gender"]=np.where(abs(H.sex)== 0,0,1)
H["hasHeartDisease"]=np.where(abs(H.target)==0,1,0)

Hmean = np.mean(H.trestbps)
Hsd = np.std(H.trestbps)
print("the mean is ",Hmean)
print("the standard deviation is ",Hsd)

WD = H.trestbps.loc[H.hasHeartDisease==1]#resting blood pressure with disease
Dm = np.mean(WD)
s1 = np.std(WD)
WO = H.trestbps.loc[H.hasHeartDisease==0]#resting blood pressure without disease
Nm = np.mean(WO)
s2 = np.std(WO)
n1,n2 = len(WD),len(WO)
print("With diease mean :",Dm)
print("with diease sd:",s1)
print("without diease mean:",Nm)
print("without diease sd:",s2)

#Compare by boxplot
fig, axs = plt.subplots(ncols=2,sharey=True)
axs[0].boxplot(WD)
axs[0].set_title('With diease')
axs[1].boxplot(WO)
axs[1].set_title('Without diease')

#Compare by histogram
fig, axs = plt.subplots(ncols=2,sharey=True)
axs[0].hist(WD)
axs[0].set_title('With diease')
axs[1].hist(WO)
axs[1].set_title('Without diease')

#Calculate the p-value
print(sy.ttest_ind(WD, WO))


s = sqrt(((n1-1) * s1**2 + (n2 - 1) * s2**2 )/(n1 + n2 - 2))
d = (Dm - Nm)/s
print("The Cohen's d is ",d)


#Count the number with the disease for each gender type
hasDiseaseCount=H[H.hasHeartDisease==True].groupby("gender").count().hasHeartDisease

#Count the number of gender type
totalCount=H.groupby("gender").count()['hasHeartDisease']

#combine into a dataframe (both are indexed with gender, so will be matched) and specify the columns
p=pd.concat([hasDiseaseCount, totalCount], axis=1)
p.columns = ["heartDiseaseCount", "totalCount"]

#create a new column and calculate the proportion
p['propHeartDisease']=p["heartDiseaseCount"]/p["totalCount"]

#print the results
print(p)
z_score = 1.96
p_fm = 24/96
n_f = 96
p_m = 114/207
n_m = 207
pp = p_m - p_fm

se_female = sqrt(p_fm * (1 - p_fm)/n_f)#Standard Error for female

se_male = sqrt(p_m * (1 - p_m)/n_m)#Standard Error for male

se_diff = sqrt(se_female**2 + se_male**2)#

lcb = pp - z_score * se_diff #lower limit of the CI
ucb = pp + z_score * se_diff #upper limit of the CI
print("The CI is ",lcb,"to",ucb)
print("The CI is 0.19 and 0.41. This range does not have 0 in it. Both the numbers are above zero. So, We cannot make any conclusion that the population proportion of females with heart disease is the same as the population proportion of males with heart disease. If the CI would be -0.12 and 0.1, we could say that the male and female population proportion with heart disease is the same.")
#lcb_fm = p_fm - z_score* se_female #lower limit of the CI
#ucb_fm = p_fm + z_score* se_female #upper limit of the CI
#print("The CI of female is ",lcb_fm,"to",ucb_fm)