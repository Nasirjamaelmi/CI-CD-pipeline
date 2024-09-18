from calculator_client.client import Client

class CalculatorUnitTestBase():
    @classmethod
    def setup_class(cls):
        cls.client =  Client(base_url="http://localhost:5001/calculate")

    def setup_class(cls):
        cls.client = None