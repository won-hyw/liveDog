import pygame.display
from datafile import *
import pyautogui


# Top3 출력 클래스
class Top3:

    def __init__(self):
        pygame.init()

        player = self.load_history()
        print(player)

        if len(player) >= 3:
            self.run(player)
        else:
            self.run2()

    def load_history(self):
        count_list = []
        with open('score.txt', 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                line_data = line.rstrip().split('\t')
                count_list.append(line_data[1])
        count_list.sort(reverse=True)
        return count_list[:3]

    def run(self, player):
        font = pygame.font.Font('font/DungGeunMo.ttf', 30)
        font_color = pygame.color.Color((255, 255, 255))

        player_1 = font.render(f'1등  {player[0]}', True, font_color)
        player_2 = font.render(f'2등  {player[1]}', True, font_color)
        player_3 = font.render(f'3등  {player[2]}', True, font_color)

        while True:
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(player_1, (380, 280))
            SCREEN.blit(player_2, (380, 320))
            SCREEN.blit(player_3, (380, 360))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                        if esc_alert == '확인':
                            pygame.quit()
        pygame.quit()

    def run2(self):
        font = pygame.font.Font('font/DungGeunMo.ttf', 30)
        font_color = pygame.color.Color((255, 255, 255))

        text = font.render('아직 점수 데이터가 3개 미만입니다.', True, font_color)

        while True:
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(text, (250, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                    if esc_alert == '확인':
                        pygame.quit()
