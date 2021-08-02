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

7. При выборе удаления человека, пользователь вводит имя человека. Программа ищет этого человека и
удаляет его если он есть, если его нет - выводит на экран что человека нет в справочнике.

Дополнительно
Документирование функций обязательно
"""

SELECTION_TEXT = "\nPlease, choose action with phonebook: \nInput ADD for adding phone number \nInput PRINT for " \
                 " display phone number \nInput DEL for deleting phone number\n"

phonebook = {}


def menu():
    """
    Console menu for select action and call selected function.
    In case of incorrect input text  will be displayed error message.

    :return:
    """

    add_func = "ADD"
    output_func = "PRINT"
    delete_func = "DEL"

    current_selection = input(SELECTION_TEXT)

    if current_selection == add_func:
        input_name = input("Please, input name for adding phone number ")
        input_number = input("Please, input phone number ")
        add_number_by_name(input_name, input_number)

    elif current_selection == output_func:
        input_name = input("Please, input name for display phone numbers ")
        output_numbers_by_name(input_name)

    elif current_selection == delete_func:
        input_name = input("Please, input name for deleting phone numbers ")
        delete_by_name(input_name)

    else:
        print("Incorrect command for action. Please, input ADD or PRINT or DEL")


def add_number_by_name(name: str, phonenumber: str):
    """
    Adding record in phonebook. In case when name is absent - will be added new record,
    in case when name already exists new number will be added in list of phone number for this name

    :param name: Name of man for record in phonebook
    :type name: str

    :param phonenumber: Phonenumber for record in phonebook
    :type phonenumber: str
    :return:
    """

    if name in phonebook:
        phonebook[name].append(phonenumber)
    else:
        phonebook[name] = [phonenumber]


def delete_by_name(name: str):
    """
    Deleting record in phonebook. Will be deleted all phonenumbers for input name.
    In case if name is absent in Phonebook will be displayed a message about this.

    :param name: Name of man in phonebook
    :type name: str
    :return:
    """
    if name in phonebook:
        del phonebook[name]
    else:
        print(f"Man with name is {name} not found in phonebook")


def output_numbers_by_name(name: str):
    """
    Display name and all phonenumbers which belong for this name.
    Format of displaing is table


    :param name:Name of man in phonebook
    :type name: str
    :return:
    """

    # имя         номер
    # Кирилл      11111111
    # Кирилл      22222222
    if name in phonebook:
        print(f'\nимя \t номер')
        for phone in phonebook[name]:
            print(f'{name} \t {phone}')
    else:
        print(f"Man with name is {name} not found in phonebook")

def main():
    while True:
        menu()


if __name__ == '__main__':
    main()


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


def test_delete_by_incorrect_name(capsys):
    global phonebook
    phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222']
    }

    reference_phonebook = phonebook.copy()
    name = "Peter"
    delete_by_name(name)
    captured = capsys.readouterr()

    assert captured.out == f"Man with name is {name} not found in phonebook\n"
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


def test_output_by_incorrect_name(capsys):
    global phonebook
    phonebook = {
        'Joe': ['111111111', '333333333'],
        'Kate': ['222222222']
    }

    name = "Peter"
    output_numbers_by_name(name)
    captured = capsys.readouterr()

    assert captured.out == f"Man with name is {name} not found in phonebook\n"
