def get_most_repeated_number(numbers):
    """
    receive an array of integers and return the biggest number of the array
    :param numbers: array of integers
    :return: biggest number in the array
    """
    record = {}
    biggest_val = 0
    biggest_key = 0
    for i in numbers:
        if i in record:
            record[i] += 1
        else:
            record[i] = 1
        if record[i] > biggest_val:
            biggest_val = record[i]
            biggest_key = i
    return biggest_key


def main():
    # case receive 9
    numbers_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 9, 10, 9, 10, 9]
    print(get_most_repeated_number(numbers_01))

    # case receive 12
    numbers_02 = [0, 1, 2, 23, 45, 3, 4, 11, 8, 9, 10, 9, 10, 12, 12, 12]
    print(get_most_repeated_number(numbers_02))


# main()
