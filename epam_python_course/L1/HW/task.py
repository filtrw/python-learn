"""
Вам необходимо написать программу на языке Python, которая выполняет следующий алгоритм.
1) Спрашивает количество студентов на курсе
2) Спрашивает количество заданий на курсе
3) Запрашивает имена каждого из студентов
4) Запрашивает оценку по шкале от 0 до 10 (только целые числа) для каждого студента и каждого задания

Выводит ТОП-3 студента по рейтингу и ТОП-3 самых сложных заданий (тех, в которых студенты в сумме
набрали меньше всего баллов)

Дополнительно
1) Ввод и вывод производится через функции input и print
2) Для прохода цикла N раз по операциям рекомендуется использовать конструкцию for i in range(students_count):
3) Программа должна быть представлена в виде одного файла с именем task.py
"""


def top3_students(students_list):
    sorted_students = sorted(students_list, key=lambda sum_score: sum_score['sum'], reverse=True)
    top3_name_list = []
    for student in sorted_students[0:3]:
        top3_name_list.append(student["name"])
    return top3_name_list


def top3_tasks(students_list):
    task_dict = {}
    for student in students_list:
        student_keys = student.keys()
        for key in student_keys:
            if not (key == "name" or key == "sum"):
                if key not in task_dict.keys():
                    task_dict[key] = student[key]
                else:
                    task_dict[key] += student[key]
    sorted_task = dict(sorted(task_dict.items(), key=lambda item: item[1]))
    return sorted_task


def fill_students_table(students_count, task_count):
    students_list = []
    for student in range(students_count):
        student_sum = 0
        students_list.append({})
        students_list[student]["name"] = input("Name of students? ")
        for task in range(task_count):
            students_list[student][task] = int(input(f"Score of student #{student} for task number task #{task}"))
            student_sum += students_list[student][task]
        students_list[student]["sum"] = student_sum
    return students_list


if __name__ == '__main__':
    students_count = int(input("How much students at the course? "))
    task_count = int(input("How much tasks at the course? "))
    students_table = fill_students_table(students_count, task_count)
    print(f"List TOP-3 Students by sum of score {top3_students(students_table)}")
    print(f"TOP-3 Most difficult tasks with number {top3_tasks(students_table)}")


def test_top_students():
    students_list = [
        {"name": "Jonh", "0": 1, "1": 0, "2": 1, "sum": 2},
        {"name": "Sid", "0": 2, "1": 2, "1": 2, "sum": 6},
        {"name": "Bill", "0": 3, "1": 3, "2": 3, "sum": 9},
        {"name": "Jess", "0": 3, "1": 2, "2": 2, "sum": 7}
    ]
    print(*top3_students(students_list))


def test_top_tasks():
    students_list = [
        {"name": "Jonh", "0": 1, "1": 0, "2": 1, "3": 0, "sum": 2},
        {"name": "Sid", "0": 2, "1": 2, "2": 2, "3": 0, "sum": 6},
        {"name": "Bill", "0": 3, "1": 3, "2": 3, "3": 0, "sum": 9},
        {"name": "Jess", "0": 3, "1": 2, "2": 2, "3": 0, "sum": 7}
    ]
    print(*top3_tasks(students_list))
