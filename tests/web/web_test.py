import time
import string
import random
from assertpy import assert_that

from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.register_page import RegisterPage
from tests.web.pages.calculator_page import CalculatorPage

class TestWeb(WebBase):
    def generate_random_username(self, length=8):
        """Generate a random username to avoid conflicts."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))


    def generateUser():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters))

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')
       
        assert CalculatorPage(self.driver).elements.username.text == 'admin'
        

        
    

    def test_register(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_Register()
        registerPage = RegisterPage(self.driver)
        unique_username = self.generate_random_username()
        registerPage.register(unique_username, 'itadori' , 'itadori')
        #time.sleep(4)
        assert_that(CalculatorPage(self.driver).elements.username.text).is_equal_to(unique_username) 
    
    def test_calc(self): 
        loginPage = LoginPage(self.driver)
        loginPage.login('admin', 'test1234')
        assert_that(CalculatorPage(self.driver).elements.username.text).is_equal_to('admin')
        calculator = CalculatorPage(self.driver)
        calculator.addition('5','5')
        assert_that(int(calculator.elements.screen.value)).is_equal_to(10) 
        calculator.subtract('9','4')
        assert_that(int(calculator.elements.screen.value)).is_equal_to(5)
        calculator.multiple('5','5')
        assert_that(int(calculator.elements.screen.value)).is_equal_to(25)
        calculator.divison('100','2')
        assert_that(int(calculator.elements.screen.value)).is_equal_to(50)

        

    def test_verify(self):
        loginPage = LoginPage(self.driver)
        loginPage.login('admin', 'test1234')
        calculator = CalculatorPage(self.driver)
        calculator.addition('5','5')

        assert int(calculator.elements.screen.value) == 10
        calculator.subtract('9','4')
      
        assert int(calculator.elements.screen.value) == 5
        calculator.multiple('5','5')
       
        assert int(calculator.elements.screen.value) == 25
        calculator.divison('100','2')
       
        assert int(calculator.elements.screen.value) == 50
        calculator.history()
        

 
    
     
        
        
   