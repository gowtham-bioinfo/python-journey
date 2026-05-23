# Day 10 : 30 Days of python programming 


#1
def add_two_nums(num1,num2) :
  total = num1 + num2
  print(total)
add_two_nums(67,29)  


#2
def calculate_area_of_circle(r) :
  PI = 3.14
  area = PI * r ** 2
  print(area)
  return area

calculate_area_of_circle(9)


#3
def add_all_nums(*args) :
   total = 0
   for item in args :
      if type (item) == int or type(item) == float :
         total += item
      else :
         return f"Error '{item}' is not a number"
   return total
   
print(add_all_nums(5,8,7))
print(add_all_nums(9,7,"Hello"))

#4
def convert (celcius) :
   farenheit = (celcius * 9/5) + 32
   return farenheit
print(convert(44))

#5

def check_season(month) :
    if month == "December" or month == "January" or month == "February" :
        return "Winter"
    if month == "March" or month == "April" or month == "May" :
        return "Spring"
    if month == "June" or month == "July" or month == "August" :
        return "Summer"
    else :
        return "Autumn"
    
print(check_season("August"))


#6

def calculate_slope (x1,y1,x2,y2) :
   slope = (y1-y2) / (x1-x2)
   return slope
print(calculate_slope(2,3,4,7))



#7

import math

def solve_quadratic_eqn (a,b,c) :
   d = b**2 - 4*a*c
   if d > 0 :
      x1 = (-b + math.sqrt(d)) /(2*a)
      x2 = (-b - math.sqrt(d)) /(2*a)
      return x1, x2
   elif d == 0 :
      x = -b /(2*a)
      return x
   else :
      return "No Real Solutions"
print(solve_quadratic_eqn(1,-5,6))



#8

def print_list(list) :
   for item in list :
      print(item)

print_list([8,5,7,3])      
   

# 9   
def reversed_list(list) :
   reversed_list = []
   for i in range (len(list)-1,-1,-1) :
      reversed_list.append(list[i])
   return reversed_list
print(reversed_list([4,7,9,1]))


def reversed_list (list) :
   reversed_list = []
   for i in range (len(list)-1,-1,-1) :
      reversed_list.append(list[i])
   return reversed_list
print(reversed_list(["A", "B", "C", "D", "E"]))


#10

def capitalize_list_items(list) :
   capitalize = []
   for items in list :
      capitalize.append(items.upper())
   return capitalize

print(capitalize_list_items(["t", "y", "p", "a"]))


#11
def add_item(lst,item) :
   added_lst = []
   for i in lst :
      added_lst.append(i)

   added_lst.append(item) 
   return added_lst

print(add_item(["Mango", "Apple", "Orange", "Banana"], "Watermelon"))                  
                  
                  

def add_items (lst, item) :
   food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
   for i in lst :
      food_stuff.append(i)
   food_stuff.append(item)
   return food_stuff

print(add_items([], 'Meat'))   



def add_items (lst,item) :
   numbers = [2, 3, 7, 9]
   for i in lst :
      numbers.append(i)
   numbers.append(item)
   return numbers

print(add_items([], 5))    
                  
                  
                  
# 12                  

def remove_item (lst, item) :
   food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'] 
   for i in lst :
      food_stuff.remove(i)
   food_stuff.remove(item)   
   return food_stuff
print(remove_item([], "Mango"))
                  

def remove_item (lst, item) :
   numbers = [2, 3, 7, 9]   
   for i in lst :
      numbers.remove(i)
   numbers.remove(item)                  
   return numbers

print(remove_item([], 9))               



#13 
                 
def sum_of_numbers (num) :
   total = 0
   for i in range (1, num+1) :
      total += 1
   return total
print(sum_of_numbers(5))                  
            

def sum_of_numbers (num) :
   total = 0
   for i in range (1, num + 1) :
      total += i
   return total
print(sum_of_numbers(100)) 


def sum_of_numbers (num) :
   total = 0
   for i in range (1, num+1) :
      total += i
   return total
print(sum_of_numbers(10))

#14


def  sum_of_evens (num) :
   even = 0
   for i in range (1, num+1) :
      if i % 2 == 0 :
         even += i
   return even
print(sum_of_evens(10))




def sum_of_odds (num) :
   odd = 0
   for i in range (1, num+1) :
      if i %2 != 0 :
         odd += i
   return odd
      
print(sum_of_odds(3))      



# EXCERCISE 2

#1
def evens_and_odds (num) :
   even = 0
   odd = 0
   for i in range (num + 1) :
      if i % 2 == 0 :
         even += i
      else :
         odd += i
   return f"The Sum Of All Evens {even} \nThe Sum Of All Odds {odd}"

print(evens_and_odds(100))


#2

def factorial (n) :
   result = 1
   for i in range (1, n+1) :
      result *= i
   return result
print(factorial(5))   

#3

def is_empty (item) :
   return len(item) == 0 

print(is_empty(" "))
print(is_empty([]))
print(is_empty(()))   


#4

def calculate_mean (num) :
   return sum(num) / len(num)

def calculate_median (num) :
   num = sorted(num) 
   n = len(num) 
   mid = n // 2
   if n % 2 == 0 :
      return (num[mid - 1] + num[mid])/2
   else :
      return num [mid]



def calculate_mode (numbers) :
   frequency = {}
   for num in numbers :
      frequency [num] = frequency.get(num,0) + 1
      
   max_count = max(frequency.values())
   for key, value in frequency.items() :
      if value == max_count :
         return key


def calculate_range (num) :
   return max(num) - min(num)      

def calculate_variance (num) :
   mean = sum(num) / len(num)
   sqr_diff = [(x - mean) ** 2 for x in num]
   return sum(sqr_diff) / len(num)


import math 
def calculate_std (num) :
   variance = calculate_variance(num)
   return math.sqrt(variance)


data = [1,2,2,3,4]
print(calculate_mean(data))
print(calculate_median(data))
print(calculate_mode(data))
print(calculate_range(data))
print(calculate_variance(data))
print(calculate_std(data))


#5

def greet (name = "Guest") :
   space = " "
   print("Hello, " +  name + "!")
greet()
greet("Arya")


#6
def show_args (**kwargs) :
   output = []
   for key, value in kwargs.items() :
      output.append(f"{key} : {value}")
   print("Recived", ",".join(output))
   
show_args(name="Alice", age=30, city="New York")



 







# def show_args (**kwargs) :
#    output = []
#    for key, value in kwargs.items() :
#       output.append(f"{key} :{value}")
#    print("Recived :",",".join(output))


# show_args(name="Alice", age=30, city="New York")
