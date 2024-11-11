import pygame
import math 
import numpy as np
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen_Width = 950
screen_Height = 950

screen = pygame.display.set_mode((screen_Width, screen_Height))
pygame.display.set_caption("Bouncing Ball")

circle_radius = 450
circle_center = np.array((screen_Width // 2, screen_Height // 2), float)

ball_radius = 15
ball_color = BLUE
ball_pos = np.array(circle_center)
ball_vel = np.array([random.choice([-2, 2]), random.choice([-2, 2])], float)



