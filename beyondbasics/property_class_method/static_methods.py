class ShippingContainer:
    next_serial = 100

    @staticmethod  # The annotation makes the method static
    def _get_next_serial():  # self arg is not needed for static methods
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @staticmethod
    def _print_info():
        print("creating a base container...")

    def __init__(self, attr):
        # ShippingContainer._print_info()  # the overridden static method will never be called
        self._print_info()  # using self keyword allows the overridden static method to be called correctly
        self.instance_attribute = attr
        self.serial = ShippingContainer._get_next_serial()


class SuperContainer(ShippingContainer):
    @staticmethod
    def _print_info():
        """ In order to have the overridden static method called, parent class need to go through "self", not class """
        print("creating a super container!!!")


if __name__ == "__main__":
    base_instance = ShippingContainer("base")
    print("base_instance.instance_attribute:", base_instance.instance_attribute)
    print("ShippingContainer.next_serial:", ShippingContainer.next_serial)
    print("\n----------\n")
    child_instance = SuperContainer("child")
    print("SuperContainer.next_serial:", SuperContainer.next_serial)
    print("child_instance.instance_attribute:", child_instance.instance_attribute)

