"""
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на
противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то
на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
"""
numbers = [int(i) for i in input().split()]
numbers_sum = []
for i in range(len(numbers)):
    if (i == len(numbers) - 1) and (len(numbers) > 1):
        numbers_sum.append(numbers[i - 1] + numbers[0])
    elif (i == len(numbers) - 1) and (len(numbers) == 1):
        numbers_sum.append(numbers[i])
    else:
        numbers_sum.append(numbers[i - 1] + numbers[i + 1])
    print(numbers_sum[i], end=' ')