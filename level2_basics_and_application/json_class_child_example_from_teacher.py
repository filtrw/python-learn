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

data = json.loads(input())
children = dict()

for cls in data:
    for par in cls["parents"]:
        if par not in children:
            children[par] = []
        children[par].append(cls["name"])


def dfs(v, used):
    size = 1
    used.add(v)
    if v not in children:
        return size

    for child in children[v]:
        if child not in used:
            size += dfs(child, used)

    return size


ans = []

for cls in data:
    ans.append((cls["name"], dfs(cls["name"], set())))

for i in sorted(ans):
    print(i[0], ":", i[1])
