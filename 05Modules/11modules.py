# Day 11 : 30 Days of python programming 

## Exercises: Level 1



# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()) 
#   '1ee33d'


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# print(user_id_gen_by_user()) # user input: 5 5


# #output:

# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   

# print(user_id_gen_by_user()) # 16 5

# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).


# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form




## MY CODE FOR ALL EX1 PROBLEMS


#1

import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id


print(random_user_id())


#2



def user_id_gen_by_user():
    chars = int(input("Enter number of characters: "))
    ids = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits

    for i in range(ids):
        user_id = ''.join(random.choice(characters) for _ in range(chars))
        print(user_id)


user_id_gen_by_user()


#3




def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    rgb_color = f"rgb({red}, {green}, {blue})"

    return rgb_color


print(rgb_color_gen())







# Day 11 : 30 Days of python programming 

## Exercises: Level 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']





## MY CODE FOR ALL EX2 PROBLEMS


#1



def list_of_hexa_colors(num):
    hexa_colors = []

    for i in range(num):

        color = '#'

        for j in range(6):
            color += random.choice('0123456789abcdef')

        hexa_colors.append(color)

    return hexa_colors


print(list_of_hexa_colors(3))



#2

import random

def list_of_rgb_colors() :
    colours = []
    for _ in range (5) :
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colour = f"rgb({r},{g},{b})"
        colours.append(colour)
    return colours



#3


def generate_colors(color_type, n):
    colors = []

    for _ in range(n):
        if color_type == "hexa":
            color = "#" + ''.join(random.choice("0123456789abcdef") for _ in range(6))
            colors.append(color)

        elif color_type == "rgb":
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"rgb({r}, {g}, {b})"
            colors.append(color)

        else:
            return "Invalid color type. Use 'hexa' or 'rgb'."

    return colors



print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))







# Day 11 : 30 Days of python programming 

# Exercises: Level 3


# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.




## MY CODE FOR ALL EX3 PROBLEMS


#1



def shuffle_list(lst):
    shuffled = lst[:]  # copy original list
    random.shuffle(shuffled)
    return shuffled


# Example usage:
numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)
print("Shuffled list:", shuffle_list(numbers))



#2



def seven_unique_numbers():
    return random.sample(range(10), 7)



print(seven_unique_numbers())
