from contextlib import closing


class Fridge:
    """
    This class behaves like a file since it has open() and close() method
    """

    def __init__(self, fridge_name):
        self.name = fridge_name

    def open(self):
        print("Open {} fridge door.".format(self.name))

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print("Taking {} from {}".format(food, self.name))

    def close(self):
        print("Close {} fridge door.".format(self.name))


def get_food(food):
    """
    The closing() function wraps the file-like fridge object with a context-manager
    The context manager always calls the close() method on the resource
    """
    with closing(Fridge("fancy")) as fridge:
        fridge.open()
        fridge.take(food)
        # The close() method will be called by the block automatically


get_food("deep fried pizza")
