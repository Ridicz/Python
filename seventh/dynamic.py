import time


def recursive(i, j):
    if i < 0 or j < 0:
        raise ValueError

    if i == 0 and j == 0:
        return 0.5

    if i == 0:
        return 1.0

    if j == 0:
        return 0.0

    return 0.5 * (recursive(i - 1, j) + recursive(i, j - 1))


dictionary = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}


def dynamic(i, j):
    if i < 0 or j < 0:
        raise ValueError

    if i == 0 and j == 0:
        return 0.5

    if i == 0:
        return 1.0

    if j == 0:
        return 0.0

    if (i, j) in dictionary:
        return dictionary.get((i, j))
    else:
        dictionary[(i, j)] = 0.5 * (dynamic(i - 1, j) + dynamic(i, j - 1))
        return dictionary[(i, j)]


start = time.time()
dyn = dynamic(7, 12)
end = time.time()
print("Dynamic: " + str(dyn) + ", time: " + str(end - start))

start2 = time.time()
rec = recursive(7, 12)
end2 = time.time()
print("Recursive: " + str(rec) + ", time: " + str(end2 - start2))
