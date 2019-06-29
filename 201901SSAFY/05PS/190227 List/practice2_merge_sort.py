def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = (len(m) - 1) // 2

    left = merge_sort(m[:mid + 1])
    right = merge_sort(m[mid + 1:])

    return merge(left, right)

def merge(left, right):
    len_left = len(left)
    len_right = len(right)

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result += left

    elif len(right) > 0:
        result += right

    return result


print(merge_sort([69, 10, 30, 2, 16, 8, 31, 22]))
