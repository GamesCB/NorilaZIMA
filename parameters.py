import pygame
from random import randint
from settings import *
from textures import *
from player import *

pygame.init()

from pygame.locals import *
from memory_profiler import profile

item_wear = {
    'down jacket' : 0.2,
    'sweater' : 1,
    'jacket' : 0.5,
}

class Item():
    def __init__(self):
        self.texture_table = None

    def use(self):
        pass

    def throw(self):
        pass

    def show_info(self):
        pass

class Food(Item):
    def __init__(self, name, hungry_plus, texture):

        super(Food, self).__init__()
        self.name = name
        self.hungry_plus = hungry_plus
        self.item_texture = texture
        self.x = 0
        self.y = 0
        self.rect_item = Rect(self.x, self.y, self.item_texture.get_width()-4, self.item_texture.get_height()-4)

    def __str__(self):
        return self.name

class Water(Item):
    def __init__(self, name, thirst_plus, texture):

        super(Water, self).__init__()
        self.name = name
        self.thirst_plus = thirst_plus
        self.item_texture = texture
        self.x = 0
        self.y = 0
        self.rect_item = Rect(self.x, self.y, self.item_texture.get_width()-4, self.item_texture.get_height()-4)

    def __str__(self):
        return self.name

class Fire(Item):
    def __init__(self, name, count, texture):
        super(Fire, self).__init__()
        self.name = name
        self.count = count
        self.item_texture = texture
        self.x = 0
        self.y = 0
        self.rect_item = Rect(self.x, self.y, self.item_texture.get_width() - 4, self.item_texture.get_height() - 4)

    def __str__(self):
        return self.name

class Trashes():
    def __init__(self):
        self.texture_big_trash = pygame.image.load('image/shops and other/trash can.png').convert_alpha()
        self.texture_mini_trash = None

        self.items_in_trash = {
            'куртка' : range(30,100),
            'пуховик' : range(10,30),
            'вода' : range(1, 10),
            'еда' : range(100,250),
            'ничего' : range(500, 1000),
        }
        self.food = [None, '3', '4', '5', '6']
        self.water = [None, '1', '2']

        # self.tryes = randint(1,3)
        self.tryes = randint(1,10)
        self.flag = False

        self.nothing_text = Dialog('ничего нет')
        self.show_nothing = False



    def search_big_trash(self, inventory:list):
        if self.tryes > 0:
            random_item = randint(1,1000)
            for key, value in self.items_in_trash.items():
                if random_item in value:
                    inventory = self.get_name_item(key, inventory)
                    # print(key, value)

            self.tryes -= 1

        return inventory

    def get_name_item(self, name_item, inventory:list):
        if name_item == 'еда':
            for row in inventory:
                for item in row:

                    if item == '0':
                        self.flag = True
                        inventory[inventory.index(row)][row.index(item)] = self.food[randint(1, len(self.food)-1)]
                        print('подобрал еду')


                    if self.flag:
                        break

                if self.flag:
                    break

        if name_item == 'вода':
            for row in inventory:
                for item in row:

                    if item == '0':
                        self.flag = True
                        inventory[inventory.index(row)][row.index(item)] = self.water[randint(1, len(self.water)-1)]
                        print('подобрал воду')


                    if self.flag:
                        break

                if self.flag:
                    break

        self.flag = False


        return inventory

class Campfire():
    def __init__(self):
        self.texture_campfire = pygame.image.load('image/tiles/campfire.png').convert_alpha() # текстура перевала
        self.radius = 300
        self.x_p = 0
        self.y_p = 0
        self.fire_cords = [-100000,-100000000]
        self.temp = 0
        self.rect_campfire = Rect(self.fire_cords[0], self.fire_cords[1],
                                  self.texture_campfire.get_width(), self.texture_campfire.get_height()) # для проверки на коллизию костра с другими объектами
        self.collide_list = Collider().hitboxes[0:-1]
        print(self.collide_list[-1].x, self.collide_list[-1].y, 'asdasd')
        self.fire_anim = Animation([pygame.image.load(f'image/shops and other/fire_anim/{i}.png') for i in range(1, 7)], 4)
        self.temp_icon = pygame.image.load('image/icons/temp_icon.png').convert_alpha()

    def render_fire(self):
        if self.check_place():
            window.blit(self.texture_campfire, (self.rect_campfire.x - scroll[0], self.rect_campfire.y - scroll[1]))


    def fire(self):
        self.fire_anim.show_anim(self.rect_campfire.x + 10, self.rect_campfire.y - 20)


    def check_place(self):
        for rect in self.collide_list:
            if rect.colliderect(self.rect_campfire):

                while rect.colliderect(self.rect_campfire):
                    if rect.x > self.rect_campfire.y:
                        self.rect_campfire.x -= 2
                    else:
                        self.rect_campfire.x += 2
                    if rect.y > self.rect_campfire.y:
                        self.rect_campfire.y -= 2
                    else:
                        self.rect_campfire.y += 2

                return False

        return True




    def create_campfire(self, temp, x_p, y_p):

        if x_p in range(self.rect_campfire.x - self.radius, self.rect_campfire.x + self.radius) and\
                y_p in range(self.rect_campfire.y - self.radius, self.rect_campfire.y + self.radius) and temp < 36.6:
            self.temp += 0.001


            if self.temp >= 36.5:
                self.temp = 0



            if self.temp < temp:

                self.temp = temp



            if temp > 36.5:
                temp = 36.6





            temp = "%.1f" % self.temp


            window.blit(self.temp_icon, (280, 50 + 84))

        return float(temp)


class Parameters():
    def __init__(self):
        self.temperature_street = -randint(20, 50)
        self.temperature_player = 36.6
        self.text_temperature = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.need_to_change = 1000
        self.health_parameter = 200
        self.hungry_parameter = 200
        self.thirst_parameter = 200
        self.text_parameter = pygame.font.Font('font/rus-pixel.ttf', 16)
        self.texture_icons = [pygame.image.load('image/icons/health icon.png').convert_alpha(),
                           pygame.image.load('image/icons/hungry icon.png').convert_alpha(),
                           pygame.image.load('image/icons/thirst icon.png').convert_alpha(),]
        self.minus = 1


    def blit_temperature(self):
        self.health_rect = Rect(54, 54, self.health_parameter, 16)
        self.hungry_rect = Rect(54, 84, self.hungry_parameter, 16)
        self.thirst_rect = Rect(54, 114, self.thirst_parameter, 16)
        pygame.draw.rect(window, (95,73,104), Rect(50, 50+50 + 100, 70, 60))
        window.blit(self.text_temperature.render(f'{self.temperature_street}', True, (255,255,255)), (60, 60+50 + 100))
        pygame.draw.rect(window, (138, 111, 48), Rect(50, 110+50 + 100, 70, 60))
        window.blit(self.text_temperature.render(f'{self.temperature_player}', True, (255,255,255)), (60, 110+50 + 100))

        self.blit_health()
        self.blit_thirst()
        self.blit_hungry()

        self.__regular_temperature_person()
        self.__minus_hungry()
        self.__minus_thirst()

    def __regular_temperature_person(self):
        self.need_to_change -= 1
        if self.need_to_change == 0:
            self.temperature_player += (self.temperature_street/100)
            self.temperature_player = "%.1f" % self.temperature_player
            self.temperature_player = float(self.temperature_player)
            self.need_to_change = 1000
            self.health_parameter += (int(self.temperature_street)//2)*self.minus

    def change_hungry(self, food):
        if isinstance(food, Food):
            if self.hungry_parameter < 200:
                self.hungry_parameter += food.hungry_plus
            if self.hungry_parameter >= 200:
                self.hungry_parameter = 200

    def change_thirst(self, drink):
        if isinstance(drink, Water):
            if self.thirst_parameter < 200:
                self.thirst_parameter += drink.thirst_plus
            if self.thirst_parameter >= 200:
                self.thirst_parameter = 200


    def __minus_hungry(self):
        self.hungry_parameter -= 0.01

    def __minus_thirst(self):
        self.thirst_parameter -= 0.005

    def blit_health(self):
        pygame.draw.rect(window, (161, 50, 50), self.health_rect)
        pygame.draw.rect(window, (200,200,200), Rect(50, 10+40, 200, 4))
        pygame.draw.rect(window, (200,200,200), Rect(50, 10+40, 4, 20))
        pygame.draw.rect(window, (200,200,200), Rect(50, 26+40, 100*2, 4))
        pygame.draw.rect(window, (200,200,200), Rect(250, 50, 4, 20))
        window.blit(self.texture_icons[0], (30, 45))
        window.blit(self.text_parameter.render(f'{int(self.health_parameter)}/200', True, (255, 255, 255)), (180, 50))

    def blit_hungry(self):
        pygame.draw.rect(window, (174, 184, 92), self.hungry_rect)
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 10 + 40 + 30, 200, 4))
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 10 + 40 + 30, 4, 20))
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 26 + 40 + 30, 100 * 2, 4))
        pygame.draw.rect(window, (200, 200, 200), Rect(250, 50 + 30, 4, 20))
        window.blit(self.texture_icons[1], (30, 75))
        window.blit(self.text_parameter.render(f'{int(self.hungry_parameter)}/200', True, (255, 255, 255)), (180, 80))

    def blit_thirst(self):
        pygame.draw.rect(window, (75, 117, 191), self.thirst_rect)
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 10 + 40 + 60, 200, 4))
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 10 + 40 + 60, 4, 20))
        pygame.draw.rect(window, (200, 200, 200), Rect(50, 26 + 40 + 60, 100 * 2, 4))
        pygame.draw.rect(window, (200, 200, 200), Rect(250, 50 + 60, 4, 20))
        window.blit(self.texture_icons[2], (30, 105))
        window.blit(self.text_parameter.render(f'{int(self.thirst_parameter)}/200', True, (255, 255, 255)), (180, 110))



