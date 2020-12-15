"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz
"""

import sys
import re

pattern_word = r"(\w)(\1){1,}"
replacement = r"\1"

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern_word, replacement, line))
