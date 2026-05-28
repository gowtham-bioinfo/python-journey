# Functions Practice


# for i in range (1,1001) :
#     print("Tanvi",)


# def greet (name, location) :
#     result = f"Hi There {name} Hows the Weather in {location}"
#     return result


# print(greet("Arya", "Banglore"))



# sen = input("Enter Input :").split(" ")

# print(len(sen))



# def  add_two_numbers (num1, num2) :
#     total = num1 + num2
#     return total

# print(add_two_numbers(5,6))




# def  area_of_circle (r) :
#     pi = 3.14
#     area = pi*r*r
#     return area

# print(area_of_circle(10))


# def convert_celsius_to_fahrenheit(celcius) :
#     faren = (celcius*9/5) + 32
#     return faren

# # print(convert_celsius_to_fahrenheit(18))


# def check_season (month) : 
#     if month == "November" or month == "December" or month == "January" or month == "Februavry" :
#         return "Winter"
#     elif month == "March" or month == "April" or month == "May" :
#         return "Summer"
#     elif month == "June" or month == "July" or month == "August" :
#         return "Spring"
#     elif month == "September" or month == "October" :
#         return "Autumn"
#     else :
#         print("Invalid Month")

# print(check_season("October"))



# def print_list (item) :
#     for i in item :
#         print(i)
    


# print_list([2,3,4,5])


def print_rev (item) :
    rev_lst = []
    for i in range (len(item)-1,-1,-1) :
        rev_lst.append(item[i])
    return rev_lst

print(print_rev([4,7,9,1]))



def rev_list (item) :
    reverse_list = []
    for i in range (len(item)-1,-1,-1) :
        reverse_list.append(item[i])
    return reverse_list

print(rev_list(["A", "B", "C"]))


def capitalize_list_items(items) :
    cap = []
    for i in items :
        cap.append(i.upper())
    return cap

print(capitalize_list_items("python"))


def added_lst (lst, item) :
    new = []
    for i in lst :
        new.append(i)

    new.append(item)
    return new

print(added_lst(["Mango", "Apple", "Orange", "Banana"], "Watermelon"))



def add_item (lst, item) :
    new = []
    for i in lst :
        new.append(i)
    new.append(item)
    return new
    
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], "Meat"))


def sum_of_numbers(n) :
    total = 0
    for i in range (1, n+1) :
        total += i
    return total

print(sum_of_numbers(5))



def  sum_of_odds(n) :
    odds = 0
    for i in range (1, n+1) :
        if i % 2 != 0 :
            odds += i
    return odds
    
print(sum_of_odds(7))







def sum_of_evns (n) :
    sum_evns = 0
    for i in range (1, n+1) :
        if i % 2 == 0 :
            sum_evns += i
    return sum_evns    

print(sum_of_evns(12))



def evens_and_odds(n) :
    evn = 0
    odd = 0
    for i in range (n+1) :
        if i % 2 == 0 :
            evn += i
        else :
            odd += i
    return f"Sum Of Evens {evn}\nSum Of Odds {odd}"

print(evens_and_odds(100))
            

def factorial (n) :
    fact = n*n
    return fact
print(factorial(8))


def greet(name = "Guest") :
    space = " "
    print("Hello ," + name + "!")
greet()
greet("Arya")

    
    
    
    
for i in range (1,21) :
    if i % 2 == 0 :
        print(i)

        
        
num = 5
for i in range (1,11) :
    print(num, "x", i, "=", num*i)


total = 0
for i in range (1,101) :
    total += i
print(total)


num = 0

while num <= 10 :
    print(num)
    num += 1


for i in range (1,6) :
    print("*" * i)


for i in range (1,6) :
    for j in range (1,6) :
        print("*", end= " ")   
    print() 


num = int(input("Enter Number :"))
fact = 1
for i in range (1,num+1) :
    fact = i * fact
print(fact)