
# coding: utf-8

# In[19]:

import numpy as np
import pandas as pd
df1 = pd.read_csv('C:/Users/saiad/Desktop/Test/1.csv')
df2 = pd.read_csv('C:/Users/saiad/Desktop/Test/2.csv')


# In[14]:

df1 = df1.drop(['No.','Time'], axis=1)
df2 = df2.drop(['No.','Time'], axis=1)


# In[20]:

df = pd.concat([df1, df2])
df = df.reset_index(drop=True)


# In[21]:

df_gpby = df.groupby(list(df.columns))


# In[22]:

idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]


# In[23]:

df.reindex(idx)


# In[ ]:



