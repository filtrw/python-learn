"""
Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.
Используйте метод split строки.
"""

numbers = (int(i) for i in input().split())
summa = 0
for i in numbers:
    summa += i
print(summa)
