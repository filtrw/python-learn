"""
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i).
Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12
Sample Output:
11
41
47
61
41
"""


def f(some_number):
    return some_number + 10


number_string = int(input())
original_array = []
i = 0
while i < number_string:
    original_array.append(int(input()))
    i += 1

dictionary_for_function = {}
for element in original_array:
    if element not in dictionary_for_function:
        dictionary_for_function[element] = f(element)
    print(dictionary_for_function[element], end="\n")
