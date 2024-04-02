import turtle
import time
from random import randint

#Turtle ekranını oluştur
pyt_screen = turtle.Screen()
pyt_screen.setup(700, 600)
pyt_screen.bgcolor("#B9F951")
pyt_screen.title("Catch The Turtle!")
pyt_screen.delay(0)

#Pencere boyutunu öğren
window_width = pyt_screen.window_width()
window_height = pyt_screen.window_height()

def rand_position():
    #Random Turtle konumu oluştur
    x = randint(-320, 320)
    y = randint(-280, 260)
    return [x, y]

turtle_ = turtle.Turtle()
turtle_.shape("turtle")
turtle_.shapesize(1.5)
turtle_.penup()
turtle_.speed(0)
def turtle_move():
    #gelen random (x, y) ikililerine göre Turtle'ı konumlandırma
    turtle_.setposition(rand_position()[0], rand_position()[1])

score = int(0)
def get_click_coordinates(click_posX, click_posY):
    #Click konumlarını alma
    compare_positions(click_posX, click_posY)

#Kalan süreyi gösteren Turtle
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.setposition(0, window_height // 2 - 24)
t.speed(0)

#Score'u gösteren Turtle
scr = turtle.Turtle()
scr.penup()
scr.hideturtle()
scr.setposition(0, window_height // 2 - 50)
scr.speed(0)
scr.write(f"SCORE: {score}", align="center", font=("Arial", 16, "bold"))
def time_display():
    #Süreyi gösteren fonksiyonu
    if timer >= 0:
        t.write(f"TIME: {timer}", align="center", font=("Fantasy", 12, "normal"))
        time.sleep(1)
    t.clear()

def compare_positions(click_posx, click_posy):
    #Click ve Turtle konumunu karşılaştırma
    scr.clear()
    global score
    if abs(click_posx - turtle_.xcor()) <= 25 and abs(click_posy - turtle_.ycor()) <= 25:
        score += 1
        scr.write(f"SCORE: {score}", align="center", font=("Arial", 16, "bold"))
    else:
        scr.write(f"SCORE: {score}", align="center", font=("Arial", 16, "bold"))

timer = 20

while timer > 0:
    turtle_move()
    pyt_screen.onclick(fun=get_click_coordinates)
    time_display()
    timer -= 1

t.write("- TIME OVER! -", align="center", font=("Futura", 12, "normal"))
turtle_.hideturtle()
pyt_screen.bgcolor("#6267D9")
time.sleep(2)
pyt_screen.exitonclick()
pyt_screen.mainloop()
