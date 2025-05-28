import random
characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

emptylist = []
print("Welcome to the PyPassword Generator!\n\n")
charlen = int(input("How many Characters would you like in your password?\n"))
i = 0
password = ""
while i < charlen:
    password += random.choice(characters)
    i += 1
print(password)