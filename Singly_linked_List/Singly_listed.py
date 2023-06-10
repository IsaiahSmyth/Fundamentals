# Create a new Python file and recreate the Node and SList classes
class SList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
# Add the add_to_front method to your SList class


def add_to_front(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node
    self.length += 1

# Add the print_values method to your SList class


def print_values(self):
    current = self.head
    while current:
        print(current.val)

# Add the add_to_back method to your SList class


def add_to_back(self, val):
    new_node = Node(val)

# Practice the above in code and on paper/whiteboard. Then try to write these methods from scratch without referencing the platform!


# Practice the above on your computer and on paper or a whiteboard. Then try to write these methods from scratch without referencing the platform!

# NINJA BONUS: complete the remove_from_front method
def remove_from_front(self):
    if self.head:
        self.head = self.head.next
        self.length -= 1
        return self.head.val

# NINJA BONUS: complete the remove_from_back method


def remove_from_back(self):
    if self.head:
        current = self.head
        while current.next.next:
            current = current.next
            current.next = None
            self.length -= 1
            return current.val

# NINJA BONUS: complete the remove_val method


def remove_val(self, val):
    if self.head:
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.length -= 1
                return current.val
            current = current.next

# SENSEI BONUS: complete the insert_at method


def insert_at(self, val, n):
    if n == 0:
        add_to_front(self, val)
        return

# SENSEI BONUS: consider and account for edge cases for all previous methods


def insert_at(self, val, n):
    if n == 0:
        add_to_front(self, val)
        return
