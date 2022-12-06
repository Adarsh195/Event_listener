col=[(50, 122, 71), (126, 93, 47), (56, 95, 140), (139, 61, 117), (133, 22, 102), (50, 181, 89), (45, 35, 143), (72, 21, 60), (26, 36, 75), (153, 159, 41), (100, 195, 127), (193, 157, 103), (205, 68, 163), (68, 43, 22), (110, 162, 205), (27, 92, 47), (201, 127, 180), (23, 59, 34), (94, 93, 212), (97, 242, 147), (80, 84, 20), (214, 226, 82), (134, 33, 21), (35, 169, 193), (181, 242, 203), (238, 228, 181), (215, 83, 59), (235, 156, 214), (21, 83, 95), (189, 215, 240), (240, 198, 230), (197, 224, 11), (61, 27, 245), (173, 168, 238), (99, 227, 242), (44, 251, 102), (238, 170, 157), (196, 9, 172), (255, 6, 2)]
from turtle import Turtle, Screen
import random,turtle
turtle.colormode(255)
pablo = Turtle()
s = Screen()
pablo.pensize(5)
def move_forward():
    pablo.pencolor(random.choice(col))
    pablo.forward(10)
def move_backward():
    pablo.pencolor(random.choice(col))
    pablo.backward(10)
def turn_left():
    pablo.left(11)
def turn_right():
    pablo.right(11)
def Clear():
    pablo.reset()
def draw():
    pablo.pendown()
def hold():
    pablo.penup()
s.listen()
s.onkey(key="s", fun=move_backward)
s.onkey(key="w", fun=move_forward)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="c", fun=Clear)
s.onkey(key="q", fun=draw)
s.onkey(key="e", fun=hold)


s.exitonclick()
