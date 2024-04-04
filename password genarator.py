import secrets
import string
import random
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
print("Welcome to the Password Generator!")
password_len = int(input("Enter the length for the password: "))
selection_list = ""
use_letters = input("Include letters? (Y/N): ")
use_numbers = input("Include numbers? (Y/N): ")
use_symbols = input("Include symbols? (Y/N): ")
if use_letters == "Y":
    selection_list += letters
if use_numbers == "Y":
    selection_list += digits
if use_symbols == "Y":
    selection_list += special_chars
password = ""
for i in range(password_len):
    password += random.choice(selection_list)
print("Password:", password)
