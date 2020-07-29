from unittest import TestCase
from intermediate.excercises.args_lab import displaystr


class TestArgsLab(TestCase):
    """
    TestArgsLab is designed to familiarize yourself with unitest in Python as well experimenting with dynamic
    method parameters
    """

    def test_named_parmeters_single_argument_default(self):
        self.assertTrue("Bob was here" in displaystr())

    def test_create_method_using_args(self):
        # Create a method that uses a variable argument length
        # iterate through the argument list and test the values
        self.assertTrue(False)

    def test_create_method_with_variable_and_keyword(self):
        # Create a method that uses a variable arguments and keyword arguments
        self.assertTrue(False)

    def test_create_second_method_with_args_and_kwargs(self):
        # Create a test where the you have one required variable, one parameter that is optional
        # three args parameters and two keyword paramters.  Have the method return three parameters in a tuple and
        # and test the three results for expected values.
        self.assertTrue(False)
