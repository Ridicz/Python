import pygame
from setups import Setup
from menu import Menu


def input_handler(input_key):
    global game_speed
    global game_map
    global probability_of_alive

    if input_key == 27:
        return False
    elif key == 273:
        game_speed += 1
    elif key == 274:
        game_speed -= 1
    elif key == 50:
        settings = menu.display_menu(screen)
        game_map = settings["Map"]
        game_speed = settings["Speed"]
        probability_of_alive = settings["Probability"]

    return True


TILE_SIZE = 10
ROWS = 70
COLUMNS = 120

pygame.init()
screen = pygame.display.set_mode((COLUMNS * TILE_SIZE, ROWS * TILE_SIZE))
clock = pygame.time.Clock()

setup = Setup(screen, TILE_SIZE, ROWS, COLUMNS)

loop = True

menu = Menu(screen, TILE_SIZE, ROWS, COLUMNS)
settings = menu.display_menu(screen)

game_map = settings["Map"]
game_speed = settings["Speed"]
probability_of_alive = settings["Probability"]

while loop:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        key = event.dict["key"]
        loop = input_handler(key)

    pygame.display.set_caption("Game speed: " + str(game_speed) + " FPS")
    clock.tick(game_speed)
    pygame.display.update()
    game_map.update_map()
    game_map.draw()

pygame.quit()
