import turtle
import time
import random



delay = 0.1
#set up the screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)   #this turns off the screen updates and animations


#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#functions
def go_up():
   head.direction ="up"
def go_down():
   head.direction = "down"
def go_left():
   head.direction = "left"
def go_right():
   head.direction = "right"

def mov():
    if head.direction == "up":
       y = head.ycor()   # new variable y to store current y coordinate
       head.sety(y + 20) 
    if head.direction == "down":
       y = head.ycor()   # new variable y to store current y coordinate
       head.sety(y - 20) 
    if head.direction == "left":
       x = head.xcor()   # new variable y to store current y coordinate
       head.setx(x - 20) 
    if head.direction == "right":
       x = head.xcor()   # new variable y to store current y coordinate
       head.setx(x + 20) 


#keyboard bindings  --> binds keyboards with up,down,left,right
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")



#main loop
while True:
    wn.update()

    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       time.sleep(1)
       head.goto(0,0)
       head.direction = "stop"
       
       for segment in segments:
            segment.goto(1000,1000)
        #clearing segments
       segments.clear()

    #checking for collision with the food
    if head.distance(food) < 20:
       # move the food to a random spot
       x = random.randint(-290,290)
       y = random.randint(-290,290)
       food.goto(x,y)
       
       #add a segment
       new_segment = turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("grey")
       new_segment.penup()
       segments.append(new_segment)
    
    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
       x = segments[index-1].xcor()
       y = segments[index-1].ycor()
       segments[index].goto(x,y)
    
    #move segment 0 to where the head is
    if len(segments) > 0:
       x = head.xcor()
       y = head.ycor()
       segments[0].goto(x,y)

    mov()  # why mov is afterwards because we are first adding the segment then moving it
    
    #checking collision with body
    for segment in segments:
       if segment.distance(head) < 20:
          time.sleep(1)
          head.goto(0,0)
          head.direction = "stop"

            #hiding the segments
          for segment in segments:
             segment.goto(1000,1000)
          
          segments.clear()
        






    time.sleep(delay)


wn.mainloop()  #it will keep the screen open