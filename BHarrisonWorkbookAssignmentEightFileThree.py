#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
Location = "datasets/gradedata.csv" 
df = pd.read_csv(Location) 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df['hours'], df['grade'])

