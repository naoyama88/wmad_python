def is_prime(num):
    """ check a number from parameter is prime number or not (this function is from problem3)
    :param num: a number
    :return: boolean: the number is prime number or not
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_next_prime_number(num):
    """ get next prime number from a number
    :param num: a number
    :return: next prime number
    """
    while True:
        num += 1
        if is_prime(num):
            print(num)
            return num


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    get_next_prime_number(1)
    get_next_prime_number(3)
    get_next_prime_number(9)
    get_next_prime_number(17)
    get_next_prime_number(29)


main()
