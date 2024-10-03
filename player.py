import pygame
from random import randint
from settings import *
from pygame.locals import *
from textures import *

pygame.init()

class Camera():
    def __init__(self):
        self.scroll = [0, 0]
        self.texture = pygame.image.load('image/player/character.png').convert_alpha()
        # self.player_rect = pygame.rect.Rect(222, 1565, self.texture.get_width(), 1)
        self.player_rect = pygame.rect.Rect(1330, 4358, self.texture.get_width(), 1)


    def move_camera(self):
        true_scroll[0] += (self.player_rect.x - true_scroll[0] + 100 - (SIZE[0] / 2)) // 10
        true_scroll[1] += (self.player_rect.y - true_scroll[1] - (SIZE[1] / 2) - 100) // 10
        self.scroll = true_scroll.copy()
        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])
        
class Collider(Camera):
    def __init__(self):
        super(Collider, self).__init__()
        self.campfire = Rect(0,0,128, 128)
        self.hitboxes = [
            Rect(20, 1080, panel_red_yellow_open_long.get_width() - 20, 365),
            Rect(2268, 2500, school.get_width() - 30, 1500),
            Rect(5435, 1080, panel_brown.get_width() - 20, 365),
            Rect(6090, 3523, big_brown_panel.get_width() - 20, 500),
            Rect(-1000, 800, big_panel_gray.get_width(), big_panel_gray.get_height() - self.player_rect.height),
            Rect(-900, 2799, electro.get_width(), electro.get_height() - 190),

            # заборы
            Rect(645, 1370, fence1.get_width(), fence1.get_height()),
            Rect(1235, 1370, fence1.get_width(), fence1.get_height()),
            Rect(2445, 1370, fence1.get_width(), fence1.get_height()),
            Rect(3630, 1370, fence1.get_width(), fence1.get_height()),
            Rect(0, 1780 + fence_horisontal_mini.get_height()-5, fence_horisontal_mini.get_width()*2 , 20),
            # Rect(100, 1780 + fence_horisontal_mini.get_height() - 5, fence_horisontal_mini.get_width(), 20),
            Rect(178, 1820 + 33, fence_mini.get_width(), 2700 - 1820 + 75),
            Rect(110, 2808-35, fence_horisontal_mini.get_width()-10, 35),
            Rect(1808, 2008, fence_horisontal_mini.get_width()*13 + 10, 40),
            Rect(3600, 2008, fence_horisontal_mini.get_width()*10, 40),
            Rect(1808, 4336, outer_school.get_width()-20, 40),
            Rect(1808, 2008, 40, outer_school.get_height()-69),
            Rect(4500, 2008, 40, outer_school.get_height()-69),

            Rect(72, 1350, trash_can.get_width(), trash_can.get_height()),
            Rect(4949, 1405, 500, 10),
            Rect(-173, 6045, panel_blue_back.get_width() * 2, 300),
            Rect(5238, 6045, panel_blue_back.get_width(), 300),
            Rect(8666,6045, pink_panel.get_width(), 300),
            Rect(4374, 1445, mini_trash.get_width(), 40),
            Rect(9882, 1445, mini_trash.get_width(), 40),
            Rect(14266, 2279, mini_trash.get_width(), 60),
            Rect(15524, 6340, mini_trash.get_width(), 80),
            Rect(1278, 4213, shop_open.get_width(), 145),
            Rect(1690, 4300, mini_trash.get_width(), 58),

            # деревья возле школы
            Rect(4890, 4303, 50, 20),
            Rect(4894, 3862, 50, 20),
            Rect(4878, 3490, 50, 20),
            Rect(4890, 3194, 50, 20),
            Rect(4886, 2706, 50, 20),
            Rect(7975, 1080, panel_brown.get_width() - 15, 365),
            Rect(10520, 1080, half_brown_panel.get_width() + 15, 365),

            Rect(7666, 4769, big_panel_gray.get_width(), 1600),
            Rect(13266, 2070, office.get_width(), 450),
            Rect(13312, 3264, 860, new_house1.get_height() - 440),
            Rect(15026, 5784, new_house2.get_width(), 580),
            Rect(15620, 6364, 2640, 130),
            Rect(14266, 2069, shop2.get_width(), 240),










            self.campfire,



        ]



class Player(Collider):
    def __init__(self):
        super(Player, self).__init__()
        self.speed = 8 # normal speed
        self.go_right = Animation([pygame.image.load(f'image/player/animation/walk/right/{i}.png').convert_alpha() for i in range(1, 8)], 4)
        self.go_left = Animation([pygame.image.load(f'image/player/animation/walk/left/{i}.png').convert_alpha() for i in range(1, 8)], 4)
        self.go_bottom = Animation([pygame.image.load(f'image/player/animation/walk/bottom/{i}.png').convert_alpha() for i in range(1, 7)], 4)
        self.go_top = Animation([pygame.image.load(f'image/player/animation/walk/top/{i}.png').convert_alpha() for i in range(1, 7)], 4)

    def render(self):
        self.key = pygame.key.get_pressed()
        self.move_camera()
        self.player_movement = [0, 0]

        if self.key[pygame.K_w]:
            self.player_movement[1] -= self.speed
            if self.key[pygame.K_a]:
                self.player_movement[0] -= self.speed
                self.go_left.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())
            elif self.key[pygame.K_d]:
                self.player_movement[0] += self.speed
                self.go_right.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())
            else:
                self.go_top.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())

        elif self.key[pygame.K_s]:
            self.player_movement[1] += self.speed
            if self.key[pygame.K_a]:
                self.player_movement[0] -= self.speed
                # window.blit(self.texture, (self.player_rect.x - scroll[0], self.player_rect.y - self.texture.get_height() - scroll[1]))
                self.go_bottom.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())
            elif self.key[pygame.K_d]:
                self.player_movement[0] += self.speed
                # window.blit(self.texture, (self.player_rect.x - scroll[0], self.player_rect.y - self.texture.get_height() - scroll[1]))
                self.go_bottom.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())
            self.go_bottom.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())


        elif self.key[pygame.K_a]:
            self.player_movement[0] -= self.speed
            self.go_left.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())


        elif self.key[pygame.K_d]:
            self.player_movement[0] += self.speed
            self.go_right.show_anim(self.player_rect.x, self.player_rect.y - self.texture.get_height())


        else:
            window.blit(self.texture, (self.player_rect.x - self.scroll[0],
                                   self.player_rect.y - self.texture.get_height() - self.scroll[1]))



        self.player_rect, self.collision = self.move(self.player_rect, self.player_movement, self.hitboxes)




    def __collision_test(self, rect, tiles):
        hitbox = []
        for tile in tiles:
            if rect.colliderect(tile):
                hitbox.append(tile)
        return hitbox

    def move(self, rect, collision_cords, tiles):  # rect --> pygame.Rect(), collision_cords --> list, tiles --> list(hitboxes)
        collision_types = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False
        }
        rect.x += collision_cords[0]
        hitbox = self.__collision_test(rect, tiles)
        for hits in hitbox:
            if collision_cords[0] > 0:
                rect.right = hits.left
                collision_types['left'] = True
            if collision_cords[0] < 0:
                rect.left = hits.right
                collision_types['right'] = True
        rect.y += collision_cords[1]
        hitbox = self.__collision_test(rect, tiles)
        for hits in hitbox:
            if collision_cords[1] > 0:
                rect.bottom = hits.top
                collision_types['top'] = True
            if collision_cords[1] < 0:
                rect.top = hits.bottom
                collision_types['bottom'] = True
        return rect, collision_types

class Dialog():

    def __init__(self, text, size = 32):
        self.word = text

        self.text = pygame.font.Font('font/rus-pixel.ttf', size)
        self.var_render = 5
        self.text_word = ''
        self.iter = 0
        self.list_word = list(self.word)
        self.click_btn = pygame.image.load('image/icons/btn_click.png').convert_alpha()

        self.blit_click = False
        self.exit_dialog = False
        self.black_surface = pygame.Surface((1280, 144))
        # self.play_var = 16

    def render_text(self, x = 0, color = (255, 255, 255), print = True, y = 600, sound = True):
        if self.var_render == 0:
            self.var_render = 4
            self.text_word += self.list_word[self.iter]
            self.iter += 1
            # self.play_var += 1

            if self.iter >= len(self.list_word):
                self.blit_click = True
                # if sound:
                #     self.sound_dialog.stop()

                self.var_render = 10000000000000



        window.blit(self.text.render(self.text_word, True, color), (150 + x, y))
        if self.blit_click and print:
            window.blit(self.click_btn, (150 + x, y + 50))
            window.blit(pygame.font.Font('font/rus-pixel.ttf', 32).render('продолжить', True, color),
                        (150 + self.click_btn.get_width() + 10 + x, y + 50))
        self.var_render -= 1

    def render_nowait(self, x = 0, color = (194, 147, 54), print = True, y = 600, sound = True):
        if not self.exit_dialog:
            window.blit(self.black_surface, (0, 720-144))
            self.black_surface.fill((0,0,0))
            if self.var_render == 0:

                self.var_render = 4
                self.text_word += self.list_word[self.iter]
                self.iter += 1
                # self.play_var += 1

                if self.iter >= len(self.list_word):
                    self.blit_click = True
                    # if sound:
                    #     self.sound_dialog.stop()

                    self.var_render = 10000000000000



            window.blit(self.text.render(self.text_word, True, color), (150 + x, y))
            if self.blit_click and print:
                if self.var_render in range(10000, 10000000000000 - 100):
                    self.exit_dialog = True

            self.var_render -= 1

    def __str__(self):
        return self.word