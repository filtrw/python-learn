"""
Напишите программу принимающую два числа и выводящую НОД по алгоритму Евклида
"""

a, b = map(int, input().split())
num1, num2 = a, b

while a and b:
    if a >= b:
        a %= b
    else:
        b %= a

print(f"The greatest common divisor for {num1} and {num2} is {max(a, b)}")