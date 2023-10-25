import pyfiglet
from pyfiglet import Figlet
from colorama import Fore

from colorama import init as colorama_init

# Initialize colorama
# autoreset=True -> Color settings will automatically reset after each print statement
colorama_init(autoreset=True)

FOLDER_PATH = 'source/lab3/Louvre/'

def settings(settings_obj):
    while True:
        print('Menu:')
        print('1. Change font')
        print('2. Change size')
        print('3. Change symbol')
        print('4. Change color')
        print('5. Reset settings')
        print('6. Back')
        
        user_input = input('Choose option: ')
        
        if user_input == '1':
            settings_obj.set_font(set_font())
        elif user_input == '2':
            settings_obj.set_size(set_size())
        elif user_input == '3':
            settings_obj.set_symbol(set_symbol())
        elif user_input == '4':
            settings_obj.set_color(set_color())
        elif user_input == '5':
            settings_obj.default_settings()
        elif user_input == '6':
            break

def create_ascii_art(settings_obj):
    user_input = input('Enter the phrase: ')   
    
    art = Figlet(font=settings_obj.font , width=settings_obj.size[0])
    art = art.renderText(user_input)
    
    if settings_obj.symbol:
        art = change_symbols(art, settings_obj.symbol)
        
    art = settings_obj.color + art
    
    preview_art(art)
    
def set_font():
    # Get list of font names
    fonts = pyfiglet.FigletFont.getFonts()
    
    # Enumerate and print fonts with numbering, starting from 1
    for index, font in enumerate(fonts, start=1):
        print(f"{index}. {font}")
        
    user_input = int(input('Enter the font number: '))
    font = fonts[user_input-1]
    
    return font

def set_size():
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    
    return width, height

def set_symbol():
    symbol = input('Enter symbol: ')
    
    # Get list of ASCII symbols
    ascii_dec_values = [i for i in range(0, 256)]
    ascii_symbols = [chr(i) for i in ascii_dec_values]
    
    # Check if symbol is in ASCII
    if symbol not in ascii_symbols:
        print('Symbol is not in ASCII.')
        return None
    else:
        print("Symbol changed!")
        return symbol

def change_symbols(art, symbol):
    for char in art:
        if char != '\n' and char != ' ':
            art = art.replace(char, symbol)
    
    return art
    
def set_color():
    # Get dictionary where key is color name and value is color code
    colors = dict(Fore.__dict__.items())

    # Enumerate and print colors with numbering, starting from 1
    for index, color in enumerate(colors.keys(), start=1):
        print(f"{index}. {colors[color]}{color}")
     
    user_input = int(input('Enter the color number: '))
     
    # Get user input
    try:
        color_code = colors[list(colors.keys())[user_input-1]]
        return color_code
    except IndexError:
        print(f'Color number is not in range. Available colors are in range from 1 to {len(colors)}.')
    

def preview_art(art):
    print(art)
    
    save_art_answ = input('Do you want to save your art? (y/n): ')
    
    if save_art_answ == 'y':
        save_art(art)
    else:
        pass

def save_art(art):    
    file_name = input('Give a file name: ')
    formated_file_name = FOLDER_PATH + file_name + '.txt'
    
    with open(formated_file_name, 'w') as file:
        file.write(art)

def show_art():
    try:
        file_name = input('Enter file name: ')
        formated_file_name = FOLDER_PATH + file_name + '.txt'
        with open(formated_file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found.')