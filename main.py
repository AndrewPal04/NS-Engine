# Final Project:
# NS Engine
# Github repo: https://github.com/AndrewPal04/NS-Engine

import pygame
from classes import Text, Background, Mob, Button

pygame.init()

#Initial screen setup
info = pygame.display.Info()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

logoIMG = pygame.image.load("logo.png")
logo = Background(screen, logoIMG, 0.5, screen_width/2, screen_height/2 - screen_height/3)

startIMG = pygame.image.load("start.png")
start = Button(screen, startIMG, 0.25, screen_width/2, screen_height/2)

#Start screen
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255,255,255))
    logo.draw()

    if start.pressing():
        break
    

    pygame.display.update()
    clock.tick(60)



#Front Page
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255,255,255))
    
    pygame.display.update()
    clock.tick(60)


"""
Homework
I want you to complete your work of designing your start page for
your final project. If you want to make any changes to the screen,
add in whatever you'd like. We can always change the sprite images
later on, but once you've completed the start screen, I want you to
begin designing the page that will come after the start screen.
Good Luck!
"""