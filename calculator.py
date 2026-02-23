# Simple Calculator App

class Calculator:
    
    def __init__(self):
        self.result = 0
    
    # addition
    def add(self, a, b):
        return a + b
    
    # subtraction
    def subtract(self, a, b):
        return a - b
    
    # multiplication
    def multiply(self, a, b):
      return a * b
    
    # division - handle division by zero
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def clear(self):
        self.result = 0
        return self.result
