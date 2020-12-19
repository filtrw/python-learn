"""
Task - 3.4.2
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта
есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:
class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не
наследуется явно от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем
формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2

[{"name": "A", "parents": []}, {"name": "B", "parents": []}, {"name": "C", "parents": []}]

"""
import json


def check_relation(parent, child, class_relations):
    if (parent in class_relations[child] or parent == child):
        return True
    for parent_instance in class_relations[child]:
        if (check_relation(parent, parent_instance, class_relations)):
            return True
    return False


class_and_parents = json.loads(input())
class_and_child = {}

class_relations = {}
for class_instance in class_and_parents:
    class_relations[class_instance["name"]] = class_instance["parents"]

for parent in class_relations:
    class_and_child[parent] = 0
    for child in class_relations:
        if check_relation(parent, child, class_relations):
            class_and_child[parent] += 1

for parent in sorted(class_and_child.keys()):
    print(f'{parent} : {class_and_child[parent]}')
