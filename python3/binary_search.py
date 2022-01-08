# Binary search will divide the sorted in two parts
# Based on first and last element of list
# it decide will part would be selected
# Find the median and follow the same process


# Time complexity of binary search is O(log n)


def binary_search(arr, find):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == find:
            return mid

        if arr[mid] > find:
            right = mid - 1
        else:
            left = mid + 1

    return -1


array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
element = 60

position = binary_search(array, element)

if position == -1:
    print("Element is not present in given list.")
else:
    print(f"Element is present at {position + 1} position")
