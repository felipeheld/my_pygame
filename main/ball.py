#!/usr/bin/env python3

# imports #
import pygame
# imports #

class Ball:

    def __init__(self, screen, color, position, radius):
        self.screen = screen
        self.color = color
        self.position = position
        self.radius = radius

    def change_color(self, color):
        self.color = change_color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)
