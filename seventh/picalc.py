import random,math


def is_inside(x, y):
    dist = math.sqrt(math.pow(x-0.5, 2)+math.pow((y-0.5), 2))    
    if dist < 0.5:
        return True
    else:
        return False


def calc_pi(n=100):
    count = 0
    for i in range(n):
        if is_inside(random.random(), random.random()):
            count += 1
    area = float(count)/float(n)
    pi = area/0.5/0.5
    return pi


print("Error depending on the number of draws:")
print("10: " + str(calc_pi(10)))
print("100: " + str(calc_pi(100)))
print("1000: " + str(calc_pi(1000)))
print("10000: " + str(calc_pi(10000)))
print("100000: " + str(calc_pi(100000)))
print("1000000: " + str(calc_pi(1000000)))
