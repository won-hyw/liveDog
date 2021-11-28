import pygame
import sys

SCREEN_SIZE = (960, 640)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

# 게임 클래스
class Game:

    def __init__(self):
        pygame.init()

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))


        self.run()

    def run(self):
        print(f'game.py에서 실행되는 멘트입니다.')
        while True:
            screen.fill((0, 0, 0))
            pygame.display.update()
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        pygame.exit()

if __name__ == "__main__":
    Game()