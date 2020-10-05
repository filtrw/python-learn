"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает
его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и
добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой
со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""

import os


def average_rate_by_students(students_rate):
    math_average = 0
    physics_average = 0
    russian_avarage = 0
    average_by_student = 0
    average_list = []
    for student in range(len(students_rate)):
        average_by_student = 0
        for rate in range(1, len(students_rate[student])):
            average_by_student += int(students_rate[student][rate])
            if (rate == 1):
                math_average += int(students_rate[student][rate])
            elif (rate == 2):
                physics_average += int(students_rate[student][rate])
            else:
                russian_avarage += int(students_rate[student][rate])
        average_list.append(average_by_student / (len(students_rate[student]) - 1))
    math_average = math_average / len(students_rate)
    physics_average = physics_average / len(students_rate)
    russian_avarage = russian_avarage / len(students_rate)
    average_list.append([math_average, physics_average, russian_avarage])
    return average_list


def input_students_list(input_file_path):
    students_list = []
    with open(input_file_path) as infile:
        for line in infile:
            students_list.append(line.split(';'))
    return students_list


def output_average_rate(output_file_path, average_list):
    with open(output_file_path, 'w') as outfile:
        for row in range(len(average_list)):
            if row < (len(average_list) - 1):
                output_string = str(average_list[row]) + "\n"
            else:
                output_string = ""
                for element in range(len(average_list[row])):
                    output_string += str(average_list[row][element]) + " "
            outfile.write(output_string)


list_of_rate = input_students_list(os.path.join(".", "file_samples", "input_student.txt"))
output_average_rate(os.path.join(".", "file_samples", "output_student.txt"), average_rate_by_students(list_of_rate))
