import pytest
from app import CalculatorApp


class TestAppIntegration:
    
    def test_add_workflow(self):
        app = CalculatorApp()
        
        app.input_num(5)
        assert app.get_display() == "5"
        
        app.do_operation("+")
        
        app.input_num(3)
        assert app.get_display() == "3"
        
        result = app.calculate()
        assert result == "8.0"
    
    def test_clear_button(self):
        app = CalculatorApp()
        
        app.input_num(1)
        app.input_num(0)
        assert app.get_display() == "10"
        
        app.do_operation("-")
        app.input_num(4)
        assert app.get_display() == "4"
        
        result = app.calculate()
        assert app.get_display() == "6.0"
        
        app.clear()
        assert app.get_display() == "0"
    
    def test_multiply_workflow(self):
        app = CalculatorApp()
        
        app.input_num(6)
        assert app.get_display() == "6"
        
        app.do_operation("*")
        
        app.input_num(7)
        assert app.get_display() == "7"
        
        result = app.calculate()
        assert result == "42.0"
    
    def test_divide_zero(self):
        app = CalculatorApp()
        
        app.input_num(1)
        app.input_num(0)
        assert app.get_display() == "10"
        
        app.do_operation("/")
        
        app.input_num(0)
        assert app.get_display() == "0"
        
        result = app.calculate()
        assert app.get_display() == "Error"
    
    def test_decimal_numbers(self):
        app = CalculatorApp()
        
        app.input_num(5)
        app.input_num(".")
        app.input_num(5)
        assert app.get_display() == "5.5"
        
        app.do_operation("+")
        
        app.input_num(2)
        app.input_num(".")
        app.input_num(5)
        assert app.get_display() == "2.5"
        
        result = app.calculate()
        assert app.get_display() == "8.0"
    
    def test_chained_ops(self):
        app = CalculatorApp()
        
        app.input_num(5)
        assert app.get_display() == "5"
        
        app.do_operation("+")
        
        app.input_num(3)
        assert app.get_display() == "3"
        
        app.do_operation("*")
        assert app.get_display() == "8.0"
        
        app.input_num(2)
        assert app.get_display() == "2"
        
        result = app.calculate()
        assert app.get_display() == "16.0"
