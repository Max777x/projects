import pygame
import random
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


IMAGES = "C:/Users/maxbe/PycharmProjects/PyGame/"
pygame.init()
size = width, hugh = 1000, 1000
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


google = {'pizza': 6183382, 'snow': 5792671, 'lv': 146795, 'gdz': 41995372, 'icecream': 1101336, 'vk': 58373158,
     'ikea': 5341684, 'kylie': 146761, 'apple': 2723992, 'la': 1720712, 'mario': 552597, 'moscowcity': 499993,
     'nintendo': 261507, 'paul': 120428, 'summer': 54561662, 'table': 12079248, 'versace': 93041, 'chain': 2051636}


def image_load(n, colorkey=None):
    Fname = os.path.join('images', n)
    image = pygame.image.load(Fname).convert()
    image = image.convert_alpha()
    return image


class Button:
    def __init__(self):

        self.size = [100, 200]  # Размер кнопки
        self.image_button = pygame.image.load(IMAGE + 'button.png')  # Загружаем изображение исходной кнопки
        self.text = 'Less'  # Текст кнопки
        self.x = 250  # Позиция х кнопки
        self.y = 500  # Позиция у кнопки
        self.rect_button = pygame.Rect(self.x, self.y, self.size[0],
                                       self.size[1])

    def create_button(self, settings, color='red'):
        """Создает кнопку на экране"""
        text_button = settings.font_text.render(self.text, True, color)  # Создаем изображение с текстом
        text_rect = text_button.get_rect()  # Возвращаем прямоугольник который занимает текст
        text_rect.center = self.rect_image_button.center  # Делаем текст посередине кнопки
        self.image_button.blit(text_button, text_rect)
        self.image_click.blit(text_button, text_rect)
        self.image_put_on_button.blit(text_button, text_rect)

    def draw_button(self, screen, control):  # Рисует созданную кнопку на экране

        screen.blit(self.image_button, (self.x, self.y))  # Если ничего не происходит,то рисуем обычную кнопку


'''class Control:
    def __init__(self):

        self.play = True  # Переменная для остановки основного цикла игры
        self.mouse_x = 0  # Позиция х курсора
        self.mouse_y = 0  # Позиция у курсора
        self.flag = "NORMAL"  # Флаг для отрисовки кнопок

    def control_game(self):
        """Все управление игрой"""
        for event in pygame.event.get():

            if event.type == QUIT:
                self.play = False

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.play = False

            elif event.type == MOUSEBUTTONDOWN:

                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                self.flag = "CLICKED"

            elif event.type == MOUSEBUTTONUP:

                self.flag = "NORMAL"'''


all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = image_load(random.choice(list(google.keys())) + '.jpg')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.y = 1500

sprite2 = pygame.sprite.Sprite()
sprite2.image = image_load(random.choice(list(google.keys())) + '.jpg')
sprite2.rect = sprite2.image.get_rect()
all_sprites.add(sprite2)
sprite2.rect.y = 2000

true_false = True
fps = 30
v = 20


clock = pygame.time.Clock()
while true_false:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true_false = False
    if sprite.rect.y == 0 and sprite2.rect.y == 500:
        break

    sprite.rect.y -= v
    sprite2.rect.y -= v
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)


while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

