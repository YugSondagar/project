import random

range_till_number = int(input("Enter range till you want: "))

if range_till_number<0:
        print("Enter number greater than 0")
        quit()

random_number = random.randint(0,range_till_number)

while True:
    num = int(input(f"Enter number till {range_till_number}: "))
    if num == random_number:
        print("You got it correct! ")
        break
    else:
        print("You got it wrong!")


