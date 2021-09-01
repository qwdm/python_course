""" Функции """


### Triangle "library" ###

def perimeter(a, b, c):
    return a + b + c


def semiperimeter(a, b, c):
    pp = perimeter(a, b, c)
    return pp / 2


def heron_area(a, b, c):
    p = semiperimeter(a, b, c)
    return (p * (p - a) * (p - b) * (p - c)) ** .5


def incircle_radius(a, b, c):
    s = heron_area(a, b, c)
    p = semiperimeter(a, b, c)
    r = s / p
    return r


def is_good_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)
