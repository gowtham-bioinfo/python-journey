
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
