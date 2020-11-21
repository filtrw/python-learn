"""
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar d


11
create foo global
create bar foo
create barz bar
create bary barz
add bar b
create zoo bar
create zoo2 zoo
create zoo3 zoo2
add bary b
create doo zoo
get zoo b


15
add global a
create foo1 global
create foo2 global
create bar1 foo1
create bar2 foo2
create new1 bar1
create new2 bar2
add global b
add foo1 a
add foo2 b
add bar1 a
add bar2 b
add new1 a
add new2 b
get new1 b


"""


def create_namespace(namespace, parent, namespace_relations):
    namespace_relations[namespace] = parent


def add_variable(namespace, variable, namespaces_variables):
    if namespace not in namespaces_variables.keys():
        namespaces_variables[namespace] = set()
    namespaces_variables[namespace].add(variable)


def get_namespace_of_variables(current_namespace, variable, namespace_relations, namespaces_variables):
    if (current_namespace == None):
        return None

    if (current_namespace in namespaces_variables.keys() and variable in namespaces_variables[current_namespace]):
        return current_namespace

    return get_namespace_of_variables(
        namespace_relations.get(current_namespace),
        variable,
        namespace_relations,
        namespaces_variables
    )


command_count = int(input())
namespace_relations = {"global": None}
namespaces_variables = {}
for command_line in range(command_count):
    command, namespace, argument = input().split()
    if command == "create":
        create_namespace(namespace, argument, namespace_relations)
    elif command == "add":
        add_variable(namespace, argument, namespaces_variables)
    elif command == "get":
        print(get_namespace_of_variables(namespace, argument, namespace_relations, namespaces_variables))
