import sys

import pyautogui
import pygame

from datafile import *


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
            font_white = pygame.Color((255,255, 255))
            font_yellow = pygame.Color((255, 255, 0))
            txt1 = font_title.render('게임 종료', True, font_white)
            txt2 = font_contents.render(f'{self.user_name}님의 점수는 {self.game_score}점입니다!', True, font_white)
            txt3 = font_detail.render(f'> Top 3 보러 가기 <', True, font_yellow)
            SCREEN.blit(txt1, (400, 100))
            SCREEN.blit(txt2, (280, 300))
            SCREEN.blit(txt3, (380, 400))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 860 < cursor[0] < 1600 and 620 < cursor[1] < 640: # Top3 보러가기
                        self.top3()

        pygame.quit()
        sys.exit()

    def top3(self):
        top3 = self.load_history()
        font = pygame.font.Font('font/DungGeunMo.ttf', 30)

        running = True
        while running:
            SCREEN.fill((0, 0, 0))
            player1 = font.render(f'{top3[0]}', True, (0, 0, 0))
            player2 = font.render(f'{top3[1]}', True, (0, 0, 0))
            player3 = font.render(f'{top3[2]}', True, (0, 0, 0))
            SCREEN.blit(player1, (250, 300))
            SCREEN.blit(player2, (280, 300))
            SCREEN.blit(player3, (310, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
        sys.exit()

    def load_history(self):
        count_list = []
        with open('score.txt', 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line_data = line.rstrip().split('\t')
                count_list.append(line_data)
        count_list.sort()
        return count_list[:3]



