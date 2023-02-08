import pygame

pygame.init()

class Car:
    def __init__(self):
        self.car = pygame.image.load('car.png').convert()
        self.car = pygame.transform.scale(self.car,(30, 20))
        self.car = pygame.transform.rotate(self.car, 180)
        self.position = [315, 455]

screen = pygame.display.set_mode((960, 540))
game_map = pygame.image.load('.\\maps\\PNG\\map.png').convert()
game_map = pygame.transform.scale(game_map, (960, 540))
car = Car()

run = True
while run:
    screen.blit(game_map, (0, 0))
    screen.blit(car.car, car.position)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        car.position[1] -= 1
    elif key[pygame.K_DOWN] == True:
        car.position[1] += 1
    elif key[pygame.K_RIGHT] == True:
        car.position[0] += 1
    elif key[pygame.K_LEFT] == True:
        car.position[0] -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()

pygame.quit()