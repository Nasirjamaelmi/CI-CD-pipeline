import requests


class TestCalculatorAPI():
    url="http://localhost:5000/calculate"
    def test_calculate_add(self):

        payload = {
            "operation":"add",
            "operand1": 1,
            "operand2": 1
        }
        response = requests.post(self.url,json=payload)

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



        

