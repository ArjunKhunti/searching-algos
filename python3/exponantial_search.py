# Applications of Exponential Search:

# Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite. Please refer Unbounded Binary Search for an example.
# It works better than Binary Search for bounded arrays, and also when the element to be searched is closer to the first element.


# Time complexity is O(log n)


def exponential_search(arr, find):
    if arr[0] == find:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= find:
        i = i * 2

    left = i // 2
    right = min(i, len(arr) - 1)

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

position = exponential_search(array, element)

if position == -1:
    print("Element is not present in given list.")
else:
    print(f"Element is present at {position + 1} position")
