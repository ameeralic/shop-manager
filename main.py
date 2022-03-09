from item import Item
from phone import Phone
from keyboard import Keyboard

Item.instantiate_csv()

item3=Keyboard('aaa', 100, 4)
item3.apply_disc()
print(item3.price)