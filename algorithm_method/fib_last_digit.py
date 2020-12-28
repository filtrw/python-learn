"""
Task-2.2.2
Дано число 1≤n≤10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если 0≤a,b≤9 — последние цифры чисел F_{i} F_{i+1} соответственно, то (a+b)mod10 — последняя цифра числа F_{i+2}

Sample Input:
841645

Sample Output:
5
"""


def fib_digit(n):
    fib_last_digit = []
    fib_last_digit.insert(0, 0)
    fib_last_digit.insert(1, 1)
    for next_element in range(2, n + 1):
        fib_numbers_digit = (fib_last_digit[next_element - 1] + fib_last_digit[next_element - 2]) % 10
        fib_last_digit.insert(next_element, fib_numbers_digit)
    return fib_last_digit[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
