import random
import pygame
from balloon import Balloon

class Meso:
    size = (600, 150)
    screen_dim = 600, 500

    def __init__(self, meso_height:int, direction: str,
                 number_of_balloons: int, num_rows: int):
        self.rect = pygame.Rect((0, meso_height), Meso.size)
        self.balloons = []
        self.add_balloons(direction, number_of_balloons, meso_height, num_rows)

    def add_balloons(self, direction: str, number_of_balloons: int, meso_height: int, num_rows: int):
        dp = []
        for row in range(num_rows):
            for _ in range(number_of_balloons):
                while True:
                    x_pos = random.randint(30, 570)
                    valid = True
                    for i in range(x_pos - 60, x_pos + 61):
                        if i in dp:
                            valid = False
                    if valid:
                        dp.extend(range(x_pos - 60, x_pos + 61))
                        self.balloons.append(Balloon((x_pos, meso_height + row * 50), direction))
                        break