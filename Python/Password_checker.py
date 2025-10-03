# Password Strength Checker
# This program checks if a given password is strong based on length and character types.

def check_password_strength(password):
    if " " in password:
        return "do not use spaces in your password"
    
    if len(password) < 8:
        return "Weak Password: Too short"

    upper = lower = digit = special = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        return "Strong Password"
    else:
        return "Weak Password: use a mixture of upper, lower, digit, and special characters"

while True:
    user_password = input("Enter a password to check: ")
    print(check_password_strength(user_password))

    choice = input("Do you want to check another password? (y/n): ").strip().lower()
    if choice == "y" or choice == "yes":
        continue
    elif choice == "n" or choice == "no":
        print("Exiting password checker")
        break
    else:
        input("Invalid input! Please type 'y' or 'n'.")
        if choice == "n" or choice == "no":
            print("Exiting password checker")
            break
        else:
            continue
        