import pygame
import random
span = 10


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.food_pos = []

    def appear(self):
        x = int(random.randint(2, (600-span*2)/span)*span)
        y = int(random.randint(2, (600-span*2)/span)*span)
        self.food_pos = [x, y]

    def get_x(self):
        return self.food_pos[0]

    def get_y(self):
        return self.food_pos[1]

