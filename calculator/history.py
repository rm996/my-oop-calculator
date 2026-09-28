from calculator.operations import Calculation


class History:
    def __init__(self):
        self._calculations = []

    def add(self, calculation: Calculation):
        self._calculations.append(calculation)

    def get_all(self):
        return list(self._calculations)

    def remove(self, index: int):
        return self._calculations.pop(index)

    def clear(self):
        self._calculations.clear()

    def __len__(self):
        return len(self._calculations)