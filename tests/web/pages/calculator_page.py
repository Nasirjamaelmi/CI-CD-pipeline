from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)
        
        page_elements = {

            'username': Element('//label[@id="user-name"]', self).find(),
            'screen': Element('//*[@id="calculator-screen"]',self).find(),
            'add': Element('//*[@id="key-add"]',self).find(),
            'subtract': Element('//*[@id="key-subtract"]',self).find(),
            'multiple': Element('//*[@id="key-multiply"]', self).find(),
            'divison': Element('//*[@id="key-divide"]', self).find(),
            'equal':   Element('//*[@id="key-equals"]', self).find(),
            'show': Element('//*[@id="toggle-button"]',self).find(),
            'result': Element('//*[@id="history"]', self).find(),
            '0': Element('//*[@id="key-0"]', self).find(),
            '1': Element('//*[@id="key-1"]', self).find(),
            '2': Element('//*[@id="key-2"]', self).find(),
            '3': Element('//*[@id="key-3"]', self).find(),
            '4': Element('//*[@id="key-4"]', self).find(),
            '5': Element('//*[@id="key-5"]', self).find(),
            '6': Element('//*[@id="key-6"]', self).find(),
            '7': Element('//*[@id="key-7"]',self).find(),
            '8': Element('//*[@id="key-8"]', self).find(),
            '9': Element('//*[@id="key-9"]', self).find(),
            'logout_button' : Element('//button[@id="logout-button"]', self).find(),
       
               

        }
        
        self.elements = munchify(page_elements)
        
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
    
   
    
        
    
        
     
    
    
  
         
