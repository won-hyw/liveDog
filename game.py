import time
import sys
import pygame
from datafile import *
import random
from ending import Ending


# 게임 클래스
class Game:

    def __init__(self, user_name):
        # 초기화
        pygame.init()

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        # 게임에 필요한 변수
        self.gameScore = 0      # 점수
        self.player_life = 50  # 생명
        self.user_name = user_name

        # 리소스 불러오기
        # 맵 불러오기
        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_1.png'))
        self.background2 = pygame.image.load(os.path.join(DIR_IMAGE, 'background_map_2.png'))

        # 아이템 불러오기
        self.items = []
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_coin.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_heart.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_time_reduction.png')))
        self.items.append(pygame.image.load(os.path.join(DIR_IMAGE, 'dog_item_eat.png')))

        # 이미지를 Rect 안에 넣기 위해 Rect 크기 지정
        size = (150, 150)

        # Item 크기 맞추기
        self.items = [pygame.transform.scale(item, size) for item in self.items]

        # 아이템 간격을 위한 None값 추가
        self.items.append(None)

        # 플레이어 이동 애니메이션 클래스
        self.player = AnimatedSprite(position=(150, 470))
        self.all_sprites = pygame.sprite.Group(self.player)

        self.run()

    def draw(self, item, x, y):
        SCREEN.blit(item, (x, y))

    def draw_text(self):
        font = pygame.font.Font('font/DungGeunMo.ttf', 25)
        font_color = pygame.color.Color((0, 0, 0))
        score_text = font.render(f'점수 : {self.gameScore}', True, font_color)
        life_text = font.render(f'목숨 : {self.player_life}', True, font_color)
        SCREEN.blit(life_text, (10, 10))
        SCREEN.blit(score_text, (10, 50))

    def game_engine(self, index):
        if index == 0:
            self.gameScore += 10
        elif index == 1:
            if self.player_life < 50:
                self.player_life += 5
        elif index == 2:
            self.player_life -= 20
        elif index == 3:
            if self.player_life < 50:
                self.player_life += 10

    def set_item(self):
        x = SCREEN_SIZE[0]
        y = random.randrange(280, 530)
        idx = random.randint(0, 3)
        return x, y, idx


    def run(self):
        item_x, item_y, index = self.set_item()
        item = self.items[index]
        item_x2, item_y2, index2 = self.set_item()
        item2 = self.items[index2]

        bg_idx = random.randint(0, 1)

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
                        CLOCK.tick(60)
                    if event.key == pygame.K_ESCAPE:
                        esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                        if esc_alert == '확인':
                            running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        self.player.state = 0
                        self.player.rect.y += 5*(0.5 * self.player.m * (self.player.v * self.player.v))
                if event.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())
            # all_sprites 그룹 안에 든 모든 Sprite update
            self.all_sprites.update(mt)
            # 배경화면 설정
            # 배경화면 설정
            if bg_idx == 0:
                SCREEN.blit(self.background, (0, 0))
            else:
                SCREEN.blit(self.background2, (0, 0))

            self.draw_text()

            # 아이템이 날라오는 간격을 조절하기 위한 장치
            if item is None:
                item_x -= 30
                item_x2 -= 30
            else:
                item_x -= 10
                item_x2 -= 10

            if item_x <= -20:
                item_x, item_y, index = self.set_item()
                item = self.items[index]
                item_x2, item_y2, index2 = self.set_item()
                item2 = self.items[index2]

            if item is not None:
                self.draw(item, item_x, item_y)
                self.draw(item2, item_x2, item_y2)

            # 충돌 체크
            player_x_pos = 180
            player_x_pos2 = 330
            if self.player.state == 0:
                player_y_pos = 450
                player_y_pos2 = 630
                if player_x_pos < item_x < player_x_pos2 and player_y_pos < item_y < player_y_pos2:
                    self.game_engine(index)
                    item_x, item_y, index = self.set_item()
                    item = self.items[index]
                if player_x_pos < item_x2 < player_x_pos2 and player_y_pos < item_y2 < player_y_pos2:
                    self.game_engine(index2)
                    item_x2, item_y2, index2 = self.set_item()
                    item2 = self.items[index2]
            elif self.player.state == 1:
                player_y_pos = 235
                player_y_pos2 = 410
                if player_x_pos < item_x < player_x_pos2 and player_y_pos < item_y < player_y_pos2:
                    self.game_engine(index)
                    item_x, item_y, index = self.set_item()
                    item = self.items[index]
                if player_x_pos < item_x2 < player_x_pos2 and player_y_pos < item_y2 < player_y_pos2:
                    self.game_engine(index2)
                    item_x2, item_y2, index2 = self.set_item()
                    item2 = self.items[index2]

            if self.player_life <= 0:
                CLOCK.tick(30)
                Ending(self.gameScore, self.user_name)

            # 모든 sprite 화면에 그리기
            self.all_sprites.draw(SCREEN)
            self.draw_text()
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.display.set_caption("리브도그")
    icon = pygame.image.load(os.path.join(DIR_IMAGE, 'dog_icon.png'))
    pygame.display.set_icon(icon)
    Game()

