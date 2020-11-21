"""
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки,
которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек,
с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5
Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2:
Отсутствует
"""

lstlst = [int(i) for i in input().split()]
number_to_find = int(input())
positions = []
if number_to_find not in lstlst:
    print("Отсутствует")
else:
    for i, val in enumerate(lstlst):
        if val == number_to_find:
            positions.append(str(i))
print(" ".join(positions))
