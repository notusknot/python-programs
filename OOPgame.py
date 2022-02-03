class Game:
    def __init__(self, name, accessories=[]):
        self.name = name
        self.accessories = accessories

g1 = Game("Minecraft",["Keyboard","Mouse"])
g2 = Game("Mario Bros")
gamelist=[g1,g2]
print("What game would you like to know about")
ans = input()
for i in gamelist:
    if ans == i.name:
        if i.accessories==[]:
            print("This game has no accessories")
        else:
            print(i.accessories)

        
    
