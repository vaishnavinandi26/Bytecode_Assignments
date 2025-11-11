#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


user_input=input("Enter any value:")
print(user_input)


# In[4]:


num=float(input("Enter a number"))
if num>0:
    print("Number is Positive")
elif num<0:
    print("Number is Negative ")
else:
    print("Number is Zero")


# In[7]:


num1=float(input("Enter a num1:"))
num2=float(input("Enter a num2:"))
num3=float(input("Enter a num3:"))
if num1>num2 and num1>num3:
    print("The greatest number is:",num1)
elif num2>num1 and num2>num3:
     print("The greatest number is:",num2)
else:
    print("The greatest number is:",num3)


    


# In[6]:


n=int(input("Enter value of n:"))
factorial=1
if n < 0:
    print("The fav=ctorial does not exists negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial *= i
    print("The factorial of",n,"is",factorial)
        



# In[10]:


a=10
b=2.4
c="Python"
d=True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))


# In[11]:


a=20
b=30
print(a,b)
a,b=b,a
print(a,b)


# In[13]:


celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit:",fahrenheit)


# In[19]:


s1="Python"
s2="Programming"
print(s1+ " " +s2)


# In[1]:


a="python"
print(a,type(a))


# In[4]:


a=40
b=20
print("Addition of two numbers:",a+b)
print("Multiplication of two numbers:",a*b)
print("Substraction of two numbers:",a-b)
print("Division of two numbers:",a/b)


# In[5]:


a=int(input("Enter first number"))
b=int(input("Enter first number"))
print("a == b:",a==b)
print("a != b:",a!=b)
print("a > b:",a>b)
print("a < b:",a<b)


# In[7]:


a=True
b=False
print("a and b=",a&b)
print("a or b=",a or b)
print("not a=",not a)
print("not b=", not b)


# In[8]:


a=2
print(a**2)


# In[9]:


n=int(input("Enter any value for n:"))
if n%2==0:
    print(" n is Even")
else:
    print("n is Odd")


# In[13]:


n=int(input("Enter n value:"))
sum_of_n=n*(n+1)//2
print(sum_of_n)


# In[14]:


y=int(input("Enter n value:"))
if (y%4==0 and y%100!=0) or (year%400==0):
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")


# In[19]:


a="Python"
reverse_str=a[::-1]
print("Revese of a string is:",reverse_str)


# In[4]:


str1=input("Enter a string")
if str1 == str1[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")
    


# In[5]:


l1=[10,20,30,5,50]
l1.sort()
print(l1)


# In[ ]:




