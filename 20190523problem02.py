def drawer(num, shape_form):
    """
    :param num: a number
    :param shape_form: has 3 types: 'SHAPE1', 'SHAPE2', 'SHAPE3'
    :return: string : shape or error message
    """
    if shape_form == "SHAPE1":
        result = drawer_shape1(num)
    elif shape_form == "SHAPE2":
        result = drawer_shape2(num)
    elif shape_form == "SHAPE3":
        result = drawer_shape3(num)
    else:
        result = "Only SHAPE1 or SHAPE2 or SHAPE3 are available"
    print(result)
    return result


def drawer_shape1(num):
    """ return like this
        *****
         ***
          *
    :param num: number of the stars of the first line
    :return: string: shaped stars
    """
    star = "*" * num
    count = 0
    string = ""
    while num > 0:
        count += 1
        string = string + star
        string = string + '\n'
        star = (" " * count) + ("*" * (num - 2))
        num = num - 2
    return string


def drawer_shape2(num):
    """
    return string like this
        *****
        ****
        ***
        **
        *
    :param num: number of the stars of the first line
    :return: string: shaped stars
    """
    string = ""
    for i in range(num, 0, -1):
        string = string + "*" * i
        string = string + '\n'
    return string


def drawer_shape3(num):
    """
    return string like this
        *
        **
        ***
        ****
        *****
    :param num: number of the stars of the last line
    :return: string: shaped stars
    """
    string = ""
    for i in range(1, num + 1):
        string = string + "*" * i
        string = string + '\n'
    return string


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    # case SHAPE1 odd number
    print("SHAPE1")
    drawer(5, "SHAPE1")
    # case SHAPE1 even number
    print()
    drawer(6, "SHAPE1")
    print()
    # case SHAPE2 odd number
    print("SHAPE2")
    drawer(5, "SHAPE2")
    # case SHAPE2 even number
    print()
    drawer(6, "SHAPE2")
    print()
    # case SHAPE3 odd number
    print("SHAPE3")
    drawer(5, "SHAPE3")
    print()
    # case SHAPE3 odd number
    drawer(6, "SHAPE3")
    print()

    # case other shape
    drawer(5, "SHAPE4")


main()
