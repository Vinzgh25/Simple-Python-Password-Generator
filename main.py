import random
import string

def generate_password(length, include_numbers=False, include_lowercase=False, include_uppercase=False, include_symbols=True):
    """Generate a random password"""
    if include_numbers and not include_lowercase and not include_uppercase and not include_symbols:
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(length))
    elif include_lowercase and not include_numbers and not include_uppercase and not include_symbols:
        letters = string.ascii_lowercase
    elif include_uppercase and not include_numbers and not include_lowercase and not include_symbols:
        letters = string.ascii_uppercase
    else:
        letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def verify_password(password):
    """Verify if the password is correct"""
    while True:
        user_input = input("Enter the password: ")
        if user_input == password:
            print("Password correct!")
            break
        else:
            print("Incorrect password, please try again.")

# Get user input for password length and options
while True:
    try:
        length = int(input("Enter the length of the password to generate (between 5-20): "))
        if length < 5 or length > 20:
            print("Please enter a length between 5-20.")
            continue
        include_numbers = input("Include numbers? (y/n) ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n) ").lower() == 'y'
        include_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n) ").lower() == 'y'
        break
    except ValueError:
        print("Please enter a valid number.")

# Generate password and verify with user
password = generate_password(length, include_numbers, include_lowercase, include_uppercase, include_symbols)
print(f"Generated password: {password}")
verify_password(password)

# Ask if user wants to generate a new password or quit
while True:
    new_password = input("Do you want to generate a new password? (y/n) ")
    if new_password.lower() == 'y':
        while True:
            try:
                length = int(input("Enter the length of the password to generate (between 5-20): "))
                if length < 5 or length > 20:
                    print("Please enter a length between 5-20.")
                    continue
                include_numbers = input("Include numbers? (y/n) ").lower() == 'y'
                include_lowercase = input("Include lowercase letters? (y/n) ").lower() == 'y'
                include_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'
                include_symbols = input("Include symbols? (y/n) ").lower() == 'y'
                break
            except ValueError:
                print("Please enter a valid number.")
        password = generate_password(length, include_numbers, include_lowercase, include_uppercase, include_symbols)
        print(f"Generated password: {password}")
        verify_password(password)
    elif new_password.lower() == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again.")