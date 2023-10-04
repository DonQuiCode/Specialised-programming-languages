import math

def add(a,b):
  return a+b
 
def sub(a,b):
  return a-b
 
def mul(a,b):
  return a*b
 
def div(a,b):
  return a/b
 
def exp(a,b):
  return a**b
  
def root(a,b):
  return pow(a,1./b)
 
def mod(a,b):
  return a%b

def display_history():
  if history:
    print("\nІсторія обчислень за сесію:")
    for i, expression in enumerate(history, start=1): # enumerate(history, start=1) - перелічування з індексом починаючи з 1
      num1, num2, operator, result = expression
      print(f"{i}) {num1} {operator} {num2} = {result}")
  else:
    print("\nІсторія обчислень пуста")
    
def save_history():
  with open('history.txt', 'a') as file:
    for i, expression in enumerate(history, start=1):
      num1, num2, operator, result = expression
      file.write(f"{i}) {num1} {operator} {num2} = {result}\n")
    file.write("\n")
  
def ask_if_repeat():
  global repeat
  querry = input("Повторити? (yes/no/menu): ")
  
  if querry.lower() == 'menu':
    call_menu()
  elif querry.lower() == 'yes':
    return
  else:
    repeat = False
    save_history()
    display_history()

def show_options():
  print("[0] --- Продовжити обчислення")
  print("[1] --- Налаштувати кількість знаків після коми")
  print("[2] --- Показати історію обчислень за дану сесію")
  print("[3] --- Очистити пам'ять за дану сесію")
  print("[4] --- Показати історію обчислень за всі сесії")
  print("[5] --- Вихід")

def call_menu():
  show_options()
  choice = input("Виберіть операцію: ")
  if choice == '0':
    return
  elif choice == '1':
    global rounding_value
    rounding_value = int(input("Введіть кількість знаків після коми: "))
    print(f"Кількість знаків після коми: {rounding_value}")
    call_menu()
  elif choice == '2':
    display_history()
    call_menu()
  elif choice == '3':
    global history
    history = []
    print("Історія обчислень очищена")
    call_menu()
  elif choice == '4':
    print("Історія обчислень за всі сесії:")
    with open('history.txt', 'r') as file:
      print(file.read())
    display_history()
    call_menu()
  elif choice == '5':
    save_history()
    global repeat
    repeat = False
    display_history()
  else:
    print("Помилка: невідома операція")
    call_menu()

operations = {'+':add, '-':sub, '*':mul, '/':div, '^':exp, '√':root, '%':mod}

operators = ['+', '-', '*', '/', '^', '√', '%']

history = []
rounding_value = 50

repeat = True

while repeat:
  try:
    num1 = input("Введіть перше число: ")
    num2 = input("Введіть друге число: ")
    operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

    while operator not in operators:
        print("Помилка: невідомий оператор")
        operator = input("Введіть один з наступних операторів: +, -, *, /, ^, √, %")
      
    result = round(operations[operator](float(num1), float(num2)), rounding_value)
    history.append((num1, num2, operator, result))

    print(f"Результат: {result}\n")
    ask_if_repeat()
    
  except ZeroDivisionError:
    print("Помилка: ділення на нуль")
    result = "undefined"
    history.append((num1, num2, operator, result))
    ask_if_repeat()
    
  except ValueError as e:
    print(f"Помилка: введено не число або його введено неправильно: {str(e)}")
    ask_if_repeat()
    
  except Exception as e:
    print(f"Помилка: {str(e)}")
  