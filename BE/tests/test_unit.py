from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that


class TestCalculator():
    def test_add(self):
        #ARRANGE
        calculator = CalculatorHelper()
        #Action
        value = calculator.add(1,1)

        assert value == 2, "Expected result to be 2"
        my_name = 'Nasir jama elmi'
        assert_that(value).is_equal_to(2)
        assert_that(my_name).is_length(15).starts_with('N').ends_with('elmi')

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
        