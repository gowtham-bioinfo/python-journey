## Day 7  : 30 Days of python programming

## Exercises: Level 1


Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries



## MY CODE FOR ALL PROBLEMS 

empty = {}
print(type(empty))

dog = {
"name" :"Daisy",
"colour" : "Golden Brown",
"breed" : "Golden Brown",
"lges" : "Good",
"age" : 4,
}

student = {
"first_name" : "Dileep",
"last_name" : "Gowtham",
"gender" : "Male",
"age" : 20,
"marital_status " : "Unmarried",
"skills" : ["Python", "Anatomy", "Physiology", "Terminology"],
"country" : "Inida",
"city" : "Anantapur", 
"address" : "Uma Nagar"
}



print(student)
print(len(student))

print(student["skills"])
print(type(student["skills"]))

print(len(student))



student["skills"].append("SQL")
print(student)

student["skills"].extend(["BioInfo, GitHub"])
print(student)

print(list(student))
print(list[student])

print(student.items())

del student["first_name"]
del student
