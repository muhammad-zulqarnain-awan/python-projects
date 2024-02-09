import random

print("Welcome to the PyPassword Generator!")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','-','_']

no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))
no_digits = int(input("How many digits would you like in your password?\n"))

password_char = []

for i in range(no_letters):
    password_char.append(random.choice(letters))
for j in range(no_digits):
    password_char.append(random.choice(digits))
for k in range(no_symbols):
    password_char.append(random.choice(symbols))

random.shuffle(password_char)

password = ''
for char in password_char:
    password += char

print(f"Here is your password: {password}")