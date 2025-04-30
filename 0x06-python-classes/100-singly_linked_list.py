#!/usr/bin/python
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not type(value) == int:
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        # If the list is empty or the new value is smaller than the head's data
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Find the correct position for the new node
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def print_list(self):
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return " \n".join(result)
    
    def __str__(self):
        """
        String representation of the Singly Linked List.
        
        Returns:
            str: The elements of the linked list as a string, 
            formatted with ' -> ' between elements.
        """
        return self.print_list()

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)