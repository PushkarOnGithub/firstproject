import pygame
import time

pygame.init()    #Initialising pygame functions
#Creating Game window

gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

#Game Specific Variable

game_over = False
game_exit = False

#Creating Game Loop

# while not game_exit:
#     for event in pygame.event.get():
#         print(event)

#Handling Different Events of the Game
"""while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #handling closing of game window
            game_exit = True
        if event.type == pygame.KEYDOWN:   #handling event of pressing a key
            if event.key == pygame.K_RIGHT:   #handling which key is pressed
                print("Finally... You pressed Right key")   # event.key doesn't exist without keydown


pygame.quit()
quit()"""

### Snake Game = continued in file named SnakeGame123.py


