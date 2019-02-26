arr = [23, 34, 46, -34, -23]

def merge(left, right):
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result += left[l_index:] + right[r_index:]
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    return merge(left, right)

print(merge_sort(arr))