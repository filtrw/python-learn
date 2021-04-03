"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся
строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
"""

row_array_input = []
input_string = "run"
while input_string != "end":
    input_string = input()
    if input_string != "end":
        row_array_input.append([int(i) for i in input_string.split(" ")])

# print(row_array_input)
# print(len(row_array_input), len(row_array_input[1]))
sum_element = 0
for row in range(len(row_array_input)):
    for column in range(len(row_array_input[row])):
        sum_element = 0
        """i-1, j"""
        sum_element += row_array_input[row - 1][column]
        """i+1, j"""
        if (row + 1 >= len(row_array_input)):
            sum_element += row_array_input[0][column]
        else:
            sum_element += row_array_input[row + 1][column]
        """i, j-1"""
        sum_element += row_array_input[row][column - 1]
        """i, j+1"""
        if (column + 1 >= len(row_array_input[row])):
            sum_element += row_array_input[row][0]
        else:
            sum_element += row_array_input[row][column + 1]

        print(sum_element, end=" ")
        # row_array_output[row].append(sum_element)
    print("")
