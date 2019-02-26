array = [i for i in range(0, 10000)]

def selection_sort(arr):
    # loop through each item
    for i in range(len(arr)):
        # loop through each item again
        for j in range(i+1, len(arr)):
            # compare current value to value in j
            # if j val < i val then swap
            if arr[j] < arr[i]:
                # swap values
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selection_sort(array))