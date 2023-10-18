#Get user input
def get_user_input():
    num1 = input("Введіть перше число: ")
    num2 = input("Введіть друге число: ")
    operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
    operators = ['+', '-', '*', '/', '^', '√', '%']
    
    #Check if operator is valid
    while operator not in operators:
        print("Помилка: невідомий оператор")
        operator = input("Введіть один з наступних операторів: +, -, *, /, ^, √, %")
    return num1, num2, operator

#Display history in the terminal
def display_history(history):
    if history:
        print("\nІсторія обчислень за сесію:")
        for i, expression in enumerate(history, start=1):
            num1, num2, operator, result = expression
            print(f"{i}) {num1} {operator} {num2} = {result}")
    else:
        print("\nІсторія обчислень пуста")
    
#Save history to file
HISTORY_FILE = 'source/lab1/history.txt'
def save_history(history):
    with open(HISTORY_FILE, 'a') as file:
        for i, expression in enumerate(history, start=1):
            num1, num2, operator, result = expression
            file.write(f"{i}) {num1} {operator} {num2} = {result}\n")
        file.write("\n")

#Ask if user wants to repeat
def ask_if_repeat(history):
    global repeat
    querry = input("Повторити? (yes/no/menu): ")
    
    if querry.lower() == 'menu':
        call_menu(history)
    elif querry.lower() == 'yes':
        return
    else:
        repeat = False
        save_history(history)  #Save history to file 
        display_history(history)
        return repeat

#Show menu options
def show_options():
    print("[0] --- Продовжити обчислення")
    print("[1] --- Налаштувати кількість знаків після коми")
    print("[2] --- Показати історію обчислень за дану сесію")
    print("[3] --- Очистити пам'ять за дану сесію")
    print("[4] --- Показати історію обчислень за всі сесії")
    print("[5] --- Вихід")

#Menu
def call_menu(history):
    #global history
    show_options()
    choice = input("Виберіть операцію: ")
    if choice == '0':
        return
    elif choice == '1':
        global rounding_value
        rounding_value = int(input("Введіть кількість знаків після коми: "))
        print(f"Кількість знаків після коми: {rounding_value}")
        call_menu(history)
    elif choice == '2':
        display_history(history)
        call_menu(history)
    elif choice == '3':
        history = []
        print("Історія обчислень очищена")
        call_menu(history)
    elif choice == '4':
        print("Історія обчислень за всі сесії:")
        with open('history.txt', 'r') as file:
            print(file.read())
        display_history(history)
        call_menu(history)
    elif choice == '5':
        save_history(history)
        global repeat
        repeat = False
        display_history(history)
    else:
        print("Помилка: невідома операція")
        call_menu()
