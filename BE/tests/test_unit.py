import pytest
from BE.calculator_helper import CalculatorHelper

class TestCalculator():



   #fråga om parametrize and enviroment python path i github
    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2),
        (2, 3, 5),
        (10, 5, 15),
        (0, 0, 0),
        (-1, -1, -2)
    ])
    
    def test_add(a, b, expected):
        calc = CalculatorHelper()
        result = calc.add(a, b)
        assert result == expected
            
    def test_add(self):
        #ARRANGE
        calculator = CalculatorHelper()
        #Action
        value = calculator.add(1,1)

        assert value == 2, "Expected result to be 2"
        my_name = 'Nasir jama elmi'
       

    def test_sub(self):
        #ARRANGE
        calculator = CalculatorHelper()
        #Action
        value = calculator.subtract(1,1)

        assert value == 0, "Expected result to be 0"
       
    
    def test_multiply(self):
        #ARRANGE 
        calculator = CalculatorHelper()
        #Action
        value = calculator.multiply(2,10)
        assert value == 20, "Expected result to be 20"
    
    
    def test_divide(self):
        #ARRANGE 
        calculator = CalculatorHelper()
        #Action
        value = calculator.divide(8,2)
        assert value == 4, "Expected result to be 2"
        