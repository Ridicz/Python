import random


class RandomQueue:
    def __init__(self, size=10):
        self.size = size
        self.items = []

    def __str__(self):
        for item in self.items:
            print item

    def is_empty(self):
        pass

    def is_full(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

queue = RandomQueue(15)
