<<<<<<< HEAD

# Day 8 : 30 Days of python programming | start = 9:32pm| End  = 11:34 pm
dog = {
"name" : "Daisy",
"color" : "Orange",
"breed" :"golden Retriver",
"Legs" : "4",
"age" : "4 Years",
"student" : {
   "maths" : "92",
   "phy" : "87",
   "eng" : "99",
}

}


studen_dict = {
    
"first_name" : "Dleep",
"last_name" : "Gowtham",
"gender" : "Male",
"age" : 20,
"marital_status" : "Not Married",
"skills" : ["Python"],
"country" : "India",
"city" : "Atp",

}
print(len(studen_dict))
print((studen_dict["skills"]))
studen_dict["skills"] = "Java"
print(studen_dict)
studen_dict["address"] = "Anantapur"
print(studen_dict)
print(list(studen_dict))
print(list(studen_dict))
values_ist = list(studen_dict.values())
print(values_ist)
print(studen_dict.items())
del studen_dict["first_name"]
print(studen_dict)
del studen_dict
=======
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
>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02
