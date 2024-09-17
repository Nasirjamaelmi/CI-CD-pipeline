import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse


class TestCalculatorAPI():
   
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"
        payload = {
            "operation":"add",
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(url, json=payload) 

    def test_calculate_sub(self):

        payload = {
            "operation":"sub",
            "operand1": 10,
            "operand2": 5
        } 
        respone = requests.post(self.url, json=payload)

    def test_calculate_multiply(self):

        payload = {
            "operation":"multiply",
            "operand1": 2,
            "operand2": 3
        } 
        respone = requests.post(self.url, json=payload)
    
    def test_calculate_divide(self):

        payload = {
            "operation":"multiply",
            "operand1": 2,
            "operand2": 2
        }
        respone = requests.post(self.url, json=payload)

    def test_generated_code_test1(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client= client, body= Calculation(Opertions.ADD, operand1=1, operand2=1))
        assert isinstance(response,ResultResponse)
        assert response.result == 2

    def test_generated_code_test2(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client= client, body= Calculation(Opertions.DIVIDE, operand1=2, operand2=2))
        assert isinstance(response,ResultResponse)
        assert response.result == 1
    
    def test_generated_code_test3(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client= client, body= Calculation(Opertions.MULTIPLY, operand1=2, operand2=2))
        assert isinstance(response,ResultResponse)
        assert response.result == 4
        
    
    def test_generated_code_test4(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client= client, body= Calculation(Opertions.SUBTRACT, operand1=9, operand2=2))
        assert isinstance(response,ResultResponse)
        assert response.result == 7
    
   
        
        
        
        

