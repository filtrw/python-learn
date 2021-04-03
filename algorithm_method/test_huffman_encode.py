import huffman_encode


@pytest.mark.parametrize('args, expected_result', [
    ('a', '1'),
    ('abacabad', '01001100100111'),
    ('accepted', '')
])
def test_huffman_encode():
    pass


from somewhere import injector


class Engine:
    def __init__(self):
        pass


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine


injector.add(Engine)
injector.add(Car)
a = injector.get(Car)
