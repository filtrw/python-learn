"""
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего
угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

number = int(input())
iteration = 0
spiral_matrix = [[0 for column in range(number)] for row in range(number)]
element = 0
while element != (number * number):
    """вправо"""
    row = iteration
    for column in range(iteration, number - iteration):
        element += 1
        spiral_matrix[row][column] = str(element)

    """вниз"""
    column = number - 1 - iteration
    for row in range(iteration + 1, number - iteration):
        element += 1
        spiral_matrix[row][column] = str(element)

    """влево"""
    row = number - 1 - iteration
    for column in range(number - iteration - 2, iteration, -1):
        element += 1
        spiral_matrix[row][column] = str(element)

    """вверх"""
    column = iteration
    for row in range(number - iteration - 1, iteration, -1):
        element += 1
        spiral_matrix[row][column] = str(element)

    iteration += 1

for row in range(number):
    print(" ".join((spiral_matrix[row])), end="\n")
