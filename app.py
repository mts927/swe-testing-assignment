"""
Quick-Calc Application: Main Interface
Provides a command-line interface for the calculator application.
"""

from calculator import Calculator


class CalculatorApp:
    """A command-line interface for the Quick-Calc calculator."""

    def __init__(self):
        """Initialize the calculator app."""
        self.calc = Calculator()
        self.display = "0"
        self.first_operand = None
        self.operation = None
        self.should_reset_display = False

    def input_number(self, digit):
        """
        Input a digit to the display.
        
        Args:
            digit: A digit (0-9) or decimal point to add to the display
        """
        if self.should_reset_display:
            self.display = str(digit)
            self.should_reset_display = False
        else:
            if self.display == "0" and digit != ".":
                self.display = str(digit)
            elif digit == "." and "." in self.display:
                return  # Prevent multiple decimal points
            else:
                self.display += str(digit)

    def perform_operation(self, op):
        """
        Perform a calculation operation.
        
        Args:
            op: The operation to perform ('+', '-', '*', '/')
        """
        current = float(self.display)
        
        if self.first_operand is not None and self.operation is not None:
            # Calculate the result of the previous operation
            try:
                if self.operation == "+":
                    result = self.calc.add(self.first_operand, current)
                elif self.operation == "-":
                    result = self.calc.subtract(self.first_operand, current)
                elif self.operation == "*":
                    result = self.calc.multiply(self.first_operand, current)
                elif self.operation == "/":
                    result = self.calc.divide(self.first_operand, current)
                
                self.display = str(result)
            except ValueError:
                self.display = "Error"
        
        self.first_operand = float(self.display) if self.display != "Error" else None
        self.operation = op
        self.should_reset_display = True

    def calculate(self):
        """
        Calculate the final result when equals is pressed.
        
        Returns:
            The result of the calculation
        """
        if self.first_operand is None or self.operation is None:
            return self.display
        
        current = float(self.display) if self.display != "Error" else None
        
        if current is None:
            return self.display
        
        try:
            if self.operation == "+":
                result = self.calc.add(self.first_operand, current)
            elif self.operation == "-":
                result = self.calc.subtract(self.first_operand, current)
            elif self.operation == "*":
                result = self.calc.multiply(self.first_operand, current)
            elif self.operation == "/":
                result = self.calc.divide(self.first_operand, current)
            
            self.display = str(result)
        except ValueError:
            self.display = "Error"
        
        self.first_operand = None
        self.operation = None
        self.should_reset_display = True
        
        return self.display

    def clear(self):
        """Clear the calculator display and internal state."""
        self.display = "0"
        self.first_operand = None
        self.operation = None
        self.should_reset_display = False

    def get_display(self):
        """
        Get the current display value.
        
        Returns:
            The current display string
        """
        return self.display


if __name__ == "__main__":
    # Example usage
    app = CalculatorApp()
    print(f"Display: {app.get_display()}")
    
    # Example calculation: 5 + 3 = 8
    app.input_number(5)
    print(f"After inputting 5: {app.get_display()}")
    
    app.perform_operation("+")
    app.input_number(3)
    print(f"After inputting 3: {app.get_display()}")
    
    result = app.calculate()
    print(f"Result of 5 + 3: {result}")
