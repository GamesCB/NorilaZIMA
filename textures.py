import pygame
from settings import *

pygame.init()

# иконки
mouse_cursor = image('image/icons/mouse_cursor.png')
buttons_menu = image('image/icons/buttons.png')
inventory_cell = pygame.image.load('image/icons/inventory cell.png').convert_alpha()
money_icon = pygame.image.load('image/icons/money.png').convert_alpha()
icon_regen = pygame.image.load('image/icons/icon_regeneration.png').convert_alpha()
icon_shield = pygame.image.load('image/icons/icon_shield.png').convert_alpha()
need_hungry_icon = pygame.image.load('image/icons/need_hungry_icon.png').convert_alpha()
need_thirst_icon = pygame.image.load('image/icons/need_thirst_icon.png').convert_alpha()
waste_paper = pygame.image.load('image/icons/inwaste_paper.png').convert_alpha()

# дома
panel_red_yellow_open_long = pygame.image.load('image/houses/panel-yellow-red_long.png').convert_alpha()
panel_brown = pygame.image.load('image/houses/panel-brown.png').convert_alpha()
school = pygame.image.load('image/houses/school.png').convert_alpha()
big_brown_panel = pygame.image.load('image/houses/big-panel-brown.png').convert_alpha()
big_panel_gray = pygame.image.load('image/houses/big-panel-gray.png').convert_alpha()
outer_school = pygame.image.load('image/houses/outer_school.png').convert_alpha()
panel_blue_back = pygame.image.load('image/houses/panel-blue.png').convert_alpha()
brown_panel_short = pygame.image.load('image/houses/brown_panel_short.png').convert_alpha()
half_brown_panel = pygame.image.load('image/houses/half panel-brown.png').convert_alpha()
pink_panel = pygame.image.load('image/houses/pink panel.png').convert_alpha()
office = pygame.image.load('image/houses/office.png').convert_alpha()
new_house1 = pygame.image.load('image/houses/new_house1.png').convert_alpha()
new_house2 = pygame.image.load('image/houses/new_house2.png').convert_alpha()
shop2 = pygame.image.load('image/houses/shop2.png').convert_alpha()

# архитектура
underporch = pygame.image.load('image/shops and other/underporch.png').convert_alpha()
electro = pygame.image.load('image/shops and other/mini shop.png').convert_alpha()
trash_can = pygame.image.load('image/shops and other/trash can.png').convert_alpha()
mini_trash = pygame.image.load('image/shops and other/mini_trash.png').convert_alpha()
shop_open = pygame.image.load('image/shops and other/shop_open.png').convert_alpha()

snow_tree1 = pygame.image.load('image/trees/snow_tree1.png').convert_alpha()
snow_tree2 = pygame.image.load('image/trees/snow_tree2.png').convert_alpha()
snow_tree3 = pygame.image.load('image/trees/snow_tree3.png').convert_alpha()
snow_tree4 = pygame.image.load('image/trees/snow_tree4.png').convert_alpha()
snow_tree5 = pygame.image.load('image/trees/snow_tree5.png').convert_alpha()

fence1 = pygame.image.load('image/shops and other/fence.png').convert_alpha()
fence_horisontal_mini = pygame.image.load('image/shops and other/fence-horisontal-mini.png').convert_alpha()
fence_mini = pygame.image.load('image/shops and other/fence-mini.png').convert_alpha()

# машины
lada6 = pygame.image.load('image/cars/lada6.png').convert_alpha()

# детская площадка
playground_p1 = pygame.image.load('image/shops and other/playground_p1.png').convert_alpha()
playground_p2 = pygame.image.load('image/shops and other/playground_p2.png').convert_alpha()
playground_p3 = pygame.image.load('image/shops and other/playground_p3.png').convert_alpha()

#щиты
red_shield = pygame.image.load('image/electronic/red_shield.png').convert_alpha()
blue_shield = pygame.image.load('image/electronic/blue_shield.png').convert_alpha()
green_shield = pygame.image.load('image/electronic/green_shield.png').convert_alpha()