class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_node(node):
    print node


def traverse(node, visit):
    print "List:"
    while node:
        visit(node)
        node = node.next


def remove_head(node):
    if node is None:
        raise ValueError

    return node.next, node.data


def remove_tail(node):
    head = node

    if node is None:
        raise ValueError

    if node.next is None:
        return None, node.data

    while node.next.next:
        node = node.next

    output = node.next.data
    node.next = None
    return head, output


head1 = None
head1 = Node(1, head1)
head1 = Node(2, head1)
head1 = Node(3, head1)
head1 = Node(4, head1)
head1 = Node(5, head1)
head1 = Node(6, head1)
traverse(head1, print_node)
head1, data = remove_tail(head1)
traverse(head1, print_node)
head1, data = remove_tail(head1)
traverse(head1, print_node)
head1, data = remove_head(head1)
traverse(head1, print_node)
head1, data = remove_head(head1)
traverse(head1, print_node)
