#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("Enter a number:"))
if n>0:
    print("Positive number:",n)


# In[3]:


n=int(input("Enter a number:"))
if n>0:
    print("Number is positive:",n)
else:
    print("Number is negative:",n)


# In[5]:


n=int(input("Enter a number:"))
if n>0:
    print("Number is positive:",n)
elif n<0:
    print("Number is negative:",n)
else:
    print("Number is zero:",n)


# In[7]:


n=int(input("Enter a Number:"))
if n>0:
    print("Number is positive:",n)
    if n%2==0:
        print("Number is even:",n)
    else:
        print("Number is odd:",n)
else:
    print("Number is negative:",n)


# In[8]:


for x in range(1,11):
    print(x)



# In[12]:


i=1
while i<= 10:
    print(i)
    i+=1


# In[18]:


for i in range(5):
    for j in range(5):
        print("*",end="")
    print()


# In[35]:


total=0
while True:
    n=int(input("Enter a number (0 to stop):"))
    if n==0:
        break
    total+=n
print("Sum=",total)


# In[17]:


for x in range(1,11):
    if x==5:
        continue
    print(x)


# In[16]:


def my_function():
    pass
print("Function defined successfully.")


# In[21]:


n=int(input("Enter a number:"))
for x in range(1,n+1):
    if x%2==0:
        print(x)
   
    


# In[24]:


n=int(input("Enter a number:"))
fact=1
x=1
while x<=n:
    fact*=x
    x+=1
print("Factorial:",fact)


# In[27]:


n=int(input("Enter a number:"))
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print("Sum of digits=",total)


# In[31]:


n=int(input("Enter a number:"))
prime=True
if n <= 1:
    prime=False
for i in range(2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print("Prime number:")
else:
    print("Not a prime number")


# In[32]:


n=int(input("Enter a value:"))
a=0
b=1
for x in range(n):
    print(a)
    c=a+b
    a=b
    b=c


# In[ ]:




