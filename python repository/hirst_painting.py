import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()
screen = turtle_module.Screen()
color_list = [(248, 247, 240), (239, 250, 245), (251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), (234, 165, 197), (121, 187, 159), (203, 31, 130), (12, 186, 212), (10, 46, 25), (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]
tim.setheading(225)
tim.forward(250) 
tim.setheading(0)
tim.speed("fastest")
number_of_dot = 100

for dot_count in range(1 , number_of_dot +1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0: 
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()

