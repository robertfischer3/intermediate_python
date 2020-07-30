from unittest import TestCase
from intermediate.excercises.decorator_lab import decorator_function


class Test(TestCase):
    def test_decorator_function_a(self):
        def display():
            print("display function ran")

        # Wrapping a function with a decorator function at the most basic level
        wrapped_function = decorator_function(display)
        wrapped_function()

    def test_decorator_function_b(self):
        # create a function in decorator_lab module that mimics decorator_function

        self.assertTrue(False)

    def test_decorator_class_a(self):
        # 1. Create and call a few functions by instantiating the decorator_class with those methods

        self.assertTrue(False)

    def test_decorator_class_a(self):
        # 2. Create a simple class with a method. Instantiate the decorator_class with
        #  the method of the simple class.

        self.assertTrue(False)