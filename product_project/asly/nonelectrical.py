from itertools import product
#درسته؟ خود پروداکت رو نتونستم بیارم.

class NonElectrical(product):
    def __init__(self,name,price,weight):
        super().__init__(name,price)
        self.weight = weight
