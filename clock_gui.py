import time
import turtle
from gammafactor import gamma, vo
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1200,height=600)
# wn.title("Simple anolog clock by using turtle modue using python in windows.")
wn.tracer(0)
h=00
m=00
s=00
ho=00
mo=00
so=00
#Creating our drawing pen
pen=turtle.Turtle()
pen.speed(0)
pen.pensize(3)
from datetime import datetime


def titles(pen):
    pen.color("#c82b5a")
    pen.penup()
    pen.goto(-300,-260)
    pen.pendown()
    pen.write("Actual Clock",False,"center",font=("Roboto",16,"bold"))
    pen.penup()
    pen.goto(300,-260)
    pen.pendown()
    pen.write("Relative Clock",False,"center",font=("Roboto",16,"bold"))
    pen.penup()
    pen.goto(-300,250)
    pen.pendown()
    pen.write(( f"{'{0:0=2d}'.format(h)} : {'{0:0=2d}'.format(m)} : {'{0:0=2d}'.format(s)}"),False,"center",font=("Roboto",16,"bold"))
    pen.penup()
    pen.goto(300,250)
    pen.pendown()
    pen.write(( f"{'{0:0=2d}'.format(ho)} : {'{0:0=2d}'.format(mo)} : {'{0:.2f}'.format(so)}"),False,"center",font=("Roboto",16,"bold"))
    pen.penup()


def draw_clock( h, m, s, pen):
    #Draw the clock face
    pen.penup()
    pen.goto(-300,210)
    pen.setheading(180)
    pen.color("#ffd300")
    pen.pendown()
    pen.circle(210)


    #Draw the lines for the hours
    pen.penup()
    pen.goto(-300,0)
    pen.setheading(90)
    pen.hideturtle()


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(-300,0)
        pen.rt(30)

    # Draw,the hour hand
    pen.penup()
    pen.goto(-300,0)
    pen.color("#33135c")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw,the minute hand
    pen.penup()
    pen.goto(-300,0)
    pen.color("#652ec7")
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw,the second hand:
    pen.penup()
    pen.goto(-300,0)
    pen.color("#de38c8")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(179)
    pen.penup()

def draw_clock2( h, m, s, pen):
    #Draw the clock face
    pen.penup()
    pen.goto(300,210)
    pen.setheading(180)
    pen.color("#ffd300")
    pen.pendown()
    pen.circle(210)


    #Draw the lines for the hours
    pen.penup()
    pen.goto(300,0)
    pen.setheading(90)
    pen.hideturtle()


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(300,0)
        pen.rt(30)

    # Draw,the hour hand
    pen.penup()
    pen.goto(300,0)
    pen.color("#33135c")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw,the minute hand
    pen.penup()
    pen.goto(300,0)
    pen.color("#652ec7")
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw,the second hand:
    pen.penup()
    pen.goto(300,0)
    pen.color("#de38c8")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(179)
    pen.penup()

while True:
    if s<60:
        s+=1
        if s==60:
            s=0
            m+=1
            if m==60:
                h+=1
                m=0
                if h==12:
                    h=0
    if so<60:
        so+=(1/gamma)
        if so>=60:
            so=0
            mo+=1
            if mo==60:
                ho+=1
                mo=0
                if ho==12:
                    ho=0

    draw_clock( h, m, s, pen)
    draw_clock2( ho, mo, so, pen)
    titles(pen)
    wn.update()
    time.sleep(.5)
    pen.clear()


wn.mainloop()
