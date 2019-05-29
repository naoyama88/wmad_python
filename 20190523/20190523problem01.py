def calculator(num1, num2, operator):
    """ calculate two numbers using operator got from parameter
    :param num1: a number
    :param num2: a number
    :param operator: plus, minus, multiplication and division only
    :return: int|string result of the calculate or error message
    """
    if operator == "+":
        result = int(num1) + int(num2)
    elif operator == "-":
        result = int(num1) - int(num2)
    elif operator == "/":
        if num1 != 0 and num2 == 0:
            result = "the operation is not possible because one number is zero"
        else:
            result = int(num1) / int(num2)
    elif operator == "*":
        result = int(num1) * int(num2)
    else:
        result = 'you have to input an operator from those operator +, -, *, /'
    print(result)
    return result


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    # case use +
    calculator(2, 3, "+")
    # case use -
    calculator(4, 2, "-")
    # case use *
    calculator(6, 7, "*")
    # case use /
    calculator(8, 2, "/")
    # case divide by 0
    calculator(8, 0, "/")
    # case use % and make sure that it fails
    calculator(9, 4, "%")


main()
