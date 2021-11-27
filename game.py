# [Python pygame] Live Dog : 리브도그
# 실행 파일 game.py
import pygame
from character import *

SCREEN_SIZE = (960, 640)

# 게임 클래스
class Game:
    def __init__(self):
        # 초기화
        pygame.init()

        # window 타이틀 설정
        pygame.display.set_caption("리브도그")
        # 화면을 초당 몇 번 출력하는가, 화면 FPS 설정
        self.clock = pygame.time.Clock()

        # window 아이콘 설정
        self.icon = pygame.image.load("image/dog_icon.png")
        pygame.display.set_icon(self.icon)

        # pygame screen 설정
        self.screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        self.gameScore = 0

        # 리소스 불러오기
        # SpriteSheet(filename, width, height, max_row, max_col, max_index)
        self.spriteSheet_player = SpriteSheet('image/dog.png',)

        self.spr_player = {} # 플레이어 스프라이트 세트
        self.spr_player['stay']
        self.spr_player['run']
        self.spr_player['jump']

        # 이벤트 루프
        self.running = True
        while self.running:  # 게임이 진행 중인가?
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    self.running = False  # 게임이 진행중이 아님
        pygame.quit()  # pygame 종료

        # self.run()

    def run(self):
        pass


if __name__ == "__main__":
    Game()
