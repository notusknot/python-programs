class Zoo:
    def __init__(self, name):
        self.name = name
        self.populationDict = {}
        self.foodDict = {}
        self.habitatDict = {}
    def addAnimal(self):
        animal = input('What animal would you like to add?\n')
        population = int(input('What is the population of the animal?\n'))
        if animal in self.populationDict:
            self.populationDict[animal] += population
        else:
            self.populationDict[animal] = population
            food = input('What does the animal eat?\n')
            self.foodDict[animal] = food
            habitat = input("What is the animal's habitat?\n")
            self.habitatDict[animal] = habitat

    def removeAnimal(self):
        animal = input('What animal would you like to remove?\n')
        population = int(input('How many do you want to remove?\n'))
        if animal not in self.populationDict:
            print('This animal is not registered')
        else:
            if self.populationDict[animal] >= population:
                self.populationDict[animal] -= population
                if self.populationDict[animal] == 0:
                    del self.populationDict[animal]
            else:
                print('You are trying to remove too many',animal+'s.')
        
    def listAnimals(self):
        for loop in self.populationDict:
            print(loop, self.populationDict[loop], self.foodDict[loop], self.habitatDict[loop])

zoo1 = Zoo('zoo1')
while True:
    choice = int(input('Option 1: add animal \nOption 2: remove animal \nOption 3: list all animals\nOption 4: quit \n'))
    if choice == 1:
        zoo1.addAnimal()
    elif choice == 2:
        zoo1.removeAnimal()
    elif choice == 3:
        zoo1.listAnimals()
    elif choice == 4:
        print('\nThank you\n')
        break
    
            
        
