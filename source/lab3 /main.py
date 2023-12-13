""" Main module for the ASCII-art program."""

# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from lab3.ascii_art_settings import AsciiArtSettings
from lab3.ascii_art_generator import create_ascii_art, show_art, settings

FOLDER_PATH = 'source/lab3/ASCII-arts/'
SETTINGS_FILE_PATH = 'source/lab3/settings.json'

def main():    
    settings_obj = AsciiArtSettings()
    settings_obj.set_settings_file_path(SETTINGS_FILE_PATH)
    settings_obj.load_settings()
    
    while True:
        print('Options (1/2/3):')
        print('1. Create ASCII-art')
        print('2. Show ASCII-art')
        print('3. Settings')
        print('4. Exit')
        
        user_input = input('Enter option number: ')
        
        if user_input == '1':
            create_ascii_art(FOLDER_PATH, settings_obj)
        elif user_input == '2':
            show_art(FOLDER_PATH)
        elif user_input == '3':
            settings(settings_obj, SETTINGS_FILE_PATH)
        elif user_input == '4':
            break
    
if __name__ == "__main__":
    main()