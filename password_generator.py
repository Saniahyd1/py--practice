import random
import string
print("Password Generator")
length = int(input("Enter password length: "))
# Characters to use
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_chars = letters + digits + symbols
password = ""
for i in range(length):
    password += random.choice(all_chars)
print("\n Generated Password:", password)