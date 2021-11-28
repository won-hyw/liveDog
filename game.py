import pygame
import sys
from datafile import *


# 게임 클래스
class Game:

    def __init__(self):
        pygame.init()

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        self.gameScore = 0

        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background.gif'))
        self.player = pygame.image.load(os.path.join(DIR_IMAGE, 'run.gif'))
        self.player = pygame.transform.scale(self.player, (200, 200))

        self.run()

    def run(self):
        while True:
            screen.fill((255, 255, 255))
            # screen.blit(self.background, (0, 0))
            screen.blit(self.player, (350, 200))
            pygame.display.update()
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        pygame.exit()


if __name__ == "__main__":
    Game()