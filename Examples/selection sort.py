def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        print("Min index: " + str(min_index))
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print("Min index now after being set to J: " + str(min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("arr[i]: " + str(arr[i]))
        print("arr[min_index]: " + str(arr[min_index]))
        print(arr)

    return arr


# Here's a step-by-step explanation:
"""1.arr[i] refers to the element at index i in the list arr.
2.arr[min_index] refers to the element at the index min_index in the same list.
3. The right side of the assignment arr[min_index], 
arr[i] creates a temporary tuple containing the values of arr[min_index] and arr[i].
4. The left side of the assignment arr[i], arr[min_index] unpacks this tuple into the list, 
effectively swapping the values of arr[min_index] and arr[i]."""


# Example usage:
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted_list)
print("Sorted list:", sorted_list)
