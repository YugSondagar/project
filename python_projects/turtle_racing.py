import turtle
import time
import random


WIDTH,HEIGHT = 700,600
COLORS = ['red','green',"purple","cyan","orange","blue","yellow","black","pink","brown"]

def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2  to 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid please try again! ")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range, try again!")

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y>= HEIGHT //2 - 10:
                return colors[turtles.index(racer)]


def create_turtle(colors):
    turtles =[]
    spacingx = WIDTH // (len(colors)+1)
    for i,color in enumerate(colors):    #why enumerate bcoz it gives us value and index 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2+(i+1) *spacingx,-HEIGHT //2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles




def init_turtle():
    screen =  turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")


def main():
    racers = get_number_of_turtles()

    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    winner = race(colors)
    print("The winner is the turtle with color: ",winner)
    time.sleep(5)

if __name__ == "__main__":
    main()









# racer = turtle.Turtle()
# racer.speed(1)
# racer.shape('turtle')
# racer.color("yellow")
# racer.penup() # it will not show line
# racer.forward(100)
# racer.left(90)
# racer.pendown() # it will show line
# racer.backward(100)
# racer.sleep(5)
