from turtle import forward, right, speed


def square(side_length: int = 200):
    """Make the turtle draws a square"""
    for i in range(4):
        forward(side_length)
        right(90)


def triangle(side_length: int = 300):
    """Make the turtle draws a triangle"""
    for i in range(3):
        forward(side_length)
        right(120)


def multiples_geoms(geom_function, n: int, turn_angle: int = 5):
    """Make the turtle draw a specific geom multiple types
    turning right a specific angle in each time the geom is
    draw
    """
    for i in range(n):
        geom_function(200)
        right(turn_angle)


def polygon(n_sides: int, side_length: int = 100):
    """Draw a polygon of equilateral sides of length side_length"""
    if n_sides < 3:
        raise ValueError("The number of sides must be at least 3")
    external_angle = 360/n_sides
    for i in range(n_sides):
        forward(side_length)
        right(external_angle)


if __name__ == "__main__":
    speed(1)
    polygon(1000, 1)
    input('enter to finish...')
