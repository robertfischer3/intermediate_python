import numpy
import sympy as sym
import numbers

class Probability_Of_A_Given_B:
    def __init__(self, probability=0):
        self.probability = probability

class Probability:
    def __init__(self):
        pass

    # Axioms
    # P(A−B)=P(A)−P(A ∩ B).
    # P(A ∪ B)=P(A)+P(B)−P(A ∩ B)


    def create_set(self, setlist):
        if type(setlist) is set:
            return setlist
        elif type(setlist) is list:
            return set(setlist)

    def choose_set(self, A, S):
        # probability of set A given S, where S is the set of probabilities
        if A is None:
            return None
        if S is None:
            return None
        if not type(A) is set and not type(S) is set:
            raise

        P_A = len(A)/len(S)
        return P_A

    def conditional(self, event_A, given_event_B, total_events):
        if isinstance(event_A, numbers.Number) \
                and isinstance(given_event_B, numbers.Number) \
                and isinstance(total_events, numbers.Number):

            # P(this|given event) = P(probability_of_this ∩ given_event_probability)/P(given_event_probability)
            intersection_probability = event_A / total_events
            given_probability = given_event_B/total_events

            return intersection_probability/given_probability



    def given_sets(self, A, B, S):

        if A is None:
            return None
        if B is None:
            return None
        if S is None:
            return None

        if type(A) is set and type(B) is set and type(S) is set:
            P_of_A_and_B =len (A & B)/len(S)
            P_of_B = len(B)/len(S)

            return (P_of_A_and_B/P_of_B)



    def find_compliment(self, A):
        pass