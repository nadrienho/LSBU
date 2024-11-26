#!/usr/bin/env python
# coding: utf-8

# In[18]:


myName = 'Adrien Ngassam'


# In[19]:


year = 2024


# In[20]:


pi = 3.14


# In[21]:


bool_ = True


# In[22]:


x =2; y = 3; z =5;


# In[23]:


print(x*y)
print(x-z)
print(x//z)
print(z/y)
print(y%z)


# In[24]:


earth_radius = 6371;
radius = earth_radius * 0.62137119
print (radius, 'miles')


# In[25]:


feet = 40000
meters = feet * 0.3048
print(meters)


# In[26]:


print(2+5*3/6-3)


# In[27]:


print((2+5)*3/6-3)


# In[28]:


print(2+5*3/(6-3)) 


# In[29]:


# Integer variable
a = 5

# String variable
b = "Hello"

# List variable
c = [1, 2, 3]

# Boolean variable
d = True

# Float variable
e = 3.14

# Dictionary variable
f = {"key": "value"}

print(a, type(a))  # Output: 5 <class 'int'>
print(b, type(b))  # Output: Hello <class 'str'>
print(c, type(c))  # Output: [1, 2, 3] <class 'list'>
print(d, type(d))  # Output: True <class 'bool'>
print(e, type(e))  # Output: 3.14 <class 'float'>
print(f, type(f))  # Output: {'key': 'value'} <class 'dict'>


# In[31]:


# Assigning a list to the variable a
a = [1, 2, 3]

# Assigning the value of a to another variable b
b = a

# Modify the list through the second variable b
b.append(4)
print("a:", a) 
print("b:", b)


# In[32]:


glass = 0.5
pull = 0.4
glass += pull
print(glass)
print(pull)


# In[33]:


glass = 0.5
pull = 0.4
glass *= pull
print(glass)
print(pull)


# In[34]:


glass = 0.5
pull = 0.4
glass /= pull
print(glass)
print(pull)


# In[35]:


glass = 5
pull = 4
glass %= pull
print(glass)
print(pull)


# In[38]:


glass = 23
pull = 4
glass //= pull
print(glass)
print(pull)


# In[41]:


num = 29
if num%2 == 0:
    print("The number is even")
else: 
    print("The number is ODD")


# In[45]:


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[ ]:




