from map import Map


class Setup:
    def __init__(self, screen, tile_size, rows, columns):
        self.screen = screen
        self.tile_size = tile_size
        self.rows = rows
        self.columns = columns

    def create_gosper_glider_gun(self, offset_x, offset_y):
        game_map = Map(self.screen, self.tile_size, self.rows, self.columns)
        game_map.set_alive_tile(0, 24)
        game_map.set_alive_tile(1, 22)
        game_map.set_alive_tile(1, 24)
        game_map.set_alive_tile(2, 12)
        game_map.set_alive_tile(2, 13)
        game_map.set_alive_tile(2, 20)
        game_map.set_alive_tile(2, 21)
        game_map.set_alive_tile(2, 34)
        game_map.set_alive_tile(2, 35)
        game_map.set_alive_tile(3, 11)
        game_map.set_alive_tile(3, 15)
        game_map.set_alive_tile(3, 20)
        game_map.set_alive_tile(3, 21)
        game_map.set_alive_tile(3, 34)
        game_map.set_alive_tile(3, 35)
        game_map.set_alive_tile(4, 0)
        game_map.set_alive_tile(4, 1)
        game_map.set_alive_tile(4, 10)
        game_map.set_alive_tile(4, 16)
        game_map.set_alive_tile(4, 20)
        game_map.set_alive_tile(4, 21)
        game_map.set_alive_tile(5, 0)
        game_map.set_alive_tile(5, 1)
        game_map.set_alive_tile(5, 10)
        game_map.set_alive_tile(5, 14)
        game_map.set_alive_tile(5, 16)
        game_map.set_alive_tile(5, 17)
        game_map.set_alive_tile(5, 22)
        game_map.set_alive_tile(5, 24)
        game_map.set_alive_tile(6, 10)
        game_map.set_alive_tile(6, 16)
        game_map.set_alive_tile(6, 24)
        game_map.set_alive_tile(7, 11)
        game_map.set_alive_tile(7, 15)
        game_map.set_alive_tile(8, 12)
        game_map.set_alive_tile(8, 13)

        return game_map
