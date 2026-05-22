
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
