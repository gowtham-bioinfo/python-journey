# Day 3 : 30 Days of python programming | start = 7:00 pm | End = 1:40 am

# Exercises - Day 3

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate t he string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Replace the word coding in the string 'Coding For All' to Python.
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 26214


 ## MY CODE FOR ALL THE QUESTIONS

# Day 3 : 30 Days of python programming | start = 7:00 pm | End = 1:40 am


word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
result ="'" + word1 +" "+ word2 +" " + word3 + " "+ word4 + "'"
print(result)


word1 = "Coding"
word2 = "For"
word3 = "All"
result = "'" +word1 + " " + word2 + " " + word3 +"'"
print(result)

company = "Coding for All "
print(company)
print(len(company))
print(company.upper())
print(company.lower())

text = "Coding for all "

print(text.capitalize())
print(text.title())
print(text.swapcase())
print(text.index("Coding"))
print(text.replace("Coding " , "Python"))

text ="Python For Everyone "
print(text.replace("Python For Everyone" , "Python For All"))


text = "Facebook , Google , Microsoft , Apple , IBM , Oracle, Amazon"


text = "Coding For All "
print(text[0])
print(text[-1])
print(text[10])

text = "Coding For All "

print(text.index("C"))
print(text.index("F"))
print(text.rfind("I"))

sentance = " You cannot end a sentence with because because because is a conjunction "
print(sentance.index("because"))
print(sentance.rindex("because"))

start = sentance.find ("because because because")
end = start + len("because because because ")
s_sentance = sentance[:start] + sentance [end:]
print(s_sentance)

sentance = " You cannot end a sentence with because because because is a conjunction "
print(sentance.find("because"))


text = "Coding for All"
print(text.startswith("Coding"))
print(text.endswith("Coding"))

text = ' Coding for All  '
print(text.strip())

sen = "I am enjoying this challenge \n I just wonder what is next ."

print("Dileep \t 18 \t india \t Atp" )

radius = 10
area = 3.14 * radius ** 2
print(f"The Area Of Cricle With Radius{area} meter square .")


# Day 4 : 30 Days of python programming : Practising Strings agian | start = 7:00 pm | End = 9:30 pm

word1 = ("Thirty")
word2 = ("Days")
word3 = ("Of")
word4 = ("Python")

print(f"'{word1} {word2} {word3} {word4} '")

word1 = "Coding"
word2 = "For"
word3 = "All"
print(f"' {word1} {word2} {word3} ' ")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper)
print(company.lower)
print(company.capitalize)
print(company.title)
print(company.swapcase)
print(company[::7])
print(company.index("Coding"))

text = "Coding For All"
print(text.replace("All ","Python" ))
print(text.split(" "))

text = "Facebook , Google , Microsoft , Apple , IBM , Oracle , Amazon"
print(text.split(","))

text = "Coding For All"
print(text[0])
print(text[-1])
print(text.index("C"))
print(text.index("F"))
print(text.rfind("l"))

sentance = "You cannot end a sentence with because because because is a conjunction"
print(text.find("because"))
print(sentance.rfind("because"))
result = (sentance[:31] + sentance[:54])
print(sentance.find("because"))

text = "Coding for All"
print(text.endswith("Coding"))
print(text.strip)

text1 = "30DaysOfPython"
print(text1.isidentifier())

text2 = "thirty_days_of_python"
print(text2.isidentifier())

libraries = ["Django","Flask","Bottle","Pyrimid","Falcon"]
result = " # " .join(libraries)
print(result)

sentance = "I am enjoying this challenges \n I just wonder what is next ."
print(sentance)

text = "Dileep\t250\tIndia\tAtp"
print(text)

radus = 10
area = 3.14 * radius ** 2
print(f"The Area Of Circle with Radius {radius} is {area} Meters square.")

a = 8
b = 6

print(f"{a}+{b} = {a + b}")
print(f"{a} - {b} = { a- b}")
print(f"{a} * {b} = { a * b}")
print(f"{a} / {b} = { a / b}")
print(f"{a} % {b} = { a % b}")
print(f"{a} // {b} = { a // b}")
print(f"{a} ** {b} = { a ** b}")










