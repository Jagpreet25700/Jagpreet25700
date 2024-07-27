from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500 , height = 400)
user_bet = screen.textinput(title = "Make your bet",prompt= "Which turtle will win the race? Enter the color: ")
print(user_bet)
colors = ["red","orange","green","blue","yellow","purple"]
y_postion = [-70,-40,-10,20,50,80]
all_turtle =[]

for turtle_index in range(0 ,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230,y = y_postion[turtle_index])
    all_turtle.append(new_turtle)
     
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Congratulations!!You won the bet.{winning_turtle} turtle has won the race.")
            else:
                print(f"Hard luck.You lost the bet.{winning_turtle} turtle has won the race.")    
        random_distance =random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()