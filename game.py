import pygame
import sys
from datafile import *

clock = pygame.time.Clock()

# 게임 클래스
class Game:
    def __init__(self):
        # 초기화
        pygame.init()

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        self.gameScore = 0

        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_1.png'))

        player = AnimatedSprite(position=(150, 400))
        self.all_sprites = pygame.sprite.Group(player)

        self.run()

    def run(self):
        while True:
            # screen.fill((255, 255, 255))
            self.all_sprites.update()
            screen.blit(self.background, (0, 0))
            self.all_sprites.draw(screen)
            pygame.display.update()
            clock.tick(8)
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()
        pygame.exit()


if __name__ == "__main__":
    Game()