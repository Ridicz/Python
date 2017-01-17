def mediana_sort(L, left, right):
    for index in range(1, len(L)):
        currentvalue = L[index]
        position = index

        while position > 0 and L[position - 1] > currentvalue:
            L[position] = L[position - 1]
            position -= 1

        L[position] = currentvalue

    mid = (len(L) - 1) / 2

    if len(L) % 2 == 0:
        return (L[mid] + L[mid + 1]) / 2.
    else:
        return L[mid]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print mediana_sort(lista, 0, 0)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print mediana_sort(lista, 0, 0)
