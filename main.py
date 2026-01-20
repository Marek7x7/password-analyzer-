#If you think this sounds boring, good. Boring projects force clean logic. This one teaches strings, functions, loops, dictionaries, file handling, and basic security thinking.
#Takes a password from the user

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

#main function
def main():
    password = input("Enter the password you want me to grade: ")
    strength, feedback = analyze_password(password)
    print(f"Password Strength: {strength}/6")
    for item in feedback:
        print(item)