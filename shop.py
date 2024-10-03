import pygame
pygame.init()
from pygame.locals import *
from settings import *

class Shop():
    def __init__(self):
        self.window_shop = pygame.image.load('image/windows/shop.png').convert_alpha()
        self.text_40 = pygame.font.Font('font/rus-pixel.ttf', 40)
        self.cost_water = 50
        self.cost_potato = 75
        self.cost_fire = 100

    def buy(self, inv:list, money):
        # self.click = pygame.mouse.get_pressed()
        # self.mouse = pygame.mouse.get_pos()

        self.render_window()
        flag = False
        self.mouse = pygame.mouse.get_pos()
        print(self.mouse)
        for mouses in pygame.event.get():
            if mouses.type == pygame.MOUSEBUTTONDOWN:
                if mouses.button == 1:
                    if money > 0:
                        if money >= 50 and self.mouse[0] in range(104, 220) and self.mouse[1] in range(84, 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = '1'
                                        money -= self.cost_water
                                        flag = True
                                        break
                                if flag:
                                    break
                        if money >= 75 and self.mouse[0] in range(270, 390) and self.mouse[1] in range(84, 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = '3'
                                        money -= self.cost_potato
                                        flag = True
                                        break
                                if flag:
                                    break
                        if money >= 100 and self.mouse[0] in range(435, 555) and self.mouse[1] in range(84, 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = 'a'
                                        money -= self.cost_fire
                                        flag = True
                                        break
                                if flag:
                                    break

        return inv, money

    def render_window(self):
        window.blit(self.window_shop, (0,0))
        window.blit(self.text_40.render('50', True, (0, 0, 0)), (110, 230))
        window.blit(self.text_40.render('75', True, (0, 0, 0)), (280, 230))
        window.blit(self.text_40.render('100', True, (0, 0, 0)), (490-64, 230))