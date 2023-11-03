def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print("Key: " + str(key))
        j = i - 1
        print("J: " + str(j))
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)


# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
