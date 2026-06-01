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

