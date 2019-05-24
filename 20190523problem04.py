def stdev_calculator():
    """ calculate the total, average, standard deviation of the numbers the user had entered
    :return: following 3 numbers
    """
    count = 0
    total = 0
    nums = []
    while True:
        num = int(input("input number: "))
        if num == 0:
            break
        nums.append(num)
        count += 1
        total += num
    average = total / count
    squared_differences = []
    for i in nums:
        squared_differences.append((i - average) ** 2)
    sum_differences = sum(squared_differences)
    stdev = sum_differences ** 0.5

    return total, average, stdev


def main():
    """ main function for test the function inside of this file
    :return: void
    """
    total, average, stdev = stdev_calculator()
    print("total is", total)
    print("average is", average)
    print("stdev is", stdev)


main()
