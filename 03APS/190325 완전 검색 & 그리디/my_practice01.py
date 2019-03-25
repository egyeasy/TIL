arr = [5, 4, 3, 1, 1]

def SelectionSort(arr):
    if len(arr) == 1:
        return arr
    else:
        min_idx = arr.index(min(arr))
        return [arr.pop(min_idx)] + SelectionSort(arr)

print(SelectionSort(arr))
