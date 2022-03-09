from item import Item

class Phone(Item):
    all=[]
    def __init__(self, name: str, price: float, quantity=0,brocken=0):
        super().__init__(name, price, quantity)
        assert brocken>=0, 'brocken phone must be an integer'
        self.brocken=brocken
        Phone.all.append(self)