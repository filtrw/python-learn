"""
9
A
F
H
G
B : A
C : A
F : B C
E : G H
D : B C F E

4
A
B : A
C : A
D : B C

4
A B
B D
C D
D A

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

count_of_checks = int(input())
for check in range(count_of_checks):
    parent, child = input().split()
    if (check_relation(parent, child, class_relations)):
        print("Yes")
    else:
        print("No")
