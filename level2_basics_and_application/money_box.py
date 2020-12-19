"""
Task-1.5.1
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то
количество монет, не превышая ее вместимость.

При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.

-- Емкость - ограниченная вместимость, количество монет
-- Сколько прямо сейчас - количество монет в копилке
-- Добавить монеты в копилку
-- Узнать можно ли добавить в копилку ещё

"""


class MoneyBox():

    def __init__(self, capacity):
        self.amount_coin = 0
        self.capacity = capacity

    # конструктор с аргументом – вместимость копилки

    def get_amount_coin(self):
        return self.amount_coin

    def can_add(self, add_count):
        # True, если можно добавить v монет, False иначе
        return add_count + self.get_amount_coin() <= self.capacity

    def add(self, add_count):
        # положить v монет в копилку
        self.amount_coin += add_count


myMoneyBox = MoneyBox(25)
print(myMoneyBox.get_amount_coin())
print("35", myMoneyBox.can_add(35))
print("20", myMoneyBox.can_add(20))
print("25", myMoneyBox.can_add(25))
myMoneyBox.add(15)
print(myMoneyBox.get_amount_coin())
myMoneyBox.add(5)
print(myMoneyBox.get_amount_coin())
myMoneyBox.add(30)
print(myMoneyBox.get_amount_coin())
