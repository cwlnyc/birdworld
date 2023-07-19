import pygame, sys
import random
from bird import Bird
from airplane import Airplane
from rocket import Rocket
from meso import Meso

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
# setting up pygame :)
screen_dim = width, height = 600, 500
screen = pygame.display.set_mode(screen_dim)
pygame.display.set_caption('Bird World')

clock = pygame.time.Clock()

fps = 60

moving_up = False
moving_down = False
moving_left = False
moving_right = False

#colors yay
black = (0, 0, 0)
white = (255, 255, 255)
green = (59, 150, 65)
yellow = (248, 249, 73)
brown = (60, 36, 6)
gray = (175, 175, 175)
blue = (137, 185, 226)

bird = Bird()
airplane = Airplane(Airplane.STARTING_POSITION, 'Right')
rocket = Rocket(Rocket.starting_pos, 'Left')

#add the mesosphere BABYYYYY
mesos = []

number_of_balloons = 3
meso_width = 500  # Adjust this value to set the width of the big mesosphere
meso_height = 300  # Adjust this value to set the height of the big mesosphere
number_balloons_per_row = 3
num_rows = 3

big_meso = Meso(meso_height, 'Right', number_balloons_per_row, num_rows)
for _ in range(number_of_balloons):
    big_meso.add_balloons('Left', number_of_balloons, meso_height, num_rows)

#game loop
 # Create an instance of the Bird class

# Game loop
while True:
    clock.tick(fps)
    screen.fill(blue)

    pygame.draw.rect(screen, gray, big_meso.rect)
    # Draw the balloons inside the big mesosphere
    for balloon in big_meso.balloons:
        screen.blit(balloon.image, balloon.rect)
        if bird.rect.colliderect(balloon.rect):
            bird.reset_position()
        balloon.move()

    screen.blit(bird.image, bird.rect)  # Draw the bird
    screen.blit(airplane.image, airplane.rect)  # Draw the airplane
    screen.blit(rocket.image, rocket.rect)  # Draw the rocket

    airplane.move()  # Move the airplane
    rocket.move()  # Move the rocket

    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_q:  # Add this here
                pygame.quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_d:
                moving_right = False


    for event in pygame.event.get():
        if event.key == pygame.K_q:
            pygame.quit()

    # Move the bird based on movement state
    if moving_up:
        bird.move_up()
    if moving_down:
        bird.move_down()
    if moving_left:
        bird.move_left()
    if moving_right:
        bird.move_right()

    if bird.rect.colliderect(airplane.rect):
        bird.move_on_airplane(airplane)

    if bird.rect.colliderect(rocket.rect):
        bird.reset_position()

pygame.quit()
sys.exit()
