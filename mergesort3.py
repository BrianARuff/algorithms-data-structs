arr = [5, -5, 25, -25, -30]

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

def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])
    return merge(left, right)

print(merge_sort(arr))