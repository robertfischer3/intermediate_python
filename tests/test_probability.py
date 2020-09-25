from unittest import TestCase
from intermediate.excercises.math_labs.probability import Probability
import logging


class TestProbability(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_given(self):
        S = {1, 2, 3, 4, 5, 6}
        A = {1, 3, 5}
        B = {3, 4, 5}

        probability = Probability()
        result = probability.given_sets(A=A, B=B, S=S)
        logging.debug("The result is {}".format(result))
        self.assertIsNotNone(result)

    def test_choose(self):
        S = {1, 2, 3, 4, 5, 6}
        A = {1, 3, 5}

        probability = Probability()
        result = probability.choose(A, S)

        logging.debug("The result is {}".format(result))
        self.assertIsNotNone(result)
        self.assertEqual(result, 0.5)

    def test_probability_A_given_C(self):
        # P(A ∩ C)
        probability = Probability()


class TestProbability(TestCase):
    def test_conditional(self):
        probability = Probability()
        result = probability.conditional(25, 100, 200)
        self.assertIsNotNone(result)
        self.assertEqual(result)
        logging.debug("The result is {}".format(result))

    def test_conditional_2(self):
        probability = Probability()
        result = probability.conditional(event_A=25, given_event_B=45, total_events=200)
        self.assertIsNotNone(result)
        print(result)
        # self.assertEqual(result)
        logging.debug("The result is {}".format(result))

    def test_conditional_3(self):
        probability = Probability()
        result = probability.conditional(event_A=75, given_event_B=145, total_events=155)
        self.assertIsNotNone(result)

        # Close enough for goverment work :)
        self.assertAlmostEqual(result, .51724, 3)
        logging.debug("The result is {}".format(result))