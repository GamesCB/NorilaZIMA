import pygame
pygame.init()
from pygame.locals import *

from settings import *

class Window_electronic():
    def __init__(self):
        self.window_shop = pygame.image.load('image/windows/electronic.png').convert_alpha()
        self.cost_mini_shield = 50
        self.cost_medium_shield = 75
        self.cost_rare_shield = 100
        self.cost_text = pygame.font.Font('font/rus-pixel.ttf', 40)

    def buy(self, inv:list, money):
        self.render_window()
        print(self.mouse)
        flag = False
        for mouses in pygame.event.get():
            if mouses.type == pygame.MOUSEBUTTONDOWN:
                if mouses.button == 1:
                    if money > 0:
                        if money >= 50 and self.mouse[0] in range(104, 220) and self.mouse[1] in range(86, 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = 'x'
                                        money -= self.cost_mini_shield
                                        flag = True
                                        break
                                if flag:
                                    break
                        if money >= 75 and self.mouse[0] in range(300, 420) and self.mouse[1] in range(85, 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = 'y'
                                        money -= self.cost_medium_shield
                                        flag = True
                                        break
                                if flag:
                                    break
                        if money >= 100 and self.mouse[0] in range(500, 620) and self.mouse[1] in range(85 , 200):
                            for row in inv:
                                for cell in row:
                                    if cell == '0':
                                        inv[inv.index(row)][row.index(cell)] = 'z'
                                        money -= self.cost_rare_shield
                                        flag = True
                                        break
                                if flag:
                                    break


        return inv, money



    def render_window(self):
        window.blit(self.window_shop, (0,0))
        self.mouse = pygame.mouse.get_pos()
        window.blit(self.cost_text.render('50', True, (0,0,0)), (100, 230))
        window.blit(self.cost_text.render('75', True, (0,0,0)), (300, 230))
        window.blit(self.cost_text.render('100', True, (0,0,0)), (490, 230))

class Electronic():
    def __init__(self, lenght, defence, texture):
        self.lenght = lenght
        self.defence = defence
        self.item_texture = pygame.transform.scale(texture, (texture.get_width() - 4, texture.get_height() - 4))
        self.x = 0
        self.y = 0
        self.rect_item = Rect(self.x, self.y, self.item_texture.get_width() - 4, self.item_texture.get_height() - 4)