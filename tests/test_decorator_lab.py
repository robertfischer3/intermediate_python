from unittest import TestCase
from intermediate.excercises.args_lab import displaystr

class TestArgsLab(TestCase):

    def test_named_parmeters_single_argument_default(self):
        self.assertTrue("Bob was here" in displaystr())

    def test_create_method_using_args(self):
        # Create a method that uses a variable argument length
        # iterate through the argument list and test the values
        self.assertTrue(False)

    def test_create_method_with_variable_and_keyword(self):
        # Create a method that uses a variable arguments and keyword arguments
        self.assertTrue(False)