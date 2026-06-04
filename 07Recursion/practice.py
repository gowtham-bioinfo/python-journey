#1Factorial

def fact(n) :
    if (n == 1 or n == 0) :
        return 1
    return fact (n-1) * n
print(fact(4))


#2Sum
def calc_sum (n) :
    if (n == 0) :
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(5)

print(sum)


#3List
def print_list(list, idx=0) :
    if (idx == len(list)) :
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Mango", "Banana", "Apple", "Orange"]

print(fruits)



def factorial(x) :
    if (x == 1) :
        return 1
    else :
        return x * factorial(x-1)
print(factorial(10))




#4

def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    return factorial(n-1) * n

print(factorial(4))



def sum_of_n(n) :
    if n == 0 :
        return 0
    return sum_of_n(n-1) + n
print(sum_of_n(4))


def print_numbers (n) :
    if n == 0 :
        return
    print(n)
    print_numbers(n-1) 

print_numbers(5)


def print_numbers (n) :
    if n == 0  :
        return
    print_numbers(n-1)
    print(n)

print_numbers(5)

def factorial (n) :
    if (n == 1 or n == 0) :
        return 1
    return factorial(n-1) * n

print(factorial(4))



def power(x, n):
    if n == 0:  
        return 1
    return x * power(x, n - 1)  


base = 2
exponent = 5
print(f"{base}^{exponent} =", power(base, exponent))


def sum_of_digits(n):
    if n == 0:  
        return 0
    return (n % 10) + sum_of_digits(n // 10)  

num = 12345
print("Sum of digits =", sum_of_digits(num))




def reverse_string(s):
    if len(s) <= 1:  
        return s
    return reverse_string(s[1:]) + s[0] 


text = "hello"
print("Reversed string:", reverse_string(text))




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


def multiply(a, b):
    if b == 0:  
        return 0
    return a + multiply(a, b - 1)  


num1 = 5
num2 = 4
print("Product =", multiply(num1, num2))





def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  




def factorial(n) :
    if (n == 1 or n == 0) :
        return 1
    return factorial(n-1) * n
print(factorial(5))


def sum_of_nat(n) :
    if (n == 0) :
        return 0
    return sum_of_nat(n-1) + n
print(sum_of_nat(5))


def calc_sum(n) :
    if (n == 0) :
        return 0
    return calc_sum(n-1) + n
print(calc_sum(5))



def power (x, n) :
    if n == 0 :
        return 1
    return x * power(x, n-1)

print(power(4,5))


def sum_of_digits(n) :
    if n == 0 :
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(8))