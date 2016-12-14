import random
import math


def is_inside(x, y):
    x2 = x - 0.5
    y2 = y - 0.5
    distance = math.sqrt(x2 * x2 + y2 * y2)
    if distance < 0.5:
        return True
    else:
        return False


def calc_pi(n=100):
    count = 0
    for i in range(n):
        if is_inside(random.random(), random.random()):
            count += 1
    area = float(count)/float(n)
    pi = area / 0.5 / 0.5
    return pi


print("Error depending on the number of draws:")
print("10: " + str(calc_pi(10)))
print("100: " + str(calc_pi(100)))
print("1000: " + str(calc_pi(1000)))
print("10000: " + str(calc_pi(10000)))
print("100000: " + str(calc_pi(100000)))
print("1000000: " + str(calc_pi(1000000)))
