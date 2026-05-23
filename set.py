<<<<<<< HEAD
# Day 7  : 30 Days of python programming  , start = 8:00 pm | End = 10:24 pm
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies_2 = {"Cognizant","GRT","Tata","AWS","Meta"}
it_companies.update(it_companies_2)
print(it_companies)

it_companies.remove('Google')
print(it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
st = A.union(B)
print(st)

=======
## Day 6  : 30 Days of python programming

## Exercises: Level 1


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard



## MY CODE FOR ALL PROBLEMS


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["AWS", "HP", "Cognizant", "JPMorgan"])
print(it_companies)

it_companies.remove("Facebook")
print(it_companies)



## Exercises: Level 2


Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely


## MY CODE FOR ALL PROBLEMS
>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
<<<<<<< HEAD
st = A.intersection(B)
print(A)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
st = A.union(B)
st = B.union(A)
print(st)
print(st)

del A,B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
st = A.symmetric_difference(B)
print(st)

age = [22, 19, 24, 25, 26, 24, 25, 24]

st=set(age)
print(st)

ist = [22, 19, 24, 25, 26, 24, 25, 24]
st = {19, 22, 24, 25, 26}
ist = len(ist)
st = len(st)

if ist > st :
    print("List one is Bigger")
elif st > ist :
    print("Set is Bigger")
else :
    print("Both Are Equal")


sentence = "I am a teacher and I love to inspire and teach people"

words =sentence.lower().split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))
=======

print(A.union(B))

A.intersection(B)
print(A)

print(A.issubset(B))
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

del A
del B



## Exercises: Level 3


Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


  
## MY CODE FOR ALL PROBLEMS  

sentance = "I am a teacher and I love to inspire and teach people"  

words = sentance.split()
unq_words = set(words)
print(unq_words)

print(len(unq_words))





>>>>>>> 7f0c54f091ce3a1078d5ec07c7055bed5e810e02
