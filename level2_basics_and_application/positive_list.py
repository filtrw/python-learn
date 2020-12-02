class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, element):
        if element > 0:
            return super(PositiveList, self).append(element)
        else:
            raise NonPositiveError(str(element) + " is not positive")


my_list = PositiveList()
my_list.append(10)
# my_list.append(0)
my_list.append(-5)
