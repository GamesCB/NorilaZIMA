import pygame
import sys
from settings import *
from textures import *
from pygame.locals import *
from atmosphere import *

pygame.init()

class Menu():
    def __init__(self):
        self.text_menu_32 = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.title_name = pygame.font.Font('font/OCR A EXTENDED.ttf', 32)

        self.rect_play = pygame.rect.Rect(100, 100, buttons_menu.get_width(), buttons_menu.get_height())
        self.rect_ach = pygame.rect.Rect(100, 200, buttons_menu.get_width(), buttons_menu.get_height())
        self.rect_stats = pygame.rect.Rect(100, 300, buttons_menu.get_width(), buttons_menu.get_height())
        self.rect_settings = pygame.rect.Rect(100, 400, buttons_menu.get_width(), buttons_menu.get_height())
        self.rect_exit = pygame.rect.Rect(100, 500, buttons_menu.get_width(), buttons_menu.get_height())

        self.flakes = Flakes()

        self.mainmenu()


    def mainmenu(self):
        exit_menu = False
        while True:

            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rect_play.collidepoint(self.mouse[0], self.mouse[1]):
                            exit_menu = True
                        elif self.rect_exit.collidepoint(self.mouse[0], self.mouse[1]):
                            pygame.quit()
                            sys.exit()
                        elif self.rect_settings.collidepoint(self.mouse[0], self.mouse[1]):
                            self.settings()

            window.blit(screen, (0,0))
            screen.fill((0,0,0))
            self.flakes.render_flakes()
            self.render_buttons()

            window.blit(mouse_cursor, self.mouse)
            # print(self.mouse)
            pygame.display.update()
            clock.tick(FPS)
            if exit_menu:
                break

    def render_buttons(self):
        window.blit(self.title_name.render('Norila.ZIMA', True, (200,200,200)), (65, 25))
        window.blit(buttons_menu, (100, 100))
        window.blit(self.text_menu_32.render('играть', True, (200,200,200)), (135, 120))
        window.blit(buttons_menu, (100, 200))
        window.blit(self.text_menu_32.render('достижения', True, (200, 200, 200)), (110, 220))
        window.blit(buttons_menu, (100, 300))
        window.blit(self.text_menu_32.render('статистика', True, (200, 200, 200)), (110, 320))
        window.blit(buttons_menu, (100, 400))
        window.blit(self.text_menu_32.render('настройки', True, (200, 200, 200)), (115, 420))
        window.blit(buttons_menu, (100, 500))
        window.blit(self.text_menu_32.render('выход', True, (200, 200, 200)), (140, 520))

    def settings(self):
        while True:
            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            self.flakes.render_flakes()

            window.blit(mouse_cursor, self.mouse)

            pygame.display.update()
            clock.tick(FPS)

    def achs(self):
        pass

    def stats(self):
        pass

class Using_menu():
    def __init__(self):
        self.text_buttons = pygame.font.Font('font/rus-pixel.ttf', 32)
        self.button_texture = pygame.image.load('image/icons/menu buttons.png').convert_alpha()
        self.button_texture = pygame.transform.scale(self.button_texture, (self.button_texture.get_width()//1.25,
                                                                           self.button_texture.get_height()//1.25))

        self.button_rect = Rect(364, -self.button_texture.get_height(), self.button_texture.get_width(), self.button_texture.get_height())

    def show_menu(self, mouse_rect):
        if self.button_rect.y < 50:
            self.button_rect.y += 8
        window.blit(self.button_texture, (self.button_rect.x, self.button_rect.y))
        window.blit(self.text_buttons.render('выйти', True, (255,255,255)), (self.button_rect.x + 25, self.button_rect.y + 10))
        self.choise_buttons(mouse_rect)

    def hide_menu(self):
        if self.button_rect.y > -self.button_texture.get_height():
            self.button_rect.y -= 8

        window.blit(self.button_texture, (self.button_rect.x, self.button_rect.y))
        window.blit(self.text_buttons.render('выйти', True, (255, 255, 255)),
                    (self.button_rect.x + 25, self.button_rect.y + 10))

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def choise_buttons(self, mouse_rect:Rect):
        for mouse_event in pygame.event.get():
            if mouse_event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_event.button == 1:
                    if mouse_rect.colliderect(self.button_rect):
                        self.exit_game()
