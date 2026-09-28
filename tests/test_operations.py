from calculator.operations import Add


def test_add():
    operation = Add(2, 3)
    assert operation.calculate() == 5