from math import sqrt


def equation(a, b, c, d):
    """Calcula uma expressao de 1 grau
    na forma ax + b = cx + d,
    de onde extraimos a forma geral por
    ax - cx = d - b
    x(a - c) = d - b
    x = (d - b) / (a - c)

    Exemplo
    ---
    Considere 2x = 10,
    Logo, tem-se a=2, b=0, c=0, d=10
    Portanto
    >>> equation(2, 0, 0, 10)
    5.0
    """
    return ((d-b)/(a-c))


def quadratic(a, b, c):
    """
    -b +-delta() / 2a
    """
    delta = abs(b**2 - 4 * a * c)
    x1 = (- b - sqrt(delta)) / 2 * a
    x2 = (- b + sqrt(delta)) / 2 * a
    return x1, x2


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug(fx):
    for x in range(-100, 101):
        if fx(x) == 0:
            return x
    raise ValueError("no solution in range")
