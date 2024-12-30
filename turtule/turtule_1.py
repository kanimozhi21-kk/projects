'''import turtle
s=turtle.Turtle()
s.speed(4)
s.pensize(5)
for x in range(20):
    for x in range(2):
        s.forward(100)
        s.right(50)
        s.backward(20)
        s.left(70)
turtle.done()'''

'''import turtle
s=turtle.Turtle()
s.speed(5)
s.pensize(2)
for x in range(37):
    for x in range(1):
        s.forward(100)
        s.right(90)
    s.right(20)
turtle.done()'''
'''import turtle
s=turtle.Turtle()
s.speed(5)
s.forward(100)
s.backward(50)
s.right(90)
s.dot()
s.forward(100)
s.home()
s.goto(50,50)
s.shape("circle")
s.left(750)
s.right(75)
s.forward(70)
s.right(70)
s.forward(110)
turtle.done()''' 


'''import turtle
t=turtle.Turtle()
t.penup()
t.setpos(-10,30)
t.pendown()
t.pensize(10)
t.pencolor("blue")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()'''

'''import turtle
colors=["violet",'blue',"sky blue","red","white"]
sketch=turtle.Pen()
turtle.bgcolor("black")
for i in range(100):
    sketch.color(colors[i % 5])
    sketch.width(1/100+1)
    sketch.forward(i)
    sketch.left(59)
turtle.done()'''

'''import turtle
t=turtle.Turtle()
color=["red","white","blue"]
turtle.setup(800,800)
t.speed(0.5)
t.width(3)
turtle.bgcolor("black")
for j in range(10):
    for i in range(15):
        t.color([i/15,j/25,1])
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
turtle.done()'''

'''import turtle
t=turtle.Turtle()
t.penup()
#t.setpos(-20,40)
t.pendown()
t.pensize(5)
t.pencolor("green")
t.forward(110)
t.backward(110)
t.right(90)
t.forward(100)
t.left(90)
t.forward(110)
t.right(90)
t.forward(110)
t.right(90)
t.forward(110)'''

turtle.done()
        
