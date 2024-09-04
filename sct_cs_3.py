

import re

def assess_password_strength(password):
    # Initialize strength score and criteria met counters
    strength_score = 0
    criteria_met = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "numbers": False,
        "special_characters": False
    }

    if len(password) >= 8:
        strength_score += 1
        criteria_met["length"] = True

    if re.search(r'[A-Z]', password):
        strength_score += 1
        criteria_met["uppercase"] = True

    if re.search(r'[a-z]', password):
        strength_score += 1
        criteria_met["lowercase"] = True

    if re.search(r'[0-9]', password):
        strength_score += 1
        criteria_met["numbers"] = True

    if re.search(r'[\W_]', password):
        strength_score += 1
        criteria_met["special_characters"] = True

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, criteria_met

def main():
    while True:
        password = input("Enter a password to assess its strength: ")
        strength, criteria_met = assess_password_strength(password)

        print(f"Password Strength: {strength}")
        print("Criteria met:")
        for criterion, met in criteria_met.items():
            print(f"  - {criterion.capitalize()}: {'Yes' if met else 'No'}")

        another = input("Do you want to assess another password? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
