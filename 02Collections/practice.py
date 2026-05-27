# Set Practice 

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)
it_companies.update(["AWS", "JP Morgan", "Deliotte", "Veetech"])
print(it_companies)

print(it_companies)


a = "Dileep"
b = "Gowtham"

jn = a + b
print(jn)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

st = A.intersection(B)
print(st)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

st = B.issubset(B)
print(st)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

st = A.isdisjoint(B)
print(st)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


jn = a+b
b = jn
print(b)


age = [22, 19, 24, 25, 26, 24, 25, 24]
st = {19, 22, 24, 25, 26}
lst = len(age)
st = len(st)




if lst > st :
    print("List Is Bigger")
elif st > lst :
    print("Set Is Biiger")
else :
    print("Both are Equal")



# Dictionary Practice :

dog = {

"name" : "Daisy",
"color" : "Golden Brown",
"breed" : "Shepherd",
"legs" : "Good",
"age" : "4",

}

student = {
    "first_name" : "Dileep",
    "last_name" : "Gowtham",
    "gender" : "Male",
    "skills" : ["Python", "Linux",  "Anatomy", "Git"],
    "age" : "20",
    "martial_Status" : "Unmarried",
    "Country" : "India",
    "city" : "Anantapur",
    "Address" : "Uma Nagar"

}

print(len(student))
print(type(student["skills"]))

student["skills"].append("SQL")
print(student)

student["skills"].extend(["Bioinfo", "Blast"])
print(student)


print(list(student.keys()))
print(list(student.values()))



