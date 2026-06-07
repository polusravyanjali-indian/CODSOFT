# CodSoft Task 3 - Password Generator
# Created by: Polu Sravyanjali

import random
import string

def generate_password(length):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("=" * 35)
print("   PASSWORD GENERATOR")
print("=" * 35)

while True:
    length = int(input("\nEnter password length: "))
    
    if length < 4:
        print("Password too short! Minimum 4 characters.")
    else:
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
        print(f"Password Length: {length}")
    
    again = input("\nGenerate another? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break