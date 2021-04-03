"""
Task-4.2.1
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита, постройте
оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате
"letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""


def huffman_encode():
    pass


string_to_encode = input()
frequency_letter = []
for letter in set(string_to_encode):
    frequency_letter.append([letter, string_to_encode.count(letter)])

frequency_letter.sort(key=lambda element: element[1], reverse=True)

index = 0
code = {}
size = 0
for element in frequency_letter:
    if index == (len(frequency_letter) - 1) and index != 0:
        code[element[0]] = "1" * index
    else:
        code[element[0]] = "1" * index + "0"
    size += len(code[element[0]]) * element[1]
    index += 1

print(len(frequency_letter), size)
for letter in code:
    print(f'{letter}: {code[letter]}')

for letter in string_to_encode:
    print(code[letter], end="")
