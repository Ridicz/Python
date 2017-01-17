def binarne_rek(L, left, right, y):
    if left >= right:
        if L[left] == y:
            return left
        else:
            return None

    mid = (left + right) / 2

    if L[mid] == y:
        return mid

    if y > L[mid]:
        return binarne_rek(L, mid + 1, right, y)
    else:
        return binarne_rek(L, left, mid - 1, y)

L = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print L
print binarne_rek(L, 0, L.__len__() - 1, 7)
