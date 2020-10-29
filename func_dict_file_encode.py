"""
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
они говорили каким-то странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный
шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли
ключ к шифру и теперь нуждаются в помощи:
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход
две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы
конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую
нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc

Sample Output 2:
badc
dcba
"""


def encode_string(coded_dict, string_to_encode):
    encrypted_string = ""
    for letter in string_to_encode:
        encrypted_string += coded_dict.get(letter)
    return encrypted_string


original_string = input()
code_string = input()
coded_dict = dict(zip(original_string, code_string))
decoded_dict = dict(zip(code_string, original_string))
string_to_encode = input()
string_to_decode = input()
print(encode_string(coded_dict, string_to_encode))
print(encode_string(decoded_dict, string_to_decode))

"""
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
"""
