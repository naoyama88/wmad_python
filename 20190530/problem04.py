from problem00 import print1DList


def remove_target_from(array, target):
    """
    remove target from array and return the array
    :param array: array of integers
    :param target: number
    :return:
    """
    new_array = []
    for v in array:
        if v != target:
            new_array.append(v)
    return new_array


def main():
    # receive [222, 333]
    print1DList(remove_target_from([111, 222, 333], 111))
    print()

    # receive [111, 333, 111, 333]
    print1DList(remove_target_from([111, 222, 333, 111, 222, 333], 222))
    print()

    # receive [111, 222, 333]
    print1DList(remove_target_from([111, 222, 333], 444))
    print()

    # receive []
    print1DList(remove_target_from([222, 222, 222], 222))
    print()


main()
