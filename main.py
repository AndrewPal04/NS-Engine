# Final Project:
# NS Engine
# Github repo: https://github.com/AndrewPal04/NS-Engine

import pygame
from classes import Text, Background, Mob, Button

pygame.init()

#Initial screen setup
info = pygame.display.Info()
screen_width = 1200
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

logoIMG = pygame.image.load("logo.png")
logo = Background(screen, logoIMG, 0.5, screen_width / 2,
                  screen_height / 2 - screen_height / 3)

startIMG = pygame.image.load("start.png")
start = Button(screen, startIMG, 0.15, screen_width / 2, screen_height / 2)

#Start screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.VIDEORESIZE:
        #     screen_width, screen_height = event.w, event.h
        #     screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        #     logo.rect.center = (screen_width/2, screen_height/2 - screen_height/3)
        #     start.rect.center = (screen_width/2, screen_height/2)
    screen.fill((255, 255, 255))
    logo.draw()

    if start.pressing():
        break

    pygame.display.update()
    clock.tick(60)

gridIMG = pygame.image.load("grid.png")
grid = Background(screen, gridIMG, 1.5, 0, screen_height / 2)
grid.rect.left = 50

greenIMG = pygame.image.load("green.png")
green = Background(screen, greenIMG, 0.25, screen_width - 100, 100)

redIMG = pygame.image.load("red.png")
red = Background(screen, redIMG, 0.25, screen_width - 100, 350)

foodIMG = pygame.image.load("food.png")
food = Background(screen, foodIMG, 0.1, screen_width - 100, 510)

plusIMG = pygame.image.load("plus.png")
minusIMG = pygame.image.load("minus.png")
plusGREEN = Button(screen, plusIMG, 0.3, green.rect.centerx + 40, green.rect.centery + 110)
minusGREEN = Button(screen, minusIMG, 0.3, green.rect.centerx - 40, green.rect.centery + 110)
plusRED = Button(screen, plusIMG, 0.3, red.rect.centerx + 40, red.rect.centery + 110)
minusRED = Button(screen, minusIMG, 0.3, red.rect.centerx - 40, red.rect.centery + 110)
plusFOOD = Button(screen, plusIMG, 0.3, food.rect.centerx + 40, food.rect.centery + 40)
minusFOOD = Button(screen, minusIMG, 0.3, food.rect.centerx - 40, food.rect.centery + 40)

numFood = 0
numGreens = 0
numReds = 0
total = 0

redCount = Text(screen, str(numReds), 30, (30,30,30), "segoeuiblack", red.rect.centerx, red.rect.centery + 90)
greenCount = Text(screen, str(numGreens), 30, (30,30,30), "segoeuiblack", green.rect.centerx, green.rect.centery + 90)
foodCount = Text(screen, str(numFood), 30, (30,30,30), "segoeuiblack", food.rect.centerx, food.rect.centery + 20)

start = Button(screen, startIMG, 0.15, screen_width - 150, screen_height - 75)
grayStartIMG = pygame.image.load("grayStart.png")
grayStart = Background(screen, grayStartIMG, 0.15, screen_width - 150, screen_height - 70)

#Front Page
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255, 255, 255))
    grid.draw()

    green.draw()
    red.draw()
    food.draw()
    redCount.draw()
    greenCount.draw()
    foodCount.draw()

    pos = pygame.mouse.get_pos()
    if green.rect.collidepoint(pos):
        descG = Text(screen, "needed food: 1", 40, (30,30,30), "segoeuibold", green.rect.x-100, green.rect.y + 30)
        descG.draw()
        descG = Text(screen, "food to spawn: 2", 40, (30,30,30), "segoeuibold", green.rect.x-100, green.rect.y + 60)
        descG.draw()
        descG = Text(screen, "speed: 1", 40, (30,30,30), "segoeuibold", green.rect.x-100, green.rect.y + 90)
        descG.draw()
        
    if red.rect.collidepoint(pos):
        descR = Text(screen, "needed food: 2", 40, (30,30,30), "segoeuibold", red.rect.x-100, red.rect.y + 30)
        descR.draw()
        descR = Text(screen, "food to spawn: 3", 40, (30,30,30), "segoeuibold", red.rect.x-100, red.rect.y + 60)
        descR.draw()
        descR = Text(screen, "speed: 2", 40, (30,30,30), "segoeuibold", red.rect.x-100, red.rect.y + 90)
        descR.draw()
        
    if food.rect.collidepoint(pos):
        descF = Text(screen, "food count", 40, (30,30,30), "segoeuibold", food.rect.x-100, food.rect.y)
        descF.draw()
    if total > 4 and numFood > 7:
        if start.pressing():
            break 
    else:
        grayStart.draw()
        if grayStart.rect.collidepoint(pos):
            Text(screen, "5 mobs and 8 foods needed to start", 40, (30,30,30), "segoeuibold", grayStart.rect.x-200, grayStart.rect.y + 55).draw()

    if numGreens == 15:
        maxText = Text(screen, "[Max]", 30, (30,30,30), "segoeuibold", green.rect.centerx, green.rect.centery + 135)
        maxText.draw()

    
    if plusGREEN.pressing():
        if numGreens < 15:
            numGreens += 1
            total += 1
            greenCount = Text(screen, str(numGreens), 30, (30,30,30), "segoeuiblack", green.rect.centerx, green.rect.centery + 90)

    if minusGREEN.pressing():
        if numGreens > 0:
            numGreens -= 1
            total -= 1
            greenCount = Text(screen, str(numGreens), 30, (30,30,30), "segoeuiblack", green.rect.centerx, green.rect.centery + 90)

    if numReds == 10:
        maxText = Text(screen, "[Max]", 30, (30,30,30), "segoeuibold", red.rect.centerx, red.rect.centery + 135)
        maxText.draw()


    if plusRED.pressing():
        if numReds < 10:
            numReds += 1
            total += 1
            redCount = Text(screen, str(numReds), 30, (30,30,30), "segoeuiblack", red.rect.centerx, red.rect.centery + 90)

    if minusRED.pressing():
        if numReds > 0:
            numReds -= 1
            total -= 1
            redCount = Text(screen, str(numReds), 30, (30,30,30), "segoeuiblack", red.rect.centerx, red.rect.centery + 90)

    if plusFOOD.pressing():
        if numFood < 40:
            numFood += 1
            foodCount = Text(screen, str(numFood), 30, (30,30,30), "segoeuiblack", food.rect.centerx, food.rect.centery + 20)

    if minusFOOD.pressing():
        if numFood > 0:
            numFood -= 1
            foodCount = Text(screen, str(numFood), 30, (30,30,30), "segoeuiblack", food.rect.centerx, food.rect.centery + 20)

    pygame.display.update()
    clock.tick(60)

#Simulation loop

# You can do mobs.add(SPRITE), and later in the loop
# you can do mobs.draw(), so only the sprites that are
# in the group will be drawn on the screen.
mobs = pygame.sprite.Group()
day = 1

foodsList = []
for i in range(numFood):
    foodsList.append(Background(screen, ))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace
    screen.fill((255,255,255))
    grid.draw()
    Text(screen, "Green count: "+ str(numGreens), 40, (30,30,30), "segoeuibold", screen_width-200, 50).draw()
    Text(screen, "Red count: "+ str(numReds), 40, (30,30,30), "segoeuibold", screen_width-200, 80).draw()
    Text(screen, "Food count: "+ str(numFood), 40, (30,30,30), "segoeuibold", screen_width-200, 110).draw()
    Text(screen, "Day: "+ str(day), 40, (30,30,30), "segoeuibold", grid.rect.centerx, grid.rect.top-40).draw()



    pygame.display.update()
    clock.tick(60)

"""
Homework
After completing the update method for your
mobs, find a way to place the foods randomly on the screen,
and have the mobs chase the foods. You should be able to see
the mobs and the foods, but you don't have to
check collision yet, or add days. Just get
them moving around in the simulation
Good Luck!
"""