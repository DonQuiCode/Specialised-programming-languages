import math
from settings_funcs import get_user_input, display_history, save_history, ask_if_repeat, call_menu
from calculator_funcs import add, sub, mul, div, exp, root, mod

operations = {'+':add, '-':sub, '*':mul, '/':div, '^':exp, '√':root, '%':mod}
history = []

#Default rounding value
rounding_value = 50

repeat = True

while repeat:
    try:
        num1, num2, operator = get_user_input()
    
        result = round(operations[operator](float(num1), float(num2)), rounding_value)
        
        #Add to history of the session
        history.append((num1, num2, operator, result))

        print(f"Результат: {result}\n")
        repeat = ask_if_repeat(history)
        
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        result = "undefined"
        history.append((num1, num2, operator, result))
        repeat = ask_if_repeat(history)
        
    except ValueError as e:
        print(f"Помилка: введено не число або його введено неправильно: {str(e)}")
        repeat = ask_if_repeat(history)
        
    except Exception as e:
        print(f"Помилка: {str(e)}")
    