import pygame


class Tile:
    COLOR_ALIVE = (200, 200, 200)
    COLOR_DEAD = (0, 0, 0)

    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.alive = False
        self.alive_future = False
        self.screen = screen

    def update(self, alive_neighbours):
        if self.alive:
            if alive_neighbours == 2 or alive_neighbours == 3:
                self.alive_future = True
            else:
                self.alive_future = False
        else:
            if alive_neighbours == 3:
                self.alive_future = True
            else:
                self.alive_future = False

    def draw(self):
        if self.alive_future:
            self.alive = True
            color = self.COLOR_ALIVE
        else:
            self.alive = False
            color = self.COLOR_DEAD

        pygame.draw.rect(self.screen, color, (self.x, self.y, self.size, self.size), 0)

    def kill(self):
        self.alive = False

    def resurrect(self):
        self.alive = True

    def is_alive(self):
        return self.alive
