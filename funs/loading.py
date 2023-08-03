import pygame
from math import sin
from math import cos
from time import sleep

white = (255, 255, 255)
black = (0, 0, 0)

screen_width = 1080/2
screen_height = 720/2
center = (screen_width/2, screen_height/2)
radius_circle = 100
radius = 3
t = 0
game_window = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Still Loading")

run = True
while(run):
    game_window.fill(white)

    # sleep(0.001)
    t += 0.003
    pygame.draw.circle(game_window, black, (center[0], center[1]), 2)
    # pygame.draw.circle(game_window, black, (center[0]+(radius_circle)*sin(t), center[1] + (radius_circle)*cos(t)), radius)
    for i in range(50):
        pygame.draw.circle(game_window, black, (center[0]+(radius_circle)*sin(t-0.02*i), center[1] + (radius_circle)*cos(t-0.02*i)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()


if __name__ == __main__:
    pass