import turtle

def turtle_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def turtle_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def turtle_s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def turtle_d():
    turtle.setheading(360)
    turtle.forward(50)
    turtle.stamp()
def turtle_re():
    turtle.reset()
    turtle.color('blue')

    
turtle.shape('turtle')
turtle.color('red')

turtle.onkey(turtle_w,'w')
turtle.listen()
turtle.onkey(turtle_a,'a')
turtle.listen()
turtle.onkey(turtle_s,'s')
turtle.listen()
turtle.onkey(turtle_d,'d')
turtle.listen()
turtle.onkey(turtle_re,'Escape')
turtle.listen()


