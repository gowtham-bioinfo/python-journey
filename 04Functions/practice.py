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

# print(convert_celsius_to_fahrenheit(18))


def check_season (month) : 
    if month == "November" or month == "December" or month == "January" or month == "Februavry" :
        return "Winter"
    elif month == "March" or month == "April" or month == "May" :
        return "Summer"
    elif month == "June" or month == "July" or month == "August" :
        return "Spring"
    elif month == "September" or month == "October" :
        return "Autumn"
    else :
        print("Invalid Month")

print(check_season("October"))