class Car:
    def __init__(self, size, brand, seats):
        self.color = "white"
        self.size = size
        self.brand = brand
        self.seats = seats
    def paint(self):
        print("What color do you want to print the car?")
        ans = input()
        self.color = ans
car1 = Car("medium", "toyota", 4)
car1.paint()
print(car1.color)
