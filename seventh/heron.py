from math import sqrt


def heron(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        raise ValueError("Not a triangle!")

    return sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4.
