# Final Project:
# NS Engine
import pygame
from classes import Text, Background, Mob

pygame.init()

#Initial screen setup
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

logoIMG = pygame.image.load("logo.png")
logo = Background()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255,255,255))
    
    pygame.display.update()
    clock.tick(60)

