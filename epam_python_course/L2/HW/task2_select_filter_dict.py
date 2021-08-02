"""
Данные:

friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    ...
]

Необходимо создать функции:
1. select(*field_name: list) - функция принимает список полей, которые должны быть в результирующем списке
2. field_filter(field_name: str, *collection: list) - функция принимает имя по которому необходимо фильтровать и
итерируемый объект - значения которые должны быть в результирующем списке
3. query(*collection: list, select: function, field_filter: function, ...) -> list - функция которая действительно
выбирает нужные поля и фильтрует их. Выбор значений и фильтрация предполагается делать один раз(!), т.е. сначала нужно
вычислить все поля а затем реально работать с данными.

Пример работы программы:
result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', ['Баскетбол', 'Волейбол']),
    field_filter('gender', ['Мужской']),
)
print(result) # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'}, ]

Дополнительно
1. Красивый, читаемый код
2. Документирование функций обязательно. Используем стиль документации Sphinx
"""


def select(*field_name: list):
    """
    Select required field from record and return updated version only with required fields

    :param field_name: required field for selection
    :type field_name: list
    :return: updated record
    :rtype: dict
    """

    def inner_select(record: dict):
        # Inner selection work with record and return new instance only with required fields
        updated_record = {key: record[key] for key in field_name}
        return updated_record

    return inner_select


def field_filter(field_name: str, collection: list):
    """
    Checks if the record contains values that match the filter.
    If record contains value will be return this record, in opposite case - will return None

    :param field_name: field by value which will be filtered
    :type field_name: str

    :param collection: values for filtering
    :type collection: list
    :return: record if record contains value in filter, None if not
    :rtype: dict
    """

    def inner_filter(record: dict):
        if record[field_name] in collection:
            return record
        return None

    return inner_filter


def query(*args):
    """
    Query executed filter and selection on transferred list of records
    The function has a number of assumptions:
    1. Function can work with several lists of records. Result will be present in one aggregated list
    2. Select operation always should be before filter operation in function call.
    3. Select operation will be applied in reverse order: last input first applied. Selection fields from several
       selection calls will not aggregate, only intersection will work correctly.
    4. Function can work with several filters. Filters will be applied in reverse order: last input first applied


    :param args: Lists of record for filtering and selection, select requests, filter requests

    :return: new collection respond filters and selection
    :rtype: list of dict
    """
    filtered_collection = list()
    input_collection = []
    action_collection = []

    # Define input args: list of record or function (selection, filter).
    for arg in args:
        if type(arg) is list:
            input_collection.extend(arg)
        else:
            # insert in beginning needs to place filters before select
            action_collection.insert(0, arg)

    # Take each record and verify filter condition and then select required fields
    for record in input_collection:
        updated_record = record
        for func in action_collection:
            updated_record = func(record)
            if updated_record is None:
                break
        if updated_record is not None:
            filtered_collection.append(updated_record)

    return filtered_collection


def main():
    friends = [
        {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
        {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
        {'name': 'Питер', 'gender': 'Мужской', 'sport': 'Футбол', 'email': 'email2@email2.com'}

    ]

    result = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', ['Баскетбол', 'Волейбол']),
        field_filter('gender', ['Мужской']),
    )

    print(result)  # [{'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'},]


if __name__ == '__main__':
    main()
