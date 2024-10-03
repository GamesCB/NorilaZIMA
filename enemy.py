import pygame
from random import randint
from settings import *

pygame.init()
from pygame.locals import *

class Dogs():
    def __init__(self):
        self.dog = pygame.image.load('image/dogs/idle_dog.png').convert_alpha() # texture dog
        self.walk_anim = Animation([pygame.image.load(f'image/dogs/animation/walk/{i}.png').convert_alpha() for i in range(1, 7)], 4)
        self.health_dog = 100
        self.attack_anim = None
        self.damage_dog = 0.05
        self.radius = 600
        # self.rect_dog = Rect(randint(1,10000), randint(1600, 5000), self.dog.get_width(), self.dog.get_height())
        self.rect_dog = Rect(randint(0, 19000), randint(700, 7000), 120, 60)
        self.player_rect = Rect(500,1500, 96, 174)

        self.wait_walk = 200
        self.walk_time = 1000
        self.speed = 5
        self.change_side = 500
        self.tex = pygame.image.load('image/player/character.png').convert_alpha()
        self.watch_icon = pygame.image.load('image/icons/see_icon.png').convert_alpha()
        self.walk_count_x = randint(1, 2)
        self.walk_count_y = randint(1, 2)
        self.health = 200

    def attack(self, health):

        health -= self.damage_dog
        self.health = health

        return self.health

    def search_and_walk(self, x_p, y_p, health=200):

        self.health = health
        if self.rect_dog.x in range(x_p - 1280, x_p + 1280) and self.rect_dog.y in range(y_p - 720, y_p + 720):
            self.walk_anim.show_anim(self.rect_dog.x, self.rect_dog.y)

        if self.walk(x_p, y_p, self.health):
            self.search(x_p, y_p, self.health)

        return self.health







    def walk(self, x, y, health):

        self.health = health
        if self.rect_dog.x in range(-200, 20283) and self.rect_dog.y in range(500, 8130):
            if self.walk_time > 0:

                if self.change_side > 0:
                    if self.walk_count_x == 1:
                        self.rect_dog.x += self.speed
                    else:
                        self.rect_dog.x -= self.speed

                    if self.walk_count_y == 1:
                        self.rect_dog.y += self.speed
                    else:
                        self.rect_dog.y -= self.speed

                    self.change_side -= 1
                else:
                    self.change_side = 500



                self.wait_walk = 200
                self.walk_time -= 1


                return self.health

            else:
                self.wait_walk -= 1
                if self.wait_walk == 0:
                    self.walk_time = 1000

                return self.health

        else:
            self.rect_dog.x = x - 1280
            self.rect_dog.y = y + 720

        return self.health



    def search(self, x_p, y_p, health):

        if x_p in range(self.rect_dog.x - self.radius - 100, self.rect_dog.x + self.radius) and y_p in range(self.rect_dog.y - 100 - self.radius,
                                                                                                       self.rect_dog.y + self.radius):
            if x_p < self.rect_dog.x:
                self.rect_dog.x -= self.speed + 4
            else:
                self.rect_dog.x += self.speed + 4

            if y_p - 300 < self.rect_dog.y:
                self.rect_dog.y -= self.speed + 4
            else:
                self.rect_dog.y += self.speed + 4

            window.blit(self.watch_icon, (54, 135))

            self.attack(self.health)

        return self.health

