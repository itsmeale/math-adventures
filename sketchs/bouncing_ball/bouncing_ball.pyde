from ball import Ball
from random import randint

ball_list = []


def setup():
    size(600, 600)
    for i in range(20):
        ball_list.append(Ball(randint(0, 600), randint(0, 600)))


def draw():
    background(255)
    for ball in ball_list:
        ball.update()
