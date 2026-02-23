from calculator import Calculator

class CalculatorApp:
    
    def __init__(self):
        self.calc = Calculator()
        self.display = "0"
        self.first_num = None
        self.op = None
        self.reset = False
    
    def input_num(self, digit):
        if self.reset:
            self.display = str(digit)
            self.reset = False
        else:
            if self.display == "0" and digit != ".":
                self.display = str(digit)
            elif digit == "." and "." in self.display:
              return
            else:
                self.display += str(digit)
    
    def do_operation(self, operation):
        current = float(self.display)
        
        if self.first_num is not None and self.op is not None:
            try:
                if self.op == "+":
                    result = self.calc.add(self.first_num, current)
                elif self.op == "-":
                    result = self.calc.subtract(self.first_num, current)
                elif self.op == "*":
                    result = self.calc.multiply(self.first_num, current)
                elif self.op == "/":
                    result = self.calc.divide(self.first_num, current)
                
                self.display = str(result)
            except ValueError:
                self.display = "Error"
        
        self.first_num = float(self.display) if self.display != "Error" else None
        self.op = operation
        self.reset = True
    
    def calculate(self):
        if self.first_num is None or self.op is None:
            return self.display
        
        current = float(self.display) if self.display != "Error" else None
        
        if current is None:
          return self.display
        
        try:
            if self.op == "+":
                result = self.calc.add(self.first_num, current)
            elif self.op == "-":
                result = self.calc.subtract(self.first_num, current)
            elif self.op == "*":
                result = self.calc.multiply(self.first_num, current)
            elif self.op == "/":
                result = self.calc.divide(self.first_num, current)
            
            self.display = str(result)
        except ValueError:
            self.display = "Error"
        
        self.first_num = None
        self.op = None
        self.reset = True
        
        return self.display
    
    def clear(self):
        self.display = "0"
        self.first_num = None
        self.op = None
        self.reset = False
    
    def get_display(self):
        return self.display


if __name__ == "__main__":
    app = CalculatorApp()
    print("Display: " + app.get_display())
    
    app.input_num(5)
    print("Input 5: " + app.get_display())
    
    app.do_operation("+")
    app.input_num(3)
    print("Input 3: " + app.get_display())
    
    result = app.calculate()
    print("Result: " + result)
