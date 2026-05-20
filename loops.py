## Day 9 : 30 Days of python programming


Exercises: Level 1
Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.

Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers






## MY CODE FOR ALL EX1 PROBLEMS



for i in range (0,11) :
    print(i)

i = 1
while i <= 10 :
    print(i)    
    i += 1


for i in range (1,8) :
    print("#" * i)

for i in range (1,8) :
    for j in range (1,8) :
        print("#", end = " ")
    print()        

for i in range (0,11) :
    print(i, "x", i, "=", i*i)    


list = ['Python', 'Numpy','Pandas','Django', 'Flask']  
for char in list :
    print(char)  

for i in range (0,101) :
    if i % 2 == 0 :
        print(i)


for i in range (1,101) :
    if i % 2 != 0 :
        print(i)








## Day 9 : 30 Days of python programming


Exercises: Level 2


Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.






## MY CODE FOR ALL EX2 PROBLEMS 



sum = 0
for i in range (0,101) :
    sum += i
    i += 1
print("Sum Of All Numbers is =", sum)    



evn_sum = 0
odds_sum = 0

for i in range (0,101) :
    if i % 2 == 0 :
        evn_sum += i
    else :
        odds_sum += i
print("The sum of all evens is =", evn_sum)       
print("The sum of all odds is =", odds_sum) 





## Day 9 : 30 Days of python programming

## Exercises: Level 3




Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world







## MY CODE FOR ALL EX3 PROBLEMS 



for country in countries :
    if "land" in country :
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']

rev_fruits = []
for i in range (len(fruits)-1,-1,-1) :
    rev_fruits.append(fruits[i])
print(rev_fruits)











