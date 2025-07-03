import re

# List of common passwords (you can add more)
common_passwords = ['password', '123456', 'qwerty', 'letmein', 'admin']

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Your password should be at least 8 characters long.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Check for digit
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Check for special character
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (like ! @ # $ %).")

    # Check if password is common
    if password.lower() in common_passwords:
        score -= 1
        feedback.append("This password is too common. Choose something less obvious.")

    # Final assessment
    if score >= 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print("- " + tip)
