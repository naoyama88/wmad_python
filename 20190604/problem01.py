def get_how_many_times_each_number_repeated(numbers):
    """
    receives a list of integer which may or may not contains repeated numbers
    return how many each item is repeated
    :param numbers: array of integers
    :return: dict: how many each item is repeated
    """
    record = {}
    for i in numbers:
        if i in record:
            record[i] += 1
        else:
            record[i] = 1
    return record


def main():
    # case receive {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 2, 9: 4, 10: 3}
    numbers_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 9, 10, 9, 10, 9]
    print(get_how_many_times_each_number_repeated(numbers_01))

    # case receive {0: 1, 1: 1, 2: 1, 23: 1, 45: 1, 3: 1, 4: 1, 11: 1, 8: 1, 9: 2, 10: 2, 12: 3}
    numbers_02 = [0, 1, 2, 23, 45, 3, 4, 11, 8, 9, 10, 9, 10, 12, 12, 12]
    print(get_how_many_times_each_number_repeated(numbers_02))


main()
