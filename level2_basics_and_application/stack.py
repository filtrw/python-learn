"""

"""


class ExtendedStack(list):

    def double_pop(self):
        return [self.pop(), self.pop()]

    def sum(self):
        # операция сложения
        self.append(sum(self.double_pop()))

    def sub(self):
        # операция вычитания
        substitution_list = self.double_pop()
        self.append(substitution_list[0] - substitution_list[1])

    def mul(self):
        # операция умножения
        multiply_list = self.double_pop()
        self.append(multiply_list[0] * multiply_list[1])

    def div(self):
        # операция целочисленного деления
        div_list = self.double_pop()
        self.append(div_list[0] // div_list[1])


myList = ExtendedStack([1, 2, 3, 4, 5, 6, 7])
print(myList.sum())
print(myList)
print(myList.sub())
print(myList)
print(myList.mul())
print(myList)
print(myList.div())
print(myList)
