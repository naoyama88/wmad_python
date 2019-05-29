from problem00 import print1DList


def bubble_sort(array):
    """
    reproduce bubble sort
    :param array: array of integers
    :return: sorted array
    """
    length = len(array)
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(length):
            if i == length - 1:
                break
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                is_sorted = True

    return array


def main():
    # receive [1, 2, 3, 4, 7, 8, 11, 12]
    sorted_array = bubble_sort([12, 3, 8, 4, 11, 2, 7, 1])
    print1DList(sorted_array)

    # receive [1, 2, 3, 3, 3, 6, 7, 9]
    sorted_array = bubble_sort([3, 1, 9, 6, 7, 2, 3, 3])
    print1DList(sorted_array)


main()
