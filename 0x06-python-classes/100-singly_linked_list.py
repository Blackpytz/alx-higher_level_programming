#!/usr/bin/python3
"""A class name Node that defines a node of a singly linked list by:

    * Private instance attribute data.
    * Private instance attribute next_node.
"""


class Node:
    """Instantiation with data and next_node:
    def __init__(self, data, next_node=None)"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """Create a private instance attribute of data"""
    @property
    def data(self):
        return self.__data

    """Validate if the data attribute is a private instance attribute"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """Create a private instance atrribute of next_node"""
    @property
    def next_node(self):
        return self.__next_node

    """Validate if the next_node attribute is a private instance attribute"""
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defined a new class SinglyLinkedList by:
        * Private instance attribue: head(no setter or getter)
        * Simple instantiation: def __init__(self)
        * Public instance method: def sorted_insert(self, value)
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None and \
                    current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.data)
            if current_node.next_node is not None:
                result += "\n"
            current_node = current_node.next_node
        return result
