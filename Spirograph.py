import turtle
import random

lucky = turtle.Turtle()
lucky.speed(0)
screen = turtle.Screen()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t = (r, g, b)
    return t


def spiro1():
    for i in range(120):
        lucky.color(random_color())
        lucky.right(3)
        lucky.circle(100)


# to access the current heading of angle we can use heading()

def spiro3():
    for i in range(120):
        lucky.color(random_color())
        lucky.circle(100)
        lucky.setheading(lucky.heading() + 3)


def spiro4(sizeOfGap):
    for _ in range(int(360 / sizeOfGap)):
        lucky.color(random_color())
        lucky.circle(100)
        lucky.setheading(lucky.heading() + sizeOfGap)


spiro4(3)
screen.exitonclick()
