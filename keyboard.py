from item import Item


class Key(Item):
    pay_rate =0.7
    def __init__(self,name:str,price:float,quantity=0):
    # call to super method to have access to all atrtibutes / methods
        super().__init__(
            name, price, quantity
        )
        
key1 = Key("Jsckeyboard", 1000, 3) 
key1.apply_discount()
print(key1.price)