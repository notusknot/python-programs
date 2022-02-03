class Base:
    def __init__(self):
        self.attr = 'something'

    def display(self):
        print(self.attr)

class Derived(Base):
    def __init__(self):
        self.attr2 = 'attr'
        super().__init__()
    def showAttr(self):
        print(self.attr, self.attr2)

derivedObj = Derived()

derivedObj.showAttr()
