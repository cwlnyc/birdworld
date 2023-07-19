import pygame

class Rocket(pygame.sprite.Sprite):
    image = pygame.image.load('resources/rocket_left.png')
    starting_pos = (-300, 100)
    size = (60, 30)
    screen_dim = (600, 500)
    move_dist = 3

    def __init__(self, starting_pos: tuple, direction: str):
        super().__init__()
        self.image = Rocket.image
        self.rect = pygame.Rect((0, 0), Rocket.size)
        self.rect.center = Rocket.starting_pos
        self.direction = direction

    def move(self):
        self.rect.centerx -= Rocket.move_dist
        if self.direction == 'Left':
            self.rect.centerx -= Rocket.move_dist

            if self.rect.right <= 0:
                self.rect.centerx = Rocket.screen_dim[0] + (Rocket.size[0]/2)

        else:
            self.rect.centerx += Rocket.move_dist

            if self.rect.left >= Rocket.screen_dim[0]:
                self.rect.centerx = -Rocket.size[0]/2