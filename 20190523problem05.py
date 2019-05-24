def print_sum_numbers_digits(num_str):
    """ print the sum of the number’s digits
    :param num_str: string of number
    :return: sum number
    """
    num = 0
    for i in range(len(num_str)):
        num += int(num_str[i])
    print(num)
    return num


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    print_sum_numbers_digits(input("input number: "))


main()
