# Final Project:
# NS Engine
# Github repo: https://github.com/AndrewPal04/NS-Engine

import pygame
import random
import time
from classes import Text, Background, Mob, Button
import matplotlib.pyplot as plt

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
food = Background(screen, foodIMG, 0.1, screen_width - 100, 540)

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

    # var1 = pygame.draw.rect(screen, (0,0,0), (82, 80, 33, 33)) #for testing
    # var2 = pygame.draw.rect(screen, (0,0,0), (575, screen_height-83, 33, 33))


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
        descF = Text(screen, "the maximum is depends", 40, (30,30,30), "segoeuibold", food.rect.x-100, food.rect.y-15)
        descF.draw()
        descF = Text(screen, "on the amount of mobs", 40, (30,30,30), "segoeuibold", food.rect.x-100, food.rect.y+15)
        descF.draw()
    if total > 4 and numFood > 7:
        if start.pressing():
            time.sleep(0.2)
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
        numFood += 1
        foodCount = Text(screen, str(numFood), 30, (30,30,30), "segoeuiblack", food.rect.centerx, food.rect.centery + 20)            

    if minusFOOD.pressing():
        if numFood > 0:
            numFood -= 1
            foodCount = Text(screen, str(numFood), 30, (30,30,30), "segoeuiblack", food.rect.centerx, food.rect.centery + 20)


    pygame.display.update()
    clock.tick(60)

#Simulation loop

mobs = pygame.sprite.Group()
day = 1

totalfood = numFood
foodsList = []
for i in range(totalfood):
    foodsList.append(Background(screen, foodIMG, 0.05, random.randint(155, 510),random.randint(185, screen_height-180)))

sprite_group = pygame.sprite.Group()

for i in range(numGreens):
    sprite_group.add(Mob(greenIMG, 0.05, 82+i*33, 80, "GREEN"))

for i in range(numReds):
    sprite_group.add(Mob(redIMG, 0.05, 82+i*33, screen_height - 85, "RED"))


graphIMG = pygame.image.load("graph.png")
graph = Button(screen, graphIMG, 0.15, screen_width - 150, screen_height - 75)
green = [numGreens]
red = [numReds]
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
    Text(screen, "Total Foods: "+ str(totalfood), 40, (30,30,30), "segoeuibold", screen_width-200, 140).draw()
    Text(screen, "Day: "+ str(day), 40, (30,30,30), "segoeuibold", grid.rect.centerx, grid.rect.top-40).draw()


    for i in range(len(foodsList)):
        foodsList[i].draw()

    sprite_group.draw(screen)
    home = 0
    numGreens = 0
    numReds = 0
    numFood = len(foodsList)

    for mob in sprite_group:
        if mob.color == "GREEN":
            numGreens += 1
        elif mob.color == "RED":
            numReds += 1


        mob.update(foodsList)
        for food in foodsList:
            if pygame.sprite.collide_rect(mob, food):
                mob.eaten += 1
                foodsList.remove(food)


        if numFood != totalfood and mob.at_origin():
            home += 1


    if home == len(sprite_group):
        for mob in sprite_group:
            if mob.eaten < mob.needed:
                if mob.color == "RED":
                    numReds -= 1
                elif mob.color == "GREEN":
                    numGreens -= 1

            if mob.eaten == mob.spawn:
                if mob.color == "RED":
                    numReds += 1
                elif mob.color == "GREEN":
                    numGreens += 1

        day += 1
        for mob in sprite_group:
            mob.kill()

        for i in range(numGreens):
            if i <= 15:
                sprite_group.add(Mob(greenIMG, 0.05, 82+i*33, 80, "GREEN"))
            elif i <= 31:
                sprite_group.add(Mob(greenIMG, 0.05, 82+(i-16)*33, 113, "GREEN"))
            elif i <= 47:
                sprite_group.add(Mob(greenIMG, 0.05, 82+(i-32)*33, 146, "GREEN"))
            else:
                numGreens = 48

        for i in range(numReds):
            if i <= 15:
                sprite_group.add(Mob(redIMG, 0.05, 82+i*33, screen_height - 85, "RED"))
            elif i <= 31:
                sprite_group.add(Mob(redIMG, 0.05, 82+(i-16)*33, screen_height - 118, "RED"))
            elif i <= 47:
                sprite_group.add(Mob(redIMG, 0.05, 82+(i-32)*33, screen_height - 151, "RED"))
            else:
                numReds = 48

        foodsList = []
        for i in range(totalfood):
            foodsList.append(Background(screen, foodIMG, 0.05, random.randint(155, 510),random.randint(185, screen_height-180)))

        green.append(numGreens)
        red.append(numReds)

    if graph.pressing():
        x = list(range(1, len(green)+1))

        plt.figure()
        if green[0] != 0:
            plt.plot(x, green, marker="o", color="green", label="green")
        if red[0] != 0:
            plt.plot(x, red, marker="o", color="red", label="red")

        plt.xlabel("day")
        plt.ylabel("amount")
        plt.title("NS-Engine: running result (foods: "+str(totalfood)+")")
        plt.legend()
        plt.show()


    pygame.display.update()
    clock.tick(60)

