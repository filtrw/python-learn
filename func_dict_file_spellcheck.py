"""Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество d известных нам слов, после чего на
d строках указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк
текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
"""

word_count = int(input())
spellcheck_dictionary = set()
for word in range(word_count):
    spellcheck_dictionary.add(input().lower())
string_count = int(input())
error_dictionary = set()
for line in range(string_count):
    check_string = input().lower().split()
    for word in check_string:
        if word not in spellcheck_dictionary:
            error_dictionary.add(word.lower())

print("\n".join(error_dictionary))
