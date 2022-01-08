# Linear search will search the elements one by one
# It will go through the every elements until it find one

# Time complexity of linear search is O(n)


def search(array, element):
    for el in array:
        if el == element:
            return array.index(el)


element_list = [10, 24, 54, 42, 36, 87, 12, 83]
find = 27

index = search(element_list, find)
if index:
    print(f"Element found at {index + 1} position.")
else:
    print("Element is not present in given list.")
