import pygame
from setups import Setup


class Menu:
    def __init__(self, screen, tile_size, rows, columns):
        self.probability_of_alive = 50
        self.starting_game_speed = 5
        self.setup = Setup(screen, tile_size, rows, columns)
        self.starting_map = None

    def display_menu(self, screen):
        loop = True

        grey_color = (200, 200, 200)

        font = pygame.font.SysFont("Courier", 28)
        text = font.render("Press Enter to start simulation with random values.", True, grey_color)
        text_game_speed = font.render(
            "Starting game speed: {0} FPS (Up and Down)".format(str(self.starting_game_speed)), True, grey_color)
        text_probability = font.render(
            "Probability of alive cell: {0}% (Left and Right)".format(str(self.probability_of_alive)), True,
            grey_color)
        text_random = font.render("Press '1' to spawn a Gosper Glider Gun.", True, grey_color)
        text_menu = font.render("Press '2' anytime to break and show menu.", True, grey_color)

        while loop:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                key = event.dict["key"]
                loop = self.input_handler(key)
                text_game_speed = font.render(
                    "Starting game speed: {0} FPS (Up and Down)".format(str(self.starting_game_speed)), True,
                    (200, 200, 200))
                text_probability = font.render(
                    "Probability of alive cell: {0}% (Left and Right)".format(str(self.probability_of_alive)), True,
                    (200, 200, 200))

            screen.fill((0, 0, 0))
            screen.blit(text, (150, 200))
            screen.blit(text_game_speed, (150, 250))
            screen.blit(text_probability, (150, 300))
            screen.blit(text_random, (150, 350))
            screen.blit(text_menu, (150, 400))
            pygame.display.flip()

        return {"Map": self.starting_map, "Speed": self.starting_game_speed, "Probability": self.probability_of_alive}

    def input_handler(self, input_key):
        if input_key == 27:
            return False
        elif input_key == 273:
            self.starting_game_speed += 1
        elif input_key == 274:
            if self.starting_game_speed > 1:
                self.starting_game_speed -= 1
        elif input_key == 275:
            self.probability_of_alive += 1
        elif input_key == 276:
            self.probability_of_alive -= 1
        elif input_key == 49:
            self.starting_map = self.setup.create_gosper_glider_gun(0, 0)
            return False
        elif input_key == 13:
            self.starting_map = self.setup.create_random_start_map(self.probability_of_alive)
            return False

        return True
