"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется
в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова
в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a

Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a

Sample Output 2:
a 3
"""


def count_word(text):
    text = text.lower()
    word_array = [word for word in text.split()]
    word_dictionary = {}
    for word in word_array:
        if word not in word_dictionary:
            word_dictionary[word] = word_array.count(word)
            print(word, word_dictionary[word], end="\n")


example_one = "a aa abC aa ac abc bcd a"
count_word(example_one)

example_two = "a A a"
count_word(example_two)

"""
text = input().lower().split()
dictionary = dict()
for word in text:
    if(word not in dictionary):
        dictionary[word] = 1
    else:
        dictionary[word]+=1
for word, count in dictionary.items():
    print(word, count)
"""
