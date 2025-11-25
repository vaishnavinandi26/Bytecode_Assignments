#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1.Core Billing Logic (Using if-else and if)
item_name=input("Enter item name:")
quantity=int(input("Enter quantity:"))
price=int(input("Enter price:"))
subtotal=price*quantity
if quantity>0:
    print(subtotal)
else:
    print("invalid")
if quantity>10:
    Discount=0.05*subtotal
    print("subtotal after applying discount:",subtotal-Discount)
else:
    print("Discount=0")
loyal=input("is the customer is loyal :(yes/no):")
total=subtotal-Discount
if loyal=="yes":
    l_discount=0.10*total
    print("Loyal discount:",l_discount)
else:
    l_discount=0
    print("Loyal discount:",l_discount)

final_bill=total-l_discount
print("final bill",final_bill)


# In[4]:


#2.Tiered Discounts & Surcharges (Using if-elif-else / match-case)
Total=int(input("Enter total purchase:"))
if Total<100:
    Discount=0
    print("Discount is",Discount)
elif Total<500:
    Discount = 0.05 * Total
    print("Discount is:",Discount)
elif Total<1000:
    Discount = 0.10 * Total
    print("Discount is:",Discount)
else:
    Discount = 0.15 * Total
    print("Discount is:",Discount)
paymethod=input("Enter payment type")
Fee=0
cash_discount=0
match(paymethod):
    case "Credit Card":
        Fee=0.01*Total
        Final=Total-Fee-cash_discount
        print("Fee is:",Final)
    case "Debit Card":
        Fee=0.01*Total
        Final=Total-Fee-cash_discount
        print("Fee is:",Final)
    case "Cash":
        Fee=0.05*Total
        Final=Total-Fee-cash_discount
        print("Fee is:",Final)
    case _:
        print("No discount")


# In[19]:


#3.Special Conditions (Using Nested if)
is_delivery=input("Is deliver required? (y/n):")
is_premium=input("Is customer is a premium member? (y/n):")
Total=eval(input("Enter total value:"))
if is_delivery:
    if Total>500:
        print("Delivery Fee is: 0")
    else:
        print("Delivery Fee is 50")
else:
    print("No delivery Delivery Fee is: 0")
if is_premium:
    if Total>200:
        delivery_fee=0
        print("Free delivery for large orders",delivery_fee)
    else:
        deliver_fee=50
        print("Delivery Fee is 50")
else:
    print("Delivery Fee is 0 if not delivered")
if is_premium:
    if Total>200:
        Bonus_points=50
        print("Bonus_points:",Bonus_points)
    else:
        Bonus_points=10
        print("Bonus_points:",Bonus_points)
else:
    Normal_Points=5
    print("Normal_points:",Normal_Points)
        
        
    


# In[13]:


#4.Tax/VAT Calculation (Using match-case or if-elif-else)
subtotal=eval(input("Enter subtotal:"))
category=input("Enter the category(Essentials/Luxury_Goods/Electronics):")
match(category):
    case "Essentials":
        tax=subtotal*0.05
        total=subtotal+tax
        print("Total price of product is:",total)
    case "Luxury_Goods":
        tax=subtotal*0.20
        total=subtotal+tax
        print("Total price of product is:",total)
    case "Electronic":
        tax=subtotal*0.12
        total=subtotal+tax
        print("Total price product is:",total)
    case _:
        print("Invalid")
tax_amount=subtotal*tax
print("Tax_amount:",tax_amount)
        
        


# In[ ]:




