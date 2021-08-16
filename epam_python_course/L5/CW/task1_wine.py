"""
Используя принципы ООП и языка Python, опишите класс Wine, который в дальнейшем может быть применим
при создании электронного каталога вин (сам электронный каталог вин вам пока реализовывать не нужно).
Подумайте, какие поля и методы понадобятся классу Wine, для выполнения следующих функций:

1. Хранение информации о виде вина: название, торговая марка, страна, дата разлива, многострочное примечание
(может быть любое количество строк).
2. Доступ (установка и получение) к хранимой информации.
3. Расчет выдержки вина (текущая дата дается как аргумент)
"""


class Wine:

    def __init__(self, name, trademark, country, date_of_bottling, text):
        self.name = name
        self.trademark = trademark
        self.country = country
        self.date = date_of_bottling
        self.text = text

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_trademark(self, trademark):
        self.trademark = trademark

    def get_trademark(self):
        return self.trademark

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country

    def set_date_of_bottling(self, date_of_bottling):
        self.date = date_of_bottling

    def get_date_of_bottling(self):
        return self.date

    def set_note(self, text):
        self.text = text

    def get_note(self):
        return self.text

    def get_wine_aging(self, today_date):
        return (today_date - self.date).years
