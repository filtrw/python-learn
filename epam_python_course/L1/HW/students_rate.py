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

from collections import Counter

if __name__ == '__main__':
    students_count = int(input("How much students at the course? "))
    task_count = int(input("How much tasks at the course? "))

    # 2 structure for save results -
    # dict of student and common score for all tasks "student":"sum_of_score"
    # dict of common rate for tasks "task": "sum_of_score"

    tasks_rate = {}
    students_rate = {}

    for student in range(students_count):
        student_sum = 0
        name = input("Name of students? ")

        for task in range(1, task_count+1):
            task_score = int(input(f"Score of student {name} for task number task #{task} "))
            if task not in tasks_rate:
                tasks_rate[task] = task_score
            else:
                tasks_rate[task] += task_score

            student_sum += task_score
        students_rate[name] = student_sum

    ordered_tasks_rate = Counter(tasks_rate).most_common()
    ordered_students_rate = Counter(students_rate).most_common(3)

    print("TOP-3 Students with greatest score")
    for student in ordered_students_rate:
        print(f"{student[0]} with total score {student[1]}")

    print("TOP-3 the most difficult tasks")
    ordered_tasks_rate.reverse()
    for task in ordered_tasks_rate[0:3]:
        print(f"Task #{task[0]} with total score {task[1]}")


