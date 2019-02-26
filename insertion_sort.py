array = [5, -25, 25, -5, 15]

def insertion_sort(arr):
    for i in range(1, len(arr)):

        if arr[i] < arr[i-1]:

            for j in range(i-1, -1, -1):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i -= 1
            
    return arr

print(insertion_sort(array))