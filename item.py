import csv

class Item:
    all=[]
    pay_rate=0.8
    def __init__(self,name: str,price: float,quantity=0):
        #Asserting vaues
        assert price>=0, f'Price:{price} is not a valid number'
        assert quantity>=0, f'Quantity:{quantity} is not a valid number'

        #Assigning values
        self.__name=name
        self.price=price
        self.quantity=quantity

        # Actions to execute
        Item.all.append(self)
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @property
    def name(self):
        print('123444')
        return self.__name
    
    @name.setter
    def name(self,value):
        print('Hello')
        self.__name=value

    @classmethod    
    def instantiate_csv(cls):
        f=open('items.csv','r')
        reader =csv.DictReader(f)
        items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))    
            )
        
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            print(num.is_integer())
            print('1')
        elif isinstance(num,int):
            print('2')
            return True
        else:
            print('3')
            return False

    def calc_total_price(self):
        return self.price*self.quantity
    def apply_disc(self):
        self.price=self.price*self.pay_rate