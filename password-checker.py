password = input("Enter your password: ")

medium_password = 3
strong_password = 5


def check_password_strength(pw):
    checks_passed = 0
    if len(pw) >= 8:
        checks_passed += 1
    if any(char.isdigit() for char in pw):
        checks_passed += 1
    if any(char.isupper() for char in pw):
        checks_passed += 1
    if any(char.islower() for char in pw):
        checks_passed += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in pw):
        checks_passed += 1
    return checks_passed


def evaluate_strength(checks):
    if checks >= strong_password:
        return "Strong"
    elif checks >= medium_password:
        return "Medium"
    else:
        return "Weak"

checks = check_password_strength(password)
strength = evaluate_strength(checks) 
print(f"Your password is: {strength}")