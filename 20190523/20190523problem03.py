def is_prime(num):
    """ check a number from parameter is prime number or not
    :param num: a number
    :return: boolean: the number is prime number or not
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    print("Is 1 prime number? ", is_prime(1))
    print("Is 2 prime number? ", is_prime(2))
    print("Is 3 prime number? ", is_prime(3))
    print("Is 9 prime number? ", is_prime(9))
    print("Is 13 prime number? ", is_prime(13))


main()
