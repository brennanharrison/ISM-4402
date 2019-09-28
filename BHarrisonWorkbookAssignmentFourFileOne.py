#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
Location = "datasets/gradedata.csv" 
df = pd.read_csv(Location)  
bins = [0, 60, 70, 80, 90, 100]  
binsTwo = [0,80,100]
group_names = ['F', 'D', 'C', 'B', 'A']
pass_fail = ['Fail', 'Pass']
df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names) 
df['Pass/Fail'] = pd.cut(df['grade'], binsTwo, labels=pass_fail) 
df

