# Fractal Rose painting

import turtle
import math
import time

# Display Settings
screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Fractal Rose")

#Turtle Settings
rose = turtle.Turtle()
rose.speed(0)
rose.width(2)
eye = turtle.Turtle()
eye.speed(0)
eye.color("White")
eye.width(1)
eye.hideturtle()

#Rose Parameters
n = 5 # number of petals
d = 97 # density
size = 150 # size
steps = 60 #FPS animation

def draw_rose(scale):
    rose.clear()
    rose.penup()
    for i in range(steps):
        theta = i * 2 * math.pi / steps
        k = n * theta
        r = size * math.sin(d * theta) * scale
        x = r * math.cos(k)
        y = r * math.sin(k)
        if i == 0:
            rose.goto(x, y)
            rose.pendown()
        else:
            rose.goto(x, y)

def draw_eye(scale):
    eye.clear()
    eye.penup()
    eye.goto(0, -20 * scale)
    eye.pendown()
    eye.begin_fill()
    eye.circle(20 * scale)
    eye.end_fill()
    eye.penup()
    eye.goto(0, -10 * scale)
    eye.color("Black")
    eye.pendown()
    eye.begin_fill()
    eye.circle(10 * scale)
    eye.end_fill()

#animation
for frame in range(30):
    scale = 0.5 + 0.5 * math.sin(frame * 0.2) # pulsation 0.5 to 1
    draw_rose(scale)
    draw_eye(scale)
    time.sleep(0.05)

turtle.done()



