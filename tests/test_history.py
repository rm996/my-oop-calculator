from calculator.history import History
from calculator.operations import Add, Subtract


def test_history_starts_empty():
    history = History()
    assert len(history) == 0


def test_add_to_history():
    history = History()
    calculation = Add(2, 3)

    history.add(calculation)

    assert len(history) == 1
    assert history.get_all()[0] is calculation


def test_remove_from_history():
    history = History()
    history.add(Add(2, 3))
    history.add(Subtract(5, 2))

    removed = history.remove(0)

    assert isinstance(removed, Add)
    assert len(history) == 1


def test_clear_history():
    history = History()
    history.add(Add(2, 3))

    history.clear()

    assert len(history) == 0