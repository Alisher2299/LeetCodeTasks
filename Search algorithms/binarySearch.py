def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        print("D", mid)
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def bin_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
x = 3

print(bin_search(arr, 0, len(arr) - 1, x))
