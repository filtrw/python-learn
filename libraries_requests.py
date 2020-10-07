"""
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и
посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру,
чтобы убрать пробельные символы по краям).

После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта
не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью
метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число.
"""

import requests
import os


def input_file_url(input_file_path):
    url_string = ""
    with open(input_file_path) as infile:
        url_string = infile.readline().strip()
    return url_string


def input_file_line(input_file_path):
    file_content = requests.get(input_file_path)
    return len(file_content.text.splitlines())


url_input = input_file_url(os.path.join(".", "file_samples", "input_url.txt"))
print(input_file_line(url_input))
