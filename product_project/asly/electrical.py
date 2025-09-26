from asly import product


class Electrical(product):
    def __init__(self,name,price,voltage):
        super().__init__(name,price)
        self.voltage = voltage
