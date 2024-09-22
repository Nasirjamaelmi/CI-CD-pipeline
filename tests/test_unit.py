import pytest
from tests.testbase import CalculatorUnitTestBase
class TestCalculator(CalculatorUnitTestBase):

   #fråga om parametrize and enviroment python path i github
    @pytest.mark.parametrize("a, b, result", [
        (1, 1, 2),
        (2, 3, 5),
        (10, 5, 15),
        (0, 0, 0),
        (-1, -1, -2)
    ])
    
    def test_add(self,a, b, result):
        value = self.calculator.add(a,b)
        assert value == result
            
    def test_add(self):
        #ARRANGE
      
        #Action
        value = self.calculator.add(1,1)

        assert value == 2, "Expected result to be 2"
        my_name = 'Nasir jama elmi'
       

    def test_sub(self):
        #ARRANGE
       
        #Action
        value = self.calculator.subtract(1,1)

        assert value == 0, "Expected result to be 0"
       
    
    def test_multiply(self):
        #ARRANGE 
        
        #Action
        value = self.calculator.multiply(2,10)
        assert value == 20, "Expected result to be 20"
    
    
    def test_divide(self):
        #ARRANGE 
      
        #Action
        value = self.calculator.divide(8,2)
        assert value == 4, "Expected result to be 2"
        