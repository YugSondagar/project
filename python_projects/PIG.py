import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = int(input("Enter number of players (2 to 4): "))
    if 2<= players <=4:
        break
    else:
        print("Invalid, try again!")
    
max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        print("\n Player number ",player_idx+1," turn just started! \n")

        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y): ")

            if should_roll.lower() != 'y':
                break
            value = roll()

            if value == 1:
                print("You rolled 1 turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a : ", value)
            
            print("Your score is: ",current_score)

        players_score[player_idx] == current_score

        print("Your ttal score is:",players_score[player_idx])

max_score = max(players_score)
winning_idx = players_score.index(max_score)  # it will give us at which index that player with highest score is
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)