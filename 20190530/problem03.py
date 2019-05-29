def array_search(haystack, needle):
    """
    return (-1, -1) if needle does not exist in haystack
    or return the index of the first occurrence and the index of the last occurrence of the needle
    :param haystack: array of integers:
    :param needle: number: target number
    :return: tuple(-1, -1)
            or tuple(the index of the first occurrence and the index of the last occurrence of the needle)
    """
    length = len(haystack)
    index = -1
    last = -1
    for i in range(length):
        if haystack[i] == needle:
            last = i
            if index == -1:
                index = i
    return index, last


def main():
    # receive 1, 1
    print(array_search([111, 222, 333], 222))
    # receive 2, 5
    print(array_search([111, 222, 333, 111, 222, 333], 333))
    # receive 2, 8
    print(array_search([111, 222, 333, 111, 222, 333, 111, 222, 333], 333))
    # receive -1, -1
    print(array_search([111, 222, 333], 444))


main()
