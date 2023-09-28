from item import Item


class Phone(Item):
    pay_rate =0.5
    def __init__(self,name:str,price:float,quantity=0, brokenPhones =0):
    # call to super method to have access to all atrtibutes / methods
        super().__init__(
            name, price, quantity
        )
        self.brokenPhones = brokenPhones 
        