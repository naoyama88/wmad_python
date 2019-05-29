def convert_to_base2_and_print(base10_num):
    """ convert base 10 number into base 2 number
    :param base10_num: a base 10 number
    :return: string: base 2 number
    """
    base2_num_str = ''
    while base10_num > 0:
        remainder = base10_num % 2
        base2_num_str = str(remainder) + base2_num_str
        base10_num = int(base10_num / 2)
    print(base2_num_str)
    return base2_num_str


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    convert_to_base2_and_print(15)
    convert_to_base2_and_print(256)


main()
