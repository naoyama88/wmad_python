def array_search(haystack, thread):
    """
    return -1 if thread does not exist in haystack
    or return the index of haystack if thread exists in haystack
    :param haystack: array of integers:
    :param thread: number: target number
    :return: tuple(-1, 0) or tuple(
                0: The index of the first occurrence
                1: The count which is how many times thread exists in haystack
            )
    """
    length = len(haystack)
    found = False
    count = 0
    for i in range(length):
        if haystack[i] == thread:
            count += 1
            if not found:
                index = i
                found = True
    if found:
        return index, count
    else:
        return -1, 0


def main():
    # receive 1, 1
    print(array_search([111, 222, 333], 222))
    # receive 2, 2
    print(array_search([111, 222, 333, 111, 222, 333], 333))
    # receive -1, 0
    print(array_search([111, 222, 333], 444))


main()
