array = [5, -25, 15, 30, -45]

def merge(l, r):
    right_count = 0
    left_count = 0
    result = []
    while left_count < len(l) and right_count < len(r):
        if l[left_count] < r[right_count]:
            result.append(l[left_count])
            left_count += 1
        else:
            result.append(r[right_count])
            right_count += 1
    result += (l[left_count:] + r[right_count:])
    return result

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


print(merge_sort(array))
