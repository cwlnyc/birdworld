import pygame
class Balloon(pygame.sprite.Sprite):
    image = pygame.image.load('resources/balloon.png')
    starting_pos = (300, 250)
    size = (60, 30)

    screen_dim = 600, 500
    move_dist = 5

    def __init__(self, starting_pos: tuple, direction: str):
        super().__init__()
        self.image = Balloon.image
        self.rect = pygame.Rect((0, 0), Balloon.size)
        self.rect.center = starting_pos
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Balloon.move_dist

            if self.rect.right <= 0:
                self.rect.centerx = Balloon.screen_dim[0] + (Balloon.size[0]/2)

        else:
            self.rect.centerx += Balloon.move_dist

            if self.rect.left >= Balloon.screen_dim[0]:
                self.rect.centerx = -Balloon.size[0]/2