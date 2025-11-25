#!/usr/bin/env python
# coding: utf-8

# In[39]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
print(d1,type(d1))


# In[19]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
print(d1[5])
for k,v in d1.items():
    print(k)


# In[17]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
d={11:121}
d1.update(d)
print(d1,type(d1))
d1.pop(1,1)
print(d1,type(d1))



# In[20]:


for k,v in d1.items():
    print(k,"-->",v,type(d1))


# In[24]:


cubes={x: x**3  for x in range(1,11)}
print(cubes,type(cubes))


# In[1]:


d1={1:1,2:4,3:9,4:16,5:25}
d2={6:36,7:49,8:64,9:81,10:100}
d3={}
d3.update(d1)
d3.update(d2)
print(d3)


# In[28]:


d1={"name":"sri","age":19,"grades":{"math":"A+","science":"O","english":"O"}}
for k,v in d1["grades"].items():
    print(k,"==>",v,type(v),type(d1))


# In[32]:


d1={1:[1,2,3,4,5],2:[2,4,8,10,12],3:[3,6,9,12,15],4:[4,8,12,16,20],5:[5,10,15,20,25]}
print(d1,type(d1))
for k,v in d1.items():
    print(k,"-->",v,type(v))


# In[33]:


d1={1:(1,1),2:(2,4),3:(3,9),4:(4,16),5:(5,25)}
print(d1,type(d1))
for k,v in d1.items():
    print(k,"-->",v,type(v))


# In[36]:


d1={1:1,2:4,3:9,4:16,5:25}
list_of_tuples=list(d1.items())
print(list_of_tuples)


# In[37]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
d2={i: square for i,square in d1.items() if i%2==0}
print(d2,type(d2))


# In[38]:


d1={1:1,2:4,3:9,4:16,5:25}
print(d1,type(d1))
swapped_dict={value: key for key,value in d1.items()}
print(swapped_dict)


# In[3]:


keys={1,2,3,4}
values=[]
d1=dict.fromkeys(keys,values)
print(d1)
values.append("apple")
values.append("banana")
values.append("mango")
values.append("guava")
print(d1)


# In[2]:


text = "hello"
count_dict = {}

for c in text:          
    if c not in count_dict:
        count_dict[c] = 0
    count_dict[c] += 1

print(count_dict)


# In[6]:


book={"title":"was I ever enough","author":"jay shah","year":2022,"genre":"sad"}
print(book,type(book))


# In[ ]:




