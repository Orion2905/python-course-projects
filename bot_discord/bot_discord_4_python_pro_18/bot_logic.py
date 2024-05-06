import random

def gen_pass(pass_length):
    elements = "12345678890qwertyuioplkjhgfdsazxcvbnm+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password