#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Programmer: Brennan Harrison
# Date: 09/02/2019
# Assignment: Workbook Assignment Two File Two
# Description: Create a dataframe from salesdata.db

import pandas as pd
from sqlalchemy import create_engine

db_file = r'datasets/salesdata.db'

# Create connection to database
engine = create_engine(r'sqlite:///{}'.format(db_file))

# Create query
sql = "select * from scores"

sales_data_df = pd.read_sql(sql,engine)
sales_data_df.head()


# In[ ]:




