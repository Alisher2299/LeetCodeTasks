arr = [3, 6, 1, 7, 4, 8, 3, 8, 234, 45]


def quick_sort(arr, x=None):
    if x is None:
        x = 0

    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[x]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sorted(less) + equal + sorted(greater)
    else:
        return arr


print(quick_sort(arr, len(arr) // 2))
