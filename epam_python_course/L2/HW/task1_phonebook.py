"""
Написать программу на языке Python имитирующую телефонный справочник.

1.Есть консольный интерфейс который выполняет роль меню с выбором действия (пользоваться
функцией input).
2. Действий три: добавить номер и имя человека, вывести номера человека по имени,
удалить человека по имени.
3. Хранить данные в глобальной переменной
4. Номеров может быть несколько
5. При выборе в меню добавления номера в тел. справочник, пользователь печатает имя
человека, затем вводит номер
6. При выборе вывода номер(а/ов), они выводятся в формате таблицы, где имя человека
может повторятся

Пример:

имя         номер
Кирилл      11111111
Кирилл      22222222

При выборе удаления человека, пользователь вводит имя человека. Программа ищет этого человека и
удаляет его если он есть, если его нет - выводит на экран что человека нет в справочнике.

Дополнительно
Документирование функций обязательно
"""

# Structure of phone book is dictionary, where
# key is name of man and value is list of phone number
# For example:
# {'Joe': ['111111111', '222222222']}
phonebook = {}


def add_number_by_name(name: str, phonenumber: str):
    """

    :param name:
    :param phonenumber:
    :return:
    """

    if name in phonebook:
        phonebook[name].append(phonenumber)
    else:
        phonebook[name] = [phonenumber]


def delete_by_name(name: str):
    """

    :param name:
    :return:
    """
    phonebook.pop(name)


def output_numbers_by_name(name: str):
    """

    :param name:
    :return:
    """

    # имя         номер
    # Кирилл      11111111
    # Кирилл      22222222

    print(f'имя \t номер')
    for phone in phonebook[name]:
        print(f'{name} \t {phone}')


def test_add_number_by_name():
    phonebook.clear()

    reference_phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222']
    }

    add_number_by_name('Joe', '111111111')
    add_number_by_name('Kate', '222222222')
    add_number_by_name('Joe', '333333333')

    assert phonebook == reference_phonebook


def test_delete_by_name():
    global phonebook
    phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222'],
        'Alex': ['444444444', '555555555', '888888888'],
        'Jess': ['666666666'],
        'Eric': ['777777777']
    }

    reference_phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222'],
        'Jess': ['666666666']
    }

    delete_by_name('Eric')
    delete_by_name('Alex')

    assert phonebook == reference_phonebook


def test_output_numbers_by_name():
    global phonebook
    phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222'],
        'Alex': ['444444444', '555555555', '888888888'],
        'Jess': ['666666666'],
        'Eric': ['777777777']
    }

    output_numbers_by_name('Alex')
    output_numbers_by_name('Kate')
    output_numbers_by_name('Joe')
