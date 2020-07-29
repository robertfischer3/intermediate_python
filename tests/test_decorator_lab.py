from unittest import TestCase
from intermediate.excercises.decorator_lab import decorator_function


class Test(TestCase):
    def test_decorator_function(self):
        def display():
            print("display function ran")

        # Wrapping a function with a decorator function at the most basic level
        wrapped_function = decorator_function(display)
        wrapped_function()

    def test_decorator(self):
        self.assertTrue(False)
