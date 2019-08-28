from turtle import forward, right


def square(side_size: int = 200):
    for i in range(4):
        forward(side_size)
        right(90)


def triangle(side_size: int = 300):
    for i in range(3):
        forward(side_size)
        right(120)


def multiples_geoms(geom_function, n: int, turn_angle: int = 5):
    for i in range(n):
        geom_function(200)
        right(turn_angle)


if __name__ == "__main__":
    turn_angle = 5
    n_geoms = int(360/turn_angle)
    multiples_geoms(square, n_geoms, turn_angle)
    input('enter to finish...')
