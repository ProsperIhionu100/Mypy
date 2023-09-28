import csv

from item import Item
from phone import Phone



Phone1 =Phone("JscPhonev18", 500, 5) 
print(Phone1.calculate_total_price())
print(Phone.all)

Phone2 =Phone("JscPhonev28", 700, 5) 

Item.instantiate_from_csv()
print(Item.all)
# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7.0))
    
# Item1 = Item("Phone",100,1) 
# # Item1.name = "Phone"
# # Item1.price =100
# # Item1.quantity =5
# Item1.apply_discount()
# print(Item1.price)



# Item2 = Item("Laptop",1000,3) 
# Item2.pay_rate = 0.7
# Item2.apply_discount()
# print(Item2.price)
# # Item2.name = "laptop"
# # Item2.price =1000
# # Item2.quantity =3
# Item2.has_numpad = False

# # print(Item1.name)
# # print(Item2.name)
# # print(Item1.price)
# # print(Item2.price)
# # print(Item1.quantity)
# # print(Item2.quantity)

# # print(Item1.calculate_total_price())
# # print(Item2.calculate_total_price())

# # print(Item.pay_rate)
# # print(Item1.pay_rate)
# # print(Item2.pay_rate)

# # print(Item.__dict__) # All the attributes for the class level
# # print(Item1.__dict__) # All the attributes for the Instance level

# item1 = Item("Phone",100,1)
# item2 = Item("Laptop",1000,3)
# item1 = Item("Cable",10,5)
# item1 = Item("Mouse",50,5)
# item1 = Item("Keyboard",75,5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)