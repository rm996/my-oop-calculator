from unittest.mock import patch

from calculator.app import CalculatorApp


def test_exit():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Goodbye!")


def test_help():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["help", "exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Available commands:")
    mock_print.assert_any_call("Goodbye!")


def test_add():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["add", "10", "5", "exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Result: 15")
    assert len(app.history) == 1


def test_subtract():
    app = CalculatorApp()

    with patch(
        "builtins.input",
        side_effect=["subtract", "10", "3", "exit"],
    ):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Result: 7")
    assert len(app.history) == 1


def test_empty_history():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["history", "exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("No calculations yet.")


def test_history_with_calculation():
    app = CalculatorApp()

    with patch(
        "builtins.input",
        side_effect=["add", "10", "5", "history", "exit"],
    ):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Calculation History")
    mock_print.assert_any_call("1. Add: 10, 5 = 15")


def test_unknown_command():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["banana", "exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call(
        "Unknown command. Type 'help' for available commands."
    )


def test_remove():
    app = CalculatorApp()

    with patch(
        "builtins.input",
        side_effect=["add", "10", "5", "remove", "1", "exit"],
    ):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("Calculation removed.")
    assert len(app.history) == 0


def test_remove_when_history_empty():
    app = CalculatorApp()

    with patch("builtins.input", side_effect=["remove", "exit"]):
        with patch("builtins.print") as mock_print:
            app.run()

    mock_print.assert_any_call("No calculations to remove.")