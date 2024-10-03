import pygame
from random import randint
from settings import *

pygame.init()

class Snowflake():
    def __init__(self):
        self.texture = pygame.image.load('image/icons/snowflake.png').convert_alpha()
        self.x = randint(50, 1800)
        self.y = -randint(self.texture.get_height(), 400)
        self.texture.set_alpha(150)
        self.speed = randint(2, 6)

    def render_snowflake(self):

        self.x -= self.speed
        self.y += self.speed
        if self.y > 720:
            self.y = -self.texture.get_height()
            self.x = randint(50, 1800)

        window.blit(self.texture, (self.x, self.y))

class Flakes():
    def __init__(self):
        self.list_flakes = [Snowflake() for i in range(25)]
        # self.snow1 = Snowflake()
        # self.snow2 = Snowflake()
        # self.snow3 = Snowflake()
        # self.snow4 = Snowflake()
        # self.snow5 = Snowflake()
        # self.snow6 = Snowflake()
        # self.snow7 = Snowflake()
        # self.snow8 = Snowflake()
        # self.snow9 = Snowflake()
        # self.snow10 = Snowflake()
        # self.snow11 = Snowflake()
        # self.snow12 = Snowflake()
        # self.snow13 = Snowflake()
        # self.snow14 = Snowflake()
        # self.snow15 = Snowflake()

    def render_flakes(self):
        # self.snow1.render_snowflake()
        # self.snow11.render_snowflake()
        # self.snow2.render_snowflake()
        # self.snow12.render_snowflake()
        # self.snow3.render_snowflake()
        # self.snow13.render_snowflake()
        # self.snow4.render_snowflake()
        # self.snow14.render_snowflake()
        # self.snow5.render_snowflake()
        # self.snow15.render_snowflake()
        # self.snow6.render_snowflake()
        # self.snow7.render_snowflake()
        # self.snow8.render_snowflake()
        # self.snow9.render_snowflake()
        # self.snow10.render_snowflake()
        for flake in self.list_flakes:
            flake.render_snowflake()
