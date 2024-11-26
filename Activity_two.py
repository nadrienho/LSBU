#!/usr/bin/env python
# coding: utf-8

# In[1]:


mynum = input("Enter a number")


# In[2]:


pi = float(input("enter the value of pi"))
print(pi)


# In[2]:


for i in range (5):
    print(i)


# In[3]:


for i in range (11):
    print(i)


# In[4]:


for i in range (1,10):
    print(i)


# In[5]:


m = int(input("Enter the lower end of the range: "))
n = int(input("Enter the higher end of the range: "))
for i in range (m,n+1):
    print(i)


# In[6]:


m = int(input("Enter the lower end of the range: "))
n = int(input("Enter the higher end of the range: "))
p = int(input("Enter how many digits to step: "))
for i in range (m,n+1,p):
    print(i)


# In[7]:


count = 7
while count<= 17:
    print (count)
    count += 1


# In[8]:


i = 1
while i <= 28:
    print(i)
    i += 2  


# In[1]:

user_input = int(input("Enter a number: "))

count = 0

while count <= user_input:
    print(f"Count is: {count}")
    
    count += 1

print("Loop has finished!")



# In[ ]:
for num in range(16): #numbers btw 0 and 15 and break when we reach 10
    if num == 10:
        break 
    print(num)


# In[ ]:

for num in range(1, 19, 2): #Odd numbers btw 0 and 18 and breaks when we reach 12
    if num == 12:
        break 
    print(num)

# In[ ]:
# user inputs range
user_input = int(input("Enter a number: "))
half_range = user_input // 2

# For loop with count <= user_input
for count in range(user_input + 1):  # range goes from 0 to user_input
    if count == half_range:
        break  # Stop when count reaches half of the user input
    print(count)



# In[ ]:
#print numbers <= 9 except those not divisible by 2
count = 0

while count <= 9:
    if count % 2 != 0:  # Check if the number is not divisible by 2
        count += 1  
        continue  # Skiping the current iteration if the number is not divisible by 2
    print(count)  
    count += 1  

# In[ ]:
#  printing out only the even values less than or equal to 16
count = 0

while count <= 16:
    if count % 2 != 0:  # Check if the number is odd
        count += 1  
        continue  # Skiping the current iteration if the number is odd
    print(count)  
    count += 1  


# In[ ]:
def print_average(num1, num2, num3): #function that prints the average of 3 numbers
    average = (num1 + num2 + num3) / 3
    # Printing the average
    print(f"The average of {num1}, {num2}, and {num3} is: {average}")


# In[ ]:
def print_sum(num1, num2, num3, num4, num5):  # function that calculates the sum of five numbers
    total = num1 + num2 + num3 + num4 + num5
    print(f"The sum of {num1}, {num2}, {num3}, {num4}, and {num5} is: {total}")


# In[ ]:
import cmath  

def solve_quadratic(a, b, c): #function to solve a quadratic equation(ax^2+bx+c=0)
    # Calculating the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculating the two roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    print(f"The roots of the equation are: {root1} and {root2}")


# In[ ]:
def calculate_area_of_triangle(base, height):  # function to Calculate the area of the triangle
    area = 0.5 * base * height
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

# In[ ]:
import math  # Import the math module for the value of pi
def calculate_area_of_circle(radius):  # function to Calculate the area of the circle
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area}")

# In[ ]:
import math  

def calculate_volume_of_cylinder(radius, height):  # function to Calculate the volume of the cylinder
    volume = math.pi * radius**2 * height
    print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume}")


# In[ ]:
import math 

def calculate_earth_circumference():#function to calculate the circumference of earth
    radius_of_earth = 6371  # Mean radius of the Earth in kilometers
    circumference = 2 * math.pi * radius_of_earth
    print(f"The circumference of the Earth is approximately: {circumference} kilometers")


# In[ ]:


