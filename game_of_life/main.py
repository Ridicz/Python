import pygame
from setups import Setup
from map import Map


def input_handler(input_key):
    global game_speed
    global game_map

    if input_key == 27:
        return False
    elif key == 273:
        game_speed += 1
    elif key == 274:
        game_speed -= 1
    elif key == 275:
        game_map = setup.create_gosper_glider_gun(0, 0)
    elif key == 276:
        game_map.random_start_map(65)

    return True


TILE_SIZE = 10
ROWS = 70
COLUMNS = 100

pygame.init()
screen = pygame.display.set_mode((COLUMNS * TILE_SIZE, ROWS * TILE_SIZE))
clock = pygame.time.Clock()

game_map = Map(screen, TILE_SIZE, ROWS, COLUMNS)
game_map.random_start_map(60)

setup = Setup(screen, TILE_SIZE, ROWS, COLUMNS)

# game_map = setup.create_gosper_glider_gun(0, 0)

game_speed = 5
loop = True

while loop:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        key = event.dict["key"]
        loop = input_handler(key)

    pygame.display.set_caption("Game speed: " + str(game_speed) + "fps")
    clock.tick(game_speed)
    pygame.display.update()
    game_map.update_map()
    game_map.draw()

pygame.quit()
