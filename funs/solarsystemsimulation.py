import pygame
# import math
pygame.init()

width, height = 800, 800
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System")

run = True
fps = 60
radius = 20
clock = pygame.time.Clock()


class Planet:
    AU = 149.6e6 * 1000
    G = 6.6742e-11
    scale = 250/AU
    timestep = 3600*24
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []
        self.x_vel = 0
        self.u_vel = 0

    def draw(self, win):
        x = self.x * self.scale + width/2
        y = self.y * self.scale + height/2
        pygame.draw.circle(window, self.color, (x, y), self.radius)
        pygame.draw.circle(win, )


Sun = Planet(0, 0, 30, yellow, 1.98892e30)
Sun.sun = True

planets = [Sun]
while run:
    clock.tick(fps)
    window.fill(white)
    pygame.draw.circle(window, black, (200, 200), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        for planet in planets:
            pygame.draw(window)

    pygame.display.update()
