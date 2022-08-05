import pygame
import sys
import snake
import food
import score
from pygame.locals import *

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)
GREEN = pygame.Color(0, 255, 0)
span = 10

pygame.init()


def main():
    level = 1
    myscore = 0
    count = 0
    score_ttf = pygame.font.Font("ttf/ziti.TTF", 40)
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('贪吃蛇')

    play = pygame.Surface(screen.get_size())
    play = play.convert()
    play.fill((255, 255, 255))

    my_snake = snake.Snake()
    new_food = food.Food()
    new_food.appear()

    draw_snake(play, my_snake.body)
    pygame.display.update()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and my_snake.direction != "DOWN":
                    my_snake.direction = "UP"
                elif (event.key == K_DOWN or event.key == K_s) and my_snake.direction != "UP":
                    my_snake.direction = "DOWN"
                elif (event.key == K_LEFT or event.key == K_a) and my_snake.direction != "RIGHT":
                    my_snake.direction = "LEFT"
                elif (event.key == K_RIGHT or event.key == K_d) and my_snake.direction != "LEFT":
                    my_snake.direction = "RIGHT"
            else:
                my_snake.move()
                if [new_food.get_x(), new_food.get_y()] in my_snake.body:
                    new_food.appear()
                    my_snake.living()
                    myscore += level
                    count += 1
                    level = count // 10 + 1
                    my_snake.speed = my_snake.speed * level
                else:
                    my_snake.body.pop()
                    my_snake.living()
                play.fill(WHITE)
                draw_snake(play, my_snake.body)
                pygame.draw.rect(play, RED, (new_food.get_x(), new_food.get_y(), span, span))
                if not my_snake.active:
                    running = False

        if not running:
            game_over(myscore)
            pygame.quit()
            sys.exit()

        score_text = score_ttf.render("Score: %s" % str(myscore), True, BLACK)
        play.blit(score_text, (0, 0))

        screen.blit(play, (0, 0))
        pygame.display.flip()
        clock.tick(15)


def draw_snake(pic, the_list):
    long = len(the_list)
    for i in range(long):
        pygame.draw.rect(pic, GREEN, (the_list[i][0], the_list[i][1], span, span))


def game_over(s):
    my_score = score.Score()
    my_score.write_out()
    my_score.append_score(s)
    print(my_score)
    my_score.write_in()


if __name__ == "__main__":
    main()
