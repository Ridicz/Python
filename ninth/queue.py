import random


class PriorityQueue:
    def __init__(self, cmpfunc=cmp):
        self.items = []
        self.cmpfunc = cmpfunc

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        max_index = 0

        for index in range(1, len(self.items)):
            if self.cmpfunc(self.items[index], self.items[max_index]) > 0:
                max_index = index
        return self.items.pop(max_index)


def cmp_first(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    return -1


def cmp_second(x, y):
    if x > y:
        return -1
    elif x == y:
        return 0
    return 1


queue = PriorityQueue(cmp_first)
for i in range(0, 10):
    queue.insert(random.randint(1, 100))
while not queue.is_empty():
    print(queue.remove())

print("\n")

queue = PriorityQueue(cmp_second)
for i in range(0, 10):
    queue.insert(random.randint(1, 100))
while not queue.is_empty():
    print(queue.remove())
