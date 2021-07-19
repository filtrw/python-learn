"""
Данные:

friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    ...
]

Необходимо создать функции:
1. select(*field_name: list) - функция принимает список полей, которые должны быть в результирующем списке
2. field_filter(field_name: str, *collection: list) - функция принимает имя по которому необходимо фильтровать и итерируемый объект - значения которые должны быть в результирующем списке
3. query(*collection: list, select: function, field_filter: function, ...) -> list - функция которая действительно выбирает нужные поля и фильтрует их. Выбор значений и фильтрация предполагается делать один раз(!), т.е. сначала нужно вычислить все поля а затем реально работать с данными.

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
