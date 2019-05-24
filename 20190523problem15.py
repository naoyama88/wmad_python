def is_correct_statement(statement):
    """ check the statement whether it's correct or not
    :param statement: a statement
    :return: result of the check
    """
    count_open_parenthesis = 0
    for c in statement:
        if c == '(':
            # if c == open parenthesis
            count_open_parenthesis = count_open_parenthesis + 1
        elif c == ')':
            # if c == close parenthesis
            if count_open_parenthesis == 0:
                # like this a+b+()+ ~~
                print('statement is invalid')
                exit()
            count_open_parenthesis = count_open_parenthesis -1
        elif c != '+'\
                and c != '-'\
                and c != '*'\
                and c != '/'\
                and c != '%'\
                and c != 'a'\
                and c != 'b'\
                and c != 'c'\
                and c != 'd'\
                and c != 'e'\
                and c != 'f'\
                and c != 'g'\
                and c != 'h'\
                and c != 'i'\
                and c != 'j'\
                and c != 'k'\
                and c != 'l'\
                and c != 'm'\
                and c != 'n'\
                and c != 'o'\
                and c != 'p'\
                and c != 'q'\
                and c != 'r'\
                and c != 's'\
                and c != 't'\
                and c != 'u'\
                and c != 'v'\
                and c != 'w'\
                and c != 'x'\
                and c != 'y'\
                and c != 'z':
            result = 'invalid character'
            print(result)
            return result

    if count_open_parenthesis != 0:
        result = 'statement is invalid'
    else:
        result = 'statement is valid'
    print(result)
    return result


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    is_correct_statement('(a+b+c+d)-x*y/z')
    is_correct_statement('(a+b+c+d)-((x*y)/z)')
    is_correct_statement('((a+b+c+d)-(x*y))/z')
    # invalid
    is_correct_statement('(((a+b+c+d)-(x*y))/z')
    is_correct_statement('((a+b+c+d)-(x*y))/z)')


main()
