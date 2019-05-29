from problem00 import print1DList


def bubble_sort(array):
    """
    reproduce bubble sort
    :param array: array of integers
    :return: sorted array
    """
    length = len(array)
    for i in range(length):
        for j in range(length - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


def main():
    # receive [1, 2, 3, 4, 7, 8, 11, 12]
    sorted_array_1 = bubble_sort([12, 3, 8, 4, 11, 2, 7, 1])
    print1DList(sorted_array_1)
    print()

    # receive [1, 2, 3, 3, 3, 6, 7, 9]
    sorted_array_2 = bubble_sort([3, 1, 9, 6, 7, 2, 3, 3])
    print1DList(sorted_array_2)
    print()

    # receive [0, 0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    sorted_array_3 = bubble_sort([10, 9, 8, 7, 0, 5, 4, 3, 2, 1, 0])
    print1DList(sorted_array_3)
    print()


main()
