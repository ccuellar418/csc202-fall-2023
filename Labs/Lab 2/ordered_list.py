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
    head: None
    tail: None
    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    """

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        if self.head == None:
            return True
        return False

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance"""
        new_node = Node(item, None, None)
        if self.head is not None:
            current_node = self.head
            return self.add_recursive(item, current_node.next_node)
        else:
            self.head = new_node
            self.tail = new_node
            return True

    def add_recursive(self, item, current_node):
        # if item exists already
        if current_node.value == current_node.value:
            return False
        # if the item should become head

        if self.head.value > current_node.value:
            current_node.next_node = self.head
            current_node.prev_node = current_node
            self.head = current_node
            return True
        # if new_node should become tail
        if current_node == self.tail:
            current_node.next_node = current_node
            current_node.prev_node = current_node
            self.tail = current_node
            return True

        # if new_node goes in middle of list
        if current_node.next_node.value > current_node.value:
            current_node.prev_node = current_node
            current_node.next_node = current_node.next_node
            current_node.next_node.prev_node = current_node
            current_node.next_node = current_node
            return True

        return self.add_recursive(item, current_node.next_node)

    def remove(self, item):
        """Removes the first occurrence of an item from OrderedList. If item is removed (was
        in the list)
        returns True.  If item was not removed (was not in the list) returns False
        MUST have O(n) average-case performance"""
        if self is not None:
            current_node = self.head
            if current_node == item:
                # if item is head
                if current_node.prev_node is None:
                    self.head = current_node.next_node
                    current_node.next_node.prev_node = None

                # if item is tail
                elif current_node.next_node is None:
                    current_node.prev_node.next_node = None
                    self.tail = current_node.prev_node

                # if item is in middle
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                return True
            return self.remove(self, item, current_node.next_node)
        else:
            # if list is empty
            return False

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
        if self.tail is None:
            return []

        # Check if it's only the tain
        if self.tail is not None and self.tail.prev_node is None:
            return [self.tail.value]

        python_list = []
        self.python_list_reversed_recursive(python_list, self.tail)
        return python_list

    def python_list_reversed_recursive(self, python_list, current_node):
        # Checks if the tail even exists
        if self.tail is not None or self.tail.prev_node is not None:
            if current_node is not None:
                # Puts values into the python_list from the current node
                print(python_list[0])

                # Now, move onto the next node
                current_node.python_list_reversed_recursive(
                    python_list, current_node.prev_node
                )
        return python_list

    """
    Returns number of items in the OrderedList
    To practice recursion, this method must call a RECURSIVE method that will count and return the number of items in the list
    MUST have O(n) performance
    """

    def size(self):
        # Checks if the head even exists
        if self.head is None:
            return 0

        # If head is the only node
        if self.head.next_node is None:
            return 1

        count = 0
        current_node = self.head

        # Add up the number of nodes in the list
        if current_node is not None:
            self.size_recursive(count, current_node.next_node)

        return count

    def size_recursive(self, count, current_node):
        if current_node is not None:
            count += 1
            current_node = current_node.next_node
            self.size_recursive(count, current_node)
