#!/usr/bin/python3

""" class Node that defines a node of a singly linked list."""


class Node:
    """Define a node of a singly linked list

    Attributes:
        __data (int): Private instance attribute representin
            the data stored in the node.
        __next_node (Node or None): Private instance attribute
            representing the next node in the linked list.

    Methods:
        data: Property method to retrive the data stored in the node.
        data.setter: Setter method to set the data stored in the node.
        next_node: Property method to retrieve the next node
                    in the linked list.
        next_node.setter: Setter method to set the next node
                    in the linked list.
    """

    def __init__(self, data, next_node=None):
        """ initializes atributes.
            
            args:
                int: __data
                Node: next_node. """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieves data value.
            
            returns an int"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data stored in the node.

        Args:
            value (int): The data to be set in the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ retrieves next_node value.

            returns a Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list

        Args:
            value (Node or None): The next node in the linked list.

        Raises:
            TypeError: If the provided value is not None or a Node object.
        """
        if value is None or isinstance(value, self):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


""" class SinglyLinkedList that defines a singly linked list."""


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialies an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node int the correct sorted position in the list.

        Args:
            value: The value of the new Node to be inserted.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result) 
