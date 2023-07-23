import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('walking game')

clock = pygame.time.Clock()

image = pygame.image.load(r'player.png')

x = 100
y = 100
velocity = 12

run = True
while run:
    clock.tick(60)
    window.fill((255, 255, 255))
    window.blit(image, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()                    
        key_pressed_is = pygame.key.get_pressed()
        if key_pressed_is[K_LEFT]:
            x -= 8
        if key_pressed_is[K_RIGHT]:
            x += 8
        if key_pressed_is[K_UP]:
            y -= 8
        if key_pressed_is[K_DOWN]:
            y += 8
        pygame.display.update()
