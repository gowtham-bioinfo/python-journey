# Day 1: 30 Days of python programming | start = 7:00 pm | End = 12:00 am

first_name = "Dileep"
last_name = "Gowtham"
full_name = "Dileep Gowtham"
country = "India"
city = "Atp"
age = "20"
year = "2026"
is_married = "False"
is_true = "False"
is_light_on = "No"

print (first_name , last_name , full_name , country , city , age , year , is_married , is_true , is_light_on)



print( type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print (type({20,2,3}))
print(type(20))
print(type(2026))
print(type(1.4))
print(type([1,2,3]))

print(len(first_name))

first_name = "Dileep"
last_name = "Jenne"

if len(first_name) >len(last_name) :
    print(f"First Name is Larger")
elif len(last_name) > len(first_name) :
    print(f"Last Name is Larger")
else :
    print(f"Both are equal")


num1 = 5
num2 = 4

total = num1 + num2
diff = num1-num2
product = num2 * num1
division = num1 / num2
remainder = num2 % num1
exp = num1 ** num2
floor_division = num1 // num2

print("total :" , total)
print("diff :" , diff)
print("product :" ,product)
print("divsion :" ,division)
print("remainder :" , remainder)
print("exp :" , exp)
print("floor_division :" , floor_division)


import math

radius = 30

area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print("area_of_circle :" ,area_of_circle )
print("circum_of_circle :", circum_of_circle )

import math
radius = float(input("Enter radius :"))
area = math.pi * radius ** 2
print("Area of Circle :" , area)


first_name = input("Enter first name :")
last_name = input("Enter last name :")
full_name = input("enter full name :")
country = input("Enter Country")
city =input("Enter city name :")
age = int(input("Enter Age :"))
year = int(input("Enter year :"))
is_married = ("Enter statement :")
is_true = input("Enter statement")
is_light_on = input("Enter value :")