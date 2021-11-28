# [Python pygame] Live Dog : 리브도그
# 실행 파일 start.py
import pygame
import time
import sys
from datafile import *
import pygame.mixer

from game import Game

SCREEN_SIZE = (960, 640)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

# 메인 클래스
class Main:
    def __init__(self):
        # 초기화
        pygame.init()

        # window 타이틀 설정
        title = "리브도그"
        pygame.display.set_caption(title)
        # 화면을 초당 몇 번 출력하는가, 화면 FPS 설정
        self.clock = pygame.time.Clock()

        # window 아이콘 설정
        icon = pygame.image.load("image/dog_icon.png")
        pygame.display.set_icon(icon)

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        self.gameScore = 0

        # 리소스 불러오기
        # SpriteSheet(filename, width, height, max_row, max_col, max_index)
        self.spriteSheet_player = SpriteSheet('dog.png', 32, 32, 4, 4, 11)

        # 플레이어 스프라이트 세트
        self.spr_player = {}
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 0, 3)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, 3, 9)
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [10])

        # 게임 시작 화면
        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background.gif'))
        self.button_image = pygame.image.load(os.path.join(DIR_IMAGE,'game_start_button.png'))

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'happiness.wav'))
        pygame.mixer.music.play(loops=-1)

        # 게임 실행
        self.run()

    def run(self):
        # 이벤트 루프
        while True:  # 게임이 진행 중인가?
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()

            # self.screen.blit(self.button_image, (345, 445))

            screen.blit(self.background, (0, 0))  # 배경화면 설정
            startButton = Button(self.button_image, 345, 445, 275, 154, startGame())
            pygame.display.update()
            self.clock.tick(15)

        pygame.quit()  # pygame 종료

# 버튼 클래스
class Button:
    def __init__(self, image, x, y, w, h, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            screen.blit(image, (x, y))
        else:
            screen.blit(image, (x, y))

def gameStart(self):
    Game()

if __name__ == "__main__":
    Main()
