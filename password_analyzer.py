import re
import random
import string

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

password = input("Enter Password: ")

strength = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if strength != "Strong":
    print("Suggested Strong Password:")
    print(generate_strong_password())
