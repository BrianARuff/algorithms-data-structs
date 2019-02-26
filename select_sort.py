# o(n^2)
# o(1) auxillary memory
# Bad for long lists
# Okay for short lists, but selection sort is typically better on the same short lists
# starts with unsorted list --> finds smallest element by swapping it with left most unsorted element and moving sublist one element to the right

array = [5, 25, -5, -25, 4, 16]

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selection_sort(array))