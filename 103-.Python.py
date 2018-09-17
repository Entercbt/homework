import turtle
snakeColor = ["black","purple","red","green","blue"]
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(snakeColor[i])
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
    
i = i + 1
turtle.pencolor(snakeColor[i % 5 ])
turtle.circle(40, 80/2)
turtle.fd(40)

i = i + 1
turtle.pencolor(snakeColor[i % 5 ])
turtle.circle(16, 180)
turtle.fd(40 * 2/ 3)
