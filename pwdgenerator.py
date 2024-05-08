import string
import random

def generate_password(length, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

generator = True
while generator:
    length = int(input("Enter password length : "))
    include_upper = input("Include uppercase letters ? (y/n) : ").lower() == "y"
    include_lower = input("Include lowercase letters ? (y/n) : ").lower() == "y"
    include_digits = input("Include digits ? (y/n) : ").lower() == "y"
    include_special = input("Include special characters ? (y/n) : ").lower() == "y"
    
    password = generate_password(length, include_upper, include_lower, include_digits, include_special)
    print(f"Generated Password : {password}")
    print()
    
    generator = input("Do you want to create another password ? (y/n) : ").lower == "y"
