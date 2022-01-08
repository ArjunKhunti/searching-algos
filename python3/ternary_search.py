# Time complexity is O(log 3 n)


def ternary_search(arr, find):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if find == arr[mid1]:
            return mid1

        if find == arr[mid2]:
            return mid2

        if find < arr[mid1]:
            right = mid1 - 1
        elif find > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
element = 60

position = ternary_search(array, element)

if position == -1:
    print("Element is not present in given list.")
else:
    print(f"Element is present at {position + 1} position")
