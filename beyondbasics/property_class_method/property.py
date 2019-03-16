class ShippingContainer:
    # A class attribute is defined in a class but outside of any methods
    next_serial = 100

    def __init__(self, owner_code, content):
        self.owner_code = owner_code
        self.content = content
        self.serial = ShippingContainer._get_next_serial()

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, None, *args, **kwargs)

    @classmethod
    def create_with_item(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, items, *args, **kwargs)


class FridgeContainer(ShippingContainer):
    MAX_CELSIUS = 4

    def __init__(self, owner_code, content, celsius):
        """ The initializer of parent classes are not called implicitly by Python """
        super().__init__(owner_code, content)
        if celsius > FridgeContainer.MAX_CELSIUS:
            raise ValueError("Too hot!")
        self._celsius = celsius

    @property  # https://stackoverflow.com/a/17330273/3363541
    def celsius(self):
        """
        High level:
        @property converts celsius method into something that, when accessed, works like an attribute: instance.celsius
        Under the hood:
        * A new property object is created and bond to the name of "celsius"
        * A reference to the original definition of method "celsius" is in the property object (how decorator works)
        * A set of property method is already declared by this time, e.g. fget, fset. However, they = None (see doc)
        * Getter, setter, deleter methods can be then created by using decorators under this property
        """
        print("property (getter) method called")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """
        The setter method is registered under the "celsius" property object
        Setter method name must match the property name ("celsius", in this case)
        """
        print("property (setter) setter method called")
        self._celsius = value


if __name__ == "__main__":
    child_instance = FridgeContainer.create_with_item("ABC Corp.", [1, 2, 3, 4], -16)
    print("--- object created ---")
    print("child_instance.celsius: ", child_instance.celsius)  # "celsius" getter method is accessed like an attribute
    child_instance.celsius = -100  # no ending (), "celsius" setter method is accessed as if is is an attribute
    print("--- object property updated ---")
    print("child_instance.celsius: ", child_instance.celsius)
