def print_input_names_and_count():
    """
    get names from user input
    print and return the input name and how many times the names input
    :return:
    """
    names = []
    while True:
        name = input('input a name: ')
        if name == '0':
            break
        names.append(name)
    if not names:
        return names
    names_dic = get_how_many_times_each_name_repeated(names)
    print(names_dic)
    return names_dic


def get_how_many_times_each_name_repeated(names):
    """
    receives a list of names which may or may not contains repeated names
    return how many each name is repeated
    :param names: array of strings
    :return: dict: how many each name is repeated
    """
    record = {}
    for name in names:
        if name in record:
            record[name] += 1
        else:
            record[name] = 1
    return record


def main():
    # case receive Marcus's information
    print_input_names_and_count()


main()
