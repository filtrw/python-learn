"""
Task-2.2.3
Даны целые числа 1≤n≤10^{18} и 2≤m≤10^5, необходимо найти остаток от деления nn-го числа Фибоначчи на mm.

Sample Input:
10 2

Sample Output:
1

"""


def fib_mod(n, m):
    fib_last_digit = []
    return fib_last_digit[n]


def main():
    n, m = input().split()

    print(fib_mod(int(n), int(m)))


if __name__ == "__main__":
    main()
