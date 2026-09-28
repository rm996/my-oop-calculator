from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def calculate(self) -> float:
        raise NotImplementedError


class Add(Calculation):
    def calculate(self) -> float:
        return self.a + self.b


class Subtract(Calculation):
    def calculate(self) -> float:
        return self.a - self.b