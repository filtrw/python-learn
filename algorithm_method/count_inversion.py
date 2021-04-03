"""
Task 6.4.1
Первая строка содержит число 1 <= n <= 10^5, вторая — массив A[1 ... n], содержащий натуральные числа, не
превосходящие 10^9. Необходимо посчитать число пар индексов 1 <= i < j <= n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором
смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
"""

from bisect import bisect_left, bisect_right


def count_inversion(array: list):
    pass


def merge(left_array, right_array):
    pass


def merge_sort(array: list):
    size = len(array)
    if size <= 1:
        return array

    median = size // 2
    left_array = merge_sort(list(array[i] for i in range(0, )))


def main():
    array_size = int(input())
    array = list(map(int, element) for element in input.split())
    print(count_inversion(array))


if __name__ == "__main__":
    main()
