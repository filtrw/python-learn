"""
Task-3.5.1
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт
об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""
import requests
from os import path

number_input_file = path.join(".", "file_samples", "input_numbers.txt")
number_output_file = path.join(".", "file_samples", "output_numbers.txt")

with open(number_input_file) as input_file:
    for line in input_file:
        number = line.strip()
        numbersapi_url = "http://numbersapi.com/" + number + "/math"
        numbers_param = {
            "json": True
        }
        numbers_response = requests.get(numbersapi_url, params=numbers_param)
        number_data = numbers_response.json()
        with open(number_output_file, "a+") as output_file:
            output_file.write("Interesting\n" if number_data['found'] else "Boring\n")
