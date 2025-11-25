#!/usr/bin/env python
# coding: utf-8

# In[5]:


l1=list(range(1,21))
print(l1,type(l1))


# In[2]:


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("First Element of l1:",l1[0])
print("Middle Element of l1:",len(l1)//2)
print("Last Element of l1:",l1[-1])



# In[19]:


print("First 5 Elements of l1:",l1[0:5])
print("Last 5 Elements of l1:",l1[-1:-6:-1])
print("Elements from index5 to 15 of l1:",l1[5:16])


# In[27]:


squares=[x**2 for x in range(1,11) ]
print(squares,type(squares))


# In[28]:


even=[x for x in range(1,21) if x%2==0]
print(even,type(even))


# In[33]:


l1=[1,4,3,9,7]
l1.sort(reverse=False)
print(l1)
l1.sort(reverse=True)
print(l1)


# In[14]:


l1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print(l1,type(l1))
print(l1[1][2])


# In[12]:


student_score=[
                {"name":"xavier","score":10},
                {"name":"yoho","score":100},
                {"name":"zoya","score":150},
              ]
sorted_list=sorted(student_score,key=lambda x: x["score"],reverse=True)
print(sorted_list)
                  


# In[18]:


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
original=[[1,2,3],[4,5,6],[7,8,9]]
transposed=transpose(original)
print("Original:",original)
print("Transposed:",transposed)


# In[19]:


def flatten(nested_list):
    flat=[]
    for sub in nested_list:
        for item in sub:
            flat.append(item)
    return flat
nested=[[1,2],[3,4],[5,6]]
print("Original:",original)
print("Flattend:",flatten(nested))


# In[25]:


l1=list(range(1,11))
print(l1,type(l1))
for i in sorted([2,4,6],reverse=True):
    l1.pop(i)
l1.insert(5,99)
print(l1)


# In[27]:


l1=[1,2,3,4]
l2=["a","b","c","d"]
l3=list(zip(l1,l2))
print(l3)


# In[30]:


def reversal(list):
    return list[::-1]
original=[1,2,3,4,5]
print("Original:",original)
print("Reversed:",reversal(original))


# In[34]:


def rotate(lst, n):
    return lst[n:] + lst[:n]

print(rotate([1,2,3,4,5], 2))
print("Original:",original)
print("Rotated by 2:",rotate(original,2))


# In[31]:


def intersect(l1,l2):
    return [i for i in l1 if i in l2]
print(intersect([1,2,3,4],[3,4,5,6]))


# In[ ]:




