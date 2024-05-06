import random
caratteri = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza = int(input("Scegli la lunghezza della password:"))

password = ""
for i in range(lunghezza):
    password += random.choice(caratteri)

print(password)