from problem00 import print1DList


def find_greatest_student(array):
    """
    find person who has highest GPA and return tuple(0:the person's name and 1:it's GPA)
    :param array: array of tuples
    :return: tuple(greatest_student_name, highest_gpa)
    """
    highest_gpa = -1
    greatest_student_name = ''
    for v in array:
        student_name = v[0]
        gpa = get_gpa([v[1], v[2], v[3], v[4], v[5]])
        if gpa > highest_gpa:
            greatest_student_name = student_name
            highest_gpa = gpa
    return greatest_student_name, highest_gpa


def get_gpa(scores):
    """
    calculate GPA from array of score
    :param scores: array of scores
    :return: number as GPA (0 or 1 or 2 or 3 or 4)
    """
    subjects_gpas = []
    for score in scores:
        subjects_gpas.append(calculate_gpa(score))
    gpa = get_average(subjects_gpas)
    return gpa


def calculate_gpa(score):
    """
    calculate GPA from score
    :param score: number between 0 and 100
    :return: number as GPA (0 or 1 or 2 or 3 or 4)
    """
    if score < 60:
        return 0
    elif 60 <= score < 70:
        return 1
    elif 70 <= score < 80:
        return 2
    elif 80 <= score < 90:
        return 3
    elif score >= 90:
        return 4


def get_average(array):
    """
    get the average of array elements
    :param array: array
    :return: the average of array elements
    """
    total = sum(array)
    count = len(array)
    average = total / count
    return average


def main():
    # receive ('Ali', 4.0)
    students_info_01 = [
        ('Marcus', 95, 90, 85, 80, 75)
        , ('Ali', 100, 100, 100, 100, 100)
        , ('Monkey', 40, 40, 40, 40, 40)
    ]
    print1DList(find_greatest_student(students_info_01))

    print()

    # receive ('Marcus', 3.0) (Marcus's GPA and Ali's GPA are same)
    students_info_02 = [
        ('Marcus', 80, 80, 80, 80, 80)
        , ('Ali', 90, 70, 90, 70, 80)
        , ('Monkey', 59, 60, 69, 70, 79)
        , ('Mike', 80, 89, 90, 50, 50)
    ]
    print1DList(find_greatest_student(students_info_02))

    print()

    # receive ('Marcus', 0.0)
    students_info_03 = [
        ('Marcus', 50, 50, 40, 30, 40)
        , ('Ali', 40, 50, 59, 50, 50)
    ]
    print1DList(find_greatest_student(students_info_03))


main()
