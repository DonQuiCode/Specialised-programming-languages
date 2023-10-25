from art_settings import *
from art_generation import *

def main():
    settings_obj = AsciiArtSettings()
    
    while True:
        print('Menu:')
        print('1. Create art')
        print('2. Settings')
        print('3. Show art')
        print('4. Exit')
        
        user_input = input('Choose option: ')
        
        if user_input == '1':
            create_ascii_art(settings_obj)
        elif user_input == '2':
            settings(settings_obj)
        elif user_input == '3':
            show_art()
        elif user_input == '4':
            break
        
    print('Bye!')
    
if __name__ == "__main__":
    main()
