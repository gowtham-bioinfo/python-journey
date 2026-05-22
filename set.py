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



A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
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
