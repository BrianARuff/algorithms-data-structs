array = [5, 25, 16, -4, 15]

def bubble_sort(arr):
    count = 0
    while count < len(arr)-1:
        # loop through each item in arry
        for i in range(0, len(arr)-1-count):
            # curr item > next item
            if arr[i] > arr[i+1]:
                # swap items
                arr[i], arr[i+1] = arr[i+1], arr[i]
        count += 1
    return arr

print(bubble_sort(array))