class ShippingContainer:
    # A class attribute is defined in a class but outside of any methods
    next_serial = 100

    def __init__(self, owner_code, content):
        self.owner_code = owner_code
        self.content = content
        self.serial = ShippingContainer._get_next_serial()

    @classmethod  # The annotation makes the method class method
    def _get_next_serial(cls):  # a cls attribute referencing the class is required as the first parameter
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        """ This class method works like a named constructor """
        return cls(owner_code, None, *args, **kwargs)

    @classmethod
    def create_with_item(cls, owner_code, items, *args, **kwargs):
        """
        Class methods are inherited by sub classes
        The cls argument are set correctly in the sub-classes
        We use *args and **kwargs to pass on any potential new argument added in the inherited class method
        """
        return cls(owner_code, items, *args, **kwargs)


class FridgeContainer(ShippingContainer):
    MAX_CELSIUS = 4

    def __init__(self, owner_code, content, celsius):
        """ The initializer of parent classes are not called implicitly by Python """
        super().__init__(owner_code, content)
        if celsius > FridgeContainer.MAX_CELSIUS:
            raise ValueError("Too hot!")
        self.celsius = celsius


if __name__ == "__main__":
    base_instance = ShippingContainer.create_with_item("ABC Corp.", [1, 2, 3, 4])
    print("base_instance.owner_code:", base_instance.owner_code)
    print("base_instance.content:", base_instance.content)
    print("ShippingContainer.next_serial:", ShippingContainer.next_serial)
    print("\n----------\n")
    child_instance = FridgeContainer.create_with_item("ABC Corp.", [1, 2, 3], 1)
    # child_instance = FridgeContainer.create_with_item("ABC Corp.", [1, 2, 3], 16)  # raises value error
