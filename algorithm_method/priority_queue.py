"""
Первая строка входа содержит число операций 1<=n<=10^5. Каждая из последующих nn строк задают операцию
одного из следующих двух типов:
- Insert x, где 0 <=x<=10^9 — целое число;
- ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и
выводит его.
Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500


4
Insert 200
Insert 200
ExtractMax
ExtractMax
"""
import heapq


def insert_element(element, list_to_add):
    heapq.heappush(list_to_add, element)


def get_max(list_to_get_max):
    return -heapq.heappop(list_to_get_max)


def main():
    command_number = int(input())
    command_to_add = "Insert"
    command_to_max = "ExtractMax"
    priority_queue = []
    for command in range(command_number):
        command = input()
        if command.startswith(command_to_add):
            element = command.split()[1]
            insert_element(-int(element), priority_queue)
        elif command.startswith(command_to_max):
            print(get_max(priority_queue))


if __name__ == "__main__":
    main()
