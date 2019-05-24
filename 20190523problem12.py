def find_the_number(num_a, num_b):
    """ find the positive number (and greater than 2),
    (let’s call it T) which has the following characteristic:
    • For all numbers which are less than T we have F1(x)< F2(x)
    • For all numbers which are greater than or equal T we have F1(x)> F2(x)
    :param num_a:
    :param num_b:
    :return:
    """
    x = 1
    while True:
        x += 1
        f1 = square(num_a, x)
        f2 = square(x, num_b)
        if f1 >= f2:
            return x


def calculate_f1(num_a, x):
    """ return num_a ** x
    :param num_a: a number
    :param x: a number
    :return: squared number
    """
    return square(num_a, x)


def calculate_f2(x, num_b):
    """ return x ** num_b
    :param x: a number
    :param num_b: a number
    :return: squared number
    """
    return square(x, num_b)


def square(a, b):
    """ square 2 numbers
    :param a: a number
    :param b: a number
    :return: squared number
    """
    return a ** b


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    print(find_the_number(2, 5))
    print(find_the_number(10, 12))
    print(find_the_number(3, 8))


main()
