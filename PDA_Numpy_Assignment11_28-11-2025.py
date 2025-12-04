#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import random
a=np.random.randint(1,21,(5,5))
print(a)
a[:,2]=1
print(a)



# In[17]:


b=np.random.randint(1,17,(4,4))
print(b)
np.fill_diagonal(b,0)
print(b)




# In[28]:


a=np.arange(1,37).reshape(6,6)
print(a)
print(a[[3,4,5],:])
print(a[:,[2,3,4]])


# In[32]:


a=np.random.randint(1,26,(5,5))
print(a)


# In[2]:


import numpy as np
a=np.random.randint(1,25,(3,4))
b=np.random.randint(1,36,(3,4))
print("addition of arrays:",a+b)
print("substraction of arrays:",a-b)
print("multiplication of arrays:",a*b)
print("division of arrays:",a/b)


# In[40]:


a=np.arange(1,17).reshape(4,4)
print(a)
print("Row wise sum:",a.sum(axis=1))
print("column wise sum:",a.sum(axis=0))


# In[45]:


a=np.random.randint(1,26,(5,5))
print(a)
print("Mean:",a.mean())
print("Median:",np.median(a))
print("Standard deviation:",a.std())
print("Variance:",a.var())


# In[46]:


a=np.arange(1,10).reshape(3,3)
mean=a.mean()
std=a.std()
normalized_array=(a-mean)/std
print(normalized_array)


# In[47]:


a=np.random.randint(1,10,(3,3))
print(a)
b=np.array([1, 2 ,3 ])
c=a+b
print(c)


# In[48]:


a=np.random.randint(1,16,(4,4))
print(a)
b=np.array([1, 2 ,3 ,4 ])
c=a-b.reshape(4,1)
print(c)


# In[2]:


import numpy as np
a=np.random.randint(1,10,(3,3))
det=np.linalg.det(a)
inv=np.linalg.inv(a)
eig=np.linalg.eig(a)
print("Determinant of matrix:",det)
print("Inverse of matrix:",inv)
print("Eigenvalues of matrix:",eig)


# In[3]:


a=np.random.randint(1,10,(2,3))
b=np.random.randint(1,10,(3,2))
result=np.matmul(a,b)
print(result)


# In[6]:


a=np.arange(1,10).reshape(3,3)
a1=a.reshape(1,9)
a2=a.reshape(9,1)
print(a1)
print(a2)


# In[8]:


a=np.random.randint(1,26,(5,5))
flat=a.flatten()
resh=flat.reshape(5,5)
print(resh)


# In[9]:


a=np.random.randint(1,26,(5,5))
corners = a[[0, 0, -1, -1], [0, -1, 0, -1]]
print(corners)


# In[10]:


a=np.random.randint(1,25,(4,4))
a[a>10]=10
print(a)


# In[16]:


data = np.array([
    ("Alice", 25, 55.5),
    ("Bob", 30, 70.2),
    ("Charlie", 22, 60.0)
], dtype=[('name','U10'),('age','i4'),('weight','f4')])

sorted_data = np.sort(data, order='age')
print(sorted_data)


# In[14]:


import numpy.ma as ma

arr = ma.masked_greater(np.random.randint(1, 20, size=(4, 4)), 10)
print("Sum of unmasked elements:", arr.sum())


# In[15]:


arr = ma.array(np.random.randint(1, 20, size=(3, 3)))
arr[np.eye(3, dtype=bool)] = ma.masked
mean_val = arr.mean()
arr = arr.filled(mean_val)
print(arr)


# In[ ]:




