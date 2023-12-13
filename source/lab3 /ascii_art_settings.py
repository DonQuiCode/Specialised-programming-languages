"""Module for storing settings for ASCII-art."""
import json

class AsciiArtSettings:
    """Class for storing settings for ASCII-art.
    
    Attributes:
        font (str): Font name.
        size (tuple): Size of ASCII-art.
        symbols (str): Symbols to replace.
        color (str): Color of ASCII-art.
    """
    def __init__(self):
        self.settings_file_path = None
        self.font = None
        self.size = None
        self.symbols = None
        self.color = None
        self.alignment = None
        self.is_3d = None
        
    def set_settings_file_path(self, settings_file_path):
        self.settings_file_path = settings_file_path
        
    def show_settings(self):
        print('Current settings:')
        print('Font:', self.font)
        print('Size:', self.size)
        print('Symbols:', self.symbols)
        print('Alignment:', self.alignment)
        print('Color:', self.color.replace('\x1b', '\\x1b'))
        print('3D:', self.is_3d)
        
    def set_font(self, font):
        self.font = font
        self.save_settings()

    def set_size(self, width, height):
        self.size = (width, height)
        self.save_settings()

    def set_symbols(self, regular_symbol, shadow_symbol):
        self.symbols = (regular_symbol, shadow_symbol)
        self.save_settings()

    def set_color(self, color):
        self.color = color
        self.save_settings()
        
    def set_alignment(self, alignment):
        self.alignment = alignment
        self.save_settings()
        
    def set_3d_option(self, is_3d):
        self.is_3d = is_3d
        self.save_settings()

    def default_settings(self):
        self.font = 'clb6x10'
        self.size = (80, 25)
        self.symbols = ("#", "*")
        self.color = '\x1b[39m'
        self.alignment = 'left'
        self.is_3d = False
        self.save_settings()
        
    def save_settings(self):
        settings_data = {
            'font': self.font,
            'size': self.size,
            'symbols': self.symbols,
            'color': self.color,
            'alignment': self.alignment,
            'is_3d': self.is_3d
        }
        with open(self.settings_file_path, 'w') as file:
            json.dump(settings_data, file)

    def load_settings(self):
        try:
            with open(self.settings_file_path, 'r') as file:
                settings_data = json.load(file)
                self.font = settings_data['font']
                self.size = settings_data['size']
                self.symbols = settings_data['symbols']
                self.color = settings_data['color']
                self.alignment = settings_data['alignment']
                self.is_3d = settings_data['is_3d']
        except FileNotFoundError:
            # If file does not exist use default settings
            self.default_settings()