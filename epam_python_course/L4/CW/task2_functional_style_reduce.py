"""
У вас есть код в нефункциональном стиле. Перепишите его в функциональном стиле

sentences = ['test string',
           'with two test words: test and test',
           'and some without ** string'
           ]

count = 0

for sentence in sentences:
    count += sentence.count('test')
"""
import functools

sentences = ['test string',
             'with two test words: test and test',
             'and some without ** string'
             ]

count = 0

for sentence in sentences:
    count += sentence.count('test')

print(f'Imperative style code count variable is {count}')

assert count == functools.reduce(lambda accum, sentence_one: accum + sentence_one.count('test'), sentences, 0)
print(f'Functional style code result is ',
      functools.reduce(lambda accum, sentence_one: accum + sentence_one.count('test'), sentences, 0))
