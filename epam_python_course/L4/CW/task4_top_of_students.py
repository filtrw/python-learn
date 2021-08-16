"""
У вас есть данные формата
[{'name': Alexey, 'rate':2, 'course': 'Python'}, ...]

Выведите топ студентов по каждому из предметов
"""
import operator


def get_student_data() -> list:
    """
    Getting students record with name, rate and course without any sorting

    :return: list of dict records in format {"name":Joe, "rate": int, "course":someCourse}
    :rtype: list
    """
    return [{'name': 'Alexey', 'rate': 5, 'course': 'Python'},
            {'name': 'Ivan', 'rate': 6, 'course': 'Java'},
            {'name': 'Petr', 'rate': 9, 'course': 'JavaScript'},
            {'name': 'Slava', 'rate': 4, 'course': 'Python'},
            {'name': 'Kirill', 'rate': 10, 'course': 'JavaScript'},
            {'name': 'Denis', 'rate': 3, 'course': 'Python'},
            {'name': 'Alexandr', 'rate': 8, 'course': 'Java'},
            {'name': 'Mikhail', 'rate': 7, 'course': 'Java'},
            {'name': 'Maxim', 'rate': 11, 'course': 'JavaScript'}
            ]


def get_courses(data: list) -> set:
    """
    Getting distinct courses from list of students record with different courses

    :param data: list of students record in format {"name":Joe, "rate": int, "course":someCourse}
    :type data: list of dict
    :return: set of distinct course
    :rtype: set
    """
    return {item['course'] for item in data}


def get_students(data: list, course: str) -> list:
    """
    Getting students rating for required course. Sorting in reverse order from more to less

    :param data: list of students record in format {"name":Joe, "rate": int, "course":someCourse}
    :type data: list of dict
    :param course: name of course for students rating
    :type course:str
    :return: list of tuple in format ('name', 'rate')
    :rtype: list
    """
    return sorted([(item['name'], item['rate']) for item in data if item['course'] == course],
                  key=operator.itemgetter(1), reverse=True)


def get_students_rating(course: str) -> str:
    """
    Getting top of students by the course in string format

    :param course: Course for rating of students
    :type course: str
    :return: String with results of sorting students rating by required courses
    :rtype:str
    """
    return f"COURSE {course}\n" + \
           "\n".join('{:10} \t {:4}'.format(*student) for student in get_students(get_student_data(), course))


def main():
    print("\n".join(get_students_rating(course) for course in get_courses(get_student_data())))


if __name__ == '__main__':
    main()


def test_get_courses():
    expected_result = {'Python', 'Java', 'JavaScript'}
    assert expected_result == get_courses(get_student_data())


def test_get_students():
    expected_result_python = [('Alexey', 5), ('Slava', 4), ('Denis', 3)]
    assert expected_result_python == get_students(get_student_data(), 'Python')


def test_get_students_rating():
    expected_result_java = f"COURSE Java\n" + \
                           '{:10} \t {:4}\n'.format(*('Alexandr', 8)) + \
                           '{:10} \t {:4}\n'.format(*('Mikhail', 7)) + \
                           '{:10} \t {:4}'.format(*('Ivan', 6))

    assert expected_result_java == get_students_rating('Java')
