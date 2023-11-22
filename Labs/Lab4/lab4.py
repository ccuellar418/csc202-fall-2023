from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int = None
    left_child: "TreeNode" = None
    right_child: "TreeNode" = None


@dataclass
class MaxHeap:
    root: "TreeNode" = None

    """inserts "item" into the heap, returns true if successful, false
        if there is no room in the heap
        "item" can be any primitive or ***object*** that can be
        compared with other
        items using the < operator"""

    def enqueue(self, item):
        pass

    """returns max without changing the heap, returns None if the heap is empty"""

    def peek(self):
        if self.root is None:
            return None
        else:
            return self.root.value

    """returns max and removes it from the heap and restores the heap
    property returns None if the heap is empty"""

    def dequeue(self):
        pass

    """returns a list of contents of the heap in the order it is
    stored internal to the heap.
    (This may be useful for in testing your implementation.)"""

    def contents(self):
        list = []
        self.in_order_recursive(self.root)
        return list

    def in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left_child)
            list.append(current_node.value)
            self._in_order_recursive(current_node.right_child)

    """Discards all items in the current heap and builds a heap from
    the items in alist using the bottom-up construction method.
    If the capacity of the current heap is less than the number of
    items in alist, the capacity of the heap will be increased to
    accommodate the items in alist"""

    def build_heap(self, alist):
        pass

    """returns True if the heap is empty, false otherwise"""

    def is_empty(self):
        return self.get_size() == 0

    """returns True if the heap is full, false otherwise"""

    def is_full(self):
        return self.get_size() == self.get_capacity()

    """this is the maximum number of a entries the heap can hold
    1 less than the number of entries that the array allocated to hold"""

    def get_capacity(self):
        pass

    """the actual number of elements in the heap, not the capacity"""

    def get_size(self):
        pass

    """where the parameter i is an index in the heap and perc_down
    moves the element stored
    at that location to its proper place in the heap rearranging
    elements as it goes."""

    def perc_down(self, i):
        pass

    """where the parameter i is an index in the heap and perc_up moves
    the element stored
    at that location to its proper place in the heap rearranging
    elements as it goes."""

    def perc_up(self, i):
        pass

    """perform heap sort on input alist in ascending order
    This method will discard the current contents of the heap, build a
    new heap using
    the items in alist, then mutate alist to put the items in
    ascending order"""

    def heap_sort_ascending(self, alist):
        pass
