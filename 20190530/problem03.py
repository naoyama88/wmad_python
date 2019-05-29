def array_search(haystack, thread):
    """
    return -1 if thread does not exist in haystack
    or return the index of haystack if thread exists in haystack and the count of thread in haystack
    :param haystack: array of integers:
    :param thread: number: target number
    :return: tuple(-1, -1)
            or tuple(the index of the first occurrence and the index of the last occurrence of the thread)
    """
    length = len(haystack)
    found = False
    last = 0
    for i in range(length):
        if haystack[i] == thread:
            last = i
            if not found:
                index = i
                found = True
    if found:
        return index, last
    else:
        return -1, -1


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
