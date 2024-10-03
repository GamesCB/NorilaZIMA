import pygame
from settings import *
from menu import *
from time_in_game import *
from player import *
from street_map import *
from random import randint
from parameters import *
from inventory import *
from memory_profiler import profile
from electronic import *
from shop import *
from enemy import *


pygame.init()

class Game():

    # @profile
    def __init__(self):
        self.menu = Menu()
        self.timer = TimeGame()
        self.map = Map()

        # дорисовать новый дом2
        self.rect1 = pygame.rect.Rect(0,0,1280,90)
        self.rect2 = pygame.rect.Rect(0,90,1280,90)
        self.rect3 = pygame.rect.Rect(0,180,1280,90)
        self.rect4 = pygame.rect.Rect(0,270,1280,90)
        self.rect5 = pygame.rect.Rect(0,360,1280,90)
        self.rect6 = pygame.rect.Rect(0,450,1280,90)
        self.rect7 = pygame.rect.Rect(0,540,1280,90)
        self.rect8 = pygame.rect.Rect(0,630,1280,90)

        self.mouse_rect = pygame.Rect(0,0, 10,10)


        self.var_min = 0
        self.fps_text = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.text_get = pygame.font.Font('font/rus-pixel.ttf', 48)

        self.player = Player()
        self.parameters = Parameters()

        self.inventory = Inventory()

        # мусорки
        self.trash1 = Trashes()
        self.trash2 = Trashes()
        self.trash3 = Trashes()
        self.trash4 = Trashes()
        self.trash5 = Trashes()
        self.trash6 = Trashes()

        self.using_menu = Using_menu()

        self.counter_electronic = 1
        self.counter_shop = 1
        self.electro = Window_electronic()
        self.lenght_shield = 0
        self.minus = 1
        self.heal = 0
        self.shop = Shop()
        self.campfire = Campfire()
        self.camp_counter = 1
        self.dogs = [Dogs() for i in range(5)]
        # self.enemy = [Enemy_dog() for i in range(10)]

        # 383 - Sound
        # 271 - music.load
        self.weapon = Weapon()
        self.attack_anim = Animation([pygame.image.load(f'image/weapon/attack_anim/{i}.png').convert_alpha() for i in range(1, 7)], 2)
        self.var_reload_anim_attack = 12


        self.st50let()


    def st50let(self):
        self.counter_menu = 0

        while True:


            self.map.cords = [self.player.player_rect.x, self.player.player_rect.y]

            self.mouse = pygame.mouse.get_pos()
            self.mouse_rect.x, self.mouse_rect.y = self.mouse[0], self.mouse[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.counter_menu += 1
                    if event.key == pygame.K_e:

                        if self.player.player_rect.x in range(14500, 14700) and self.player.player_rect.y in range(2309, 2320):
                            self.counter_electronic += 1
                        if self.player.player_rect.x in range(1254, 1374) and self.player.player_rect.y in range(4358, 4398):
                            self.counter_shop += 1

                    if event.key == pygame.K_f:
                        self.camp_counter += 1
                        if self.camp_counter % 2 == 0 and self.inventory.waste_paper_count >= 50:
                            self.campfire.rect_campfire.x = self.player.player_rect.x + 150
                            self.campfire.rect_campfire.y = self.player.player_rect.y - 64
                            self.inventory.waste_paper_count -= 50
                        else:

                            self.campfire.rect_campfire.y = 10000000

                    if event.key == pygame.K_r:
                        self.lenght_shield = 0

                    if event.key == pygame.K_SPACE:
                        if self.weapon.taked:
                            self.kick_dogs()
                            self.var_reload_anim_attack = 12



            window.blit(screen, (0,0))
            screen.fill((200,200,200))
            self.map.render_50_let()
            self.map.render_under()

            if self.camp_counter % 2 == 0:
                self.campfire.render_fire()
                if 'a' in self.inventory.inventory[0] or 'a' in self.inventory.inventory[1]:
                    self.campfire.fire()
                    self.parameters.temperature_player = self.campfire.create_campfire(self.parameters.temperature_player,
                                                                                       self.player.player_rect.x,
                                                                                       self.player.player_rect.y)

            self.weapon.blit_weapon()
            self.player.render()
            self.render_shields()
            self.regular_icons()
            if self.var_reload_anim_attack != 0:
                self.attack_anim.show_anim(self.player.player_rect.x, self.player.player_rect.y - 200)
                self.var_reload_anim_attack -= 1




            self.map.render_above()

            self.render_dogs()




            self.timer.go_day_and_night()       # день и ночь

            # print(self.player.player_rect.x, self.player.player_rect.y, 'player')
            print(self.mouse)

            self.cutscene_show()                # начало сцены


            self.GUI()
            self.any_changes()
            self.map.events()
            if self.counter_electronic % 2 == 0:
                self.inventory.inventory, self.inventory.total_money = self.electro.buy(self.inventory.inventory, self.inventory.total_money)
            if self.counter_shop % 2 == 0:
                self.inventory.inventory, self.inventory.total_money = self.shop.buy(self.inventory.inventory, self.inventory.total_money)

            window.blit(self.fps_text.render(f'{int(clock.get_fps())}', True, (255,255,255)), (1200, 40))
            window.blit(mouse_cursor, self.mouse)

            pygame.display.update()
            clock.tick(60)

    def any_changes(self):
        self.player.hitboxes[-1].x = self.campfire.rect_campfire.x
        self.player.hitboxes[-1].y = self.campfire.rect_campfire.y
        if self.weapon.taked:
            self.inventory.get_weap = True



    def render_dogs(self):

        self.parameters.health_parameter = self.dogs[0].search_and_walk(self.player.player_rect.x, self.player.player_rect.y,
                                                                        self.parameters.health_parameter)
        self.parameters.health_parameter = self.dogs[1].search_and_walk(self.player.player_rect.x, self.player.player_rect.y,
                                                                        self.parameters.health_parameter)
        self.parameters.health_parameter = self.dogs[2].search_and_walk(self.player.player_rect.x, self.player.player_rect.y,
                                                                        self.parameters.health_parameter)
        self.parameters.health_parameter = self.dogs[3].search_and_walk(self.player.player_rect.x, self.player.player_rect.y,
                                                                        self.parameters.health_parameter)
        self.parameters.health_parameter = self.dogs[4].search_and_walk(self.player.player_rect.x, self.player.player_rect.y,
                                                                        self.parameters.health_parameter)

    def kick_dogs(self):
        self.dogs[0].rect_dog.x, self.dogs[0].rect_dog.y = self.weapon.operate_weapon(self.dogs[0].rect_dog.x, self.dogs[0].rect_dog.y,
                                                                                      self.player.player_rect.x, self.player.player_rect.y)
        self.dogs[1].rect_dog.x, self.dogs[1].rect_dog.y = self.weapon.operate_weapon(self.dogs[1].rect_dog.x, self.dogs[1].rect_dog.y,
                                                                                      self.player.player_rect.x, self.player.player_rect.y)
        self.dogs[2].rect_dog.x, self.dogs[2].rect_dog.y = self.weapon.operate_weapon(self.dogs[2].rect_dog.x, self.dogs[2].rect_dog.y,
                                                                                      self.player.player_rect.x, self.player.player_rect.y)
        self.dogs[3].rect_dog.x, self.dogs[3].rect_dog.y = self.weapon.operate_weapon(self.dogs[3].rect_dog.x, self.dogs[3].rect_dog.y,
                                                                                      self.player.player_rect.x, self.player.player_rect.y)
        self.dogs[4].rect_dog.x, self.dogs[4].rect_dog.y = self.weapon.operate_weapon(self.dogs[4].rect_dog.x, self.dogs[4].rect_dog.y,
                                                                                      self.player.player_rect.x, self.player.player_rect.y)

    def cutscene_show(self):
        self.var_min += 3
        self.rect1.x += int(self.var_min)
        self.rect3.x += int(self.var_min)
        self.rect5.x += int(self.var_min)
        self.rect7.x += int(self.var_min)
        self.rect2.x -= int(self.var_min)
        self.rect4.x -= int(self.var_min)
        self.rect6.x -= int(self.var_min)
        self.rect8.x -= int(self.var_min)

        pygame.draw.rect(window, (0,0,0), self.rect1)
        pygame.draw.rect(window, (0,0,0), self.rect2)
        pygame.draw.rect(window, (0,0,0), self.rect3)
        pygame.draw.rect(window, (0,0,0), self.rect4)
        pygame.draw.rect(window, (0,0,0), self.rect5)
        pygame.draw.rect(window, (0,0,0), self.rect6)
        pygame.draw.rect(window, (0,0,0), self.rect7)
        pygame.draw.rect(window, (0,0,0), self.rect8)

    def cutscene_awake(self):
        pass

    def trash_update_item(self):
        self.inventory.total_money += randint(1, 5)
        self.inventory.waste_paper_count += 1

    def search_trash(self):
        self.key = pygame.key.get_pressed()
        if self.trash1.tryes > 0 and self.player.player_rect.x in range(0, 230) and self.player.player_rect.y in range(1445, 1520):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255,255,255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash1.search_big_trash(self.inventory.inventory)
                self.trash_update_item()


        if self.trash2.tryes > 0 and self.player.player_rect.x in range(4278, 4438) and self.player.player_rect.y in range(1445, 1509):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255, 255, 255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash2.search_big_trash(self.inventory.inventory)
                self.trash_update_item()

        if self.trash3.tryes > 0 and self.player.player_rect.x in range(1622, 1725) and self.player.player_rect.y in range(4254, 4400):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255, 255, 255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash3.search_big_trash(self.inventory.inventory)
                self.trash_update_item()

        if self.trash4.tryes > 0 and self.player.player_rect.x in range(9786, 9930) and self.player.player_rect.y in range(1445, 1510):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255, 255, 255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash4.search_big_trash(self.inventory.inventory)
                self.trash_update_item()

        if self.trash5.tryes > 0 and self.player.player_rect.x in range(14266, 14330) and self.player.player_rect.y in range(2310, 2340):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255, 255, 255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash5.search_big_trash(self.inventory.inventory)
                self.trash_update_item()

        if self.trash6.tryes > 0 and self.player.player_rect.x in range(15428, 15524) and self.player.player_rect.y in range(6364, 6444):
            window.blit(self.text_get.render('нажмите "е", чтобы обыскать мусорку', True, (255, 255, 255)), (274, 50))
            if self.key[pygame.K_e]:
                self.inventory.inventory = self.trash6.search_big_trash(self.inventory.inventory)
                self.trash_update_item()

    def GUI(self):
        self.parameters.blit_temperature()
        hungry = 0
        thirst = 0
        if self.lenght_shield == 0:
            hungry, thirst, self.lenght_shield = self.inventory.render_inventory_full(self.mouse_rect, self.parameters.hungry_parameter,
                                                                                  self.parameters.thirst_parameter, self.lenght_shield)

        if self.counter_menu % 2 == 1:
            self.using_menu.show_menu(self.mouse_rect)
        else:
            self.using_menu.hide_menu()

        self.parameters.hungry_parameter += (hungry)
        self.parameters.thirst_parameter += (thirst)
        if self.parameters.health_parameter < 200:
            self.parameters.health_parameter += ((hungry + thirst) // 2)
        if self.parameters.health_parameter > 200:
            self.parameters.health_parameter = 200

        self.search_trash()


    def regular_icons(self):
        if self.parameters.hungry_parameter < 50:
            if self.camp_counter % 2 == 1:
                window.blit(need_hungry_icon, (280, 50 + 84))
            else:
                window.blit(need_hungry_icon, (280 + 70, 50 + 84))

        if self.parameters.hungry_parameter > 50 and self.parameters.thirst_parameter < 50:
            if self.camp_counter % 2 == 1:
                window.blit(need_thirst_icon, (280, 50 + 84))
                return True
            else:
                window.blit(need_thirst_icon, (280 + 70, 50 + 84))
                return True

        if self.parameters.thirst_parameter < 50:
            if self.camp_counter % 2 == 1 and self.parameters.hungry_parameter < 50:
                window.blit(need_thirst_icon, (350, 50 + 84))
                return True
            else:
                window.blit(need_thirst_icon, (350 + 70, 50 + 84))
                return True



    def render_shields(self):

        if self.lenght_shield in range(5000, 7501):
            window.blit(green_shield, (self.player.player_rect.x - 20 - scroll[0], self.player.player_rect.y - self.player.texture.get_height() - 20 - scroll[1]))
            self.lenght_shield -= 1
            self.parameters.minus = 0.3
            window.blit(icon_regen, (350, 50))
            window.blit(icon_shield, (280, 50))
            if self.parameters.health_parameter < 200:
                self.parameters.health_parameter += 0.03
        elif self.lenght_shield in range(2500, 5000):
            window.blit(blue_shield, (self.player.player_rect.x - 20 - scroll[0], self.player.player_rect.y - self.player.texture.get_height() - 20 - scroll[1]))
            self.lenght_shield -= 1
            self.parameters.minus = 0.5
            window.blit(icon_shield, (280, 50))
        elif self.lenght_shield in range(1, 2500):
            window.blit(red_shield, (self.player.player_rect.x - 20 - scroll[0], self.player.player_rect.y - self.player.texture.get_height() - 20 - scroll[1]))
            self.lenght_shield -= 1
            self.parameters.minus = 0.8
            window.blit(icon_shield, (280, 50))
        else:
            self.parameters.minus = 1

        # print(self.lenght_shield)
        if int(self.timer.hours) == 10 and int(self.timer.minutes) == 0:
            self.lenght_shield = 0
            self.trash1 = Trashes()
            self.trash2 = Trashes()
            self.trash3 = Trashes()
            self.trash4 = Trashes()
            self.trash5 = Trashes()
            self.trash6 = Trashes()
            self.rect1.x = 0
            self.rect2.x = 0
            self.rect3.x = 0
            self.rect4.x = 0
            self.rect5.x = 0
            self.rect6.x = 0
            self.rect7.x = 0
            self.rect8.x = 0

    def various_of_death(self):
        if self.parameters.health_parameter <= 0:
            pass

        if self.parameters.thirst_parameter <= 50:
            self.parameters.thirst_parameter = 0
            self.parameters.health_parameter -= 0.1

        if self.parameters.hungry_parameter <= 50:
            self.parameters.hungry_parameter = 0
            self.parameters.health_parameter -= 0.1

        if self.parameters.temperature_player <= 32:
            pass


# список задач
# сделать загрузочный экран

# добавить звуки и музыку для игры (звуки роботов, ударов, звуки ветра, музыку в главное меню)
# сделать туториал



if __name__ == '__main__':
    start = Game()