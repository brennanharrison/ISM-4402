#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Programmer: Brennan Harrison
# Date: 08/31/2019
# Assignment: Workbook Assignment One File One
# Description: Import a CSV file into Python from http://census.ire.org/data/bulkdata.html

import pandas as pd
Location = "datasets/state.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:




