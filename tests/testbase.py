from assignment_1_calculator_2024.BE.calculator_helper import CalculatorHelper

class CalculatorUnitTestBase():
    @classmethod
    def setup_class(cls):
        cls.calculator = CalculatorHelper()

    def teardown_class(cls):
        cls.calculator = None