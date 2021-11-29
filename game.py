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

        # 리소스 불러오기
        # 맵 1
        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_1.png'))
        # 플레이어 이동 애니메이션 클래스
        self.player = AnimatedSprite(position=(150, 400))
        self.all_sprites = pygame.sprite.Group(self.player)

        self.run()

    def run(self):
        while True:
            # 각 loop를 도는 시간
            # clock.tick()은 밀리초를 반환하므로 1000을 나누어주어 초 단위로 변경
            mt = clock.tick(60) / 1000

            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.player.state = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.player.state = 0

            # all_sprites 그룹 안에 든 모든 Sprite update
            self.all_sprites.update(mt)
            # 배경화면 설정
            screen.blit(self.background, (0, 0))
            # 모든 sprite 화면에 그리기
            self.all_sprites.draw(screen)
            pygame.display.update()


if __name__ == "__main__":
    Game()