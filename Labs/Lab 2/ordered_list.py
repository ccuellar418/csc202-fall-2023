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

    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    """

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        pass

    def add(self, item, head):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance"""
        new_node = Node(item, None, None)
        if self.head is not None:
            current_node = head
            #if item exists already
            if current_node.value == new_node.value:
                return False
            #if the item should become head

            if self.head.value > new_node.value:
                new_node.next_node = self.head
                current_node.prev_node = new_node
                self.head = new_node
                return True
            #if new_node should become tail
            if current_node == self.tail:
                current_node.next_node = new_node
                new_node.prev_node = current_node
                self.tail = new_node
                return True

            #if new_node goes in middle of list
            if current_node.next_node.value > new_node.value:
                new_node.prev_node = current_node
                new_node.next_node = current_node.next_node
                current_node.next_node.prev_node = new_node
                current_node.next_node = new_node
                return True

            return(self.add(item, current_node.next_node))
        else:
            self.head = new_node
            self.tail = new_node
            return True

    head : None
    tail : None

    def __init__(self, h, t):
        self.head = h
        self.tail = t

    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    """

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        if self.head == None:
            return True
        return False


    def add(self, item, head):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list) and returns True.
        If the item is already in the list, do not add it again and return False.
        MUST have O(n) average-case performance"""
        new_node = Node(item, None, None)
        if self.head is not None:
            current_node = head
            #if item exists already
            if current_node.value == new_node.value:
                return False
            #if the item should become head

            if self.head.value > new_node.value:
                new_node.next_node = self.head
                current_node.prev_node = new_node
                self.head = new_node
                return True
            #if new_node should become tail
            if current_node == self.tail:
                current_node.next_node = new_node
                new_node.prev_node = current_node
                self.tail = new_node
                return True

            #if new_node goes in middle of list
            if current_node.next_node.value > new_node.value:
                new_node.prev_node = current_node
                new_node.next_node = current_node.next_node
                current_node.next_node.prev_node = new_node
                current_node.next_node = new_node
                return True

            return(self.add(item, current_node.next_node))
        else:
            self.head = new_node
            self.tail = new_node
            return True





    def remove(self, item, head):
        """Removes the first occurrence of an item from OrderedList. If item is removed (was
        in the list)
        returns True.  If item was not removed (was not in the list) returns False
        MUST have O(n) average-case performance"""
        if head is not None:
            current_node = head
            if current_node.value == item:
                #if item is head
                if current_node.prev_node is None:
                    self.head = current_node.next_node
                    current_node.next_node.prev_node = None

                #if item is tail
                elif current_node.next_node is None:
                    current_node.prev_node.next_node = None
                    self.tail = current_node.prev_node

                #if item is in middle
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                return True
            return(self.remove(item, current_node.next_node))
        else:
            #if list is empty
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

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]
        MUST have O(n) performance"""
        pass

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using
        recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]
        To practice recursion, this method must call a RECURSIVE method that
        will return a reversed list
        MUST have O(n) performance"""
        pass

    def size(self):
        """Returns number of items in the OrderedList
        To practice recursion, this method must call a RECURSIVE method that
        will count and return the number of items in the list
        MUST have O(n) performance"""
        pass
