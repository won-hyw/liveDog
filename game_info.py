import sys
import pygame.image
from datafile import *
from game import Game

pygame.init()
COLOR_INACTIVE = pygame.Color((255, 255, 255))
COLOR_ACTIVE = pygame.Color((255, 255, 255))
FONT1 = pygame.font.Font('font/DungGeunMo.ttf', 32)
FONT2 = pygame.font.Font('font/DungGeunMo.ttf', 28)

# 입력창 클래스
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT1.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if len(self.text) > 0:
                        Game(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT1.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        txt = FONT1.render('플레이어 이름을 작성해주세요', True, self.color)
        screen.blit(txt, (250, 230))
        txt2 = FONT2.render('※ 게임을 시작하고 싶을 시 엔터키를 입력하세요 ※', True, (255, 255, 0))
        screen.blit(txt2, (120, 400))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


# 플레이어 Info 클래스
class Info:
    def __init__(self):
        self.draw_info()

    def draw_info(self):
        pygame.init()

        clock = pygame.time.Clock()
        box = InputBox(350, 300, 140, 50)

        running = True
        while running:
            pygame.display.update()
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                        if esc_alert == '확인':
                            running = False
                box.handle_event(event)

            box.update()
            SCREEN.fill((0, 0, 0))
            box.draw(SCREEN)
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()
        sys.exit()


