import turtle as t
import random
screen = t.Screen()
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)   

screen.exitonclick()