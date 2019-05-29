def print_distance_between_two_numbers():
    """ get max, min and distance
    :return: max, min, distance
    """
    num_a = 0
    num_b = 0
    num_a_has_num = False
    num_b_has_num = False

    contain_string = False
    while not contain_string:
        contain_string = False
        input_string = input('input a number : ')
        i = 0
        if len(input_string) == 0:
            exit('input a number')
        for c in input_string:
            is_num = False
            if c == '-':
                if i == 0:
                    is_num = True
                else:
                    is_num = False
            elif c == '0'\
                    or c == '1'\
                    or c == '2'\
                    or c == '3'\
                    or c == '4'\
                    or c == '5'\
                    or c == '6'\
                    or c == '7'\
                    or c == '8'\
                    or c == '9':
                is_num = True

            if not is_num:
                contain_string = True
            i = i + 1
        if not contain_string:
            if not num_b_has_num:
                num_b = int(input_string)
                num_b_has_num = True
            else:
                if num_a_has_num:
                    if num_b <= int(input_string):
                        num_b = int(input_string)
                    elif num_a > int(input_string):
                        num_a = int(input_string)
                else:
                    if num_b < int(input_string):
                        num_a = num_b
                        num_a_has_num = True
                        num_b = int(input_string)
                    else:
                        num_a = int(input_string)
                        num_a_has_num = True

    if not num_a_has_num or not num_b_has_num:
        exit('input at least two numbers')

    absolute_num = abs(num_b - num_a)

    print('Max num is', num_b)
    print('Min num is', num_a)
    print('Distance is', absolute_num)
    return num_b, num_b, absolute_num


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    max, min, distance = print_distance_between_two_numbers()


main()
