def is_string_same_as_reverse(string):
    """ check whether string and string which is reversed of string are same or not
    :param string: a string
    :return:
    """
    reverse_string = ''
    for c in string:
        reverse_string = c + reverse_string

    if string == reverse_string:
        result = string + 'and' + reverse_string + 'are same string'
    else:
        result = string + 'and' + reverse_string + 'are not same string'
    print(result)
    return result


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    is_string_same_as_reverse('asdfdsa')
    is_string_same_as_reverse('asdfdsA')
    is_string_same_as_reverse('bABABAb')
    is_string_same_as_reverse('bABABAB')


main()
