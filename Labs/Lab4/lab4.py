from dataclasses import dataclass


@dataclass
class MaxHeap:
    size: int = 0
    capacity: int = 0
    heap: list = None

    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        self.heap = [None] * self.capacity

    # Insert item into the heap and restores the heap property
    # Returns true if successful, false if there is no room in the heap
    # "item" can be any primitive or object that can be compared with other items using the < operator
    def enqueue(self, item) -> bool:
        if self.is_full():
            return False
        self.heap = self.heap + [item]
        self.heap = self.build_heap(self.heap)
        return True

    # Returns max without changing the heap, returns None if the heap is empty
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    # Returns max and removes it from the heap and restores the heap property
    def dequeue(self):
        if self.is_empty():
            return None
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.max_heapify(self.heap, 0)
        self.size -= 1
        return max

    # Returns a list of contents of the heap in the order it is stored internal to the heap.
    def contents(self) -> list:
        return self.heap

    # Discards all items in the current heap and builds a heap from the items in alist using the bottom-up construction method.
    # If the capacity of the current heap is less than the number of items in alist, the capacity of the heap will be increased to accommodate the items in alist
    def build_heap(self, alist: list) -> list:
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.size = len(alist)
        self.heap = alist
        for i in range(len(self.heap) // 2, -1, -1):
            self.max_heapify(self.heap, i)
        return self.heap

    # Swap two elements in the heap
    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

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
            self.swap(index, largest)
            self.max_heapify(alist, largest)

    # Returns true if the heap is empty. Otherwise, returns false.
    def is_empty(self) -> bool:
        return self.get_size() == 0

    # Returns true if the heap is full. Otherwise, returns false.
    def is_full(self) -> bool:
        return self.get_size() == self.get_capacity()

    # Returns the capacity of the heap
    def get_capacity(self) -> int:
        return self.capacity

    # Returns the number of actual (non-None) elements in the heap
    def get_size(self) -> int:
        return self.size

    # Get the index of the left child of the element at index i
    def get_left_child_index(self, i) -> int:
        return (2 * i) + 1

    # Get the index of the right child of the element at index i
    def get_right_child_index(self, i) -> int:
        return (2 * i) + 2

    # Where the parameter i is an index in the heap and perc_down moves the element stored at that location to its proper place in the heap rearranging elements as it goes.
    def perc_down(self, i) -> None:
        if len(self.heap) < i:
            return
        else:
            while (i * 2) <= self.size:
                j = max(self.get_left_child_index(i), self.get_right_child_index(i))
                if self.heap[i] < self.heap[j]:
                    self.swap(i, j)
                i = j

    # Where the parameter i is an index in the heap and perc_up moves the element stored at that location to its proper place in the heap rearranging elements as it goes.
    def perc_up(self, i) -> None:
        if len(self.heap) < i:
            return
        else:
            while (
                i // 2 > 0
                and i // 2 < len(self.heap)
                and self.heap[i] > self.heap[i // 2]
            ):
                self.swap(i, i // 2)
            i = i // 2

    # Perform heap sort on input alist in ascending order. This method will discard the current contents of the heap, build a new heap using the items in alist, then mutate alist to put the items in ascending order
    def heap_sort_ascending(self, alist) -> None:
        self.heap = self.build_heap(alist)
        self.heap = self.heap.sort()
