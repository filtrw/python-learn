"""
Task 6.1.1
В первой строке даны целое число 1 <= n <= 10^5 и массив A[1 ... n] из n различных
натуральных чисел, не превышающих 10^9, в порядке возрастания, во второй — целое
число 1 <= k <= 10^5 и k натуральных чисел b_1, ... , b_k, не превышающих 10^9. Для
каждого i от 1 до k необходимо вывести индекс 1 <= j <= n, для которого A[j]=b_i, или -1,
если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""


def binary_order_search(array: list, key: int):
    left_end = 0
    right_end = len(array)
    while left_end <= right_end:
        median = (left_end + right_end) // 2
        if median >= len(array):
            break
        if array[median] == key:
            return median + 1
        elif array[median] > key:
            right_end = median - 1
        else:
            left_end = median + 1
    return -1


def main():
    array_for_search = list(map(int, input().split()))
    size_arr_for_search = array_for_search.pop(0)
    array_for_search = array_for_search[:size_arr_for_search]

    keys_array = list(map(int, input().split()))
    count_of_keys = keys_array.pop(0)
    keys_array = keys_array[:count_of_keys]

    for key in keys_array:
        print(binary_order_search(array_for_search, key), end=" ")


if __name__ == "__main__":
    main()
