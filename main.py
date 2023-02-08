import pygame

pygame.init()

class Car:
    def __init__(self):
        self.car = pygame.image.load('car.png').convert()
        self.car = pygame.transform.scale(self.car,(30, 20))
        self.car = pygame.transform.rotate(self.car, 180)
        self.angle = 0
        self.position = [315, 455]
    def draw(self):
        self.car = pygame.transform.rotate(self.car, self.angle)
        screen.blit(self.car, self.position)

screen = pygame.display.set_mode((960, 540))
game_map = pygame.image.load('.\\maps\\PNG\\map.png').convert()
game_map = pygame.transform.scale(game_map, (960, 540))
car = Car()

run = True
while run:
    screen.blit(game_map, (0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        car.angle = 90
        car.position[1] -= 1
    elif key[pygame.K_DOWN] == True:
        car.angle = -90
        car.position[1] += 1
    elif key[pygame.K_RIGHT] == True:
        car.angle = 0
        car.position[0] += 1
    elif key[pygame.K_LEFT] == True:
        car.angle = 180
        car.position[0] -= 1

    car.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()

pygame.quit()