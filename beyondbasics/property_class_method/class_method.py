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
    def create_empty(cls, owner_code):
        """ This class method works like a named constructor """
        return cls(owner_code, None)

    @classmethod
    def create_with_item(cls, owner_code, items):
        """ This class method works like a named constructor """
        return cls(owner_code, items)


if __name__ == "__main__":
    instance = ShippingContainer.create_with_item("ABC Corp.", [1, 2, 3, 4])
    print("instance.owner_code:", instance.owner_code)
    print("instance.content:", instance.content)
    print("ShippingContainer.next_serial:", ShippingContainer.next_serial)
