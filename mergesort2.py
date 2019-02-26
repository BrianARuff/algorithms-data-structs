array = [5, 4, 3, 2, 1]

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:] + right[right_index:]
    return result
        

def merge_sort(arr):
    if len(arr) <= 1: return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print("LEFT", left)
    # print("RIGHT", right)
    return merge(left, right)

print(merge_sort(array))