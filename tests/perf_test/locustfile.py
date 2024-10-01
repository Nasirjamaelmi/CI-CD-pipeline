from locust import HttpUser, between, task
import json
import random


class CalculatorUser(HttpUser):

    def on_start(self):
        pass

    wait_time = between(2, 4)

    equations = {
        "add": [(1, 1, 2), (-5, 3, -2), (10, -10, 0), (100, 200, 300), (-50, -50, -100)],
        "subtract": [(10, 5, 5), (100, 25, 75), (-20, 10, -30), (200, 100, 100)],
        "multiply": [(2, 5, 10), (-3, 3, -9), (10, 10, 100), (7, 0, 0)],
        "divide": [(10, 2, 5), (100, 25, 4), (-20, 5, -4), (200, 100, 2)]
    }

 
    

    @task(2)
    def add(self):
        operand1, operand2, expected_result = random.choice(self.equations["add"])
        add = {
            "operation": "add",
            "operand1": operand1,
            "operand2": operand2
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == expected_result:
                response.failure(f"Expected result to be {expected_result} but was {response_data['result']}")
                
    @task()
    def subtract(self):
        operand1, operand2, expected_result = random.choice(self.equations["subtract"])
        add = {
            "operation": "subtract",
            "operand1": operand1,
            "operand2": operand2
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == expected_result:
                response.failure(f"Expected result to be {expected_result} but was {response_data['result']}")
    
    @task()
    def multiply(self):
        operand1, operand2, expected_result = random.choice(self.equations["multiply"])
        add = {
            "operation": "multiply",
            "operand1": operand1,
            "operand2": operand2
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == expected_result:
                response.failure(f"Expected result to be {expected_result} but was {response_data['result']}")
    
    @task()
    def divide(self):
        operand1, operand2, expected_result = random.choice(self.equations["divide"])
        add = {
            "operation": "divide",
            "operand1": operand1,
            "operand2": operand2
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == expected_result:
                response.failure(f"Expected result to be {expected_result} but was {response_data['result']}")
                
                
                
                
if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
