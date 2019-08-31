#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Programmer: Brennan Harrison
# Date: 08/31/2019
# Assignment: Workbook Assignment One File Two
# Description: Import an Excel file into Python from https://www.census.gov/support/USACdataDownloads.html

import pandas as pd
Location = 'datasets/ANC01.xls'
df = pd.read_excel(Location)
df.head()


# In[ ]:




