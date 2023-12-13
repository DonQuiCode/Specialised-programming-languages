class AsciiArtSettings:
    def __init__(self):
        self.font = "doh"
        self.size = [100, 100]
        self.color = "red"
        self.symbol = None
    
    def set_font(self, font):
        self.font = font
    
    def set_size(self, size):
        self.size = size
        
    def set_color(self, color):
        self.color = color
        
    def set_symbol(self, symbol):
        self.symbol = symbol
        
    def default_settings(self):
        self.font = "doh"
        self.size = [100, 100]
        self.color = "red"
        self.symbol = None