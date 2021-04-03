import heapq
# очередь с приоритетами есть в стандартной реализации языка Python
from collections import Counter, namedtuple


# специализация словаря, когда мы хотим отображать объекты в числа
# чтобы посчитать сколько раз каждый объект встретился в строк S  -
# надо вызвать  Counter

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        # acc - префикс кода, который мы накопили спускаясь от кода до
        # данного узла или до листа
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"
    #
    # def __lt__(self, other):
    #     return


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    # heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        # heapq.heappush(h, (freq1 + freq2, Node(left, right)))
        # как избежать ошибки о сравнение Leaf с str() -
        # можно ввести метод __lt__(self, other): return self
        # либо добавить третий компонент в сравнение
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h

    root.walk(code, "")
    # {ch: ch for ch in s } - отображать символ в сам себя
    return code


def main():
    s = input()  # входная строка
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


# def test(n_iter=100):
#     import random
#     import string
#
#     for i in range(n_iter):
#         length = random.randint(0, 32)
#         s = "".join(random.choice(string.ascii_letters) for _ range(length))
#         code = huffman_encode(s)
#         encoded = "".join(code[ch] for ch in s)
#         assert huffman_decode(encoded, code) == s
#

if __name__ == "__main__":
    main()
