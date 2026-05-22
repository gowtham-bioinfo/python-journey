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


