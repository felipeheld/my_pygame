#!/usr/bin/env python3

# imports #
import pygame
# imports #

class Rectangle:

    number_rectangles = 0

    def __init__(self, screen, color, area, hit_points = 100):
        self.screen = screen
        self.color = color
        self.area = area
        self.hit_points = hit_points

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.area)
