from turtle import *
colors=["red","blue","green","yellow","purple"]
for i in range(300):
    pencolor(colors[i%5])
    width(i/100+1)
    forward(i)
    left(59)
exitonclick()
