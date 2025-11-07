import random

letters = list(range(65,91)) + list(range(97,123))
symbols = list(range(35,48)) + list(range(91,97)) + list(range(123,126))
numbers = list(range(0,10))

n_letters = int(input("Enter number of letters required: "))
n_symbols = int(input("Enter number of symbols required: "))
n_numbers = int(input("Enter number of numbers required: "))
password = []

for i in range(n_letters):
    password += chr(random.choice(letters))
for i in range(n_symbols):
    password += chr(random.choice(symbols))
for i in range(n_numbers):
    password += str(random.choice(numbers))
random.shuffle(password)
print("".join(password))

