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


#8

def reverse_string(s):
    if len(s) <= 1:  
        return s
    return reverse_string(s[1:]) + s[0] 


text = "hello"
print("Reversed string:", reverse_string(text))



#9

def is_palindrome(s):
    if len(s) <= 1:  
        return True
    if s[0] != s[-1]:  
        return False
    return is_palindrome(s[1:-1])  


text = "radar"

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")



# 10

def multiply(a, b):
    if b == 0:  
        return 0
    return a + multiply(a, b - 1)  


num1 = 5
num2 = 4
print("Product =", multiply(num1, num2))




## Day 13 : 30 Days of python programming

# Exercise 2 – Intermediate


# Write a recursive function to find the nth Fibonacci number.
# Write a recursive function to generate the Fibonacci series up to n terms.
# Write a recursive function to find the greatest common divisor (GCD) of two numbers.
# Write a recursive function to convert a decimal number to binary.
# Write a recursive function to find the sum of elements in a list.
# Write a recursive function to find the maximum element in a list.
# Write a recursive function to count occurrences of a given element in a list.
# Write a recursive function to check if a list is sorted.
# Write a recursive function to flatten a nested list.
# Write a recursive function to search for an element in a list.




## MY CODE FOR ALL EX2 PROBLEMS


#1

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  


#2

def fibonacci_series(n, series=None):
    if series is None:
        series = []

   
    if len(series) == n:
        return series

  
    if len(series) == 0:
        series.append(0)
    elif len(series) == 1:
        series.append(1)
    else:
        series.append(series[-1] + series[-2])

    return fibonacci_series(n, series)



print(fibonacci_series(6)) 


#3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, 18))  