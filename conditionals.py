<<<<<<< HEAD
# Day 9 : 30 Days of python programming | start = 7:20 pm| End  =  10:15pm

user = int(input("Enter Your Age :"))
if user >= 18 :
    print("You Are Old Enough To Drive :")
else :
    years_left = 18-user
    print(f"Wait for {years_left} More Years :")    

my_age = int(input("Enter My Age :"))
your_age = int(input("Enter Your Age :"))

if my_age > your_age :
    diff = my_age - your_age
    if diff == 1 :
         print("Iam 1 Year Older Than You.")
    else :
         print(f"Iam {diff} Years older Than You.")
elif your_age > my_age :
    diff = your_age - my_age
    if diff == 1:
        print("Your 1 Year Older Than Me.")   
    else :     
        print(f"Your {diff} Years older Than Me.")
else :
    print("We Are Same Age.")


a = int(input("Enter first Number :"))
b = int(input("Enter second Number :"))

if a > b :
    print(f"{a} is Greater Than {b}.")
elif a < b :
    print(f"{a} is Lesser Than {b}.")    
else :
    print(f"{a} is Equal To {b}.")    
    

score = int(input("Enter Students Score :"))

if 90 <= score <= 100 :
    grade = "A" 
elif 80 <= score <= 89 :
    grade = "B"
elif 70 <= score <= 79 :
    grade = "c"
elif 60 <= score <= 69 :
    grade = "D"
elif 0 <= score <= 59 :
    grade = "F"
else :
    grade = "Invalid score"
print("Grade",grade)


month = input("Enter the month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = ("Invalid Month")
print(f"The Season is {season}")


fruits = ["banana","orange","mango","lemon"] 
fruit= input("Enter a Fruit :").strip().lower() 
if fruit in fruits : 
    print("That Fruit Alredy exists in the List.")
else :
    fruits.append(fruit) 
    print("Modified List", fruits)


=======
## Day 8  : 30 Days of python programming

## Exercises: Level 1


Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
                                                                                                                                                                                          


  
## MY CODE FOR ALL PROBLEMS
## Exercises: Level 1  


  
age = int(input("Enter You Age :"))

if (age >=18 ):
    print("Your Old Enough To Drive")
else : 
    years_left = 18-age
    print(f"You need {years_left} more years to learn Drive")                                                                                                                                                           

                                                                                                                                                                                          
                                                                                                                                                                                          
                                                                                                                                                                                          
my_age = int(input("Enter My Age : "))
your_age = int(input("Enter Your Age : ")) 

if (my_age > your_age) :
    diff = my_age-your_age
    if diff == 1 :
        print("Iam 1 year Elder Than You  ")
    else :
        print(f"Iam {diff} years Elder than You")
elif (your_age > my_age) :
    diff = your_age-my_age
    if diff == 1 :
        print("You are 1 year older than me")
    else : 
        print(f"You are {diff} years Elder than me")        
else :
    print("We Are Same Age  ") 




num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter NUmber 2 :"))

if (num1 > num2) :
    print(f"{num1} is greater than {num2}")
elif (num1<num2) :
    print(f"{num1} is smaller than {num2}")
else :
    print("Both Are Equal")    





## Day 8  : 30 Days of python programming

## Exercises: Level 2

Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
    
                                                                                                                                            




    
## MY CODE FOR ALL PROBLEMS IN EX2 :
    

marks = int(input("Enter Your Maarks"))
if (marks >= 90) and (marks <= 100) :
    print("Grade A")
elif (marks >= 80)  and (marks <= 89) :
    print("Grade B")  
elif (marks >= 70)  and (marks <= 79) :
    print("Grade C")  
elif (marks >= 60)  and (marks <= 69) :
    print("Grade D")      
elif (marks >= 0)  and (marks <= 59) :
    print("Grade F")   
else :
    print("Invalid Marks")





month = input("Enter Month : ").strip().capitalize()

if month in ["September", "October", "November"] :
    print("Autumn")
elif month in ["December", "January", "February"] :
    print("Winter")     
elif month in ["March", "April", "May"] :
    print("Spring")
elif month in ["JUne", "July", "August"] :
    print("Summer")      
else :
    print("invalid Season")    





fruits = ['banana', 'orange', 'mango', 'lemon']

fruits = input("Enter Fruit : ").strip().capitalize()
if fruits in fruits :
    print('That fruit already exist in the list')
else :
    fruits.append(fruits)
print("Modified List : ", fruits)



## Day 8  : 30 Days of python programming

## Exercises: Level 3



Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.



## MY CODE FOR ALL PROBLEMS IN EX3 :

>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
<<<<<<< HEAD
    }
    } 

print(person["skills"][2])
result = "Python" in person ['skills']
print(result)


if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set) and not {'React'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")




age = int(input("Enter Your Age:"))
if age >= 18 :
    print("You are old enough to drive.")
elif age <= 18 :
    age-18
    print(f"You need {age} more years to drive.")    



















=======
    }}

if 'skills' in person :
    print(True)
    middle_index = len(person['skills']) // 2
    print(person['skills'] [middle_index])  



if 'skills' in person :
    print(True)
result = "Python" in person['skills'] 
print(result)



skills = person['skills']      

if "JavaScript" in skills and "React" in skills and len(skills) == 2 :
    print('He is a front end developer')
elif "Node" in skills and  "Python" in skills and "MongoDB" in skills :
    print('He is a backend developer')
elif "React" in skills and "Node" in skills and "MongoDB" in skills :
    print('He is a fullstack developer')

else :
     print("Unknown Title")


if person['is_married'] and person['country'] == "Finland" :
    print(f"{person['first_name']} {person['last_name']} lives in Finland and he is married ")
>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02






