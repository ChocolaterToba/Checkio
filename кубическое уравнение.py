from math import sqrt, sin, cos
from cmath import rect, pi, polar, phase, sqrt as csqrt

def cube_root(number):
    negative = False
    if number < 0:
        negative = True
        number = abs(number)
    minimum = 0
    maximum = number + 1
    middle = (number + 1) / 2
    while not(number - 0.000000001 < middle ** 3 < number + 0.000000001):
        if middle ** 3 > number:
            maximum = middle
        else:
            minimum = middle
        middle = (maximum + minimum) / 2
    if negative:
        middle = - middle
    return middle


def cubic_equation(a, b, c, d):
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    Q = (p / 3) ** 3 + (q / 2) ** 2
    if Q >= 0:
        root = rect(sqrt(Q), 0)
    else:
        root = csqrt(Q)
    z = - q / 2 + root
    alpha = cube_root(abs(z))* rect(cos(phase(z) / 3), sin(phase(z) / 3))
    betha = -p/(3 * alpha)
    zed = sqrt(3) * (alpha - betha) / 2
    y_options = [alpha + betha,
         -(alpha + betha) / 2 + rect(-polar(zed)[1], polar(zed)[0]),
         -(alpha + betha) / 2 - rect(-polar(zed)[1], polar(zed)[0])]
    x = [str(y - b / (3 * a)) for y in y_options]
    return ','.join(x)
print(cubic_equation(1, 1, -1, -1))