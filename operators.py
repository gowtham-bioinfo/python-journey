# Day 2 : 30 Days of python programming | start = 7:28 pm | End  = 12:20 am

# Question 1 :
# Declare Your Age, Height,Complex as Variable And Assign Value To It

age = 20
height = 5.8
comp = 18j

# Question 2 :
# find out Area Of Triangle
base = int(input("Enter Base :"))

height = int(input("Enter Height :"))
area = 0.5 * base * height
print(f"Area Of Triangle is {area}")

# Question 3 :
# find out Perimeter Of The Triangle

side_a = int(input("Enter Side A :"))
side_b = int(input("Enter Side B :"))
side_c = int(input("Enter Side C :"))
peri = side_a + side_b + side_c
print(f"Perimeter Of The Triangle is {peri}")

# Question 4 :
# find out Area of Rectangle and Perimeter of Rectangle 

length = int(input("Enter Length :"))
width = int(input("Enter Width :"))
area = length * width 
perimeter = 2 * (length + width)

print(f"Area of Rectangle is {area}")
print(f"Perimeter of Rectangle is {perimeter}")

# Question 5 :
# find out radius of circle 

radius = float(input("Enter Radius :"))
pi = 3.14
area = pi * radius * radius
c =  2 * pi * radius
print(f"Radius of Circle is {area}" )
print(f"Circumstances of Circle {c}")

# Question 6 :
# calculate the slop 

# y = 2x - 2

m = 2          # slope
y_intercept = -2
x_intercept = 1

print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Question 7 :
# length comparison and Falsy Comaparison 

python = "Python"
dragon = "Dragon"

print(len(python))
print(len(dragon))


a =len(python) != len(dragon)
print(a)

# Question 8 :
# and operator 

python = "Python"
dragon = "Dragon"

result = "on" in python and "on" in dragon 
print(result)

# Question 9 :
# in operator 

ab = "i hope this course is not full of jargon :"
result = "jargon" in ab
print(result)


python = "Python"
dragon = "Dragon"

result = "on" not in python and "on" not in dragon
print(result)

# Question 10 :
# Find the length of the text python and convert the value to float and convert it to string

text = "Python"
length = len(text)
fl = float(length)
st = str(fl)

print(length)
print(fl)
print(st)


# Question 11 :
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num1 = int(input("Enter a number :"))
if num1 % 2 == 0 :
    print("Even Number")
else :
    print("Odd Number")    

# Question 12 :
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.



num1 = 7/3
num2 = int(2.7)
print(num1==num2)

# Question 13 :
# Check if type of '10' is equal to type of 10

num1 = 10
num2 = 10
print(type(num1) == type(num2))

# Question 14 :
# Check if int of (9.8) is equal to 10

num1 = 9.8
num2 = 10
print(num1 == num2)

# Question 15 :
# Calculate pay of the person

hours = int(input("Enter Hours :"))
rate_per_hour = int(input("Enter Pay Per Hour :"))
result = hours * rate_per_hour
print(f"Pay Of The Person , {result}")

# Question 15 :
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

num_y = int(input("Number of Years :"))
seconds = num_y * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds ")

# Question 16 :
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range (1,6) :
    print(i , i**0 , i**1 , i**2 , i**3)

for i in range (9 , 11) : 
    print(i ** 1)  






