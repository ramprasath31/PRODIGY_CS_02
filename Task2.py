import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak",
    }

    return strength_levels[strength], feedback

if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")