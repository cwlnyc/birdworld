import pygame

class Airplane(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/airplane.png')
    STARTING_POSITION = (300, 150)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 5

    # Creates a Log object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Airplane.IMAGE
        # Log Information
        self.rect = pygame.Rect((0, 0), Airplane.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Log is going left
        if self.direction == 'Left':
            self.rect.centerx -= Airplane.MOVE_DIST
            # Log has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Airplane.SCREEN_DIM[0] + Airplane.SIZE[0] / 2
        # Log is going right
        else:
            self.rect.centerx += Airplane.MOVE_DIST
            # Log has moved off the screen
            if self.rect.left >= Airplane.SCREEN_DIM[0]:
                self.rect.centerx = -Airplane.SIZE[0] / 2