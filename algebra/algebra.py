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
    >>> 5.0
    """
    return ((d-b)/(a-c))
