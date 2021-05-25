import level2_basics_and_application.stack as testStack
import pytest


@pytest.fixture(scope="function")
def create_stack():
    my_list = testStack.ExtendedStack([1, 2, 3, 4, 5, 6, 7])
    return my_list


def test_sum(create_stack):
    create_stack.sum()
    assert create_stack[-1] == 13


def test_sub(create_stack):
    create_stack.sub()
    assert create_stack[-1] == 1


def test_mul(create_stack):
    create_stack.mul()
    assert create_stack[-1] == 42


def test_div(create_stack):
    create_stack.div()
    assert create_stack[-1] == 1


def test_div_error():
    my_list = testStack.ExtendedStack([1, 2, 3, 4, 5, 0, 7])
    with pytest.raises(ZeroDivisionError):
        my_list.div()
