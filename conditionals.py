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

























