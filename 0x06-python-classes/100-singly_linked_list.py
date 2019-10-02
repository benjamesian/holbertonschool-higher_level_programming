#!/usr/bin/python3
"""Singly linked list
"""


class Node:
    """Node in a SinglyLinkedList
    """
    def __init__(self, data, next_node=None):
        """Initialize a Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        if not isinstance(d, int):
            raise TypeError("data must be an integer")
        self.__data = d

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, n):
        if not (n is None or isinstance(n, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = n


class SinglyLinkedList:
    """Singly Linked List of Nodes
    """
    def __init__(self):
        """Initialize a SinglyLinkedList
        """
        self.__head = None

    def __str__(self):
        out = ""
        n = self.__head
        while n is not None:
            out = out + str(n.data) + '\n'
            n = n.next_node
        return out

    def sorted_insert(self, data):
        n = self.__head
        new = Node(data)
        if n is None:
            self.__head = new
        elif n.data > data:
            new.next_node = self.__head
            self.__head = new
        else:
            while n.next_node and n.next_node.data < data:
                n = n.next_node
            new.next_node = n.next_node
            n.next_node = new
