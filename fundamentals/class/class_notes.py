from pprint import pprint


class EmptyClass:
    """
    By convention, class names are in CamelCase
    """
    pass  # Empty block is not allowed so a pass statement is needed for an empty class


# flight = Flight() <- error, class Flight is not yet defined
empty = EmptyClass()  # create a new object doesn't need new keyword like Java
print("type(empty):", type(empty), "\n")


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def searing_plan(self):
        # if we return multiple objects, it is actually a tuple of objects
        return range(1, self._num_rows + 1), "ABCDEFGHJ"[:self._num_seats_per_row]


ac = Aircraft("REG", "Boeing 777", num_rows=23, num_seats_per_row=6)
print("ac.model():", ac.model())
print("ac.searing_plan():", ac.searing_plan(), "\n")


class Flight:

    def __init__(self, f_number: str, aircraft: Aircraft):  # self is always the first argument to all instance methods
        """
        * Starting from Python 3.5, we can declare methods and variables like:
            * def function_name(parameter1: type) -> return_type:
            * varName: VarType
        * __init__() is NOT the constructor, constructors in Python are provided by Python runtime
        * __init__() is called by the constructor which checks the existence of instance initializer
        * __init__() (instance initializers) return nothing
        *   self     is equivalent to this in Java
        :param f_number: flight number
        """
        if not f_number[:2].isalpha():
            raise ValueError("Airline code missing in '{}'".format(f_number))

        if not f_number[:2].isupper():
            raise ValueError("Airline should be in upper case in '{}'".format(f_number))

        if not (f_number[2:].isdigit() and int(f_number[2:]) <= 9999):
            raise ValueError("Invalid route number in '{}'".format(f_number))

        # Assigning values to a property that doesn't exist creates such property automatically
        # "Private" property names are prefixed by _ by convention
        self._flight_number = f_number
        self._aircraft = aircraft

        # tuple unpacking
        rows, seats = self._aircraft.searing_plan()
        # Initialize seating plan using dictionary comprehension nested inside a list comprehension
        # Use a dummy value at position 0 in the list to for the fact that seating plan starts from 1st row
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def flight_number(self):  # method names are separated by an underscore: _
        return self._flight_number

    def model(self):
        return self._aircraft.model()

    def seating(self):
        return self._seating


flight = Flight("CA160", ac)
print("flight.flight_number():", flight.flight_number())
print("flight.model():", flight.model())
pprint(flight.seating())
