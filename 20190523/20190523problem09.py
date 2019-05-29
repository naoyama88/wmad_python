def print_numbers(A, B):
    """ print numbers
    :param A: a number
    :param B: a number
    :return: void
    """
    print_number_01(A, B)
    print_number_02(A, B)
    print_number_03(A, B)


def print_number_01(num_a, num_b):
    """ print numbers
    which are between num_a and num_b(num_a and num_b are not included)
    and which are divisible to both 3 and 5
    :param num_a: a number
    :param num_b: a number
    :return: void
    """
    for i in range(num_a + 1, num_b):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


def print_number_02(num_a, num_b):
    """ print numbers
    which are between num_a and num_b(num_a included by num_b not included)
    and which are divisible by both 6 and 7
    :param num_a: a number
    :param num_b: a number
    :return: void
    """
    for i in range(num_a, num_b):
        if i % 6 == 0 or i % 7 == 0:
            print(i)


def print_number_03(num_a, num_b):
    """ print numbers
    which are between num_a and num_b(num_a and num_b are included)
    and which are not divisible by 3
    :param num_a: a number
    :param num_b: a number
    :return: void
    """
    for i in range(num_a, num_b + 1):
        if i % 3 != 0:
            print(i)


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    print_numbers(1, 10)
    print_numbers(10, 20)


main()
