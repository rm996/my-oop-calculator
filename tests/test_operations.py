import pytest

from calculator.operations import Add, Calculation, Subtract


def test_add():
    operation = Add(2, 3)
    assert operation.calculate() == 5


def test_subtract():
    operation = Subtract(5, 3)
    assert operation.calculate() == 2


def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(1, 2)


def test_abstract_calculate_method():
    class TestCalculation(Calculation):
        def calculate(self):
            return super().calculate()

    calculation = TestCalculation(1, 2)

    with pytest.raises(NotImplementedError):
        calculation.calculate()