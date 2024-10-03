from random import randint

import pygame
from settings import *
from textures import *
from parameters import *
from electronic import *

pygame.init()
from pygame.locals import *

class Inventory():
    def __init__(self):

        # slots = 10
        self.inventory = blit_all_tiles('parameters/inventory')
        print(self.inventory)
        self.text_32 = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.text_32_US = pygame.font.Font('font/OCR A Extended.ttf', 32)
        self.text_16 = pygame.font.Font('font/rus-pixel.ttf', 16)
        self.inv_btn = pygame.transform.scale(pygame.image.load('image/icons/inv_btn.png').convert_alpha(), (142, 32))

        # self.potato = Food('остаток картошки фри', 40, pygame.image.load('image/items/potato.png').convert_alpha())
        # self.half_water = Water('полбутылки воды', -20, pygame.image.load('image/items/half water.png').convert_alpha())
        # self.full_water = Water('полная бутылка воды', -100, pygame.image.load('image/items/full water.png').convert_alpha())
        # self.half_pizza = Food('кусочек пиццы', 20, pygame.image.load('image/items/half pizza.png').convert_alpha())
        # self.bread = Food('пропавший хлеб', 70, pygame.image.load('image/items/bread.png').convert_alpha())
        # self.donut = Food('пончик', 10, pygame.image.load('image/items/donut.png').convert_alpha())

        self.weap_btn = pygame.transform.scale(inventory_cell, (inventory_cell.get_width() * 2 + 6, inventory_cell.get_height() * 2 + 6))

        self.lenght_mini_sh = 2500
        self.lenght_medium_sh = 5000
        self.lenght_rare_sh = 7500

        self.items_all = {
            '3' : Food('остаток картошки фри', 40, pygame.image.load('image/items/potato.png').convert_alpha()),
            '2' : Water('полбутылки воды', 20, pygame.image.load('image/items/half water.png').convert_alpha()),
            '1' : Water('полная бутылка воды', 100, pygame.image.load('image/items/full water.png').convert_alpha()),
            '4' : Food('кусочек пиццы', 20, pygame.image.load('image/items/half pizza.png').convert_alpha()),
            '5' : Food('пропавший хлеб', 70, pygame.image.load('image/items/bread.png').convert_alpha()),
            '6' : Food('пончик', 10, pygame.image.load('image/items/donut.png').convert_alpha()),
            'x' : Electronic(self.lenght_mini_sh, 80, pygame.image.load('image/electronic/small_indicate.png').convert_alpha()),
            'y' : Electronic(self.lenght_medium_sh, 50, pygame.image.load('image/electronic/medium_indicate.png').convert_alpha()),
            'z' : Electronic(self.lenght_rare_sh, 30, pygame.image.load('image/electronic/rare_indicate.png').convert_alpha()),
            'a' : Fire('спички', 10, pygame.image.load('image/items/fire.png').convert_alpha()),
        }

        self.total_money = 200
        self.active_info = False
        self.waste_paper_count = 0
        self.get_weap = False
        self.texture_metal_pipe = pygame.transform.scale(pygame.image.load('image/weapon/metal pipe.png').convert_alpha(), (120, 120))


        self.drop_btn = pygame.Rect(408, 658, self.inv_btn.get_width(), self.inv_btn.get_height())


    def render_inventory_full(self, mouserect:Rect, hungry, thirst, lenght):
        self.y = 9
        hungry_add = 0
        thirst_add = 0
        self.mouse = mouserect
        self.click = pygame.mouse.get_pressed()
        self.blit_money()
        for cells in self.inventory:
            self.x = 0.78125
            for item in cells:
                window.blit(inventory_cell, (self.x * 64, self.y * 64))
                if item in self.items_all:
                    self.items_all[item].rect_item.x, self.items_all[item].rect_item.y = int(self.x * 64 + 4), int(self.y * 64 + 4)

                    if self.items_all[item].rect_item.colliderect(mouserect):

                        pygame.draw.rect(window, (54, 112, 88), self.items_all[item].rect_item)
                        hungry_add, thirst_add, lenght = self.use_anything(self.items_all[item], hungry, thirst, self.inventory.index(cells), cells.index(item))

                    window.blit(self.items_all[item].item_texture, (self.x * 64, self.y * 64))

                self.x += 1.1
            self.y += 1.1

        # if self.active_info:
        #     self.blit_item_parameter(self.x * 64 + 4, self.y * 64 + 14)
        if '0' not in self.inventory[0] and '0' not in self.inventory[1]:
            window.blit(self.text_32.render('- выбросить', True, (255,255,255)), (582, 655))
            window.blit(self.text_32_US.render('B', True, (255,255,255)), (550, 655))

        window.blit(waste_paper, (54, 420))
        window.blit(self.text_16.render(f'{self.waste_paper_count}', True, (255,255,255)), (92, 460))
        window.blit(self.weap_btn, (400, 576))
        if self.get_weap:
            window.blit(self.texture_metal_pipe, (400 + 8, 576 + 8))

        return hungry_add, thirst_add, lenght

    def use_anything(self, item, hungry, thirst, row, index):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if isinstance(item, Food):
                        self.inventory[row][index] = '0'
                        if hungry + item.hungry_plus >= 200:
                            return 200 - hungry, 0, 0

                        return item.hungry_plus, 0, 0

                    if isinstance(item, Water):

                        self.inventory[row][index] = '0'
                        if thirst + item.thirst_plus >= 200:
                            return 0, 200 - thirst, 0

                        return 0, item.thirst_plus, 0

                    self.active_info = False

                    if isinstance(item, Electronic):
                        self.inventory[row][index] = '0'
                        print(item.lenght)

                        return 0, 0, item.lenght

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.active_info:
                        self.active_info = False
                        break
                    self.active_info = True
                    print(self.active_info)
                    print(item)
                    print('АААААААААААААААААААААААА')
                    self.inventory[row][index] = '0'
                    self.active_info = False

        return 0, 0, 0

    def blit_money(self):
        window.blit(money_icon, (50, 500))
        window.blit(self.text_32.render(f'{self.total_money}', True, (255,255,255)), (60 + money_icon.get_width(), 510))

class Weapon():
    def __init__(self):
        self.texture_metal_pipe = pygame.transform.scale(pygame.image.load('image/weapon/metal pipe.png').convert_alpha(), (128, 128))
        self.rect_weap = pygame.Rect(4292, 4079, self.texture_metal_pipe.get_width(), self.texture_metal_pipe.get_height())
        self.text_take = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.taked = False


    def get_weapon(self):
        pass

    def operate_weapon(self,x_d, y_d, x_p, y_p):
        if x_d in range(x_p - 200, x_p + 200) and y_d in range(y_p - 300, y_p + 100):
            return randint(100, 20000), randint(500, 12000)

        return x_d, y_d

    def blit_weapon(self):
        if not self.taked:
            window.blit(self.texture_metal_pipe, (self.rect_weap.x - scroll[0], self.rect_weap.y - scroll[1]))
            key = pygame.key.get_pressed()
            if key[pygame.K_e]:
                self.taked = True

            # print(self.rect_weap.x, self.rect_weap.y)

