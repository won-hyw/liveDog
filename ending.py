import sys

import pyautogui
import pygame

from datafile import *
from printTop3 import Top3


class Ending:

    def __init__(self, game_score, user_name):
        # pygame 초기화
        pygame.init()

        self.game_score = game_score
        self.user_name = user_name

        self.save_history(user_name, game_score)

        self.run()


    def save_history(self, user_name, game_score):
        with open('score.txt', 'a') as f:
            data = f'{user_name}\t{game_score}\n'
            f.write(data)

    def run(self):
        running = True
        while running:
            cursor = pyautogui.position()
            SCREEN.fill((0, 0, 0))
            font_title = pygame.font.Font('font/DungGeunMo.ttf', 40)
            font_contents = pygame.font.Font('font/DungGeunMo.ttf', 30)
            font_detail = pygame.font.Font('font/DungGeunMo.ttf', 25)
            font_white = pygame.Color((255, 255, 255))
            font_yellow = pygame.Color((255, 255, 0))
            txt1 = font_title.render('게임 종료', True, font_white)
            txt2 = font_contents.render(f'{self.user_name}님의 점수는 {self.game_score}점입니다!', True, font_white)
            txt3 = font_detail.render(f'> Top 3 보러 가기 (Enter 입력) <', True, font_yellow)
            SCREEN.blit(txt1, (400, 100))
            SCREEN.blit(txt2, (280, 300))
            SCREEN.blit(txt3, (280, 400))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Top3()

        pygame.quit()
        sys.exit()


