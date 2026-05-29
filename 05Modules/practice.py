
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
        

user_id_gen_by_user()



import random 

def  rgb_color_gen() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return f"rgb {r} {g} {b}"