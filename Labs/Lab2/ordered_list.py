from dataclasses import dataclass


@dataclass
class Node:
    value: int
    prev_node: None
    next_node: None

    def __init__(self, val, prev, next):
        self.value = val
        self.prev_node = prev
        self.next_node = next


@dataclass
class doubly_Ordered_List:
    head: Node = None
    tail: Node = None

    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    """

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        if self.head is None:
            return True
        else:
            return False

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance"""
        if self.head is None:
            self.head = Node(item, None, None)
            self.tail = self.head
            return True
        else:
            current_node = self.head
            while current_node is not None:
                # If the item is already in the list, do not add it again and return False.
                if current_node.value == item:
                    return False
                # If the item is less than the current node, add it before the current node
                elif item < current_node.value:
                    # If the current node is the head
                    if current_node.prev_node is None:
                        self.head = Node(item, None, current_node)
                        current_node.prev_node = self.head
                        return True
                    # If the current node is not the head
                    else:
                        new_node = Node(item, current_node.prev_node, current_node)
                        current_node.prev_node.next_node = new_node
                        current_node.prev_node = new_node
                        return True
                # If the item is greater than the current node, move onto the next node
                elif item > current_node.value:
                    # If the current node is the tail
                    if current_node.next_node is None:
                        self.tail = Node(item, current_node, None)
                        current_node.next_node = self.tail
                        return True
                    # If the current node is not the tail
                    else:
                        current_node = current_node.next_node

    def remove(self, item):
        """Removes the first occurrence of an item from OrderedList. If item is removed (was
        in the list)
        returns True.  If item was not removed (was not in the list) returns False
        MUST have O(n) average-case performance"""
        if self.head is None:
            return False
        else:
            current_node = self.head
            while current_node is not None:
                # If the item is found
                if current_node.value == item:
                    # If the item is the head
                    if current_node.prev_node is None:
                        # If the item is the only node
                        if current_node.next_node is None:
                            self.head = None
                            self.tail = None
                            return True
                        # If the item is not the only node
                        else:
                            self.head = current_node.next_node
                            self.head.prev_node = None
                            return True
                    # If the item is the tail
                    elif current_node.next_node is None:
                        self.tail = current_node.prev_node
                        self.tail.next_node = None
                        return True
                    # If the item is neither the head nor the tail
                    else:
                        current_node.prev_node.next_node = current_node.next_node
                        current_node.next_node.prev_node = current_node.prev_node
                        return True
                # If the item is not found, move onto the next node
                else:
                    current_node = current_node.next_node
            return False

    def index(self, item):
        """Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
        If item is not in list, return None
        MUST have O(n) average-case performance"""
        if self.head is None:
            return None
        else:
            current_node = self.head
            index = 0
            while current_node is not None:
                # If the item is found
                if current_node.value == item:
                    return index
                # If the item is not found, move onto the next node
                else:
                    current_node = current_node.next_node
                    index += 1
            return None

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError
        MUST have O(n) average-case performance"""
        if self.head is None:
            raise IndexError
        else:
            current_node = self.head
            current_index = 0
            while current_node is not None:
                # If the index is found
                if current_index == index:
                    # If the index is the head
                    if current_node.prev_node is None:
                        # If the index is the only node
                        if current_node.next_node is None:
                            self.head = None
                            self.tail = None
                            return current_node.value
                        # If the index is not the only node
                        else:
                            self.head = current_node.next_node
                            self.head.prev_node = None
                            return current_node.value
                    # If the index is the tail
                    elif current_node.next_node is None:
                        self.tail = current_node.prev_node
                        self.tail.next_node = None
                        return current_node.value
                    # If the index is neither the head nor the tail
                    else:
                        current_node.prev_node.next_node = current_node.next_node
                        current_node.next_node.prev_node = current_node.prev_node
                        return current_node.value
                # If the index is not found, move onto the next node
                else:
                    current_node = current_node.next_node
                    current_index += 1
            raise IndexError

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"
        To practice recursion, this method must call a RECURSIVE method that
        will search the list
        MUST have O(n) average-case performance"""
        if self.head is None:
            return False
        else:
            current_node = self.head
            while current_node is not None:
                # If the item is found
                if current_node.value == item:
                    return True
                # If the item is not found, move onto the next node
                else:
                    current_node = current_node.next_node
            return False

    def python_list(self):
        """
        Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]
        MUST have O(n) performance
        """

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

    def python_list_reversed(self):
        """
        Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]
        To practice recursion, this method must call a RECURSIVE method that will return a reversed list
        MUST have O(n) performance
        """
        # Checks if the tail even exists
        if self.tail is None:
            return []

        # Check if it's only the tail
        if self.tail is not None and self.tail.prev_node is None:
            return [self.tail.value]

        python_list = []

        # Call the recursive function
        self.python_list_reversed_recursive(python_list, self.tail)
        return python_list

    def python_list_reversed_recursive(self, python_list, current_node):
        # Checks if the tail even exists
        if self.tail is not None or self.tail.prev_node is not None:
            if current_node is not None:
                # Puts values into the python_list from the current node
                python_list.append(current_node.value)

                # Now, move onto the next node
                self.python_list_reversed_recursive(python_list, current_node.prev_node)
        return python_list

    def size(self):
        """
        Returns number of items in the OrderedList
        To practice recursion, this method must call a RECURSIVE method that will count and return the number of items in the list
        MUST have O(n) performance
        """
        # Check if the head even exists
        if self.head is None:
            return 0
        else:
            # Call the recursive function
            return self.size_recursive(self.head)

    def size_recursive(self, current_node):
        # Check if the head even exists
        if self.head is not None:
            if current_node is not None:
                # Now, move onto the next node
                return 1 + self.size_recursive(current_node.next_node)
            else:
                # If the current node is None, return 0
                return 0
        else:
            # If the head is None
            return 0
