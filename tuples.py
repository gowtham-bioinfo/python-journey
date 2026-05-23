<<<<<<< HEAD

# Day 6  : 30 Days of python programming  , start = 8:56 pm | End = 11:08 pm

tup = ()
siblings= ("Arya", "Sonu","Laddu","Pani" ,"Ronnie","Honey")
print(type(siblings))

brothers = ("Arya","Laddu","Pani","Ronnie")
sisters = ("Sonu","Honey")
siblings = brothers + sisters 
print(f"Siblings", siblings)
print(len(siblings))

siblings= ("Arya", "Sonu","Laddu","Pani" ,"Ronnie","Honey")
family_members = siblings + ("Ramesh" , 'Varalakshmi')
print(family_members)


family_members = ('Arya', 'Sonu', 'Laddu', 'Pani', 'Ronnie', 'Honey', 'Ramesh', 'Varalakshmi')
*siblings,father,mother = family_members
print("Sibligs",siblings)
print("Father",father)
print("Mother",mother)

fruits = ("Apple","Banana","orange","Mango")
vegitables = ("Tomato","Carrot","Beans","Brinjal")
animals = ("Bear","Tiger","Lion","Deer")
food_stuff_tp = fruits + vegitables + animals
print(food_stuff_tp)

food_stuff_it = list(food_stuff_tp)
print(food_stuff_tp)


food_stuff_tp = ['Apple', 'Banana', 'orange', 'Mango', 'Tomato', 'Carrot', 'Beans', 'Brinjal', 'Bear', 'Tiger', 'Lion', ]
print(food_stuff_tp[5])
print(food_stuff_tp[0:3])
print(food_stuff_tp[-3:])


del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_country = "Estonia" in nordic_countries
print("Nodric Country" , nordic_country)

nordic_country = "Iceland" in nordic_countries
print("Nodric Country" , nordic_country)
=======
## Day 5  : 30 Days of python programming

## Exercises: Level 1


Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Unpack siblings and parents from family_members




## MY CODE FOR EXERCISE 1 PROBLEMS


tple = tuple()

sisters = ("Deepika", "Sonu", "Laddu", "Elina", "Rosy", "Mary")
brothers = ("Nihaan", "Avyukt", "Pani", "Gowtham", "Sohan")

siblings = sisters + brothers
print(f"Siblings : ", siblings)
print(len(siblings))

family_mem = siblings + ("Ramesh", "Varalakshmi")
print(family_mem)

father, mother, *siblings = family_mem
print("Father :", father)
print("Mother :", mother)
print("Sibligns", siblings)


## Exercises: Level 2
## Day 5  : 30 Days of python programming


Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')




## MY CODE FOR EXERCISE 2 PROBLEMS


fruits = ("Apple", "Orange", "Banana", "Grape", "Mango")
veg = ("Potato", "Tomato", "Onion", "Spinach","Garlic")
animal_pro = ("Meat", "Milk", "Eggs", "Honey")

food_stuff_tp = fruits + veg + animal_pro
print("Food_Stuff_TP :", food_stuff_tp)

print(list(food_stuff_tp))
print(len(food_stuff_tp))

middle = len(food_stuff_tp)//2
print(food_stuff_tp[middle])

first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-3:]

print(first_three)
print(last_three)

del food_stuff_tp
food_stuff_tp = ('Apple', 'Orange', 'Banana', 'Grape', 'Mango', 'Potato', 'Tomato', 'Onion', 'Spinach', 'Garlic', 'Meat', 'Milk')

does_exist = "Onion" in food_stuff_tp

print(does_exist)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

does_exist = 'Estonia' in nordic_countries 
exist = 'Iceland'  in nordic_countries
print(does_exist)
print(exist)



## EXTRA PRACTISE PROBLEMS

Question : 1
## WAP to ask the user to enter name of their 3 fav movies and stotre them in list

## Answer:

movies = []
movie1 = input("Enter Movie 1 : ")
movie2 = input("Enter Movie 2 : ")
movie3 = input("Enter Movie 3 : ")
movie4 = input("Enter Movie 4 : ")
movie5 = input("Enter Movie 4 : ")


movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
movies.append(movie4)
movies.append(movie5)

print(movies)


## Another Method


movies.append(input("Enter Movie 1 : "))
movies.append(input("Enter Movie 2 : "))
movies.append(input("Enter Movie 3 : "))
movies.append(input("Enter Movie 4 : "))
movies.append(input("Enter Movie 5 : "))

print(movies)

Question 2 :
## WAP to check if a list contains a palindrome of elements 
## A) [2,3,5,5]

## Answer :

list1 = [2,3,5,5]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1) :
    print("Palindrome")
else :
    print("Not Palindrome")   



 ## B) [1, "abc", "abc", 1]

list = [1, "abc", "abc", 1]

copy_list = list.copy()
copy_list.reverse()

if (copy_list == list) :
    print("Palindrome")
else :
    print("Not Palindrome"


Question 3 :
## WAP to count the number of students with the grade "A" in the following Tuple
## Store the above values in a list and sort them from "A" to "D"


["C", "D", "A", "A", "B", "B", "A"]

grade = ["C", "D", "A", "A", "B", "B", "A"]    
result = grade.count
print(result)

grade.sort()
print(grade)



>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02
