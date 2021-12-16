import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

#LOADING IMAGES
BIRD_IMGS = [pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIPE_IMG = pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
BASE_IMG = pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
BG_IMG = pygame.tranform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
      self.vel = -10.5
      self.tick_count = 0
      self.height = self.y

    def move(self):
        self.tick_count += 1
        #https://youtu.be/ps55secj7iU?t=23