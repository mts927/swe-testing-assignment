"""
Quick-Calc: A Simple Calculator Application
A command-line calculator that performs basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result of 0."""
        self.result = 0

    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        return a * b

    def divide(self, a, b):
        """
        Divide two numbers.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The quotient of a and b
            
        Raises:
            ValueError: If division by zero is attempted
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def clear(self):
        """Reset the calculator result to zero."""
        self.result = 0
        return self.result
