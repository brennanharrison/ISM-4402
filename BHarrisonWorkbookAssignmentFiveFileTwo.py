#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0]
columns = ['Names', 'Grades','BSDegrees','MSDegrees','PHDDegrees']
dataList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=dataList, columns = columns)


# In[ ]:


df.count()


# In[ ]:


df.mean()


# In[ ]:


df.min()


# In[ ]:


df.max()


# In[ ]:


df.std()


# In[ ]:


df.quantile(.25)


# In[ ]:


df.quantile(.5)


# In[ ]:


df.quantile(.75)

