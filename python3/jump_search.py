# Jump sort will jump some steps
# When the next step is greater than finding elements
# It will get back to previous element
# And perform linear sort

# Time Complexity is O(n^0.5)


def jump_search(arr, find):
    length = len(arr)

    step = pow(length, 0.5)

    prev = 0

    while arr[int(min(step, length) - 1)] < find:
        prev = int(step)
        step += pow(length, 0.5)
        if prev >= find:
            return -1

    while arr[prev] < find:
        prev += 1

        if prev == min(step, length):
            return -1

    if arr[prev] == find:
        return prev


element_list = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find = 1

index = jump_search(element_list, find)
if index:
    print(f"Element found at {index + 1} position.")
else:
    print("Element is not present in given list.")
