import turtle
import time
import requests
import json

def init_turtle():
    screen = turtle.Screen()
    screen.setup(800,600)
    screen.title("Weather App")
    turtle.Screen().bgcolor("black")
    turtle.color("white")
    turtle.hideturtle()
    
def main():
    api_key="d10d8970e18029c560918300b9fbcf3a"

    init_turtle()

    city = turtle.textinput("City Input","Enter name of city: ")

    if not city:
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    r=requests.get(url)

    weather = json.loads(r.text)
    
    if r.status_code == 200:
        name = weather["name"]
        temperature = weather['main']['temp']
        winds = weather["wind"]["speed"]

        turtle.write(f" Name of the city: {name}\n Temperature :{temperature}\n Wind speed: {winds}", align="center",font=("Arial",16,"bold"))
    else:
        turtle.write("City not found!",align = "center", font = ("arial",16,"normal"))



    time.sleep(3)

if __name__ == "__main__":
    main()