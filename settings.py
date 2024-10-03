import pygame
import ctypes

pygame.init()

user32 = ctypes.windll.user32
# SIZE = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
SIZE = (1280, 720)
# print(SIZE)
del user32

def image(var):
    return pygame.image.load(var).convert_alpha()

window = pygame.display.set_mode(SIZE, pygame.FULLSCREEN | pygame.DOUBLEBUF)
screen = pygame.Surface(SIZE).convert_alpha()

FPS = 60
# FPS = 120
clock = pygame.time.Clock()
scroll = [0, 0]
true_scroll = scroll

pygame.mouse.set_visible(False)

class Button():
    def __init__(self, text = '', color = (255,255,255), color_font = None, size = 8, font = None, x = 0, y = 0, width = 10, height = 10):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(f'font/{font}', size)
        self.color_font = color_font
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_btn = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def render_btn(self):
        pygame.draw.rect(screen, self.color, self.rect_btn)
        window.blit(self.font.render(self.text, True, self.color_font), (self.x + 10, self.y + 10))

class Animation():
    def __init__(self, list_sprites, delay):
        self.list_sprites = list_sprites
        self.anim_count = 0
        self.delay = delay

    def show_anim(self, x, y):
        if self.anim_count < len(self.list_sprites) * self.delay:
            window.blit(self.list_sprites[self.anim_count//self.delay], (x - scroll[0], y - scroll[1]))
            self.anim_count += 1
        else:
            self.anim_count = 0


def blit_all_tiles(path):
    f = open(path + '.cb', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))

    gm = []
    for row in game_map:
        gm2 = []
        for sim in row:
            if sim == ',':
                continue
            gm2.append(sim)
        gm.append(gm2)

    game_map = gm


    return game_map


