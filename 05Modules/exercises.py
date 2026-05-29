import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def generate_name(first_name, last_name) :
    space = " "
    full_name = first_name + space + last_name
    return full_name

print(generate_name("Dileep","Gowtham"))