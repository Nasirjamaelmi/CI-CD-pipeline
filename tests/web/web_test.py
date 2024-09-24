import time
import pytest
from assignment_1_calculator_2024.tests.web.test_base import WebBase
from assignment_1_calculator_2024.tests.web.pages.login_page import LoginPage
from assignment_1_calculator_2024.tests.web.pages.register_page import RegisterPage
from assignment_1_calculator_2024.tests.web.pages.calculator_page import CalculatorPage

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')
        assert CalculatorPage(self.driver).elements.username.text == 'admin'
        
        
    
    def test_register(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_Register()
        registerPage = RegisterPage(self.driver)
        registerPage.register('Yuji' , 'itadori' , 'itadori')
        assert RegisterPage(self.driver).elements.username.text == 'Yuji'
    
    def test_calc(self): 
        calculator = CalculatorPage(self.driver)
        calculator.addition('5','5')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 10
        calculator.subtract('9','4')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 5
        calculator.multiple('5','5')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 25
        calculator.divison('100','2')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 50
        

    def test_verify(self):
        loginPage = LoginPage(self.driver)
        loginPage.login('admin', 'test1234')
        calculator = CalculatorPage(self.driver)
        calculator.addition('5','5')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 10
        calculator.subtract('9','4')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 5
        calculator.multiple('5','5')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 25
        calculator.divison('100','2')
        time.sleep(2) 
        assert int(calculator.elements.screen.value) == 50
        calculator.history()
        time.sleep(10)
 
    
     
        
        
   