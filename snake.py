import pygame

span = 10


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.body = [[300, 500], [300, 500+span], [300, 500+2*span]]
        self.speed = span
        self.direction = "UP"
        self.length = len(self.body)
        self.active = True

    def get_body(self):
        self.tubody = []
        for i in range(self.length):
            self.tubody.append(tuple(self.body[i]))
        tuple_body = tuple(self.tubody)
        return tuple_body

    def up(self):
        if self.body[0][1] > 0:
            self.body.insert(0, [self.body[0][0], self.body[0][1]-span])
        else:
            self.active = False

    def down(self):
        if self.body[0][1] < 600:
            self.body.insert(0, [self.body[0][0], self.body[0][1]+span])
        else:
            self.active = False

    def right(self):
        if self.body[0][0] < 600:
            self.body.insert(0, [self.body[0][0]+span, self.body[0][1]])
        else:
            self.active = False

    def left(self):
        if self.body[0][0] > 0:
            self.body.insert(0, [self.body[0][0]-span, self.body[0][1]])
        else:
            self.active = False

    def move(self):
        count = self.speed//span
        while count >= 1:
            if self.direction == "UP":
                self.up()
            elif self.direction == "DOWN":
                self.down()
            elif self.direction == "RIGHT":
                self.right()
            elif self.direction == "LEFT":
                self.left()
            if count > 1:
                self.body.pop()
            count -= 1

    def living(self):
        if self.body[0] in self.body[1:]:
            self.active = False

