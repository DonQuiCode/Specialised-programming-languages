# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Imports
from lab3.ascii_art_generator import get_phrase
from lab3.ascii_art_generator import set_size, set_symbols, set_color, set_alignment, set_3d_option
from lab3.ascii_art_generator import check_size, preview_art
from lab4.font8x8 import font8x8

# Constants
SPACE = 0
SYMBOL = 1
SHADOW = 2

def settings(settings_obj):
    while True:
        print('Options:')
        print('0. Show current settings')
        print('1. Change size')
        print('2. Change symbol')
        print('3. Change color')
        print('4. Change alignment')
        print('5. Change 3D option')
        print('6. Reset settings')
        print('7. Back')
        
        user_input = input('Enter option number: ')
        if user_input == '0':
            settings_obj.show_settings()
        elif user_input == '1':
            settings_obj.set_size(*set_size())
        elif user_input == '2':
            settings_obj.set_symbols(*set_symbols())
        elif user_input == '3':
            settings_obj.set_color(set_color())
        elif user_input == '4':
            settings_obj.set_alignment(set_alignment())
        elif user_input == '5':
            settings_obj.set_3d_option(set_3d_option())
        elif user_input == '6':
            settings_obj.default_settings()
        elif user_input == '7':
            break
        
def str_to_ascii_list(char_str):
    """Convert string to list of ASCII codes."""
    char_list = []
    for char in char_str:
        char_list.append(ord(char))
    return char_list

def row_to_string(row, regular_symbol, shadow_symbol):
    """Convert row items (SPACE, SYMBOL, SHADOW) to requested symbols."""
    row_string = ""
    for item in row:
        if item == SPACE:
            row_string += " "
        elif item == SYMBOL:
            row_string += regular_symbol
        elif item == SHADOW:
            row_string += shadow_symbol
    return row_string
    
def add_shadow(set_bit_list):
    """Add shadow to ASCII-art. 
    Check if there is a SYMBOL and SPACE next to each other. 
    If so, replace SPACE with SHADOW.
    """
    for i in range(len(set_bit_list)):
        if set_bit_list[i] == SYMBOL and set_bit_list[i + 1] == SPACE:
            set_bit_list[i] = SHADOW
    
    return set_bit_list

def twod_to_threed(set_bit_list, column_item, char_item):
    """Add 3D effect to ASCII-art.
    For the first character in the row, add SPACE to the beginning of the row.
    In ascending order, add SPACE to the beginning of the rows that represent a character.
    """
    if char_item == 0:
        for _ in range(column_item, 8):
            set_bit_list.insert(0, SPACE)
    return set_bit_list

def set_lines(char_list, width):
    """Get number of lines for ASCII-art.
    If string is longer than width, split string into multiple lines.
    """
    char_width = 8
    if len(char_list) * char_width > width:
        lines_list = []
        chars_in_line = width // 8 
        for i in range(len(char_list) // chars_in_line + 1):
            lines_list.append(char_list[i * chars_in_line: (i + 1) * chars_in_line])
    else:
        lines_list = [char_list]
    return lines_list

def align(alignment, width, row_string):
    if alignment == 'left':
        left_padding = 0
    elif alignment == 'center':
        left_padding = (width - len(row_string)) // 2
    elif alignment == 'right':
        left_padding = (width - len(row_string))
        
    return left_padding  

def render(char_str, color, regular_symbol, shadow_symbol, width, height, alignment, threed):
    """Render ASCII-art."""
    char_width = 8
    char_height = 8
    art = ""
    
    ascii_list = str_to_ascii_list(char_str)
    lines = set_lines(ascii_list, width)
      
    for line in lines:
        for column_item in range(char_height):
            row = ""
            for char_item in range(len(line)):
                set_bit_list = []                
                for row_item in range(char_width):
                    bitmap = font8x8[line[char_item]]
                    set_bit = (1 << row_item) & bitmap[column_item]
                    if set_bit:
                        set_bit_list.append(SYMBOL)
                    else:
                        set_bit_list.append(SPACE)
                
                if shadow_symbol:
                    set_bit_list = add_shadow(set_bit_list)
                    
                if threed:
                    set_bit_list = twod_to_threed(set_bit_list, column_item, char_item)

                row_string = row_to_string(set_bit_list, regular_symbol, shadow_symbol)
                row += row_string
            left_padding = align(alignment, width, row_string)   
            art += " " * left_padding + row + "\n"
            art = color + art
    return art

def create_ascii_art(FOLDER_PATH, settings_obj):
    """Ask user for phrase and show ASCII-art.
    
    Args:
        FOLDER_PATH (str): Path to folder with ASCII-arts.
        settings_obj (AsciiArtSettings): Object with settings.
    """
    char_str = get_phrase()
    width, height = settings_obj.size
    
    try:
        check_size(char_str, width, height)
    except ValueError as e:
        print(f"An error occurred: {e}")
        return None
    
    while True:
        art = render(char_str, 
                    settings_obj.color,
                    settings_obj.symbols[0], 
                    settings_obj.symbols[1], 
                    settings_obj.size[0], 
                    settings_obj.size[1], 
                    settings_obj.alignment,
                    settings_obj.is_3d)
        
        try:
            preview_art(FOLDER_PATH, art)
        except Exception as e:
            print(f"An error occurred while previewing the ASCII art: {str(e)}")
            
        change_settings = input('Do you want to change settings? (y/n): ')
         
        if change_settings == 'y':
            settings(settings_obj)
        else:
            break