
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self):
        if self.tail is None:
            return None

        old_tail = self.tail
        value = old_tail.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.previous
            self.tail.next = None

        old_tail.next = None
        old_tail.previous = None

        return value

    def remove(self, node):
        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        node.next = None
        node.previous = None
