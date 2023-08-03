import pygame, random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
run = True
x_upper = 1920
x_lower = 0
y_upper = 1080
y_lower = 0
size = 2
game_window = pygame.display.set_mode((1550, 815))
pygame.display.set_caption("Blank TV")

while(run):
    game_window.fill(white)
    for i in range(10000):
        pygame.draw.circle(game_window, black, (random.randint(x_lower, x_upper), random.randint(y_lower, y_upper)), size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()


