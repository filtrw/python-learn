"""
Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError
"""


def check_relation(parent, child, class_relations):
    if (parent in class_relations[child] or parent == child):
        return True
    for parent_instance in class_relations[child]:
        if (check_relation(parent, parent_instance, class_relations)):
            return True
    return False


count_of_class = int(input())
class_relations = {}
for class_example in range(count_of_class):
    string_to_unpack = input().split(":")
    class_child = string_to_unpack[0].strip()
    if len(string_to_unpack) > 1:
        class_relations[class_child] = string_to_unpack[1].split()
    else:
        class_relations[class_child] = []

count_of_exceptions = int(input())
order_of_exceptions = []
for check in range(count_of_exceptions):
    exception_instance = input()
    for element in order_of_exceptions:
        if (check_relation(element, exception_instance, class_relations)):
            print(exception_instance)
            break
    order_of_exceptions.append(exception_instance)
