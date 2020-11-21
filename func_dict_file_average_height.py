"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11
включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса
(для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив
него прочерк.

В качестве ответа прикрепите файл с полученными данными о среднем росте.

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
"""
import os


def read_table_height(input_file_path):
    data_array = []
    with open(input_file_path) as infile:
        for line in infile:
            new_line = line.rstrip()
            data_array.append(new_line.split('\t'))
    return data_array


def write_table_height(output_file_path, school_data):
    with open(output_file_path, 'w') as outfile:
        for school_class in range(1, 12):
            if str(school_class) in school_data.keys():
                result_line = str(school_class) + " " + str(school_data[str(school_class)]) + "\n"
            else:
                result_line = str(school_class) + " -\n"
            outfile.write(result_line)


school_data_array = read_table_height(os.path.join(".", "file_samples", "input_student_height.txt"))

total_height_by_class = {"1": [0, 0], "2": [0, 0], "3": [0, 0], "4": [0, 0], "5": [0, 0], "6": [0, 0], "7": [0, 0],
                         "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0]}
average_height = {}
for student in school_data_array:
    total_height_by_class[student[0]][0] += int(student[2])
    total_height_by_class[student[0]][1] += 1

for school_class in total_height_by_class:
    if (total_height_by_class[school_class][1] != 0):
        average_height[school_class] = total_height_by_class[school_class][0] / total_height_by_class[school_class][1]

print(average_height)
write_table_height(os.path.join(".", "file_samples", "output_student_height.txt"), average_height)
