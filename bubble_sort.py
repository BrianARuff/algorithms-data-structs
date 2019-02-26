array = [5, 25, -5, -25, 4, 16]

def bubble_sort(arr):
    for k in range(len(arr)):
        for i in range(len(arr)-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort(array))