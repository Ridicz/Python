def odwracanie_recursive(L, left, right):
    if left >= right:
        return None
    L[left], L[right] = L[right], L[left]
    if left + 1 != right:
        odwracanie_recursive(L, left + 1, right - 1)


def odwracanie_iterative(L, left, right):
    if left >= right:
        return None
    for i in range(int((right - left) / 2)):
        L[left + i], L[right - i] = L[right - i], L[left + i]


print("Type lists length: ")
listLength = input()
print("Type start position: ")
startPosition = input()
print("Type end position: ")
endPosition = input()

myList = list(range(listLength))
odwracanie_recursive(myList, startPosition, endPosition)
print(myList)

myList = list(range(listLength))
odwracanie_iterative(myList, startPosition, endPosition)
print(myList)
