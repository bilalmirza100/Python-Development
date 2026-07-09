import random
l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
s = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))
# easy level
# password = ""
# for char in range(1, letters + 1):
#     password += random.choice(l)
# for char in range(1, symbols + 1):
#     password += random.choice(s)
# for char in range(1, numbers + 1):
#     password += random.choice(n)
# print("Your password is: " + password)

# hard level
password_list = []
for char in range(1, letters + 1):
    password_list.append(random.choice(l))
for char in range(1, symbols + 1):
    password_list.append(random.choice(s))
for char in range(1, numbers + 1):
    password_list.append(random.choice(n))

random.shuffle(password_list)
password = ""
for char in password_list:
    password = password + char
print("Your strong password is: " + password)
