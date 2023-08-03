import pygame
import random
import os

pygame.init()

# Colours
white = (255, 255, 255)
sky = (0, 191, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Creating Game Screen
screen_width = 1080
screen_height = 720
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hungry Snake")
pygame.display.update()   # if any changes made to the window we have to update it
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 45)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])


def plot_snake(gamewindow,color,list,snake_size):
    for x,y in list:
        pygame.draw.rect(gamewindow,color,[x, y,snake_size,snake_size])

def welcome():
    rungame = True
    while rungame:
        game_window.fill((230,230,230))
        text_screen("Welcome to Snakes",sky,350,300)
        text_screen("Press Spcae Bar to Play",sky,350,330)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rungame = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)


def gameloop():
    # Game specific variables
    run_game = True
    game_over = False

    snake_x = random.randint(10, screen_width - 10)
    snake_y = random.randint(10, screen_height - 10)

    snake_x2 = random.randint(10, screen_width - 10)
    snake_y2 = random.randint(10, screen_height - 10)

    snake_size = 20
    snake_size2 = 20

    fps = 30

    v_x = 0
    v_y = 0

    v_x2 = 0
    v_y2 = 0

    foodx, foody = random.randint(20, screen_width - 20), random.randint(20, screen_height - 20)

    score = 0

    score2 = 0

    snake_list = []
    snake_length = 1

    snake_list2 = []
    snake_length2 = 1

    chance = 0
    chance2 = 0

    # if (not os.path.exists("highscore.txt")):
    #     with open("highscore.txt","w") as hs:
    #         hs.write(str(0))
    # with open("highscore.txt","r") as hs:
    #     highscore = hs.read()

    # Game Loop
    while run_game:

        if game_over:
            game_window.fill(white)
            if score2 < score:
                text_screen("Green Won!!", green, screen_width-900, screen_height/2-50)
            elif score2 > score:
                text_screen("Red Won!!", red, screen_width-900, screen_height/2-50)
            elif score2 == score:
                text_screen("Its A Tie!!", black, screen_width - 900, screen_height / 2 - 50)
            text_screen("Game Over!! Press SpaceBar to continue, ESC to quit.", sky, screen_width-900,screen_height/2)
            # with open("highscore.txt","w") as hs:
            #     hs.write(str(highscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_game = False
                    elif event.key == pygame.K_SPACE :
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and v_x == 0:
                        v_x += 10
                        v_y = 0
                    if event.key == pygame.K_LEFT and v_x == 0:
                        v_x += -10
                        v_y = 0
                    if event.key == pygame.K_UP and v_y == 0:
                        v_y += - 10
                        v_x = 0
                    if event.key == pygame.K_DOWN and v_y == 0:
                        v_y += + 10
                        v_x = 0
                    if event.key == pygame.K_d and v_x2 == 0:
                        v_x2 += 10
                        v_y2 = 0
                    if event.key == pygame.K_a and v_x2 == 0:
                        v_x2 += -10
                        v_y2 = 0
                    if event.key == pygame.K_w and v_y2 == 0:
                        v_y2 += - 10
                        v_x2 = 0
                    if event.key == pygame.K_s and v_y2 == 0:
                        v_y2 += + 10
                        v_x2 = 0

            snake_x = snake_x + v_x
            snake_y = snake_y + v_y

            snake_x2 = snake_x2 + v_x2
            snake_y2 = snake_y2 + v_y2
            game_window.fill(black)   # fill the window with the RGB color code given in a tuple

            # pygame.draw.rect(game_window, green, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.circle(game_window, yellow, center=(foodx, foody), radius=5)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if snake_x<0 or snake_y<0 or snake_x>screen_width or snake_y>screen_height:
                chance = chance - 1
                game_over = True

            if head in snake_list[:-1]:
                game_over = True

            head2 = []
            head2.append(snake_x2)
            head2.append(snake_y2)
            snake_list2.append(head2)

            if len(snake_list2) > snake_length2:
                del snake_list2[0]

            if snake_x2 < 0 or snake_y2 < 0 or snake_x2 > screen_width or snake_y2 > screen_height:
                chance2 = chance2 - 1
                game_over = True

            if head2 in snake_list2[:-1]:
                game_over = True

            plot_snake(game_window,green,snake_list,snake_size)

            plot_snake(game_window, red, snake_list2, snake_size2)

            if abs(snake_x-foodx) < 15 and abs(snake_y-foody) < 15:
                score += 10
                snake_length = snake_length + 3
                # if score > int(highscore):
                #     highscore = score
                foodx, foody = random.randint(20, screen_width - 20), random.randint(20, screen_height - 20)

            if abs(snake_x2 - foodx) < 15 and abs(snake_y2 - foody) < 15:
                score2 += 10
                snake_length2 = snake_length2 + 3
                foodx, foody = random.randint(20, screen_width - 20), random.randint(20, screen_height - 20)

            # text_screen("Score: " + str(score)+"   Highscore :"+str(highscore), white, 10, 10)
            text_screen("Score: "+ str(score), green, 10, 10)
            text_screen("Score: "+ str(score2), red, 900, 10)
            game_window.blit(pygame.font.SysFont(None,25).render("snake",True,red),[screen_width-60,screen_height-20])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()