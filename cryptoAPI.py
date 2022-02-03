from pygame.locals import *
import pygame

import math, requests, random, time
pygame.init()
clock = pygame.time.Clock()
color = (255, 255, 255)
black = (0,0,0)
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")

cryptoIDs = [ 'safemoon', 'ripple', 'road', 'bitcoin', 'ethereum' ]

def calculateDistance(x1, x2, y1, y2):
    return abs(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
def randomcolor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
class Circle:
    def __init__(self, name):
        self.radius = 100
        self.x = random.randint(100,500)
        self.y = random.randint(100,500)
        self.color = randomcolor()
        self.name = name
circleList = []
for loop in cryptoIDs:
    circleList.append(Circle(loop))

def getPrice():
    coinsDictionary = { 'safemoon':10000000, 'ripple':100, 'road':10000, 'bitcoin':0.001, 'ethereum':0.01} 
    for loop in circleList:
        try:
            data = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+loop.name+'&vs_currencies=usd')
            time.sleep(0.5)
            data = data.json()
            print(data)
            price = data[loop.name]['usd']
            finalPrice = price * coinsDictionary[loop.name]
            print(finalPrice)
            print(loop.radius)
            loop.radius = finalPrice
            print(loop.radius)
        except:
            



while True:
    time.sleep(0.5)
    getPrice()
    screen.fill(black)
    for loop in circleList:
            pygame.draw.circle(screen, loop.color, (loop.x, loop.y), loop.radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
