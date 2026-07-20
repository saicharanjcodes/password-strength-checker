commonpasslist = ["supmanhoiw","huhwhatthere","whatwhatwhat","verycommonpass","password123","8letterbigpass"]
specialchars = "!@#$%^&*_+()?>:;}][}<~`."

def strength(password, score):
    if len(password) < 8:
        print("lenth should be greater than 8")
    else:
        print("length check passed")
        score += 1

        print("")

        print("characters check")
        print("-------------------------------")
        print("")

        if " " in password:
            print("no spaces alowed")
            return score
        else:
            print("spaces check passed")
            score += 1

        print("")

        if any(c.islower() for c in password):
            print("lowercase check passed")
            score += 1
        else:
            print("add lowercase letters")
            return score
        
        print("")
        
        if any(c.isupper() for c in password):
            print("uppercase check passed")
            score += 1
        else:
            print("add uppercase letters")
            return score
        
        print("")
        
        if any(c.isdigit() for c in password):
            print("digits check passed")
            score += 1
        else:
            print("suggestion: you could add digits")
        
        if any(c in specialchars for c in password):
            print("special character check passed")
            score += 1
        else:
            print("suggestion: you could add some special characters")

    return score
                
def points(score):
    if score < 4:
        return
    elif score == 4:
        print("Your password is basic")
    else:
        print("Your password is strong")



while  True:
    score = 0


    print("")
    print("Welcome to Password Strenth Checker")
    print("------------------------------------------------------------------------------------------")
    print("")

    enteredpass = input("Enter your password; ")


    if enteredpass in commonpasslist:
        print("password too common")
    else:
        score = strength(enteredpass, score)

        print("")
        points(score)
        print(f"Password strength score is: {score}")

    if score >= 4:
        break