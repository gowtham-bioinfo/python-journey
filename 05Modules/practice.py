
def generate_name(first_name, last_name) :
    space = " "
    full_name = first_name + space + last_name
    return full_name



import random
import string

def random_user () :
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(6))


import random
import string

def user_id_gen_by_user () :
    char = int(input("Enter Characters :"))
    count = int(input("Enter Numbers Of ID's :"))

    characters = string.ascii_letters + string.digits

    for _ in range (count) :
        print("".join(random.choice(characters) for _ in range (char)))
        

# user_id_gen_by_user()   # made this comment to run file in exercsies , like import you can comeent out and run it here it self



import random 

def  rgb_color_gen() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return f"rgb {r} {g} {b}"

# print(rgb_color_gen())     # made this comment to run file in exercsies , like import you can comeent out and run it here it self


import random

def list_of_hexa_colors() :
    hex = "0123456789abcdef"
    colours = []

    for _ in range (5) :
        colour = "#"+"".join(random.choice(hex) for _ in range (6))
        colours.append(colour)
    return colours
    
# print(list_of_hexa_colors())   # made this comment to run file in exercsies , like import you can comeent out and run it here it self
 
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

# print(list_of_rgb_colors())    # made this comment to run file in exercsies , like import you can comeent out and run it here it self


import random 

def generate_colour(colour_type, count) :
    colours = []
    if colour_type == "hexa" :
        hex_char = "0123456789abcdef"
        for _ in range (count) :
            colour = "#"+ "".join(random.choice(hex_char)for _ in range(6))
            colours.append(colour)
        return colours
    elif colour_type == "rgb" :
        for _ in range (count) :
            r = random.randint(0,255) 
            g = random.randint(0,255) 
            b = random.randint(0,255) 
            colour = f"rgb({r},{g},{b})"
            colours.append(colour)
        return colours
    
print(generate_colour("hexa", 5))
print(generate_colour("rgb", 3))

import random

def shuffle_list (item) :
    random.shuffle(item)
    return item

numbers = [1,2,3,4,5]
# print(shuffle_list(numbers))
