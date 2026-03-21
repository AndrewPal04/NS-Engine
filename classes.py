import pygame

class Text():
    def __init__(self, surface, text, size, color, font, x, y):
        font_name = pygame.font.match_font(font)
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)

class Button(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.surface = surface
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
    
    def pressing(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        pressed = False
        pos = pygame.mouse.get_pos()
    
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return pressed

class Background(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    

class Mob(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, foods):
        #Find nearest food
        closest = foods[0]
        distance = ((self.rect.centerx-closest.rect.centerx)**2 + (self.rect.centery-closest.rect.centery)**2)**0.5

        for food in foods:
            newdistance = ((self.rect.centerx-food.rect.centerx)**2 + (self.rect.centery-food.rect.centery)**2)**0.5
            if newdistance < distance:
                closest = food
        #now chase closest
        if closest.rect.centerx < self.rect.centerx:
            self.rect.x -= self.speed
        if closest.rect.centerx > self.rect.centerx:
            self.rect.x += self.speed
        if closest.rect.centery < self.rect.centery:
            self.rect.y -= self.speed
        if closest.rect.centery > self.rect.centery:
            self.rect.y += self.speed


class Particle(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass