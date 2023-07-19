import random
import pygame
from balloon import Balloon

class Meso:
    size = (600, 150)
    screen_dim = 600, 500

    def __init__(self, meso_height:int, direction: str, number_of_balloons: int, number_of_rows: int):
        print(f"I'm now creating a new instanxce of Meso and the number of rows is {number_of_rows}")
        self.rect = pygame.Rect((0, meso_height), Meso.size)
        self.balloons = []
#        self.add_balloons(direction, number_of_balloons, meso_height, number_of_rows)

    def add_balloons(self, direction: str, number_of_balloons: int, meso_height: int, number_of_rows: int):
        for row in range(number_of_rows):
            dp = []
            print(f"Row number is {row}")
            attempts = 0
            while len(dp) < number_of_balloons and attempts < 100:
                x_pos = random.randint(10, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 61):
                    if i in dp:
                        valid = False
                if valid:
                    print(f"Row number is {row}")
                    dp.extend(range(x_pos - 60, x_pos + 61))
                    height = meso_height + row * 50
                    print(height)
                    self.balloons.append(Balloon((x_pos, height), direction))
                attempts += 1


