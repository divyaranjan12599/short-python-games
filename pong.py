import turtle

win = turtle.Screen()
win.title("Ping-Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# padle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# padle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5

# functions
def paddle_a_up():
    y = paddle_a.ycor() # returns y coordinates
    if y == 300:
        paddle_a.sety(-300)
    else:
        y+=20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor() # returns y coordinates
    if y == -300:
        paddle_a.sety(300)
    else:
        y-=20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # returns y coordinates
    if y == 300:
        paddle_b.sety(-300)
    else:
        y+=20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # returns y coordinates
    if y == -300:
        paddle_b.sety(300)
    else:
        y-=20
        paddle_b.sety(y)

# keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')

win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True :
    win.update()


    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+45 and ball.ycor() > paddle_b.ycor()-45):
        ball.setx(340)
        ball.dx += -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+45 and ball.ycor() > paddle_a.ycor()-45):
        ball.setx(-340)
        ball.dx += -1
    

# win.mainloop()