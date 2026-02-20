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
logo = Background(screen, logoIMG, 0.5, screen_width/2, screen_height/2 - screen_height/3)

startIMG = pygame.image.load("start.png")
start = Button(screen, startIMG, 0.15, screen_width/2, screen_height/2)

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
    screen.fill((255,255,255))
    logo.draw()

    if start.pressing():
        break
    

    pygame.display.update()
    clock.tick(60)

gridIMG = pygame.image.load("grid.png")
grid = Background(screen, gridIMG, 1.5, 0, screen_height/2)
grid.rect.left = 50

greenIMG = pygame.image.load("green.png")
green = Background(screen, greenIMG, 0.25, screen_width-100, 100)

redIMG = pygame.image.load("red.png")
red = Background(screen, redIMG, 0.25, screen_width-100, 350)

plusIMG = pygame.image.load("plus.png")
minusIMG = pygame.image.load("minus.png")
plusGREEN = Button(screen, plusIMG, 0.3, green.rect.centerx+40, green.rect.centery+110)
minusGREEN = Button(screen, minusIMG, 0.3, green.rect.centerx-40, green.rect.centery+110)

numGreens = 0
numReds = 0

#Front Page
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255,255,255))
    grid.draw()
    
    green.draw()
    red.draw()

    if plusGREEN.pressing():
        pass
    if minusGREEN.pressing():
        pass

    pygame.display.update()
    clock.tick(60)


# Homework
# Continue working through the front page by creating plus and minus buttons
# for the green and red mobs. Make sure to use the text class to display the
# number for both mobs, and make sure the number updates when the buttons are pressed.
# IMPORTANT:
# The user should NOT be able to create negative mobs, and you can put a limit to the
# number of mobs they can make
# Good Luck
