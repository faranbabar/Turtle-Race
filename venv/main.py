from turtle import Turtle, Screen
import random
colors=["red","green","blue","purple","yellow","black","violet","orange"]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput("Make your Bet","Which color turtle will win")
y_pos = [140,100,60,20,-20,-60]
turtles=[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-235,y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])

if user_bet:
    is_race_on = True
while is_race_on:
    for i in turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The winning color is {winning_color},your color is {user_bet}")
            else:
                print(f"You have lost. The winning color is {winning_color}, your color is {user_bet}")
        ran_dist=random.randint(0,10)
        move=random.choice(turtles)
        move.forward(ran_dist)
screen.exitonclick()
