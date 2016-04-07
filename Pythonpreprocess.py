
# coding: utf-8

# In[17]:

import numpy as np


# In[1]:

import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/kddcup.csv')


# In[8]:

normal = df.loc[df['V42'] == 'normal.']
neptune = df.loc[df['V42'] == 'neptune.']


# In[13]:

import numpy as np
from sklearn.cross_validation import train_test_split
normal_train1, normal_train2 = train_test_split(normal, test_size=0.50, random_state=42)
neptune_train1, neptune_train2 = train_test_split(neptune, test_size=0.50, random_state=42)


# In[18]:

samplenormal_train1 = df.loc[np.random.choice(normal_train1.index, 1000, replace=False)]


# In[14]:

dataset1 = pd.concat([normal_train1, neptune_train1])
dataset2 = pd.concat([normal_train2, neptune_train2])


# In[20]:

del dataset1['Unnamed: 0']
del dataset2['Unnamed: 0']


# In[60]:

data1 = dataset1.drop(['V2','V3','V4','V42'], axis = 1 )
cols_to_merge1 = dataset1[['V2','V3','V4','V42']]
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
data1_minmax = min_max_scaler.fit_transform(data1)
data1_normalized = pd.DataFrame(data1_minmax)
data1_normalized.columns = ['V1', 'V5','V6', 'V7','V8', 'V9','V10', 'V11','V12', 'V13','V14', 'V15','V16', 'V17',
                            'V18', 'V19','V20','V21', 'V22','V23', 'V24','V25', 'V26','V27', 'V28','V29', 'V30',
                           'V31', 'V32','V33', 'V34','V35', 'V36','V37','V38','V39','V40','V41']


# In[61]:

data2 = dataset2.drop(['V2','V3','V4','V42'], axis = 1 )
cols_to_merge2 = dataset2[['V2','V3','V4','V42']]
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
data2_minmax = min_max_scaler.fit_transform(data2)
data2_normalized = pd.DataFrame(data2_minmax)
data2_normalized.columns = ['V1', 'V5','V6', 'V7','V8', 'V9','V10', 'V11','V12', 'V13','V14', 'V15','V16', 'V17',
                            'V18', 'V19','V20','V21', 'V22','V23', 'V24','V25', 'V26','V27', 'V28','V29', 'V30',
                           'V31', 'V32','V33', 'V34','V35', 'V36','V37','V38','V39','V40','V41']


# In[62]:

data1_normalized.to_csv('C:/Users/User/Downloads/data1_normalized.csv')
data2_normalized.to_csv('C:/Users/User/Downloads/data2_normalized.csv')
cols_to_merge1.to_csv('C:/Users/User/Downloads/cols_to_merge1.csv')
cols_to_merge2.to_csv('C:/Users/User/Downloads/cols_to_merge2.csv')


# In[ ]:



