from calculator_client.client import Client

class CalculatorUnitTestBaseAPI():
    @classmethod
    def setup_class(cls):
        cls.client =  Client(base_url="http://localhost:5001")

    def teardown_class(cls):
        cls.client = None