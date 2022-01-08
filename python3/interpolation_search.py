def interpolation_search(arr, find):
    left = 0
    right = len(arr) - 1

    while left <= right and find >= arr[left] and find <= arr[right]:
        index = left + ((right - left) // (arr[right] - arr[left]) * (find - arr[left]))

        if arr[index] == find:
            return index

        if arr[index] < find:
            left = index + 1
        else:
            right = index - 1

    return -1


elements = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
find = 22

position = interpolation_search(elements, find)
if position == -1:
    print("Element was not present in given list.")
else:
    print(f"Element is presented at {position + 1} position.")
