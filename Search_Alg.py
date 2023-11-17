
def linear_search(array, element):
    length = len(array)
    i = 0
    while i < length:
        if array[i] == element:
            return i
        i += 1
    return -1


def binary_search(array, element):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == element:
            return mid
        if element > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def test_linear_search():
    # Test 1: Element exists in the array
    array1 = [1, 2, 3, 4, 5]
    assert linear_search(array1, 3) == 2

    # Test 2: Element doesn't exist in the array
    array2 = [10, 20, 30, 40, 50]
    assert linear_search(array2, 35) == -1

    # Test 3: Empty array
    empty_array = []
    assert linear_search(empty_array, 10) == -1

    # Test 4: Element exists at the first index
    array3 = [7, 8, 9, 10]
    assert linear_search(array3, 7) == 0


# Test cases for binary_search
def test_binary_search():
    # Test 1: Element exists in the array
    array1 = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(array1, 7) == 3

    # Test 2: Element doesn't exist in the array
    array2 = [2, 4, 6, 8, 10]
    assert binary_search(array2, 15) == -1

    # Test 3: Empty array
    empty_array = []
    assert binary_search(empty_array, 5) == -1

    # Test 4: Element exists at the last index
    array3 = [20, 30, 40, 50, 60]
    assert binary_search(array3, 60) == 4


if __name__ == "__main__":
    # Run the tests
    test_linear_search()
    test_binary_search()
    print("All tests passed!")
