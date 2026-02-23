"""
Integration tests for the Calculator application.
Tests the interaction between the UI layer (CalculatorApp) and the calculation logic (Calculator).
"""

import pytest
from app import CalculatorApp


class TestCalculatorAppIntegration:
    """Integration tests for the CalculatorApp."""

    def test_full_addition_workflow(self):
        """
        Integration test: Simulate user entering "5 + 3 =" and verify result is "8".
        This tests the complete workflow from input through calculation.
        """
        app = CalculatorApp()
        
        # User enters: 5
        app.input_number(5)
        assert app.get_display() == "5"
        
        # User presses: +
        app.perform_operation("+")
        
        # User enters: 3
        app.input_number(3)
        assert app.get_display() == "3"
        
        # User presses: =
        result = app.calculate()
        assert result == "8.0"
        assert app.get_display() == "8.0"

    def test_clear_after_calculation(self):
        """
        Integration test: Verify that pressing Clear after a calculation resets display to "0".
        """
        app = CalculatorApp()
        
        # Perform a calculation: 10 - 4 = 6
        app.input_number(1)
        app.input_number(0)
        assert app.get_display() == "10"
        
        app.perform_operation("-")
        app.input_number(4)
        assert app.get_display() == "4"
        
        result = app.calculate()
        assert app.get_display() == "6.0"
        
        # Press clear
        app.clear()
        assert app.get_display() == "0"

    def test_full_multiplication_workflow(self):
        """
        Integration test: Simulate user entering "6 * 7 =" and verify result is "42".
        """
        app = CalculatorApp()
        
        # User enters: 6
        app.input_number(6)
        assert app.get_display() == "6"
        
        # User presses: *
        app.perform_operation("*")
        
        # User enters: 7
        app.input_number(7)
        assert app.get_display() == "7"
        
        # User presses: =
        result = app.calculate()
        assert result == "42.0"
        assert app.get_display() == "42.0"

    def test_division_by_zero_handling(self):
        """
        Integration test: Verify that attempting to divide by zero shows an error.
        User enters "10 / 0 =" and should see "Error".
        """
        app = CalculatorApp()
        
        # User enters: 10
        app.input_number(1)
        app.input_number(0)
        assert app.get_display() == "10"
        
        # User presses: /
        app.perform_operation("/")
        
        # User enters: 0
        app.input_number(0)
        assert app.get_display() == "0"
        
        # User presses: =
        result = app.calculate()
        assert app.get_display() == "Error"

    def test_decimal_input_handling(self):
        """
        Integration test: Verify that decimal numbers are properly handled.
        User enters "5.5 + 2.5 =" and should get "8.0".
        """
        app = CalculatorApp()
        
        # User enters: 5.5
        app.input_number(5)
        app.input_number(".")
        app.input_number(5)
        assert app.get_display() == "5.5"
        
        # User presses: +
        app.perform_operation("+")
        
        # User enters: 2.5
        app.input_number(2)
        app.input_number(".")
        app.input_number(5)
        assert app.get_display() == "2.5"
        
        # User presses: =
        result = app.calculate()
        assert app.get_display() == "8.0"

    def test_chained_operations(self):
        """
        Integration test: Verify that chaining operations works correctly.
        User enters "5 + 3 * 2 =" - should calculate 5 + 3 = 8, then 8 * 2 = 16.
        """
        app = CalculatorApp()
        
        # User enters: 5
        app.input_number(5)
        assert app.get_display() == "5"
        
        # User presses: +
        app.perform_operation("+")
        
        # User enters: 3
        app.input_number(3)
        assert app.get_display() == "3"
        
        # User presses: * (which should calculate 5 + 3 first)
        app.perform_operation("*")
        assert app.get_display() == "8.0"
        
        # User enters: 2
        app.input_number(2)
        assert app.get_display() == "2"
        
        # User presses: =
        result = app.calculate()
        assert app.get_display() == "16.0"
