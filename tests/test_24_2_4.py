import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 20, 5) == 25

    def test_subtraction(self):
        assert self.calc.subtraction(self, 20, 5) == 15

    def test_multiply(self):
        assert self.calc.multiply(self, 20, 5) == 100

    def test_division(self):
        assert self.calc.division(self, 20, 5) == 40

    def teardown(self):
        print('Выполнение метода Teardown')