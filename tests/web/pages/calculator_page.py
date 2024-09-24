from assignment_1_calculator_2024.tests.web.pages.page_base import PageBase
from assignment_1_calculator_2024.tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)
        
        page_elements = {
            'username': Element('//input[@id="username"]',self),
            'screen': Element('//*[@id="calculator-screen"]',self),
            'add': Element('//*[@id="key-add"]',self),
            'subtract': Element('//*[@id="key-subtract"]',self),
            'multiple': Element('//*[@id="key-multiply"]', self),
            'divison': Element('//*[@id="key-divide"]', self),
            'equal':   Element('//*[@id="key-equals"]', self),
            'show': Element('//*[@id="toggle-button"]',self),
            'result': Element('//*[@id="history"]', self),
           
            '0': Element('//*[@id="key-0"]', self),
            '1': Element('//*[@id="key-1"]', self),
            '2': Element('//*[@id="key-2"]', self),
            '3': Element('//*[@id="key-3"]', self),
            '4': Element('//*[@id="key-4"]', self),
            '5': Element('//*[@id="key-5"]', self),
            '6': Element('//*[@id="key-6"]', self),
            '7': Element('//*[@id="key-7"]', self),
            '8': Element('//*[@id="key-8"]', self),
            '9': Element('//*[@id="key-9"]', self)
        
       
            
        }
        
        self.elements = munchify(page_elements)
        
    # def login(self, username, password):
    #     self.elements.username.set(username)
    #     self.elements.password.set(password)
    #     self.elements.login.click()
    
    def number(self,number):
        for digit in str(number):
            self.elements[digit].find().click()
    
    def addition(self,value, value2):
        self.number(value)
        
        self.elements.add.click()
        
        self.number(value2)
        
        self.elements.equal.click()
    
    def subtract(self,value,value2):
        self.number(value)
        
        self.elements.subtract.click()
        
        self.number(value2)
        
        self.elements.equal.click()
    
    def multiple(self,value,value2):
        
        self.number(value)
        
        self.elements.multiple.click()
        
        self.number(value2)
        
        self.elements.equal.click()
    
    def divison(self,value,value2):
        
        self.number(value)
        
        self.elements.divison.click()
        
        self.number(value2)
        
        self.elements.equal.click()
          
    def history(self):
        self.elements.show.click()
    
        
        
    
        
       
        
     
    
    
  
         
