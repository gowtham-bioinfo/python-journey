## Day 10 : 30 Days of python programming

## Exercises: Level 1



Declare a function add_two_numbers. It takes two parameters and it returns a sum.
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
Write a function called calculate_slope which return the slope of a linear equation
Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.








## MY CODE FOR ALL EX1 PROBLEMS

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

#3
def add_all_nums(*args) :
   total = 0
   for item in args :
      if type(item) == int or type(item) == float :
         total += item
      else :
         return f"Error : '{item}' is not a Number"
   return total
   
print(add_all_nums(2,3,5))
print(add_all_nums(2,3, "Hello"))



#4

def convertor (celcius) :
   farenheit = (celcius * 9/5) + 32
   return farenheit
print(convertor(32))



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
print(calculate_slope(2,5,7,3))


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


