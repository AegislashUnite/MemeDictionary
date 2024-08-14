import random
password = ""
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("¿Cuantos caracteres tendra tu contrasena?"))
for i in range(long):
    password += random.choice(characters)
print(password)
