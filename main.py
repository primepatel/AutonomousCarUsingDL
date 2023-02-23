import pygame, sys
from math import sin, cos, atan, sqrt
from math import radians as rad
ROAD_COLOR = (58, 58, 60, 255)
pygame.init()

class Car:
    def __init__(self):
        self.car = pygame.image.load('car.png').convert()
        self.car = pygame.transform.scale(self.car,(30, 20))
        self.car = pygame.transform.rotate(self.car, 180)
        self.rotated_car = self.car
        self.angle = 0
        self.position = [315, 455]
        self.edges = [[self.position[0]-15, self.position[1]-10], [self.position[0]+15, self.position[1]-10], [self.position[0]+15, self.position[1]+10], [self.position[0]-15, self.position[1]+10]]
        self.sensor_data = []

    def draw(self):
        self.rotated_car = pygame.transform.rotate(self.car, -self.angle)
        screen.blit(self.rotated_car, (int(self.position[0])-15, int(self.position[1])-10))
        self.sensor_data.clear()
        loc = [int(abs((self.edges[1][0]+self.edges[2][0])/2)), int(abs((self.edges[1][1]+self.edges[2][1])/2))]
        for i in self.get_sensor_data():
            boundary = i[0]
            pygame.draw.line(screen, (0, 255, 0),loc , boundary, 1)
            pygame.draw.circle(screen, (0, 255, 0), boundary, 5)

    def set_edges(self, cords):
        r, theta = sqrt(15**2 + 10**2), atan(2/3)
        dx, dy = int(r*cos(theta + rad(self.angle))), int(r*sin(theta + rad(self.angle)))
        self.edges[0][0], self.edges[0][1] = cords[0] - dx, cords[1] - dy
        self.edges[1][0], self.edges[1][1] = cords[0] + dx, cords[1] - dy
        self.edges[2][0], self.edges[2][1] = cords[0] + dx, cords[1] + dy
        self.edges[3][0], self.edges[3][1] = cords[0] - dx, cords[1] + dy

    def check_crash(self):
        for i in self.edges:
            # print(game_map.get_at(tuple(i)))
            if game_map.get_at(tuple(i)) != ROAD_COLOR:
                print("crashed")
                return True
        print("not crashed")
        return False
    
    def get_sensor_data(self):
        for sensor_angle in range(-90, 91, 30):
            x, y = int(abs((self.edges[1][0]+self.edges[2][0])/2)), int(abs((self.edges[1][1]+self.edges[2][1])/2))
            length = 0
            a, b = x, y
            while game_map.get_at((x, y)) == ROAD_COLOR and length < 150:
                length = length + 1
                x = int(a + cos(rad( self.angle + sensor_angle)) * length)
                y = int(b + sin(rad( self.angle + sensor_angle)) * length)
            dist = int((pow(x - a, 2) + pow(y - b, 2))**0.5)
            self.sensor_data.append([(x, y), dist])
        return self.sensor_data

screen = pygame.display.set_mode((960, 540))
game_map = pygame.image.load('.\\maps\\PNG\\map.png').convert()
game_map = pygame.transform.scale(game_map, (960, 540))
car = Car()

run = True
while run:
    screen.blit(game_map, (0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        cords = (int(car.position[0] + cos(rad(car.angle))), int(car.position[1] + sin(rad(car.angle))))
        car.set_edges(cords)
        car.check_crash()
        car.position[0], car.position[1] = car.position[0] + cos(rad(car.angle)), car.position[1] + sin(rad(car.angle))
    elif key[pygame.K_DOWN] == True:
        cords = (int(car.position[0] + cos(rad(car.angle))), int(car.position[1] + sin(rad(car.angle))))
        car.set_edges(cords)
        car.check_crash()
        car.position[0], car.position[1] = car.position[0] - cos(rad(car.angle)), car.position[1] - sin(rad(car.angle))
    
    elif key[pygame.K_RIGHT] == True:
        cords = (int(car.position[0] + cos(rad(car.angle))), int(car.position[1] + sin(rad(car.angle))))
        car.set_edges(cords)
        car.check_crash()
        car.angle += 1
    
    elif key[pygame.K_LEFT] == True:
        cords = (int(car.position[0] + cos(rad(car.angle))), int(car.position[1] + sin(rad(car.angle))))
        car.set_edges(cords)
        car.check_crash()
        car.angle -= 1

    car.draw()
    # print(car.position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()

pygame.quit()