"""
У вас есть код в нефункциональном стиле. Перепишите его в функциональном стиле

sentences = ['test string',
           'with two test words: test and test',
           'and some without ** string'
           ]

count = 0

for sentence in sentences:
    count += len(sentence)
"""
import functools

sentences = ['test string',
             'with two test words: test and test',
             'and some without ** string'
             ]

count = 0

for sentence in sentences:
    count += len(sentence)

print(f'Imperative result is {count}')

assert count == functools.reduce(lambda accum, sentence_one: accum + len(sentence_one), sentences, 0)
print('Functional results (reduce) is ',
      functools.reduce(lambda accum, sentence_one: accum + len(sentence_one), sentences, 0))

assert count == sum(len(sentence_two) for sentence_two in sentences)
print('Functional result (list comprehension) is ', sum(len(sentence_two) for sentence_two in sentences))
