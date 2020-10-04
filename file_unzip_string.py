"""
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет
восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью
кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас
появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со
входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных
данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
"""
import os


def unzip_string(input_string):
    output_string = ""
    cursor = 0
    while cursor < len(input_string):
        str_count = ""
        letter = input_string[cursor]
        cursor += 1
        while (cursor < len(input_string) and input_string[cursor].isdigit()):
            str_count += input_string[cursor]
            cursor += 1
        output_string += letter * int(str_count)
    return output_string


def read_zip_string(input_file_path):
    with open(input_file_path) as infile:
        return infile.readline().strip()


def write_unzip_string(output_file_path, output_string):
    with open(output_file_path, 'w') as outfile:
        outfile.write(output_string)


test_string = read_zip_string(os.path.join(".", "file_samples", "dataset_3363_2.txt"))
write_unzip_string(os.path.join(".", "file_samples", "output.txt"), unzip_string(test_string))
