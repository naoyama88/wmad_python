def divide(A, B):
    """ divide using 2 numbers
    :param A: operand which will be divided by B
    :param B: operand which will divide A
    :return:
    """
    # result = A / B
    count = 0
    while A - B >= 0:
        A = A - B
        count += 1
    print(count)
    return count


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    divide(4, 2)
    divide(1, 5)
    divide(6, 5)


main()
