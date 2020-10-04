"""
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не
так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и
выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких
слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
"""
import os


def count_word(text):
    text = text.lower().split()
    word_array = dict()
    max = 0
    for word in text:
        if (word not in word_array):
            word_array[word] = 1
        else:
            word_array[word] += 1
        if word_array[word] > max:
            max = word_array[word]
    return [max, word_array]


def frequent_word(word_dictionary, max):
    top_frequent_words = []
    for word in word_dictionary:
        if (word_dictionary[word] == max):
            top_frequent_words.append(word)
    top_frequent_words.sort()
    return top_frequent_words


def read_strings(input_file_path):
    text = ""
    with open(input_file_path) as infile:
        for line in infile:
            text += line.strip() + " "
    return text


def output_file_rating(output_file_path, max_count, frequent_words):
    with open(output_file_path, 'w') as outfile:
        for word in frequent_words:
            output_string = word + " " + str(max_count) + "\n"
            outfile.write(output_string)


test_string = read_strings(os.path.join(".", "file_samples", "input_rating.txt"))
[max_number, word_rate] = count_word(test_string)
top = frequent_word(word_rate, max_number)
output_file_rating(os.path.join(".", "file_samples", "output_rating.txt"), max_number, top)
