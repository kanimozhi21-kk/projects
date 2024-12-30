from turtle import*
import colorsys
h=0.2
pensize(2)
bgcolor("black")

penup()
setpos(-100,250)
pendown()
speed(20)
for i in range(37):
    for i in range(10):
        c=colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.007
        bk(70)
        lt(-150)
    fd(70)
    rt(50)
    bk(100)
    lt(100)
    hideturtle()
done()
'''from turtle import*
import colorsys
tracer(20)
h=0.3
bgcolor("black")
pensize(3)
for i in range(180):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.006
    circle(190-i,90)
    rt(140)
    rt(140)
    circle(190-i,90)
    rt(50)
    hideturtle()
done()'''