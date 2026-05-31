# Day 13 : 30 Days of python programming 

# Exercise 1 – Basics
# Write a recursive function to calculate the factorial of a number.
# Write a recursive function to find the sum of the first n natural numbers.
# Write a recursive function to print numbers from n to 1.
# Write a recursive function to print numbers from 1 to n.
# Write a recursive function to calculate the power of a number (x^n).
# Write a recursive function to find the sum of digits of a number.
# Write a recursive function to count the number of digits in a number.
# Write a recursive function to reverse a string.
# Write a recursive function to check whether a string is a palindrome.
# Write a recursive function to find the product of two numbers using repeated addition.





## MY CODE FOR ALL EX1 PROBLEMS


#1

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1) 


num = 5
print("Factorial of", num, "is", factorial(num))



#2


def sum_natural(n):
    if n == 1:  
        return 1
    else:
        return n + sum_natural(n - 1)  


num = 5
print("Sum of first", num, "natural numbers is", sum_natural(num))



#3

def print_numbers(n):
    if n == 0:  
        return
    print(n)
    print_numbers(n - 1) 


print_numbers(5)


#4


def print_numbers(n):
    if n == 0: 
        return
    print_numbers(n - 1) 
    print(n)


print_numbers(5)


#5


def power(x, n):
    if n == 0:  
        return 1
    return x * power(x, n - 1)  


base = 2
exponent = 5
print(f"{base}^{exponent} =", power(base, exponent))


#6


def sum_of_digits(n):
    if n == 0:  
        return 0
    return (n % 10) + sum_of_digits(n // 10)  

num = 12345
print("Sum of digits =", sum_of_digits(num))



#7

def count_digits(n):
    if n < 10:  
        return 1
    return 1 + count_digits(n // 10)  


num = 12345
print("Number of digits =", count_digits(num))