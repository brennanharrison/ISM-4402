#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gender_to_numeric(x):
    if x == 'female':
        return 1
    else:
        return 0




import pandas as pd
import statsmodels.formula.api as sm
Location = 'datasets/gradedata.csv'
df = pd.read_csv(Location)
df['gender_val'] = df['gender'].apply(gender_to_numeric)
df.drop('gender', axis =1)
result = sm.ols(formula='grade ~ gender_val + exercise + hours',data=df).fit() 
result.summary()


#Adding gender_val did not improve our R-squared.

