from dataclasses import dataclass


@dataclass
class MaxHeap:
    capacity: int = 0
    heap: list = None
    heap_internal: list = None

    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.heap = [None] * self.capacity

    # Insert item into the heap and restores the heap property
    # Returns true if successful, false if there is no room in the heap
    # "item" can be any primitive or object that can be compared with other items using the < operator
    def enqueue(self, item) -> bool:
        pass

    # Returns max without changing the heap, returns None if the heap is empty
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    # Returns max and removes it from the heap and restores the heap property
    def dequeue(self):
        pass

    # Returns a list of contents of the heap in the order it is stored internal to the heap.
    def contents(self) -> list:
        return self.heap

    # Discards all items in the current heap and builds a heap from the items in alist using the bottom-up construction method.
    # If the capacity of the current heap is less than the number of items in alist, the capacity of the heap will be increased to accommodate the items in alist
    def build_heap(self, alist: list) -> list:
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.heap = alist
        for i in range(len(self.heap) // 2, -1, -1):
            self.max_heapify(self.heap, i)
        return self.heap

    # Process for finding the largest
    def max_heapify(self, alist: list, index: int):
        largest = index
        left = (2 * index) + 1
        right = (2 * index) + 2
        if left < len(alist) and alist[left] > alist[largest]:
            largest = left
        if right < len(alist) and alist[right] > alist[largest]:
            largest = right
        if largest != index:
            alist[index], alist[largest] = alist[largest], alist[index]
            self.max_heapify(alist, largest)

    # Returns true if the heap is empty. Otherwise, returns false.
    def is_empty(self) -> bool:
        return not self.is_full()

    # Returns true if the heap is full. Otherwise, returns false.
    def is_full(self) -> bool:
        return self.get_capacity() == self.get_size()

    # Returns the capacity of the heap
    def get_capacity(self) -> int:
        return self.capacity

    # Returns the number of actual (non-None) elements in the heap
    def get_size(self) -> int:
        for i in range(len(self.heap)):
            if self.heap[i] is None:
                return i

    # Where the parameter i is an index in the heap and perc_down moves the element stored at that location to its proper place in the heap rearranging elements as it goes.
    def perc_down(self, i) -> None:
        pass

    # Where the parameter i is an index in the heap and perc_up moves the element stored at that location to its proper place in the heap rearranging elements as it goes.
    def perc_up(self, i) -> None:
        pass

    # Perform heap sort on input alist in ascending order. This method will discard the current contents of the heap, build a new heap using the items in alist, then mutate alist to put the items in ascending order
    def heap_sort_ascending(self, alist) -> None:
        pass
