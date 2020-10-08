"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""

import requests
import os


def read_input_file(input_file_path):
    url_string = ""
    with open(input_file_path) as infile:
        url_string = infile.readline().strip()
    return url_string


def output_remote_file_content(output_file_path, content):
    with open(output_file_path, 'w') as outfile:
        outfile.write(content)


common_url = "https://stepic.org/media/attachments/course67/3.6.3/"
first_word = ""
next_url = read_input_file(os.path.join(".", "file_samples", "input_file_chain.txt"))
content = ""
while not (first_word.startswith("We")):
    file_content = requests.get(next_url)
    first_word = file_content.text.splitlines()[0]
    if first_word.startswith("We"):
        content = file_content.text
    else:
        next_url = common_url + first_word
        print(next_url)

output_remote_file_content(os.path.join(".", "file_samples", "output_file_chain.txt"), content)
