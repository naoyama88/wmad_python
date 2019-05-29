from problem00 import print2DList


def reverse_2d_array(array):
    """
    print and return the mirror of the array
    :param array: array of integers
    :return: reversed array
    """
    reversed_array_1 = []
    for v_1 in reversed(array):
        reversed_array_2 = []
        for v_2 in reversed(v_1):
            reversed_array_2.append(v_2)
        reversed_array_1.append(reversed_array_2)

    print2DList(reversed_array_1)
    return reversed_array_1


def main():
    # receive [[666, 555, 444], [333, 222, 111]]
    reversed_array = reverse_2d_array([[111, 222, 333], [444, 555, 666]])
    print()

    # receive [[999, 888, 777], [666, 555, 444], [333, 222, 111]]
    reversed_array = reverse_2d_array([[111, 222, 333], [444, 555, 666], [777, 888, 999]])
    print()


main()
