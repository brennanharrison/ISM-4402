#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


df['Cars Sold'].mean()


# In[7]:


df['Cars Sold'].max()


# In[8]:


df['Cars Sold'].min()


# In[9]:


df.groupby('Gender')['Cars Sold'].mean()


# In[10]:


df.loc[df['Cars Sold'] > 3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[11]:


df.loc[df['Cars Sold'] > 3]['Years Experience'].mean()


# In[15]:


df.groupby('SalesTraining')['Cars Sold'].mean()


# In[14]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
totalYes = df.loc[df['SalesTraining'] == 'Y']['Cars Sold'].sum()
totalNo= df.loc[df['SalesTraining'] == 'N']['Cars Sold'].sum()
inputDataOne = ['Y','N']
inputDataTwo = [totalYes,totalNo]
finalData = zip(inputDataOne,inputDataTwo)
df2 = pd.DataFrame(data = finalData, columns = ['SalesTraining', 'Total Cars Sold'])
df3 = df2.set_index(df2['SalesTraining'])
ax = df3.plot(kind='bar')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))


# In[13]:


df.boxplot(by='Gender', column='Hours Worked')


# In[ ]:




