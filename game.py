# [Python pygame] Live Dog : 리브도그
# 실행 파일 game.py
import pygame, sys
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
        self.spriteSheet_player = SpriteSheet('dog.png', 32, 32, 16, 16, 11)

        # 플레이어 스프라이트 세트
        self.spr_player = {}
        self.spr_player['sit'] = createSpriteSet(self.spriteSheet_player, [10])
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 4)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [5, 6, 7, 8, 9])

        self.run()

    def run(self):
        # 이벤트 루프
        while True:  # 게임이 진행 중인가?
            self.screen.blit(self.spriteSheet_player.spr[0], (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)) # 캐릭터 화면에 그리기

            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()  # pygame 종료


if __name__ == "__main__":
    Game()
