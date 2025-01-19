import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(0,24)
nr_symbols = random.randint(0,10)
nr_numbers = random.randint(0,10)

password = []
for i in range(0,nr_letters):
    password.append(random.choice(letters))
for sym in range(0,nr_symbols):
    password.append(random.choice(symbols))
for num in range(0,nr_numbers):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)

pas = ''
for i in password:
    pas += i
print("Your password is:",pas)
