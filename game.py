import pygame
import sys
from datafile import *
import random


# 게임 클래스
class Game:

    def __init__(self):
        # 초기화
        pygame.init()

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        self.gameScore = 0

        # 리소스 불러오기
        # 맵 불러오기
        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_1.png'))
        self.background2 = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_2.png'))

        self.items = []
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_coin.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_heart.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_time_reduction.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_eat.png')))

        # 플레이어 이동 애니메이션 클래스
        self.player = AnimatedSprite(position=(150, 450))
        self.all_sprites = pygame.sprite.Group(self.player)

        self.run()

    def run(self):
        running = True
        while running:
            # 각 loop를 도는 시간
            # clock.tick()은 밀리초를 반환하므로 1000을 나누어주어 초 단위로 변경
            mt = CLOCK.tick(60) / 1000
            # 이벤트 발생
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.player.state = 1
                        self.player.rect.y -= 5*(0.5 * self.player.m * (self.player.v * self.player.v))
                        CLOCK.tick(15)
                    if event.key == pygame.K_ESCAPE:
                        esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                        if esc_alert == '확인':
                            running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.player.state = 0
                        self.player.rect.y += 5*(0.5 * self.player.m * (self.player.v * self.player.v))
            # all_sprites 그룹 안에 든 모든 Sprite update
            self.all_sprites.update(mt)
            # 배경화면 설정
            SCREEN.blit(self.background, (0, 0))
            # 모든 sprite 화면에 그리기
            self.all_sprites.draw(SCREEN)
            pygame.display.update()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.display.set_caption("리브도그")
    icon = pygame.image.load(os.path.join(DIR_IMAGE, 'dog_icon.png'))
    pygame.display.set_icon(icon)
    Game()

