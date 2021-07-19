"""
Дописать универсальные функции работы с множествами

def intersect(*args):
     pass

def union(*args):
     pass

>> intersect(s1, s2), union(s1, s2) #Два операнда
(['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C'])
>> intersect([1,2,3], (1,4)) #Смешивание типов
[1]
"""


def intersect(*args):
    intersect_set = set()
    for element in args[0]:
        is_intersect_element = True
        for arg in args[1:]:
            if element not in arg:
                is_intersect_element = False
                break
        if is_intersect_element:
            intersect_set.add(element)
    return list(intersect_set)


def union(*args):
    union_set = set()
    for arg in args:
        for element in arg:
            union_set.add(element)
    return list(union_set)


s1 = "SAM"
s2 = "SPAM"
s3 = "WHAT"

print(f'Intersect of {s1}, {s2} is {intersect(s1, s2)}')
print(f'Intersect of {s1}, {s2}, {s3} is {intersect(s1, s2, s3)}')
print(f'Intersect of {[1, 2, 3]}, {(1, 4)} is {intersect([1, 2, 3], (1, 4))}')
print(f'Union of {s1}, {s2}, {s3} is {union(s1, s2, s3)}')
print(f'Union of {[1, 2, 3]}, {(1, 4)} is {union([1, 2, 3], (1, 4))}')
