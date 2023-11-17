def bubble_sort(array):
    length = len(array)
    while length > 0:
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        length -= 1
    return array


def merge(array1, array2):
    array3 = []
    len1 = len(array1)
    len2 = len(array2)
    i = 0
    j = 0
    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    if i == len1 and j != len2:
        array2 = array2[j:]
        for item in array2:
            array3.append(item)
    if i != len1 and j == len2:
        array1 = array1[i:]
        for item in array1:
            array3.append(item)
    return array3


def merge_sort(array):
    if len(array) == 1 or not array:
        return array
    middle = len(array) // 2  # Find the middle index
    first_half = array[:middle]  # Slice from the start to the middle
    second_half = array[middle:]  # Slice from the middle to the end

    last_array = merge(merge_sort(first_half), merge_sort(second_half))
    return last_array


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array.pop()  # Select the last element as the pivot and remove it from the array
    lesser_than_pivot = []
    greater_than_pivot = []

    for item in array:
        if item <= pivot:
            lesser_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)

    return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


if __name__ == "__main__":
    # Example usage:
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Bubble Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Merge Sort:", merge_sort(arr.copy()))

    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Quick Sort:", quick_sort(arr.copy()))
