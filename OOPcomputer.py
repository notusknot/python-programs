class shoppingList:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart
        
    def add(self):
        print('What item would you like to add')
        item=input()
        print('How many would you like to add?')
        count=int(input())
        if item in self.cart:
            self.cart[item]+=count
        else:
            self.cart[item]=count
    
    def remove(self):
        print('What item would you like to remove?')
        item=input()
        if item in self.cart:
            print('How many of these would you like to remove?')
            count=int(input())
            if self.cart[item] > count:
                self.cart[item]-=count
            else:
                del self.cart[item]
        else:
            print('Item not found, try again.')
            
    def showInfo(self):
        for loop in self.cart:
            print("\n",self.cart[loop], loop, "\n")
list1 = shoppingList("list1",{})
while True:
    print('Option 1: add')
    print('Option 2: remove')
    print('Option 3: display info')
    ans=int(input())
    if ans == 1:
        list1.add()
    elif ans == 2:
        list1.remove()
    elif ans == 3:
        list1.showInfo()
        
