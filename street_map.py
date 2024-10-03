import pygame
from settings import *
from textures import *
from random import randint
from parameters import *
from player import Dialog

pygame.init()


class Trees():

    cords = [0,0]
    def __init__(self, x, y, texture = pygame.image.load('image/trees/snow_tree1.png').convert_alpha()):
        self.tree = texture
        self.x = x
        self.y = y

    def render_under(self):
        if self.cords[1] >= self.y + self.tree.get_height():
            window.blit(self.tree, (self.x - scroll[0], self.y - scroll[1]))

    def render_above(self):
        if self.cords[1] < self.y + self.tree.get_height():
            window.blit(self.tree, (self.x - scroll[0], self.y - scroll[1]))




class Map():

    def __init__(self):
        self.cords = [0, 0]
        self.map50 = blit_all_tiles('maps/50 лет Октября')
        self.map50_dict = {
            '1' : pygame.image.load('image/tiles/street way personal/1.png').convert_alpha(),
            '2' : pygame.image.load('image/tiles/street way personal/2.png').convert_alpha(),
            '3' : pygame.image.load('image/tiles/street way personal/3.png').convert_alpha(),
            '4' : pygame.image.load('image/tiles/street way personal/4.png').convert_alpha(),
            '5' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/4.png').convert_alpha(), 90), # left
            '6' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/4.png').convert_alpha(), 270), # right
            '7' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/4.png').convert_alpha(), 180), # bottom
            '8' : pygame.image.load('image/tiles/street way personal/8.png').convert_alpha(),
            '9' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/8.png').convert_alpha(), 180),
            'f' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/8.png').convert_alpha(), 90),
            'g' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/8.png').convert_alpha(), 270),
            'a' : pygame.image.load('image/tiles/street way personal/a.png').convert_alpha(),
            'b' : pygame.image.load('image/tiles/street way personal/b.png').convert_alpha(),
            'c' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/b.png').convert_alpha(), -90),
            'd' : pygame.image.load('image/tiles/street way personal/d.png').convert_alpha(),
            'e' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/d.png').convert_alpha(), -90),
            'h' : pygame.transform.rotate(pygame.image.load('image/tiles/street way personal/d.png').convert_alpha(), 180),

        }
        self.text1 = pygame.font.Font('font/rus-pixel.ttf', 20)
        self.text2 = pygame.font.Font('font/rus-pixel.ttf', 40)
        self.list_random_cars = [bool(randint(0,1)) for i in range(5)]
        self.dialog_cant_entry = Dialog('я не могу туда пройти', 32)

        self.tree1 = Trees(4758, 3700)
        self.tree2 = Trees(4758, 3300, pygame.image.load('image/trees/snow_tree3.png').convert_alpha())
        self.tree3 = Trees(4758, 3100, pygame.image.load('image/trees/snow_tree4.png').convert_alpha())
        self.tree4 = Trees(4758, 2600)
        self.tree5 = Trees(4758, 2100)


    def render_under(self):
        Trees.cords = self.cords
        window.blit(panel_red_yellow_open_long, (0 - scroll[0], 0 - scroll[1]))
        window.blit(panel_brown, (5424 - scroll[0], 0 - scroll[1]))
        window.blit(panel_brown, (7975 - scroll[0], 0 - scroll[1]))
        window.blit(half_brown_panel, (7975 + panel_brown.get_width() - scroll[0], 0 - scroll[1]))
        # window.blit(half_brown_panel, (7975 + panel_brown.get_width() - scroll[0], 0 - scroll[1]))
        if self.cords[1] >= 2500:
            window.blit(school, (2248 - scroll[0], 2000 - scroll[1]))
        if self.cords[1] >= 3523:
            window.blit(big_brown_panel, (6080 - scroll[0], 2000 - scroll[1]))
        window.blit(big_panel_gray, (-1000 - scroll[0], 800 - scroll[1]))
        window.blit(electro, (-900 - scroll[0], 2600 - scroll[1]))
        window.blit(self.text1.render('осторожно!', True, (255,255,255)), (-520 - scroll[0], 2800 - scroll[1]))
        window.blit(self.text1.render('напряжение', True, (255,255,255)), (-520 - scroll[0], 2830 - scroll[1]))
        # self.trees.square(0,0)
        self.trees_func()
        window.blit(fence1, (645 - scroll[0], 1370 - scroll[1]))
        window.blit(fence1, (1235 - scroll[0], 1370 - scroll[1]))
        window.blit(fence1, (2445 - scroll[0], 1370 - scroll[1]))
        window.blit(fence1, (3630 - scroll[0], 1370 - scroll[1]))
        if self.cords[1] >= 1856 and self.cords[0] < 825:
            window.blit(fence_horisontal_mini, (0 - scroll[0], 1780 - scroll[1]))
            window.blit(fence_horisontal_mini, (100 - scroll[0], 1780 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 1820 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 1860 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 1900 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 1940 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 1980 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2020 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2060 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2100 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2140 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2180 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2220 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2260 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2300 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2340 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2380 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2420 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2460 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2500 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2540 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2580 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2620 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2660 - scroll[1]))
            window.blit(fence_mini, (178 - scroll[0], 2700 - scroll[1]))

            if self.cords[1] >= 2784:
                window.blit(fence_horisontal_mini, (100 - scroll[0], 2700 - scroll[1]))

        if self.list_random_cars[0]:
            window.blit(lada6, (5070 - scroll[0], 1228 - scroll[1]))

        if self.cords[1] >= 1541:
            self.blit_underporch()
        if self.cords[1] >= 4368 or self.cords[1] in range(2040, 2216):
            window.blit(outer_school, (1808 - scroll[0], 1912 - scroll[1]))

        window.blit(trash_can, (72 - scroll[0], 1350 - scroll[1]))
        window.blit(mini_trash, (4374 - scroll[0], 1485 - mini_trash.get_height() - scroll[1]))

        if self.cords[1] >= 4213:
            window.blit(shop_open, (1278 - scroll[0], 4053 - scroll[1]))
            window.blit(self.text1.render('фруктовощи', True, (45, 104, 80)), (1350 - scroll[0], 4125 - scroll[1]))

        self.tree5.render_under()
        self.tree4.render_under()
        self.tree3.render_under()
        self.tree2.render_under()
        self.tree1.render_under()

        if self.cords[1] >= 4300:
            window.blit(mini_trash, (1690 - scroll[0], 4236 - scroll[1]))

        if self.cords[1] >= 6325:
            window.blit(panel_blue_back, (-173 - scroll[0], 4900 - scroll[1]))
            window.blit(brown_panel_short, (-173 + panel_blue_back.get_width() - scroll[0], 4900 - scroll[1]))

            window.blit(panel_blue_back, (5238 - scroll[0], 4900 - scroll[1]))
            window.blit(pink_panel, (8666 - scroll[0], 4900 - scroll[1]))

        if self.cords[1] >= 6137:
            window.blit(big_panel_gray, (7666 - scroll[0], 4369 - scroll[1]))

        if self.cords[1] >= 2072:
            window.blit(office, (13266 - scroll[0], 700 - scroll[1]))

        if self.cords[1] >= 5168:
            window.blit(new_house1, (13250 - scroll[0], 2816 - scroll[1]))

        if self.cords[1] >= 5800:
            window.blit(new_house2, (15026 - scroll[0], 4000 - scroll[1]))


        window.blit(shop2, (14266 - scroll[0], 1500 - scroll[1]))
        window.blit(self.text2.render('магазин электроники', True, (200,200,200)), (14362 - scroll[0], 1880 - scroll[1]))

        window.blit(mini_trash, (9882 - scroll[0], 1485 - mini_trash.get_height() - scroll[1]))
        window.blit(mini_trash, (14266 + 10 - scroll[0], 2309 + 20 - mini_trash.get_height() - scroll[1]))
        window.blit(mini_trash, (15524 - scroll[0], 6300 - scroll[1]))



    def render_above(self):
        if self.cords[1] < 4368 and self.cords[1] not in range(2040, 2216):
            window.blit(outer_school, (1808 - scroll[0], 1912 - scroll[1]))
        if self.cords[1] < 2500:
            window.blit(school, (2248 - scroll[0], 2000 - scroll[1]))
        if self.cords[1] < 3523:
            window.blit(big_brown_panel, (6080 - scroll[0], 2000 - scroll[1]))


        if self.cords[1] < 2784:
            window.blit(fence_horisontal_mini, (100 - scroll[0], 2700 - scroll[1]))
            if self.cords[1] < 1856 and self.cords[0] < 825:
                window.blit(fence_horisontal_mini, (0 - scroll[0], 1780 - scroll[1]))
                window.blit(fence_horisontal_mini, (100 - scroll[0], 1780 - scroll[1]))

                window.blit(fence_mini, (178 - scroll[0], 1820 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 1860 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 1900 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 1940 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 1980 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 2020 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 2060 - scroll[1]))
                window.blit(fence_mini, (178 - scroll[0], 2100 - scroll[1]))

        if self.cords[1] < 1541:
            self.blit_underporch()


        if self.cords[1] < 6325:
            window.blit(panel_blue_back, (-173 - scroll[0], 4900 - scroll[1]))
            window.blit(brown_panel_short, (-173 + panel_blue_back.get_width() - scroll[0], 4900 - scroll[1]))
            window.blit(panel_blue_back, (5238 - scroll[0], 4900 - scroll[1]))
            window.blit(pink_panel, (8666 - scroll[0], 4900 - scroll[1]))

        if self.cords[1] < 4213:
            window.blit(shop_open, (1278 - scroll[0], 4053 - scroll[1]))

            window.blit(self.text1.render('фруктовощи', True, (45,104,80)), (1350 - scroll[0], 4125 - scroll[1]))


        self.tree5.render_above()
        self.tree4.render_above()
        self.tree3.render_above()
        self.tree2.render_above()
        self.tree1.render_above()
        if self.cords[1] < 4300:
            window.blit(mini_trash, (1690 - scroll[0], 4236 - scroll[1]))

        if self.cords[1] < 6137:
            window.blit(big_panel_gray, (7666 - scroll[0], 4369 - scroll[1]))

        if self.cords[1] < 2072:
            window.blit(office, (13266 - scroll[0], 700 - scroll[1]))
        if self.cords[1] < 5168:
            window.blit(new_house1, (13250 - scroll[0], 2816 - scroll[1]))

        if self.cords[1] < 5800:
            window.blit(new_house2, (15026 - scroll[0], 4000 - scroll[1]))



    def events(self):
        if self.cords[0] in range(4949, 5339) and self.cords[1] < 1551:
            self.dialog_cant_entry.render_nowait()

    def trees_func(self):
        window.blit(snow_tree4, (640 - scroll[0], 1100 - scroll[1]))
        window.blit(snow_tree2, (1200 - scroll[0], 900 - scroll[1]))
        window.blit(snow_tree5, (2430 - scroll[0], 1000 - scroll[1]))
        window.blit(snow_tree1, (3600 - scroll[0], 900 - scroll[1]))



    def render_50_let(self):
        y = 10
        for tile in self.map50:
            x = 0
            for tiles in tile:

                if tiles in self.map50_dict:
                    window.blit(self.map50_dict[tiles], (x * 128 - scroll[0], y * 128 - scroll[1]))

                x += 1
            y += 1

    def blit_underporch(self):
        # window.blit(underporch, (315 - scroll[0], 1225 - scroll[1]))
        window.blit(underporch, (910 - scroll[0], 1225 - scroll[1]))
        window.blit(underporch, (1500 - scroll[0], 1225 - scroll[1]))
        # window.blit(underporch, (2090 - scroll[0], 1225 - scroll[1]))