import random
import math


def random_list(n):
    rlist = list(range(n))
    random.shuffle(rlist)
    return rlist


def nearly_sorted_list(n):
    nslist = list(range(n))
    distance = round(math.log(n) * 2)
    for i in range(n):
        a = i - distance
        b = i + distance
        if a < 0:
            a = 0
        if b >= n:
            b = n - 1
        r = random.randint(a, b)
        nslist[i], nslist[r] = nslist[r], nslist[i]
    return nslist


def nearly_sorted_list_reversed(n):
    return nearly_sorted_list(n)


def gaussian_list(n):
    return [round(random.gauss(n / 2, n / 6)) for _ in range(n)]


def repeated_list(n):
    return [random.randint(0, math.floor(math.sqrt(n))) for _ in range(n)]
