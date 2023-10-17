class Calculator:
    def __init__(self):
        self.result = None

    def get_user_input(self):
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                raise ValueError("Недійсний оператор")
            num2 = float(input("Введіть друге число: "))
            return num1, operator, num2
        except ValueError as e:
            print(f"Помилка: {e}")
            return None, None, None

    def calculate(self, num1, operator, num2):
        try:
            if operator == '+':
                self.result = num1 + num2
            elif operator == '-':
                self.result = num1 - num2
            elif operator == '*':
                self.result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе")
                self.result = num1 / num2
            elif operator == '^':
                self.result = num1 ** num2
            elif operator == '√':
                self.result = num1 ** (1 / num2)
            elif operator == '%':
                self.result = num1 % num2
            else:
                raise ValueError("Недійсний оператор")
        except Exception as e:
            print(f"Помилка: {e}")

    def run(self):
        while True:
            num1, operator, num2 = self.get_user_input()
            if num1 is None:
                continue
            self.calculate(num1, operator, num2)
            print(f"Результат: {self.result}")
            repeat = input("Бажаєте продовжити обчислення? (Так/Ні): ").lower()
            if repeat != 'так':
                break

# Створюємо об'єкт калькулятора і запускаємо програму
calc = Calculator()
calc.run()
