from pprint import pprint


class MyEmptyClass:
    """
    By convention, class names are in CamelCase
    """
    pass  # Empty block is not allowed so a pass statement is needed for an empty class


# flight = Flight() <- error, class Flight is not yet defined
empty = MyEmptyClass()  # create a new object doesn't need new keyword like Java
print("type(MyEmptyClass()):", type(empty))


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        The instance attribute of the class does not need to be declared explicitly
        They are created the moment a value is assigned
        Assigning values in other class function also creates instance attributes but it's not recommended
        :param registration:
        :param model:
        :param num_rows:
        :param num_seats_per_row:
        """
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        # if we return multiple objects, it is actually a tuple of objects
        return range(1, self._num_rows + 1), "ABC"[:self._num_seats_per_row]


ac = Aircraft("REG", "Bowen 777", num_rows=3, num_seats_per_row=3)
print("\nac.model():", ac.model())
print("ac.seating_plan():", ac.seating_plan())


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
        rows, seats = self._aircraft.seating_plan()
        # Initialize seating plan using dictionary comprehension nested inside a list comprehension
        # Use a dummy value at position 0 in the list to for the fact that seating plan starts from 1st row
        # Note that the list items don't have to be the same type
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def flight_number(self):  # method names are separated by an underscore: _
        return self._flight_number

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat: str, passenger: str):
        """
        Allocate a seat to a passenger
        :param seat: A seat designator, such as '12C' or '21F'
        :param passenger: The passenger's name
        """
        row_num, row_letter = self._parse_seat(seat)

        if self._seating[row_num][row_letter] is not None:
            raise ValueError("The seat is already occupied: {}".format(seat))
        self._seating[row_num][row_letter] = passenger

    def _parse_seat(self, seat):
        """
        parse a seat designator into a valid row and letter
        :param seat: A seat designator such 20B
        :return: A tuple containing an interger and a string for row and seat
        """
        rows, seat_letters = self._aircraft.seating_plan()

        # Validate column letter
        row_letter = seat[-1]
        if row_letter not in seat_letters:
            raise ValueError("Invalid seat letter: {}".format(row_letter))

        # Validate row number
        row_num_str = seat[:-1]
        try:
            # Python uses function scope (LEGB rule), blocks like try-catch and if-else does not have their own scope
            # row_num var is declared in a tye-catch block, but can be accessed outside of the block
            row_num = int(row_num_str)
        except ValueError:
            raise ValueError("Invalid row number: {}".format(row_num_str))
        if row_num not in rows:
            raise ValueError("Invalid row number: {}".format(row_num_str))
        return row_num, row_letter

    def relocate_passenger(self, from_seat, to_seat):
        """
        Relocate a passenger from a seat to another seat.
        :param from_seat: The existing seat designator for the passenger to be moved
        :param to_seat: The new seat designator
        """
        from_row, from_letter = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger is currently seated at {}".format(from_seat))
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seated {} is not available".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        # Use nested generator comprehension to calculate all empty seats
        return sum(
            sum(1 for row_letter in row if row[row_letter] is None)  # Sum up available seats in one row
            for row in self._seating if row is not None)  # Sum up available seats in all row, skipping dummy first row

    def print_boarding_cards(self, printer_func):
        # Note that the printer function is passed in as a parameter, all functions are objects as well
        for passenger, seat in sorted(self._passenger_seats()):
            printer_func(passenger, self._flight_number, seat, self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger and their seats"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row_number in row_numbers:
            for seat_letter in seat_letters:
                passenger = self._seating[row_number][seat_letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row_number, seat_letter))


def card_printer(passenger: str, flight_num: str, seat: str, aircraft: str):
    text = "| Name: {} Flight:{} Seat: {} Aircraft: {} |".format(passenger, flight_num, seat, aircraft)
    border = "+" + "-"*(len(text) - 2) + "+"
    padding = "|" + " "*(len(text) - 2) + "|"
    lines = [border, padding, text, padding, border]
    card = "\n".join(lines)
    print(card)


flight = Flight("CA160", ac)
print("\nflight.flight_number():", flight.flight_number())
print("flight.model():", flight.aircraft_model(), "\n")

flight.allocate_seat("1A", "John")
flight.allocate_seat("2A", "Bill")
flight.allocate_seat("3A", "Anna")
# flight.allocate_seat("3A", "Kate")  # Seat occupied error
# flight.allocate_seat("5A", "Walter")  # Invalid row number
# flight.allocate_seat("2Z", "Walter")  # Invalid row letter
print("John -> 1A, Bill -> 2A, Anna -> 3A")
pprint(flight._seating)  # All properties in classes are public in Python. Protected properties names are prefixed by _.
flight.relocate_passenger("3A", "3B")

print("\nPassenger at 3A is relocated to 3B")
pprint(flight._seating)

print("\nflight.num_available_seats()", flight.num_available_seats())

print("\nflight.print_boarding_cards(card_printer)")
# Note that the printer function is passed in as a parameter, all functions are objects as well
flight.print_boarding_cards(card_printer)
