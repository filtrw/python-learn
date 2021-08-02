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
    intersection = args[0]
    for arg in args:
        intersection = set(intersection) & set(arg)
    return list(intersection)


def union(*args):
    union_set = args[0]
    for arg in args:
        union_set = set(union_set) | set(arg)
    return list(union_set)


def main():
    s1 = "SAM"
    s2 = "SPAM"
    s3 = "WHAT"

    print(f'Intersect of {s1}, {s2} is {intersect(s1, s2)}')
    print(f'Intersect of {s1}, {s2}, {s3} is {intersect(s1, s2, s3)}')
    print(f'Intersect of {[1, 2, 3]}, {(1, 4)} is {intersect([1, 2, 3], (1, 4))}')
    print(f'Union of {s1}, {s2}, {s3} is {union(s1, s2, s3)}')
    print(f'Union of {[1, 2, 3]}, {(1, 4)} is {union([1, 2, 3], (1, 4))}')


# TODO: need add parametrize tests instead simple tests

def test_intersect_strings():
    s1 = "SAM"
    s2 = "SPAM"
    expected_res = ['S', 'A', 'M'].sort()

    assert expected_res == intersect(s1, s2).sort()
    print(f'Intersect of {s1}, {s2} is {intersect(s1, s2)}')


def test_intersect_more_than_two_arguments():
    s1 = "SAM"
    s2 = "SPAM"
    s3 = "WHAT"

    expected_res = ['A']
    assert expected_res == intersect(s1, s2, s3)
    print(f'Intersect of {s1}, {s2}, {s3} is {intersect(s1, s2, s3)}')


def test_intersect_different_types():
    list_arg = [1, 2, 3]
    set_arg = (1, 4)
    expected_res = [1]
    assert expected_res == intersect(list_arg, set_arg)
    print(f'Intersect of {[1, 2, 3]}, {(1, 4)} is {intersect([1, 2, 3], (1, 4))}')


def test_union_strings():
    s1 = "SAM"
    s2 = "SPAM"
    s3 = "WHAT"
    expected_res = ['W', 'H', 'A', 'T', 'S', 'P', 'M'].sort()
    assert expected_res == union(s1, s2, s3).sort()
    print(f'Union of {s1}, {s2}, {s3} is {union(s1, s2, s3)}')


def test_union_different_types():
    list_arg = [1, 2, 3]
    set_arg = (1, 4)
    expected_res = [1, 2, 3, 4].sort()
    assert expected_res == union(list_arg, set_arg).sort()
    print(f'Union of {[1, 2, 3]}, {(1, 4)} is {union([1, 2, 3], (1, 4))}')


if __name__ == '__main__':
    main()
