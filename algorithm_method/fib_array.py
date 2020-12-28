"""
Task-2.2.1
Задача на программирование: небольшое число Фибоначчи


Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F_0=0, F_1=1 F_n=F_{n-1}+F_{n-2}
при n≥2).

Sample Input:
3

Sample Output:
2

"""


def fib(n):
    # put your code here
    fib_array = []
    fib_array.append(0)
    fib_array.append(1)

    for element in range(2, n + 1):
        fib_array.insert(element, (fib_array[element - 1] + fib_array[element - 2]))

    return fib_array[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
