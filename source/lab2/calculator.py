import sys 
from constants import home_path
sys.path.append(home_path + 'source/lab1')

#import functions from lab1 to handle user input and perform calculations
from settings_funcs import ask_if_repeat, call_menu, get_user_input
from calculator_funcs import *

class Calculator:
	def __init__(self):
		self.result = None
		self.history = []
		self.repeat = True
		self.rounding_value = 50
		self.operations = {'+':add, '-':sub, '*':mul, '/':div, '^':exp, '√':root, '%':mod}
		self.num1 = 0
		self.num2 = 0
		
  
	def calculate(self):
		while self.repeat:
			num1, num2, operator = get_user_input()
			result = round(self.operations[operator](float(num1), float(num2)), self.rounding_value)
			self.history.append((num1, num2, operator, result))
			self.repeat = ask_if_repeat(self.history)
		call_menu(self.history)
		