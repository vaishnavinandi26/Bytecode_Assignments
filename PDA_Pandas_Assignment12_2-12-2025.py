#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import random
df=pd.DataFrame(
    np.random.randint(1,101,(10,5)),
    columns=['A','B','C','D','G'])
print("Data Frame:\n",df)
a=df.iloc[3,2]
a
                


# In[7]:


b=df.iloc[:,[0,2]]
b


# In[9]:


c=df.iloc[[2,4,7],:]
c


# In[10]:


d=df.iloc[[1,3,5],[0,2]]
d


# In[18]:


df=pd.DataFrame(
    np.random.randint(1,101,(10,5)),
    columns=['A','B','C','D','E'])

df['E'] = [10,20,30,40,50,60,70,80,90,100]
df


# In[21]:


df.drop(columns=['C'])


# In[23]:


df.iloc[:,[1]]=0
df


# In[25]:


df.iloc[[3],:]=[1,2,3,4,5]
df


# In[27]:


df.loc[[2,5],'A']=99
df


# In[29]:


import warnings
warnings.simplefilter("ignore")
df.iloc[[0,1,2],:]=[ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ]
df


# In[30]:


df.loc[0,'A']=np.nan
df


# In[32]:


df.drop(index=3)


# In[33]:


df.drop(columns='D')


# In[34]:


df.drop(columns=['B','E'])


# In[35]:


df.drop(index=[0,2,5])


# In[53]:


df=pd.DataFrame(
    np.random.randint(1,101,(10,5)),
    columns=['A','B','C','D','E'])
print(df)
df['A']=df['A']+10
print(df)


# In[54]:


df['B']=df['B']*2
df


# In[56]:


df.loc[5].sum()


# In[59]:


mean_cols=df.mean()
mean_cols


# In[60]:


a=df[df['A']>50]
a


# In[64]:


B_C = df[(df['B'] < 30) & (df['D'] > 10)]
print(B_C)


# In[68]:


df.iloc[df['C']<50]=0
df


# In[6]:


import pandas as pd
import numpy as np
df=pd.DataFrame(
    np.random.randint(1,101,(10,5)),
    columns=['A','B','C','D','E'])
df.loc[[1,2],['B','D']]=999
df


# In[8]:


df.loc[[1,2],['A','C']]=[[7,8],[9,10]]
df


# In[9]:


df.iloc[1,2]


# In[10]:


df.loc[2,'A']


# In[ ]:




