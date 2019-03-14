class ShippingContainer:
    # A class attribute is defined in a class but outside of any methods
    next_serial = 100

    @staticmethod  # The annotation makes the method static
    def _get_next_serial():  # self arg is not needed for static methods
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, attr):
        self.instance_attribute = attr
        self.serial = ShippingContainer._get_next_serial()


if __name__ == "__main__":
    instance = ShippingContainer("val")
    print("instance.instance_attribute:", instance.instance_attribute)
    print("ShippingContainer.next_serial:", ShippingContainer.next_serial)
