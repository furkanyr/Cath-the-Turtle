import turtle
import time
from random import randint

pyt_screen = turtle.Screen()
pyt_screen.setup(700, 600)
pyt_screen.bgcolor("#6267D9")
pyt_screen.title("Catch The Turtle!")
pyt_screen.delay(0)

turtle_ = turtle.Turtle()
turtle_.shape("turtle")
turtle_.color("#B9F951")
turtle_.shapesize(1.7)
turtle_.penup()

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.setposition(0, 600 // 2 - 24)

score = 0
scr = turtle.Turtle()
scr.penup()
scr.hideturtle()
scr.setposition(0, 600 // 2 - 50)
scr.write(f"SCORE: {score}", align="center", font=("Verdana", 16, "bold"))

def time_display():
    if timer >= 0:
        t.write(f"TIME: {timer}", align="center", font=("Verdana", 12, "normal"))
        time.sleep(1)
    t.clear()

def rand_position():
    #Random Turtle konumu oluştur
    x = randint(-320, 320)
    y = randint(-280, 250)
    return [x, y]

def turtle_move():
    #gelen random (x, y) ikililerine göre Turtle'ı konumlandırma
    turtle_.setposition(rand_position()[0], rand_position()[1])

def compare_positions(click_posx, click_posy):
    #Click ve Turtle konumunu karşılaştırma
    scr.clear()
    global score
    if abs(click_posx - turtle_.xcor()) <= 25 and abs(click_posy - turtle_.ycor()) <= 25:
        score += 1
    scr.write(f"SCORE: {score}", align="center", font=("Verdana", 16, "bold"))

timer = 20
while timer > 0:
    turtle_move()
    pyt_screen.onclick(fun=compare_positions)
    time_display()
    timer -= 1

t.setposition(0, 0)
t.write(f"- TIME OVER! -", align="center", font=("Verdana", 24, "bold"))
turtle_.hideturtle()
pyt_screen.bgcolor("#B9F951")
time.sleep(2)
pyt_screen.exitonclick()
pyt_screen.mainloop()
