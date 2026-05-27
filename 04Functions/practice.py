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




    
