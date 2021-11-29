# [Python pygame] Live Dog : 리브도그
# 실행 파일 start.py
from datafile import *
import pygame.mixer
from game import Game


# 메인 클래스
class Main:
    def __init__(self):
        # 초기화
        pygame.init()

        # window 타이틀 설정
        title = "리브도그"
        pygame.display.set_caption(title)

        # window 아이콘 설정
        icon = pygame.image.load("image/dog_icon.png")
        pygame.display.set_icon(icon)

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

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
            screen.blit(self.background, (0, 0))  # 배경화면 설정
            startButton = Button(self.button_image, 345, 445, 275, 154)
            pygame.display.update()
            clock.tick(15)
            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN: # 버튼이 눌리면 화면 전환
                    Game()
        pygame.quit()  # pygame 종료


# 버튼 클래스
class Button:
    def __init__(self, image, x, y, w, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            screen.blit(image, (x, y))
        else:
            screen.blit(image, (x, y))


if __name__ == "__main__":
    Main()
