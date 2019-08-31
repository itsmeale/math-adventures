from turtle import fd, lt, xcor, ycor, speed
from random import randint


def wander():
    while(True):
        fd(3)
        x, y = xcor(), ycor()
        if x > 200 or x < -200 or y > 200 or y < -200:
            lt(randint(90, 180))


if __name__ == "__main__":
    speed(0)
    wander()
