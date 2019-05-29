def print2DList(array):
    """
    print depth 2 array
    :param array: array: depth 2 array
    :return: void
    """
    print('print2DList')
    length = len(array)
    for i in range(length):
        print('array[' + str(i) + ']:')
        print1DList(array[i])


def print1DList(array):
    """
    print depth 1 array
    :param array: array: depth 1 array
    :return: void
    """
    print('print1DList')
    length = len(array)
    for i in range(length):
        print('[' + str(i) + ']', array[i])

