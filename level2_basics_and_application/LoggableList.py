import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, element):
        super(LoggableList, self).append(element)
        self.log(element)


myList = LoggableList([1, 2, 3, 4, 5])
myList.append(99)
print(myList)
