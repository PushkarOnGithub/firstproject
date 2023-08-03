import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
sky = (0, 191, 255)
screen_width = 1080
screen_height = 720
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dice Roller")
run = True
radius = 8
centerx = screen_width/2
centery = screen_height/2
font = pygame.font.SysFont(None, 45)

def text_on_gamewindow(text, color, *coordinates):
    game_window.blit(font.render(text, True, color), coordinates)

def DrawDice1():
        pygame.draw.circle(game_window, green, center = (centerx, centery), radius = radius)

def DrawDice2():
    pygame.draw.circle(game_window, green, center = (centerx-25, centery-25), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx+25, centery+25), radius = radius)

def DrawDice3():
    pygame.draw.circle(game_window, green, center=(centerx-25, centery-25), radius=radius)
    pygame.draw.circle(game_window, green, center = (centerx, centery), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx+25, centery+25), radius = radius)

def DrawDice4():
    pygame.draw.circle(game_window, green, center=(centerx - 25, centery - 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx + 25, centery - 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx - 25, centery + 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx + 25, centery + 25), radius=radius)

def DrawDice5():
    pygame.draw.circle(game_window, green, center=(centerx - 25, centery - 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx + 25, centery - 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx, centery), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx - 25, centery + 25), radius=radius)
    pygame.draw.circle(game_window, green, center=(centerx + 25, centery + 25), radius=radius)

def DrawDice6():
    pygame.draw.circle(game_window, green, center=(centerx-25, centery-20), radius=radius)
    pygame.draw.circle(game_window, green, center = (centerx+25, centery-20), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx-25, centery), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx+25, centery), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx-25, centery+20), radius = radius)
    pygame.draw.circle(game_window, green, center = (centerx+25, centery+20), radius = radius)


List_of_func = [DrawDice1, DrawDice2, DrawDice3, DrawDice4, DrawDice5, DrawDice6]
dice = random.choice(List_of_func)
while run:
    game_window.fill(sky)
    pygame.draw.rect(game_window, black, [centerx-50, centery-50, 100, 100], border_radius=20)
    dice()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice = random.choice(List_of_func)


    pygame.display.update()

