#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import matplotlib.pyplot as plt
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,83,77,78,95] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades']) 
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot() 
displayText = "Wow!" 
xloc = 0
yloc = 76
xtext = 8 
ytext = 100
plt.annotate(displayText,xy=(xloc, yloc),
             arrowprops=dict(facecolor='black',shrink=0.05),xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),textcoords='offset points')

