#!/usr/bin/env python
# coding: utf-8

# ```
# Q1. Write a program to accept percentage from the user and display the grade according to the following criteria: 
# ```
# | Marks           | Grade   |
# | --------------- | ------- |
# | >90             | A       |
# | >80 and <= 90   | B       |
# | >=60 and <= 80  | C       |
# | below 60        | D       |

# In[3]:


marks=int(input("enter your marks "))
if marks >90 :
    print("grade A")
elif marks >80 and marks <= 90 :
    print("grade B")
elif marks >= 60 and marks<= 80 :
    print("grade C")
else :
    print("grade C")


# ```
# Q2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria: 
# 
# ```
# | Tax             | Cost Price (In Rs.)   |
# | --------------- | -------               |
# | 15%             | > 100000              |
# | 10%             | > 50000 and <= 100000 |
# | 5%              | <= 50000              |
# 

# In[5]:


cost_price=int(input(" enter the cost price of your bike "))
if cost_price >100000 :
    print(" 15% road tax ")
elif cost_price > 50000 and cost_price <=100000 :
    print(" 10 % road tax ")
else  :
    print(" 5% road tax ")


# ```
# Q3. Accept any city from the user and display monuments of that city.
# 
# ```
# | City      | Monument  |
# | --------- | -------   |
# | Delhi     | Red Fort  |
# | Agra      | Taj Mahal |
# | Jaipur    | Jal Mahal |

# In[8]:


city=input("enter city name ")
if city == "Delhi" :
    print("monument present here is Red Fort ")
elif city=="Agra":
    print("monument present here is Taj Mahal")
elif city =="Jaipur":
    print("monument present here is Jal Mahal")


# ```
# Q4. Check how many times a given number can be divided by 3 before it is less than or equal to 10. 
# 
# ```
# 

# In[13]:


num = int(input("enter any number"))
counter = 0 
while num >10:
    num = num/3
    print(num)
    counter = counter+1
print(f'Times the Number can be divided by Three : {counter} times.')


# ### Q5. Why and When to use While loop in python give a detailed description with example
# Ans. The while loop in Python is used when one wants to repeatedly execute a block of code as long as a certain condition is correct . The loop continues to execute as long as the condition is True.For example :-
# 
# 
# 

# In[1]:


a=20
while a <=35 :
    print(a)
    a+=1


# #### Q6. Use nested while loop to print 3 different pattern. 

# In[9]:


#PATTERN 1 

a=int(input("enter number of rows "))
while a>0 :
    a-=1
    print("*"*a)


# In[6]:


#PATTERN 2

a=int(input('enter number of rows '))
b=1 
while a>0 :
    a-=1
    print(" "*a , end ="*"*b +"\n")
    b+=1


# In[8]:


# PATTERN 3 

a=int(input("enter number of rows "))
b=1
while a >0 :
    a-=1
    print(" "*a + "*"*b , end =" "*a +"\n")
    b+=2


# ```
# Q7. Reverse a while loop to display numbers from 10 to 1 
# ```
# 

# In[10]:


a=10
while a >0 :
    print(a)
    a-=1


# ```
# Q8. Reverse a while loop to display numbers from 10 to 1 
# ```

# In[11]:


a=10
while a >0 :
    print(a)
    a-=1


# In[ ]:




