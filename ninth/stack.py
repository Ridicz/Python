class Stack:

    def __init__(self, size=10):
        self.objects = size * [None]
        self.elements = 0
        self.size = size
        self.taken = size * [False]

    def __str__(self):
        output = ""

        for i in range(0, self.elements):
            output += str(self.objects[i]) + " "

        return output

    def is_empty(self):
        return self.elements == 0

    def is_full(self):
        return self.elements == self.size

    def push(self, value):
        if self.is_full():
            return

        if self.taken[value]:
            return

        self.taken[value] = True
        self.objects[self.elements] = value
        self.elements += 1

    def pop(self):
        if self.is_empty():
            raise ValueError

        self.elements -= 1
        pop = self.objects[self.elements]
        self.taken[pop] = False

        return pop

stack = Stack()
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)
print stack
stack.push(7)
print stack
stack.pop()
print stack
stack.push(7)
print stack
