def get_highest_average_student(students_information):
    """
    receive a list of students
    and return the student who has the highest average
    :param students_information: array of dictionaries which has student information
    :return: dictionary: one student information
    """
    highest_average = 0
    highest_student = {}
    for student in students_information:
        if highest_average < student['average']:
            highest_average = student['average']
            highest_student = student
    return highest_student


def main():
    # case receive Marcus's information
    students_information_01 = [
        {
            'first_name': 'Ali'
            , 'last_name': 'Teacher'
            , 'address': 'Homer st 1112, Vancouver, BC, CA'
            , 'year_of_birth': '1980'
            , 'average': 86
        }
        , {
            'first_name': 'Marcus'
            , 'last_name': 'Araki'
            , 'address': 'Homer st 1111, Vancouver, BC, CA'
            , 'year_of_birth': '1991'
            , 'average': 89
        }
        , {
            'first_name': 'Bob'
            , 'last_name': 'Marley'
            , 'address': 'Homer st 1113, Vancouver, BC, CA'
            , 'year_of_birth': '1960'
            , 'average': 50
        }
        ]
    print(get_highest_average_student(students_information_01))


main()
