class ShippingContainer:
    next_serial = 100

    def __init__(self, attr):
        self.instance_attribute = attr
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

        # Does not rebind ShippingContainer.next_serial.
        # Instead, a new instance attr is created by the same name and it hides the class attribute
        # self.next_serial = 200


if __name__ == "__main__":
    instance = ShippingContainer("val")
    print("instance.instance_attribute:", instance.instance_attribute)
    print("instance.serial:", instance.serial)
    print("instance.next_serial:", instance.next_serial)  # accessing class attr via instances works, but is bad
    print("ShippingContainer.next_serial:", ShippingContainer.next_serial)
    # print("ShippingContainer.serial:", ShippingContainer.serial)  # compilation error, serial only exists on instances
