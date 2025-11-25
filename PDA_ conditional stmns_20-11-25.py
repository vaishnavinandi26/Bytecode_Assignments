#!/usr/bin/env python
# coding: utf-8

# In[4]:


password="admin123"
user_input=input("Enter Password")
if user_input==password:
    print("Login successful")
else:
    print("Invalid Password")


# In[5]:


Age=int(input("Enter age of user:"))
if Age>=18:
    print("The user is eligible to vote")
else:
    print("The user is not eligible to vote")


# In[6]:


mobile_recharge=int(input("Enter price of recharge:"))
if mobile_recharge>199:
    print("free 2GB data coupon is applicable")
else :
    print("data coupon is not applicable")


# In[10]:


marks=eval(input("Enter marks of student:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
else:
    print("fail")
    
    
    
    
                 


# In[14]:


temp=eval(input("Enter temperature:"))
if temp>=25:
    print("Hot Weather")
elif temp>=20:
    print("cool temperature")
else:
    print("Extreme cool weather")


# In[15]:


sal=int(input("Enter salary:"))
cibil=int(input("Enter CIBIL Score:"))
if sal>=30000 and cibil>750:
    print("The user is eligible for credit card")
else:
    print("The user is not eligible for credit card")


# In[28]:


balance=100000
withdrawal=int(input("Enter withdrawal amount:"))
if withdrawal<=balance:
    if withdrawal%100==0:
        print("Amount is mutiple of 100")
    else:
        print("Amount is not mutiple of 100")
else:
    print("Insufficient balance")


# In[18]:


mobileno=int(input("Enter mobile number:"))
mb=str(mobileno)
if len(mb)==10 and mb[0] in '6789':
    print("Valid mobile number")
else:
    print("Invalid mobile number")



# In[30]:


bill=input("Enter type of bill:")
match(bill):
    case 'domestic':
        print("5 rupees per unit")
    case 'commercial':
        print("8 rupees per unit")
    case 'industrial':
        print("10 rupees per unit")
    case _:
        print("Invalid bill type")


# In[19]:


num1=eval(input("Enter first number:"))
num2=eval(input("Enter second number:"))
ch=input("Enter your choice ('+','-','*','/'):")
match(ch):
    case '+':
        print(f'{num1} and {num2} is {num1+num2}')
    case '-':
        print(f'{num1} and {num2} is {num1-num2}')
    case '*':
        print(f'{num1} and {num2} is {num1*num2}')
    case '/':
        print(f'{num1} and {num2} is {num1/num2}')
    case _:
        print("Invalid operator")



# In[26]:


Item_name=input("Enter item name:")
price=eval(input("Enter item price:"))
quantity=int(input("Enter number of items purchased:"))
Subtotal=price*quantity
if for i in range(1,100):
    print(Subtotal)



# In[ ]:




