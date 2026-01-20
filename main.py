#Password Strength Analyzer

#Analyzes its strength

#Explains why it's weak or strong

#Suggests concrete improvements

#Your program must check:

#Length

#Uppercase letters

#Lowercase letters

#Numbers
#Special characters

#Repeated characters

#Common patterns (like 123, password, qwerty)

def analyze_password(password):
    strength = 0
    feedback = []

    #check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("password is too short, use atleast 8 characters")

    #check for uppercase letters
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("add uppercase letters to your password")

    #check for lowercase letters
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("add lowercase letters to your password")
    
    #check for numbers
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("add numbers to your password")

    #check for special characters
    special_characters = "!@#$%^&*()_+-=[]{};:',.<>?/"
    if any(c in special_characters for c in password):
        strength += 1
    else:
        feedback.append("add special characters to your password")

    #check for repeated characters
    if len(set(password)) < len(password):
        feedback.append("avoid using repeating character")
    
    #check for commun patters
    common_patterns = ["123", "password", " qwerty", "abc"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("avoid using commun passwords like '123', 'password' or 'qwerty'")

    return strength, feedback


#main function
def main():
    password = input("Enter your password to analyze: ")
    strength, feedback = analyze_password(password)

    print(f"Password Strength: {strength}/7")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")
        
if __name__ == "__main__":
    main()
