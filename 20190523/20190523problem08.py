def print_reverse_number():
    """ print reverse number
    some number which is divisible by 10 or has floating point are not valid
    :return: reverse number
    """
    while True:
        has_point = False
        num = input("input number : ")
        for i in range(len(num)):
            if num[i] == ".":
                has_point = True
        if not has_point:
            if int(num) % 10 != 0:
                break
    result = ""
    for i in range(len(num)):
        result = num[i] + result
    print(result)
    return result


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    print_reverse_number()


main()
