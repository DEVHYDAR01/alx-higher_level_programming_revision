#!/usr/bin/python
"""
linked_list.py: This module defines a Node class for singly linked lists and
a SinglyLinkedList class that maintains a sorted list of integers.
"""

class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The integer data stored in the node.
        next_node (Node): The next node in the list (or None).
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The value stored in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets the data stored in the node.

        Returns:
            int: The integer data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value for the node.

        Args:
            value (int): The integer value to store.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets the next node.

        Returns:
            Node: The next node in the list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node reference.

        Args:
            value (Node): The next node object or None.

        Raises:
            TypeError: If value is not a Node instance or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list of integers in ascending order.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list in the correct sorted position.

        Args:
            value (int): The data value of the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def print_list(self):
        """
        Builds and returns the string representation of the list.

        Returns:
            str: A newline-separated string of node data values.
        """
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def __str__(self):
        """
        Returns the printable string version of the list.

        Returns:
            str: The linked list elements as a newline-separated string.
        """
        return self.print_list()
