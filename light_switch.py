import pygame
import time

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Light Switch By:Avira')

img = pygame.image.load('birthday_card/light_off.png')
img2 = pygame.image.load('birthday_card/light_on.png')
image = pygame.transform.scale(img, (WIDTH, HEIGHT))
image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))

while True: 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    screen.fill('black')
    screen.blit(image, (0,0))
    
    pygame.display.update()
    time.sleep(3)

    screen.fill('black')
    screen.blit(image2, (0,0))
    
    pygame.display.update()
    time.sleep(3)