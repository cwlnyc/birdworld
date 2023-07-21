import pygame
from airplane import Airplane

class Bird(pygame.sprite.Sprite):
    starting_position = (300, 490)
    size = (20, 10)
    image = [pygame.image.load('./resources/tile000.png'), pygame.image.load('./resources/tile001.png')]

    move_dist = 10
    screen_dim = 600, 500


    def __init__(self):
        super().__init__()
        self.frames = Bird.image
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = pygame.Rect((0, 0), Bird.size)
        self.rect.center = Bird.starting_position
        self.lives = 1
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= 10:  # Update every 10th frame
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # Cycle through the frames
            self.image = self.frames[self.current_frame]  # Update the image

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Bird.move_dist

    def move_down(self):
        if self.rect.bottom <= Bird.screen_dim[1] - 20:
            self.rect.centery += Bird.move_dist

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Bird.move_dist


    def move_right(self):
        if self.rect.right <= Bird.screen_dim[1] - 20:
            self.rect.centerx += Bird.move_dist

    def reset_position(self):
        self.rect.center = Bird.starting_position
        self.lives -= 1

    def move_on_airplane(self, airplane: Airplane):
        # Airplane moving right
        if airplane.direction == 'Right':
            self.rect.centerx += Airplane.MOVE_DIST
            #bird has moved off screen
            if self.rect.left >= Airplane.SCREEN_DIM[0]:
                diff = airplane.rect.right - self.rect.centerx
                self.rect.centerx = -diff
        #airplane moving left
        else:
            self.rect.centerx -= Airplane.MOVE_DIST
            #Bird has moved off screen
            if self.rect.right <= 0:
                diff = abs(airplane.rect.left - self.rect.centerx)
                self.rect.centerx = Airplane.SCREEN_DIM[0] + diff