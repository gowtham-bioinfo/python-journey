# Loops Practice 
for i in range (0,11) :
    print(i)
 
i = 1
while i < 11 :
    print(i)
    i += 1


for i in range (1,7) :
    print("#" * i)

for i in range(1,8) :
    for j in range (1,8) :
        print("#",end = " ")
    print()

num = 5
for i in range (0,11) :
    print(num, "x", num, "=", i*i)    

lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for i in lst :
    print(i)

for i in range (0,100) :
    if i % 2 == 0 :
        print(i)

for i in range (0,100) :
    if i % 2 != 0 :
        print(i)


sum = 0
for i in range (0,101) :
    sum += i
    i += 1
print(f"The sum of all numbers is {i}")



all_evns = 0
all_odds = 0
for i in range (0,101) :
    if i % 2 == 0 :
        all_evns += i
    
    else :
        all_odds += i
print(f"The sum of all Evens is {all_evns}")     
print(f"The sum of all Odds is {all_odds}")        


