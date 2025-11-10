## Author
#      Kartik Kumar

# password_strength_checker.py

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char in "!@#$%^&*()_+-=[]{};:'\",.<>?/\\|" for char in password):
    strength += 1

if strength <= 1:
    print("Password is WEAK ❌")
elif strength == 2:
    print("Password is MODERATE ⚠️")
else:
    print("Password is STRONG ✅")
