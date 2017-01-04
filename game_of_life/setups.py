from map import Map


class Setup:
    def __init__(self, screen, tile_size, rows, columns):
        self.game_map = Map(screen, tile_size, rows, columns)

    def create_random_start_map(self, probability_of_alive):
        return self.game_map.random_start_map(probability_of_alive)

    def create_gosper_glider_gun(self, offset_x, offset_y):
        self.game_map.reset_map()

        self.game_map.set_alive_tile(0, 24)
        self.game_map.set_alive_tile(1, 22)
        self.game_map.set_alive_tile(1, 24)
        self.game_map.set_alive_tile(2, 12)
        self.game_map.set_alive_tile(2, 13)
        self.game_map.set_alive_tile(2, 20)
        self.game_map.set_alive_tile(2, 21)
        self.game_map.set_alive_tile(2, 34)
        self.game_map.set_alive_tile(2, 35)
        self.game_map.set_alive_tile(3, 11)
        self.game_map.set_alive_tile(3, 15)
        self.game_map.set_alive_tile(3, 20)
        self.game_map.set_alive_tile(3, 21)
        self.game_map.set_alive_tile(3, 34)
        self.game_map.set_alive_tile(3, 35)
        self.game_map.set_alive_tile(4, 0)
        self.game_map.set_alive_tile(4, 1)
        self.game_map.set_alive_tile(4, 10)
        self.game_map.set_alive_tile(4, 16)
        self.game_map.set_alive_tile(4, 20)
        self.game_map.set_alive_tile(4, 21)
        self.game_map.set_alive_tile(5, 0)
        self.game_map.set_alive_tile(5, 1)
        self.game_map.set_alive_tile(5, 10)
        self.game_map.set_alive_tile(5, 14)
        self.game_map.set_alive_tile(5, 16)
        self.game_map.set_alive_tile(5, 17)
        self.game_map.set_alive_tile(5, 22)
        self.game_map.set_alive_tile(5, 24)
        self.game_map.set_alive_tile(6, 10)
        self.game_map.set_alive_tile(6, 16)
        self.game_map.set_alive_tile(6, 24)
        self.game_map.set_alive_tile(7, 11)
        self.game_map.set_alive_tile(7, 15)
        self.game_map.set_alive_tile(8, 12)
        self.game_map.set_alive_tile(8, 13)

        return self.game_map
