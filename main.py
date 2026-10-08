import random
import string

alphabet = string.ascii_letters
number = string.digits
symbol = """!@#$%&*_-+=?./,`~'":;"""

characters = alphabet + number + symbol

length = int(input("Enter the length of the password: "))
password = ""

for char in range(length):
    password+= random.choice(characters)

print(password)