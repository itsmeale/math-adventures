from grid import Grid


def setup():
    size(600, 600)


def f(x):
    return x**2


def g(x):
    return (x+4)/3


def draw():
    grid = Grid(width, height, (-10, 10), (-10, 10))
    grid.draw()
    grid.plot_fx(g)
    grid.plot_fx(f)
    
