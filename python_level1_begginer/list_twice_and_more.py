"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4
"""

numbers = [int(i) for i in input().split()]
numbers.sort()
twice_or_more = []

for i in range(len(numbers) - 1):
    if (numbers[i] == numbers[i + 1] and (numbers[i] not in twice_or_more)):
        print(numbers[i], end=" ")
        twice_or_more.append(numbers[i])
