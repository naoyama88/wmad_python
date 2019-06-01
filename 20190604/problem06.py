def print_inputted_numbers_sum():
    """
    get numbers from user input
    and return the sum of the numbers
    unavailable to get inputted same number
    :return: integer: sum of the numbers
    """
    numbers = []
    while True:
        number = input('input a number: ')
        if number == '0':
            break
        if int(number) in numbers:
            print('It\'s already inputted')
            continue
        numbers.append(int(number))
    return sum(numbers)


def main():
    # case
    print(print_inputted_numbers_sum())


main()
