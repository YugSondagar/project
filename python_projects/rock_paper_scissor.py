import random

user_wins = 0

computer_wins = 0

game = ["rock","scissor","paper"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in game:
        print("please re-enter")
        continue
    random_number = random.randint(0,2)

    computer_guess = game[random_number]
    print(f"Computer picked: {computer_guess}")

    if user_input == "rock" and computer_guess == "scissor":
        print("User won!")
        user_wins += 1
    elif user_input == "paper" and computer_guess =="rock":
        print("User won!")
        user_wins += 1
    elif user_input == "scissor" and computer_guess =="paper":
        print("User won!")
        user_wins += 1
    else:
        print("Computer won!")
        computer_wins += 1

print(f"User score: {user_wins}")
print(f"Computer score: {computer_wins}")
print("GoodBye!")
