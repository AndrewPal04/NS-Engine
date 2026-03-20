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

plusIMG = pygame.image.load("plus.png")
minusIMG = pygame.image.load("minus.png")
plusGREEN = Button(screen, plusIMG, 0.3, green.rect.centerx + 40, green.rect.centery + 110)
minusGREEN = Button(screen, minusIMG, 0.3, green.rect.centerx - 40, green.rect.centery + 110)
plusRED = Button(screen, plusIMG, 0.3, red.rect.centerx + 40, red.rect.centery + 110)
minusRED = Button(screen, minusIMG, 0.3, red.rect.centerx - 40, red.rect.centery + 110)

numGreens = 0
numReds = 0
total = 0

redCount = Text(screen, str(numReds), 30, (30,30,30), "segoeuiblack", red.rect.centerx, red.rect.centery + 90)
greenCount = Text(screen, str(numGreens), 30, (30,30,30), "segoeuiblack", green.rect.centerx, green.rect.centery + 90)

start = Button(screen, startIMG, 0.15, screen_width - 150, screen_height - 105)
grayStartIMG = pygame.image.load("grayStart.png")
grayStart = Background(screen, grayStartIMG, 0.15, screen_width - 150, screen_height - 100)

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
    redCount.draw()
    greenCount.draw()

    if total > 4:
        if start.pressing():
            break 
    else:
        grayStart.draw()

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

    pygame.display.update()
    clock.tick(60)

#Simulation loop

# You can do mobs.add(SPRITE), and later in the loop
# you can do mobs.draw(), so only the sprites that are
# in the group will be drawn on the screen.
mobs = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace



    pygame.display.update()
    clock.tick(60)


"""
Homework
Use the food.png, and the Map we made in the last 
pygame loop, to create the map in the new loop, where
food will randomly spawn in the map. Make sure it can only
spawn in the map, and wont pop up outside of it. You can also
continue working on the Mob class by figuring out what
kind of methods we'll need.
Good Luck!

"""