from tile import Tile
import numpy as np
import random


class Map:
    def __init__(self, screen, size, rows, columns):
        self.rows = rows
        self.columns = columns
        self.map = np.empty((rows, columns), dtype=object)
        for row in range(0, rows):
            for col in range(0, columns):
                self.map[row, col] = Tile(col * size, row * size, size, screen)

    def update_map(self):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                self.map[row, col].update(self.number_of_alive_neighbours(row, col))

    def number_of_alive_neighbours(self, row, column):
        alive_neighbours = 0

        if row > 0:
            if self.map[row - 1][column].is_alive():
                alive_neighbours += 1
            if column > 0:
                if self.map[row - 1][column - 1].is_alive():
                    alive_neighbours += 1
            if column < self.columns - 1:
                if self.map[row - 1][column + 1].is_alive():
                    alive_neighbours += 1

        if column > 0:
            if self.map[row][column - 1].is_alive():
                alive_neighbours += 1
            if row < self.rows - 1:
                if self.map[row + 1][column - 1].is_alive():
                    alive_neighbours += 1

        if row < self.rows - 1:
            if self.map[row + 1][column].is_alive():
                alive_neighbours += 1

        if column < self.columns - 1:
            if self.map[row][column + 1].is_alive():
                alive_neighbours += 1
            if row < self.rows - 1:
                if self.map[row + 1][column + 1].is_alive():
                    alive_neighbours += 1

        return alive_neighbours

    def draw(self):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                self.map[row, col].draw()

    def set_alive_tile(self, x, y):
        self.map[x][y].resurrect()

    def random_start_map(self, probability_of_alive):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                if random.randint(0, 100) < probability_of_alive:
                    self.map[row, col].resurrect()
                else:
                    self.map[row, col].kill()

        return self

    def reset_map(self):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                self.map[row, col].kill()
