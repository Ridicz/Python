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

print dynamic(5, 10)
print recursive(5, 10)
