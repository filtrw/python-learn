"""
Task-1.6.2
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:
class B(A):
    pass

Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass
class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс
не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и
"No", если не является.

Sample Input:
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
Sample Output:
Yes
Yes
Yes
No

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
