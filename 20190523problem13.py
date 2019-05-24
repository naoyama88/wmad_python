def draw_multiplication_table(max_num):
    """ print the multiplication table for 1 to max_num
    :param max_num: the max number of each column
    :return:
    """
    # to tidy a table
    print()

    # the left side of x
    print("%3s" % "x ", end="")

    # the first line of numbers
    for n in range(1, max_num + 1):
        print("%3d" % n, end="")
    print()

    # make a table
    for x in range(1, max_num + 1):
        # the left vertical line
        print("%3d" % x, end="")
        for n in range(1, max_num + 1):
            print("%3.0f" % (x * n), end="")
        print()

    # to tidy a table
    print()


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    draw_multiplication_table(1)
    draw_multiplication_table(3)
    draw_multiplication_table(12)
    draw_multiplication_table(7)


main()
