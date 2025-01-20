print("Welcome to my Quiz")
score = 0
playing = input("Do you want to play ?  ")
if playing != 'yes':
    quit()
else:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "centeral processing unit":
        print("Correct! ")
        score = score + 1
    else:
        print("Incorrect")
        score = score -1

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphical processing unit":
        print("Correct! ")
        score = score + 1
    else:
        print("Incorrect")
        score = score -1

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct! ")
        score = score + 1
    else:
        print("Incorrect")
        score = score -1

    answer = input("What does ROM stand for? ")
    if answer.lower() == "read only memory":
        print("Correct! ")
        score = score + 1
    else:
        print("Incorrect")
        score = score -1

print("Your score is: ",score)
    



