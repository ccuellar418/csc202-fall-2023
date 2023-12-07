from dataclasses import dataclass


@dataclass
class MaxHeap:
    size: int = 0
    capacity: int = 0
    heap: list = None

    def __init__(self, capacity: int = 0): #We have this init function to initialize the self.heap to be alist of nones the size of the capacity.
        self.capacity = capacity 
        self.heap = [None] * self.capacity

    # Insert item into the heap and restores the heap property
    # Returns true if successful, false if there is no room in the heap
    # "item" can be any primitive or object that can be compared with other items using the < operator
    def enqueue(self, item) -> bool:
        if self.is_full():#makes it so if the capacity is the same as the size, it will not let any more items into the heap.
            return False
        self.heap = self.heap + [item] #places item into the heap. kind of like appending it into the list
        self.heap = self.build_heap(self.heap) #restructures the heap to ensure the maximum value is at the top
        return True

    # Returns max without changing the heap, returns None if the heap is empty
    def peek(self):#basically calls the max (which is the root) of the heap
        if self.is_empty(): #if it is empty, return none because there is no max
            return None 
        return self.heap[0] #else you return the heap at index 0

    # Returns max and removes it from the heap and restores the heap property
    def dequeue(self): #does what the peek function does, but instead of just looking at it, it pulls the max out and reshuffles the heap, so that the new max is at the top
        if self.is_empty():
            return None
        max = self.heap[0]
        self.heap[0] = self.heap[-1] #takes the last leaf and makes it the root. 
        self.heap = self.heap[:-1]#this slices off the root.
        self.max_heapify(self.heap, 0) #remake the heap of the function
        self.size -= 1 #reduce the size of the heap by one
        return max #return the maximum value from the original heap.

    # Returns a list of contents of the heap in the order it is stored internal to the heap.
    def contents(self) -> list: #returns the entire list as it is (which holds the 'contents' of the heap)
        return self.heap

    # Discards all items in the current heap and builds a heap from the items in alist using the bottom-up construction method.
    # If the capacity of the current heap is less than the number of items in alist, the capacity of the heap will be increased to accommodate the items in alist
    def build_heap(self, alist: list) -> list:
        if self.capacity < len(alist):
            self.capacity = len(alist) #gets the length of the list and makes it the capacity of the heap
        self.size = len(alist) #makes the size of the heap equal to the length of the list
        self.heap = alist #make the heap equal to the list
        for i in range(len(self.heap) // 2, -1, -1): #this uses selection sort since it starts from the back and goes forward. right to left
            self.max_heapify(self.heap, i)#
        return self.heap

    # Swap two elements in the heap
    def swap(self, i: int, j: int) -> None: #swaps two items in the heap, which will be used for the max_heapify function
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Process for finding the largest
    def max_heapify(self, alist: list, index: int):
        largest = index
        left = (2 * index) + 1 #left side
        right = (2 * index) + 2 #right side
        if left < len(alist) and alist[left] > alist[largest]:
            largest = left
        if right < len(alist) and alist[right] > alist[largest]:
            largest = right 
        if largest != index:
            self.swap(index, largest) #move the larger node up
            self.max_heapify(alist, largest) #recursively do this until the node is smaller than the next item, or it is at the top of the list

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
