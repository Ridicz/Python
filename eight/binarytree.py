class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False


def count_leafs(top):
    if not top.left and not top.right:
        return 1

    count = 0

    if top.left:
        count += count_leafs(top.left)

    if top.right:
        count += count_leafs(top.right)

    return count


def calc_total(top):
    count = top.data

    if top.left:
        count += calc_total(top.left)

    if top.right:
        count += calc_total(top.right)

    return count


root = Node(15)
root.insert(10)
root.insert(5)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(20)
root.insert(21)
root.insert(22)

print("Number of leafs: " + str(count_leafs(root)))
print("Total sum of leafs data: " + str(calc_total(root)))
