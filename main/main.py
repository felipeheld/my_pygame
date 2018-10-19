#!/usr/bin/env python3

# imports #
import pygame
from ball import Ball
from rectangle import Rectangle
# imports #

pygame.init()

# variables #
screen_width, screen_height = screen_size = 800, 600
screen        = pygame.display.set_mode(screen_size)
clock         = pygame.time.Clock()
# variables #

# game object variables #
ball = Ball(screen, color = (150, 200, 0), position = [400, 300], radius = 10)
one_rectangle = Rectangle(screen, color = (231, 43, 120), area = (40, 40, 40, 30))

pos_x_rect, pos_y_rect, rect_width, rect_height = one_rectangle.area
left_side = [[pos_x_rect, y] for y in range(pos_y_rect, pos_y_rect + rect_height + 1)]
right_side = [[pos_x_rect + rect_width, y] for y in range(pos_y_rect, pos_y_rect + rect_height + 1)]
top_side = [[x, pos_y_rect] for x in range(pos_x_rect, pos_x_rect + rect_width + 1)]
bottom_side = [[x, pos_y_rect + rect_height] for x in range(pos_x_rect + rect_width + 1)]
# game object variables #
print(left_side)
print(right_side)
# session variables #
mov_x, mov_y = 1, 1
# session variables #
pygame.display.set_caption('Hello there')

# TESTING VARIABLES #

# TESTING VARIABLES #

# main game loop #
while True:
    pygame.Surface.fill(screen, (0, 0, 0))

    ball.draw()
    one_rectangle.draw()

    # ball movement
    pos_x_circle, pos_y_circle = ball.position
    pos_x_circle, pos_y_circle = pos_x_circle + mov_x, pos_y_circle + mov_y
    ball.position = pos_x_circle, pos_y_circle

    if [ball.position[0] - ball.radius, ball.position[1]] in right_side:
        mov_x = 1
    if [ball.position[0], ball.position[1] - ball.radius] in bottom_side:
        mov_y = 1

    if pos_x_circle + ball.radius >= screen_width:
        mov_x = -1
    elif pos_x_circle - ball.radius <= 0:
        mov_x = 1
    if pos_y_circle + ball.radius >= screen_height:
        mov_y = -1
    elif pos_y_circle - ball.radius <= 0:
        mov_y = 1
    # ball movement

    # ball collision
    # ball collision

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(450)
    pygame.display.flip()
# main game loop #
