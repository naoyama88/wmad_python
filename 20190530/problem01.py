def array_search(haystack, needle):
    """
    return -1 if the thread does not exist in haystack
    or return the index of haystack if needle exists in haystack.
    :param haystack: array of integers:
    :param needle: number: target number
    :return: integer or -1
    """
    length = len(haystack)
    for i in range(length):
        if haystack[i] == needle:
            return i
    return -1


def main():
    # receive 1
    print(array_search([111, 222, 333], 222))
    # receive 2
    print(array_search([111, 222, 333, 111, 222, 333], 333))
    # receive -1
    print(array_search([111, 222, 333], 444))

main()
