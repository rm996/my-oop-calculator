from calculator.history import History
from calculator.operations import Add, Subtract


class CalculatorApp:
    def __init__(self):
        self.history = History()

    def run(self):
        while True:
            command = input("> ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                self.show_help()

            elif command == "history":
                self.show_history()

            elif command == "add":
                self.perform_calculation(Add)

            elif command == "subtract":
                self.perform_calculation(Subtract)

            elif command == "remove":
                self.remove_calculation()

            else:
                print("Unknown command. Type 'help' for available commands.")

    def perform_calculation(self, operation_class):
        first = float(input("First number: "))
        second = float(input("Second number: "))

        calculation = operation_class(first, second)
        result = calculation.calculate()

        self.history.add(calculation)

        print(f"Result: {result:g}")

    def show_history(self):
        print("Calculation History")

        calculations = self.history.get_all()

        if not calculations:
            print("No calculations yet.")
            return

        for index, calculation in enumerate(calculations, start=1):
            name = calculation.__class__.__name__
            result = calculation.calculate()

            print(
                f"{index}. {name}: "
                f"{calculation.a:g}, {calculation.b:g} = {result:g}"
            )

    def show_help(self):
        print("Available commands:")
        print("add - Add two numbers")
        print("subtract - Subtract two numbers")
        print("history - Show calculation history")
        print("remove - Remove a calculation")
        print("help - Show available commands")
        print("exit - Exit the calculator")

    def remove_calculation(self):
        if len(self.history) == 0:
            print("No calculations to remove.")
            return

        index = int(input("Calculation number to remove: ")) - 1
        self.history.remove(index)
        print("Calculation removed.")