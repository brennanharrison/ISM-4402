#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Programmer: Brennan Harrison
# Date: 08/31/2019
# Assignment: Workbook Assignment Two File One
# Description: Load all of the weekly call data into one dataframe.

import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()

for f in glob.glob("datasets/weekly_call_data/weekdata*.xlsx"):
    df= pd.read_excel(f)
    all_data = all_data.append(df,ignore_index = True)
all_data.describe()


# In[ ]:




