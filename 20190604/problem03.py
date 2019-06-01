def get_number_repeated_once(numbers):
    """
    receives a list of integer
    from each number there are exactly 2 in the list except one number that is repeated only once
    return the number that is repeated only once
    :param numbers: array of integers
    :return: integer: number repeated only once in the array of integer
    """
    record = {}
    for i in numbers:
        if i in record:
            record.pop(i)
        else:
            record[i] = 1
    for key in record:
        # record has only one elements
        return key


def main():
    # case receive 3
    numbers_01 = [1, 2, 1, 2, 3, 4, 5, 6, 4, 5, 6]
    print(get_number_repeated_once(numbers_01))

    # case receive 6
    numbers_02 = [12, 0, 12, 3, 0, 3, 4, 4, 5, 6, 5]
    print(get_number_repeated_once(numbers_02))


main()
