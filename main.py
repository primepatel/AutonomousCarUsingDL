import pygame

pygame.init()

class Car:
    def __init__(self):
        self.car = pygame.image.load('car.png').convert()
        self.car = pygame.transform.scale(self.car,(30, 20))
        self.car = pygame.transform.rotate(self.car, 180)
        self.rotated_car = self.car
        self.angle = 0
        self.position = [315, 455]
        self.center = [self.position[0], self.position[1] + 10]
        self.edges = [[self.position[0]-15, self.position[1]-10], [self.position[0]+15, self.position[1]-10], [self.position[0]+15, self.position[1]+10], [self.position[0]-15, self.position[1]+10]]

    def draw(self):
        self.rotated_car = pygame.transform.rotate(self.car, self.angle)
        screen.blit(self.rotated_car, (self.position[0]-15, self.position[1]-10))
    
    def set_edges(self, cords):
        self.edges[0][0], self.edges[0][1] = cords[0] - 15, cords[1] - 10
        self.edges[1][0], self.edges[1][1] = cords[0] + 15, cords[1] - 10
        self.edges[2][0], self.edges[2][1] = cords[0] + 15, cords[1] + 10
        self.edges[3][0], self.edges[3][1] = cords[0] - 15, cords[1] + 10

    def check_crash(self):
        for i in self.edges:
            print(game_map.get_at(tuple(i)))
            if game_map.get_at(tuple(i)) != (58, 58, 60, 255):
                return True
        return False

screen = pygame.display.set_mode((960, 540))
game_map = pygame.image.load('.\\maps\\PNG\\map.png').convert()
game_map = pygame.transform.scale(game_map, (960, 540))
car = Car()

run = True
while run:
    screen.blit(game_map, (0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        cords = (car.position[0], car.position[1]-1)
        car.set_edges(cords)
        if not car.check_crash():
            car.angle = 90
            car.position[1] -= 1
    elif key[pygame.K_DOWN] == True:
        cords = (car.position[0], car.position[1]+1)
        car.set_edges(cords)
        if not car.check_crash():
            car.angle = -90
            car.position[1] += 1
    elif key[pygame.K_RIGHT] == True:
        cords = (car.position[0]+1, car.position[1])
        car.set_edges(cords)
        if not car.check_crash():
            car.angle = 0
            car.position[0] += 1
    elif key[pygame.K_LEFT] == True:
        cords = (car.position[0]-1, car.position[1])
        car.set_edges(cords)
        if not car.check_crash():
            car.angle = 180
            car.position[0] -= 1
    car.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()

pygame.quit()