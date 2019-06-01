def get_distinct_numbers(numbers):
    """
    receives a list of integer which may contains repeated numbers
    remove the repeated numbers and keeps the distinct number
    return the list of distinct numbers
    :param numbers: array of integers
    :return: array: return the list of distinct numbers
    """
    return list(set(numbers))


def main():
    # case receive [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 9, 10, 9, 10, 9]
    print(get_distinct_numbers(numbers_01))

    # case receive [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 45, 23]
    numbers_02 = [0, 1, 2, 23, 45, 3, 4, 11, 8, 9, 10, 9, 10, 12, 12, 12]
    print(get_distinct_numbers(numbers_02))


main()
