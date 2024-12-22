def password_strength(password):
    score = 0
    special_characters=["!","@","#","$","%","^","&","*"]
    if len(password)>15:
        score += 3
    elif len(password) <=15 and len(password)>=12:
        score +=2
        print("You can improve your password")
    else:
        score -=2
        print("make your password atleat 12 characters")
    
    if any(char.islower() for char in password):
        score +=2
    else:
        print("use of lowercase letters")
    if any(char.isupper() for char in password):
        score +=2
    else:
        print("use of uppercase letters")
    if any(char.isdigit() for char in password):
        score +=2
    else:
        print("use digits")
    if any(char in "!@#$%^&*" for char in password):
        score +=3
    else:
        print("Use special characters")
    if any(char in ["123","abc","ABC","qwert"] for char in password):
        score -= 5
        print("Avoid using common patterns")
    
    if score >=8:
        print("Strong password")
    elif 4<=score<=7:
        print("Moderate password")
    else:
        print("Weak password")
    
    return score


    
password = input("Enter password:")

sc = password_strength(password)

print(f"score is {sc}")






















