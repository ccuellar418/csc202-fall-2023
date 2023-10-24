from dataclasses import dataclass


@dataclass
class Node:
    value: int
    prev_node: None
    next_node: None


@dataclass
class doubly_Ordered_List:
    head: "Node" = None
    tail: "Node" = None
    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    """

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        pass

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance"""
        pass

    def remove(self, item):
        """Removes the first occurrence of an item from OrderedList. If item is removed (was
        in the list)
        returns True.  If item was not removed (was not in the list) returns False
        MUST have O(n) average-case performance"""
        pass

    def index(self, item):
        """Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
        If item is not in list, return None
        MUST have O(n) average-case performance"""
        pass

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError
        MUST have O(n) average-case performance"""
        pass

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"
        To practice recursion, this method must call a RECURSIVE method that
        will search the list
        MUST have O(n) average-case performance"""
        pass

    """
    Return a Python list representation of OrderedList, from head to tail
    For example, list with integers 1, 2, and 3 would return [1, 2, 3]
    MUST have O(n) performance
    """

    def python_list(self):
        # Checks if the head even exists
        if self.head is None:
            return []

        # Checks if the head is the only node
        elif self.head.next_node is None:
            return [self.head.value]

        else:
            python_list = []
            current_node = self.head
            while current_node is not None:
                # Puts values into the python_list from the current node
                python_list.append(current_node.value)
                # Now, move onto the next node
                current_node = current_node.next_node
            return python_list

    """
    Return a Python list representation of OrderedList, from tail to head, using recursion
    For example, list with integers 1, 2, and 3 would return [3, 2, 1]
    To practice recursion, this method must call a RECURSIVE method that will return a reversed list
    MUST have O(n) performance
    """

    def python_list_reversed(self):
        # Checks if the tail even exists
        if self.tail is None or self.tail.prev_node is None:
            return []

        global python_list
        global current_node

        while current_node is not None:
            # Puts values into the python_list from the current node
            python_list.append(current_node.value)

            # Now, move onto the next node
            current_node.python_list_reversed(current_node.prev_node)
        return python_list

    """
    Returns number of items in the OrderedList
    To practice recursion, this method must call a RECURSIVE method that will count and return the number of items in the list
    MUST have O(n) performance
    """

    def size(self):
        global count
        global current_node

        # Checks if the head even exists
        if self.head is None or self.head.next_node is None:
            return 0

        # Add up the number of nodes in the list
        if current_node is not None:
            count += 1
            current_node = current_node.next_node
            self.size()
        else:
            return count
