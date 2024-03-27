def mergeSort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr) // 2
    Left = arr[:mid]
    Right = arr[mid:]
    return merge(mergeSort(Left), mergeSort(Right))


def merge(Left, Right):
    result = []
    while Left and Right:
        if Left[0] <= Right[0]:
            result.append(Left.pop(0))
        else:
            result.append(Right.pop(0))
    while Left:
        result.append(Left.pop(0))
    while Right:
        result.append(Right.pop(0))
    return result
