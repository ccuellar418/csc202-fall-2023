def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        print(pivot)
        left = [x for x in arr[1:] if x < pivot]
        print(left)
        right = [x for x in arr[1:] if x >= pivot]
        print(right)
        return quicksort(left) + [pivot] + quicksort(right)
