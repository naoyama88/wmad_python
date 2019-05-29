def array_search(haystack, needle):
    """
    return (-1, 0) if needle does not exist in haystack
    or return the index of haystack if needle exists in haystack and the number of needles
    :param haystack: array of integers:
    :param needle: number: target number
    :return: tuple(-1, 0) or tuple(
                0: The index of the first occurrence
                1: The count how many times needle exists in haystack
            )
    """
    length = len(haystack)
    index = -1
    count = 0
    for i in range(length):
        if haystack[i] == needle:
            count += 1
            if index == -1:
                index = i
    return index, count


def main():
    # receive 1, 1
    print(array_search([111, 222, 333], 222))
    # receive 2, 2
    print(array_search([111, 222, 333, 111, 222, 333], 333))
    # receive -1, 0
    print(array_search([111, 222, 333], 444))


main()
