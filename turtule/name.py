from turtle import*
import turtle
k=turtle.Screen()
t=turtle.Turtle()

t.reset()
t.pensize(5)
t.speed(25)
t.pencolor("red")
t.penup()
t.goto(-500,100)
#k
t.pendown()
t.right(90)
t.forward(150)
t.backward(75)
t.left(45)
t.forward(100)
t.backward(100)
t.left(90)
t.forward(100)
t.penup()
t.goto(-500,100)
#a   
t.penup()
t.goto(-390,100)
t.pendown()
t.lt(30)
t.bk(150)
t.forward(150)
t.lt(30)
t.bk(150)
t.forward(75)
t.lt(70)
t.forward(40)
t.pendown()
#n
t.penup()
t.goto(-340,100)
t.pendown()
t.lt(95)
t.fd(140)
t.bk(140)
t.lt(30)
t.fd(160)
t.lt(150)
t.fd(140)
#i
t.penup()
t.goto(-240,100)
t.pendown()
t.left(90)
t.bk(100)
t.fd(50)
t.lt(90)
t.fd(140)
t.rt(90)
t.fd(60)
t.bk(100)
#m
t.penup()
t.goto(-140,100)
t.pendown()
t.lt(90)
t.fd(140)
t.bk(140)
t.lt(30)
t.fd(140)
t.lt(130)
t.fd(140)
t.rt(150)
t.fd(140)
#o
t.penup()
t.goto(10,50)
t.pendown()
t.rt(10)
t.circle(60,None,60)
#z
t.penup()
t.goto(150,100)
t.pendown()
t.lt(90)
t.fd(100)
t.rt(130)
t.fd(150)
t.left(130)
t.forward(100)
#h
t.penup()
t.goto(260,-20)
t.pendown()
t.rt(90)
t.bk(120)
t.fd(60)
t.lt(90)
t.fd(90)
t.rt(90)
t.fd(60)
t.bk(120)
#i
t.penup()
t.goto(460,-20)
t.pendown()
t.left(90)
t.bk(100)
t.fd(50)
t.lt(90)
t.fd(120)
t.rt(90)
t.fd(50)
t.bk(100)
#ontimer(bye,1000)
t.hideturtle()
turtle.done()
